import type { Metadata } from "next";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { NewCourseForm } from "./NewCourseForm";

export const metadata: Metadata = { title: "Add course" };

export default function NewCoursePage() {
  return (
    <>
      <Breadcrumbs crumbs={[{ label: "Add course" }]} />
      <p className="kicker">New</p>
      <h1 className="page-title">Add course</h1>
      <p className="page-intro">
        Creates <code>data/&lt;slug&gt;/info.md</code> with the course metadata and an empty lecture table.
      </p>
      <NewCourseForm />
    </>
  );
}
