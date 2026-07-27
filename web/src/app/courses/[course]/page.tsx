import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getCoursePage } from "@/lib/courses";

export const dynamic = "force-dynamic";

interface Props {
  params: Promise<{ course: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { course } = await params;
  const page = getCoursePage(course);
  return { title: page?.title ?? "Course" };
}

export default async function CoursePage({ params }: Props) {
  const { course } = await params;
  const page = getCoursePage(course);
  if (!page) notFound();

  const source = page.meta["Source"];
  const withConspect = page.rows.filter((r) => r.lecture).length;

  return (
    <>
      <Breadcrumbs crumbs={[{ label: page.title }]} />
      <p className="kicker">Course</p>
      <h1 className="page-title">{page.title}</h1>
      <div className="page-meta">
        {page.meta["Instructor"] && (
          <span>
            <span className="meta-label">Instructor · </span>
            {page.meta["Instructor"]}
          </span>
        )}
        {source && /^https?:\/\//.test(source) && (
          <span>
            <span className="meta-label">Source · </span>
            <a href={source} target="_blank" rel="noreferrer">
              {new URL(source).hostname}
            </a>
          </span>
        )}
        <span>
          <span className="meta-label">Notes · </span>
          {withConspect} of {page.rows.length} lectures
        </span>
      </div>
      <p style={{ marginTop: "1.25rem" }}>
        <Link href={`/courses/${page.slug}/new`} className="btn">
          + Add lecture
        </Link>
      </p>

      <div className="panel">
        <div className="table-scroll">
          <table className="lecture-table">
            <thead>
              <tr>
                <th className="num">#</th>
                <th>Lecture</th>
                <th>Materials</th>
                <th>Study</th>
              </tr>
            </thead>
            <tbody>
              {page.rows.map((row) => (
                <tr key={row.index}>
                  <td className="num">{row.index}</td>
                  <td className="lecture-title">
                    {row.lecture ? (
                      <Link href={`/courses/${page.slug}/${row.lecture.slug}`}>{row.title}</Link>
                    ) : (
                      <span className="pending">{row.title}</span>
                    )}
                  </td>
                  <td className="materials">
                    {row.materials.length
                      ? row.materials.map((m, i) => (
                          <span key={m.column}>
                            {i > 0 && " · "}
                            <a href={m.links[0].href} target="_blank" rel="noreferrer">
                              {m.column.toLowerCase()}
                            </a>
                          </span>
                        ))
                      : "—"}
                  </td>
                  <td className="status-cell">
                    {row.lecture ? (
                      <>
                        <span className="badge badge-accent">conspect</span>{" "}
                        {row.lecture.hasQuiz && <span className="badge badge-ok">quiz</span>}{" "}
                        {row.lecture.attempts > 0 && (
                          <span className="badge badge-muted">{row.lecture.attempts} attempts</span>
                        )}
                      </>
                    ) : (
                      <span className="badge badge-muted">not processed</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}
