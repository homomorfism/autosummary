import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getCoursePage } from "@/lib/courses";
import { getAttempt, loadRetired, questionId } from "@/lib/db";
import { renderMathText } from "@/lib/markdown";
import { loadQuiz, type QuizQuestion } from "@/lib/quiz";

export const dynamic = "force-dynamic";

export const metadata: Metadata = { title: "Quiz results" };

interface Props {
  params: Promise<{ id: string }>;
}

/** question_id → full question, from the live quiz and the retired archive
 *  (an answered question may have been retired since the attempt). */
function questionLookup(course: string, lecture: string): Map<string, QuizQuestion> {
  const lookup = new Map<string, QuizQuestion>();
  for (const row of loadRetired(course, lecture)) {
    lookup.set(row.question_id, JSON.parse(row.question_json) as QuizQuestion);
  }
  const quiz = loadQuiz(course, lecture);
  for (const q of quiz?.questions ?? []) {
    lookup.set(questionId(course, lecture, q.question), q);
  }
  return lookup;
}

function ScoreRing({ score, total }: { score: number; total: number }) {
  const pct = total > 0 ? score / total : 0;
  const r = 40;
  const circumference = 2 * Math.PI * r;
  const color = pct >= 0.8 ? "var(--ok)" : pct >= 0.5 ? "var(--warn)" : "var(--bad)";
  return (
    <svg className="score-ring" viewBox="0 0 92 92" role="img" aria-label={`Score ${score} of ${total}`}>
      <circle cx="46" cy="46" r={r} fill="none" stroke="var(--surface-2)" strokeWidth="8" />
      <circle
        cx="46"
        cy="46"
        r={r}
        fill="none"
        stroke={color}
        strokeWidth="8"
        strokeLinecap="round"
        strokeDasharray={`${pct * circumference} ${circumference}`}
        transform="rotate(-90 46 46)"
      />
      <text x="46" y="52" textAnchor="middle" className="score-label">
        {score}/{total}
      </text>
    </svg>
  );
}

export default async function ResultsPage({ params }: Props) {
  const { id } = await params;
  const attemptId = Number(id);
  if (!Number.isInteger(attemptId)) notFound();
  const found = getAttempt(attemptId);
  if (!found) notFound();

  const { attempt, answers } = found;
  const coursePage = getCoursePage(attempt.course);
  const lookup = questionLookup(attempt.course, attempt.lecture);
  const pct = attempt.total > 0 ? Math.round((100 * attempt.score) / attempt.total) : 0;
  const headline =
    pct >= 80 ? "Excellent — you know this lecture." : pct >= 50 ? "Solid, but reread the misses." : "Worth another pass through the conspect.";

  return (
    <>
      <Breadcrumbs
        crumbs={[
          { label: coursePage?.title ?? attempt.course, href: `/courses/${attempt.course}` },
          { label: attempt.lecture, href: `/courses/${attempt.course}/${attempt.lecture}` },
          { label: "Results" },
        ]}
      />
      <p className="kicker">Attempt #{attempt.id}</p>
      <h1 className="page-title">Quiz results</h1>

      <div className="score-card">
        <ScoreRing score={attempt.score} total={attempt.total} />
        <div>
          <p className="score-headline">{headline}</p>
          <p className="score-sub">
            {attempt.score} of {attempt.total} correct ({pct}%) · {attempt.created_at} UTC
          </p>
        </div>
      </div>

      <div className="quiz-list">
        {answers.map((answer, i) => {
          const question = lookup.get(answer.question_id);
          return (
            <section key={answer.id} className="question-card">
              <p className="question-num">Question {i + 1}</p>
              <h2 className="question-text" dangerouslySetInnerHTML={{ __html: renderMathText(answer.question) }} />
              {question ? (
                question.options.map((opt, optIdx) => {
                  const chosen = optIdx === answer.chosen_index;
                  const cls = opt.is_correct ? " correct" : chosen ? " chosen-wrong" : "";
                  return (
                    <div key={optIdx} className={`result-option${cls}`}>
                      <span className="marker">{opt.is_correct ? "✓" : chosen ? "✗" : ""}</span>
                      <span>
                        <span dangerouslySetInnerHTML={{ __html: renderMathText(opt.text) }} />
                        {chosen && <strong> — your answer</strong>}
                        {(chosen || opt.is_correct) && (
                          <span
                            className="explanation"
                            dangerouslySetInnerHTML={{ __html: renderMathText(opt.explanation) }}
                          />
                        )}
                      </span>
                    </div>
                  );
                })
              ) : (
                <p className="reason">This question is no longer in the quiz and its archive entry was not found.</p>
              )}
              <p className={`result-verdict ${answer.is_correct ? "good" : "bad"}`}>
                {answer.is_correct ? "Correct" : "Incorrect"}
              </p>
            </section>
          );
        })}
      </div>

      <div className="action-bar">
        <Link href={`/courses/${attempt.course}/${attempt.lecture}`} className="btn btn-primary">
          Back to the conspect
        </Link>
      </div>
    </>
  );
}
