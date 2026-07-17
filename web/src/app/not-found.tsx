import Link from "next/link";

export default function NotFound() {
  return (
    <div className="empty-note">
      <p style={{ fontSize: "1.1rem", fontWeight: 600 }}>Page not found</p>
      <p>
        This course, lecture, or attempt doesn&apos;t exist. <Link href="/">Back to the courses</Link>.
      </p>
    </div>
  );
}
