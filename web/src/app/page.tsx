import Link from "next/link";
import { getCourses } from "@/lib/courses";

export const dynamic = "force-dynamic";

export default function HomePage() {
  const courses = getCourses();
  return (
    <>
      <p className="kicker">Library</p>
      <h1 className="page-title">Courses</h1>
      <p className="page-intro">
        Every course below was distilled from its lecture recordings and slides: read the conspect, then check
        yourself with the quiz.
      </p>
      <p style={{ marginTop: "1.25rem" }}>
        <Link href="/courses/new" className="btn">
          + Add course
        </Link>
      </p>

      {courses.length === 0 ? (
        <div className="empty-note">
          No courses yet — generate a conspect first: <code>uv run python -m app.conspect data/&lt;course&gt;/&lt;lecture&gt;</code>
        </div>
      ) : (
        <div className="course-grid">
          {courses.map((course) => (
            <Link key={course.slug} href={`/courses/${course.slug}`} className="course-card">
              <p className="kicker">Course</p>
              <h2>{course.title}</h2>
              {course.instructor && <p className="course-instructor">{course.instructor}</p>}
              <div className="course-stats">
                <span className="badge badge-accent">
                  {course.lectures.length} lecture{course.lectures.length === 1 ? "" : "s"}
                </span>
                <span className="badge badge-muted">
                  {course.lectures.filter((l) => l.hasQuiz).length} quiz
                  {course.lectures.filter((l) => l.hasQuiz).length === 1 ? "" : "zes"}
                </span>
                {course.totalAttempts > 0 && (
                  <span className="badge badge-ok">{course.totalAttempts} attempts</span>
                )}
              </div>
            </Link>
          ))}
        </div>
      )}
    </>
  );
}
