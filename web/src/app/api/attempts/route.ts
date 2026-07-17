import { randomUUID } from "node:crypto";
import { cookies } from "next/headers";
import { NextResponse } from "next/server";
import { activeAttemptFor, attemptMatchesQuestions, CLIENT_ID_COOKIE, recordAttempt } from "@/lib/db";
import { loadQuiz } from "@/lib/quiz";

const CLIENT_ID_MAX_AGE = 60 * 60 * 24 * 365;

/** Client IP as seen through a reverse proxy (first x-forwarded-for hop). */
function clientIp(request: Request): string | null {
  const forwarded = request.headers.get("x-forwarded-for");
  if (forwarded) return forwarded.split(",")[0].trim();
  return request.headers.get("x-real-ip");
}

interface AttemptBody {
  course: string;
  lecture: string;
  answers: number[]; // chosen option index per question, in quiz order
}

export async function POST(request: Request) {
  let body: AttemptBody;
  try {
    body = (await request.json()) as AttemptBody;
  } catch {
    return NextResponse.json({ error: "invalid JSON" }, { status: 400 });
  }

  const { course, lecture, answers } = body;
  if (typeof course !== "string" || typeof lecture !== "string" || !Array.isArray(answers)) {
    return NextResponse.json({ error: "course, lecture and answers are required" }, { status: 400 });
  }

  const quiz = loadQuiz(course, lecture);
  if (!quiz) return NextResponse.json({ error: "quiz not found" }, { status: 404 });

  if (answers.length !== quiz.questions.length) {
    return NextResponse.json({ error: "answer every question" }, { status: 400 });
  }
  const graded = quiz.questions.map((q, i) => {
    const chosen = answers[i];
    if (!Number.isInteger(chosen) || chosen < 0 || chosen >= q.options.length) return null;
    return { question: q.question, chosen_index: chosen, is_correct: q.options[chosen].is_correct };
  });
  if (graded.some((g) => g === null)) {
    return NextResponse.json({ error: "invalid option index" }, { status: 400 });
  }

  const cookieStore = await cookies();
  const clientId = cookieStore.get(CLIENT_ID_COOKIE)?.value ?? randomUUID();

  // One attempt per browser and quiz version — a second submission is rejected,
  // pointing at the existing results. A stale attempt (regenerated quiz, no
  // overlapping question_id) does not lock; recordAttempt soft-deletes it.
  const existing = activeAttemptFor(course, lecture, clientId);
  if (existing && attemptMatchesQuestions(existing.id, course, lecture, quiz.questions.map((q) => q.question))) {
    return NextResponse.json(
      { error: "you have already taken this quiz", attemptId: existing.id },
      { status: 409 },
    );
  }
  cookieStore.set(CLIENT_ID_COOKIE, clientId, {
    httpOnly: true,
    sameSite: "lax",
    maxAge: CLIENT_ID_MAX_AGE,
    path: "/",
  });

  const attemptId = recordAttempt(course, lecture, graded as NonNullable<(typeof graded)[number]>[], {
    clientId,
    ip: clientIp(request),
  });
  return NextResponse.json({ attemptId });
}
