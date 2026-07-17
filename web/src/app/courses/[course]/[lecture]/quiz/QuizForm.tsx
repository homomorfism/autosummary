"use client";

import { useRouter } from "next/navigation";
import { useRef, useState } from "react";

interface ClientQuestion {
  questionHtml: string;
  optionsHtml: string[];
}

export function QuizForm({
  course,
  lecture,
  questions,
}: {
  course: string;
  lecture: string;
  questions: ClientQuestion[];
}) {
  const router = useRouter();
  const [answers, setAnswers] = useState<(number | null)[]>(() => questions.map(() => null));
  const [missing, setMissing] = useState<Set<number>>(new Set());
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const cardRefs = useRef<(HTMLElement | null)[]>([]);

  const answered = answers.filter((a) => a !== null).length;

  function choose(qIdx: number, optIdx: number) {
    setAnswers((prev) => prev.map((a, i) => (i === qIdx ? optIdx : a)));
    setMissing((prev) => {
      if (!prev.has(qIdx)) return prev;
      const next = new Set(prev);
      next.delete(qIdx);
      return next;
    });
  }

  async function submit() {
    const unanswered = new Set(answers.flatMap((a, i) => (a === null ? [i] : [])));
    if (unanswered.size > 0) {
      setMissing(unanswered);
      const first = Math.min(...unanswered);
      cardRefs.current[first]?.scrollIntoView({ behavior: "smooth", block: "center" });
      return;
    }

    setSubmitting(true);
    setError(null);
    try {
      const res = await fetch("/api/attempts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ course, lecture, answers }),
      });
      if (res.status === 409) {
        // Already taken (e.g. submitted from another tab) — show that attempt.
        const { attemptId } = (await res.json()) as { attemptId?: number };
        if (attemptId) {
          router.push(`/results/${attemptId}`);
          return;
        }
        throw new Error("You have already taken this quiz.");
      }
      if (!res.ok) throw new Error(`submit failed (${res.status})`);
      const { attemptId } = (await res.json()) as { attemptId: number };
      router.push(`/results/${attemptId}`);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong — please try again.");
      setSubmitting(false);
    }
  }

  return (
    <>
      <div className="quiz-list">
        {questions.map((q, qIdx) => (
          <section
            key={qIdx}
            className={`question-card${missing.has(qIdx) ? " missing" : ""}`}
            ref={(el) => {
              cardRefs.current[qIdx] = el;
            }}
          >
            <p className="question-num">
              Question {qIdx + 1} of {questions.length}
            </p>
            <h2 className="question-text" dangerouslySetInnerHTML={{ __html: q.questionHtml }} />
            {q.optionsHtml.map((html, optIdx) => (
              <label key={optIdx} className={`option${answers[qIdx] === optIdx ? " selected" : ""}`}>
                <input
                  type="radio"
                  name={`q${qIdx}`}
                  checked={answers[qIdx] === optIdx}
                  onChange={() => choose(qIdx, optIdx)}
                />
                <span dangerouslySetInnerHTML={{ __html: html }} />
              </label>
            ))}
            {missing.has(qIdx) && <p className="missing-hint">Please pick an answer to this question.</p>}
          </section>
        ))}
      </div>

      <div className="quiz-footer">
        <span className="quiz-progress">
          {answered} / {questions.length} answered
        </span>
        <div className="quiz-progress-bar">
          <div className="quiz-progress-fill" style={{ width: `${(answered / questions.length) * 100}%` }} />
        </div>
        {error && <span className="quiz-error">{error}</span>}
        <button className="btn btn-primary" onClick={submit} disabled={submitting}>
          {submitting ? "Submitting…" : "Submit answers"}
        </button>
      </div>
    </>
  );
}
