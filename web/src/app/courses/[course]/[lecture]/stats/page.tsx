import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getCoursePage, lectureDir } from "@/lib/courses";
import { attemptCount, loadRetired } from "@/lib/db";
import { renderMathText } from "@/lib/markdown";
import {
  applyRejectionRule,
  computeItemStats,
  MIN_ATTEMPTS,
  MIN_POINT_BISERIAL,
  TARGET_P_RANGE,
  type ItemStatus,
} from "@/lib/quality";

export const dynamic = "force-dynamic";

export const metadata: Metadata = { title: "Question stats" };

interface Props {
  params: Promise<{ course: string; lecture: string }>;
}

const STATUS_BADGE: Record<ItemStatus, { label: string; cls: string }> = {
  ok: { label: "OK", cls: "badge-ok" },
  too_easy: { label: "too easy", cls: "badge-warn" },
  too_hard: { label: "too hard", cls: "badge-bad" },
  low_discrimination: { label: "low discrimination", cls: "badge-warn" },
  insufficient_data: { label: "collecting data", cls: "badge-muted" },
};

export default async function StatsPage({ params }: Props) {
  const { course, lecture } = await params;
  if (!lectureDir(course, lecture)) notFound();

  const coursePage = getCoursePage(course);
  const stats = applyRejectionRule(computeItemStats(course, lecture));
  stats.sort((a, b) => Number(a.status === "ok") - Number(b.status === "ok") || a.question.localeCompare(b.question));
  const retired = loadRetired(course, lecture);
  const attempts = attemptCount(course, lecture);

  return (
    <>
      <Breadcrumbs
        crumbs={[
          { label: coursePage?.title ?? course, href: `/courses/${course}` },
          { label: lecture, href: `/courses/${course}/${lecture}` },
          { label: "Question stats" },
        ]}
      />
      <p className="kicker">Item analysis</p>
      <h1 className="page-title">Question statistics</h1>
      <div className="page-meta">
        <span>
          <span className="meta-label">Attempts · </span>
          {attempts}
        </span>
        <span>
          <span className="meta-label">Questions with data · </span>
          {stats.length}
        </span>
      </div>

      {stats.length === 0 ? (
        <div className="empty-note">No recorded attempts yet — take the quiz first.</div>
      ) : (
        <div className="panel">
          <div className="table-scroll">
            <table className="stats-table">
              <thead>
                <tr>
                  <th>Question</th>
                  <th>n</th>
                  <th>Difficulty p</th>
                  <th>Discrimination r_pb</th>
                  <th>Verdict</th>
                </tr>
              </thead>
              <tbody>
                {stats.map((s) => {
                  const badge = STATUS_BADGE[s.status];
                  return (
                    <tr key={s.questionId}>
                      <td>
                        <span dangerouslySetInnerHTML={{ __html: renderMathText(s.question) }} />
                        {s.reason && <div className="reason">{s.reason}</div>}
                      </td>
                      <td className="metric">{s.n}</td>
                      <td className="metric">{s.pValue.toFixed(2)}</td>
                      <td className="metric">{s.pointBiserial === null ? "n/a" : s.pointBiserial.toFixed(2)}</td>
                      <td>
                        <span className={`badge ${badge.cls}`}>{badge.label}</span>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}

      <p className="thresholds-note">
        Rejection rule (from {MIN_ATTEMPTS} attempts): a question is flagged when its difficulty p falls outside{" "}
        {TARGET_P_RANGE[0].toFixed(2)}–{TARGET_P_RANGE[1].toFixed(2)} (share answering correctly) or its point-biserial
        discrimination drops below {MIN_POINT_BISERIAL.toFixed(2)} (correlation with the rest of the attempt score).
        Retiring and regenerating flagged questions runs offline: <code>uv run python -m app.quality … --regenerate</code>.
      </p>

      {retired.length > 0 && (
        <>
          <h2 className="section-title">Retired questions</h2>
          <div className="panel">
            <div className="table-scroll">
              <table className="stats-table">
                <thead>
                  <tr>
                    <th>Question</th>
                    <th>n</th>
                    <th>p</th>
                    <th>r_pb</th>
                    <th>Reason</th>
                    <th>Retired</th>
                  </tr>
                </thead>
                <tbody>
                  {retired.map((row) => (
                    <tr key={row.id}>
                      <td>
                        <span
                          dangerouslySetInnerHTML={{
                            __html: renderMathText((JSON.parse(row.question_json) as { question: string }).question),
                          }}
                        />
                      </td>
                      <td className="metric">{row.n_attempts ?? "—"}</td>
                      <td className="metric">{row.p_value?.toFixed(2) ?? "—"}</td>
                      <td className="metric">{row.point_biserial?.toFixed(2) ?? "—"}</td>
                      <td className="reason">{row.reason}</td>
                      <td className="metric">{row.retired_at.slice(0, 10)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </>
      )}
    </>
  );
}
