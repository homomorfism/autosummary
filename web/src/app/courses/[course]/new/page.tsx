import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getCoursePage } from "@/lib/courses";
import { NewLectureForm } from "./NewLectureForm";

export const dynamic = "force-dynamic";

interface Props {
  params: Promise<{ course: string }>;
}

export const metadata: Metadata = { title: "Add lecture" };

export default async function NewLecturePage({ params }: Props) {
  const { course } = await params;
  const page = getCoursePage(course);
  if (!page) notFound();

  return (
    <>
      <Breadcrumbs crumbs={[{ label: page.title, href: `/courses/${page.slug}` }, { label: "Add lecture" }]} />
      <p className="kicker">{page.title}</p>
      <h1 className="page-title">Add lecture</h1>
      <p className="page-intro">
        Creates the lecture folder under <code>data/{page.slug}/</code> and adds a row to the course table. Give a
        link, a file, or both for the video and slides.
      </p>
      <NewLectureForm course={page.slug} />
    </>
  );
}
