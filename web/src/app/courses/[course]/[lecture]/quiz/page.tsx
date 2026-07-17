import type { Metadata } from "next";
import { cookies } from "next/headers";
import { notFound, redirect } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getCoursePage } from "@/lib/courses";
import { activeAttemptFor, attemptMatchesQuestions, CLIENT_ID_COOKIE } from "@/lib/db";
import { renderMathText } from "@/lib/markdown";
import { loadQuiz } from "@/lib/quiz";
import { QuizForm } from "./QuizForm";

export const dynamic = "force-dynamic";

interface Props {
  params: Promise<{ course: string; lecture: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { course, lecture } = await params;
  return { title: loadQuiz(course, lecture)?.title ?? "Quiz" };
}

export default async function QuizPage({ params }: Props) {
  const { course, lecture } = await params;
  const quiz = loadQuiz(course, lecture);
  if (!quiz) notFound();

  const coursePage = getCoursePage(course);

  // One attempt per browser: an existing attempt freezes the quiz — show its
  // results instead of the form. An attempt only counts if it answered
  // questions of the CURRENT quiz: after a full regeneration no question_id
  // overlaps, the old attempt is stale and the quiz is effectively new.
  const clientId = (await cookies()).get(CLIENT_ID_COOKIE)?.value;
  const lastAttempt = clientId ? activeAttemptFor(course, lecture, clientId) : null;
  const questionTexts = quiz.questions.map((q) => q.question);
  if (lastAttempt && attemptMatchesQuestions(lastAttempt.id, course, lecture, questionTexts)) {
    redirect(`/results/${lastAttempt.id}`);
  }

  // Only question and option texts go to the client — grading happens server-side.
  // TeX math is rendered to KaTeX HTML here so the client form stays LaTeX-free.
  const questions = quiz.questions.map((q) => ({
    questionHtml: renderMathText(q.question),
    optionsHtml: q.options.map((o) => renderMathText(o.text)),
  }));

  return (
    <>
      <Breadcrumbs
        crumbs={[
          { label: coursePage?.title ?? course, href: `/courses/${course}` },
          { label: lecture, href: `/courses/${course}/${lecture}` },
          { label: "Quiz" },
        ]}
      />
      <p className="kicker">Self-check</p>
      <h1 className="page-title">{quiz.title}</h1>
      <p className="page-intro">
        One answer per question, one attempt per quiz — you cannot retake it.
      </p>
      <QuizForm course={course} lecture={lecture} questions={questions} />
    </>
  );
}
