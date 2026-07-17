import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import fs from "node:fs";
import path from "node:path";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getCoursePage, lectureDir } from "@/lib/courses";
import { attemptCount } from "@/lib/db";
import { renderMarkdown } from "@/lib/markdown";

export const dynamic = "force-dynamic";

interface Props {
  params: Promise<{ course: string; lecture: string }>;
}

function loadConspect(course: string, lecture: string): string | null {
  const dir = lectureDir(course, lecture);
  if (!dir) return null;
  const conspectPath = path.join(dir, "conspect.md");
  if (!fs.existsSync(conspectPath)) return null;
  return fs.readFileSync(conspectPath, "utf-8");
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { course, lecture } = await params;
  const conspect = loadConspect(course, lecture);
  const title = conspect?.split("\n").find((l) => l.startsWith("# "));
  return { title: title ? title.slice(2).trim() : "Lecture" };
}

export default async function LecturePage({ params }: Props) {
  const { course, lecture } = await params;
  const conspect = loadConspect(course, lecture);
  if (!conspect) notFound();

  const coursePage = getCoursePage(course);
  const { html, toc, title } = await renderMarkdown(conspect);
  const hasQuiz = fs.existsSync(path.join(lectureDir(course, lecture)!, "quiz.json"));
  const attempts = attemptCount(course, lecture);

  return (
    <>
      <Breadcrumbs
        crumbs={[
          { label: coursePage?.title ?? course, href: `/courses/${course}` },
          { label: title ?? lecture },
        ]}
      />
      <p className="kicker">Lecture conspect</p>
      <h1 className="page-title">{title ?? lecture}</h1>

      <div className="action-bar">
        {hasQuiz && (
          <Link href={`/courses/${course}/${lecture}/quiz`} className="btn btn-primary">
            Check yourself →
          </Link>
        )}
        <Link href={`/courses/${course}/${lecture}/stats`} className="btn">
          Question stats
        </Link>
        <span className="spacer" />
        <span className="attempts-note">
          {attempts > 0 ? `${attempts} quiz attempt${attempts === 1 ? "" : "s"} so far` : "no quiz attempts yet"}
        </span>
      </div>

      <div className="lecture-layout">
        <article className="prose" dangerouslySetInnerHTML={{ __html: html }} />
        {toc.length > 1 && (
          <aside className="toc">
            <p className="toc-title">On this page</p>
            <ul>
              {toc.map((entry) => (
                <li key={entry.id} className={`depth-${entry.depth}`}>
                  <a href={`#${entry.id}`}>{entry.text}</a>
                </li>
              ))}
            </ul>
          </aside>
        )}
      </div>
    </>
  );
}
