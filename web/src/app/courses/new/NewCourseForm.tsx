"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export function NewCourseForm() {
  const router = useRouter();
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(null);
    setBusy(true);
    const form = new FormData(e.currentTarget);
    try {
      const res = await fetch("/api/courses", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: form.get("title"),
          slug: form.get("slug") || undefined,
          instructor: form.get("instructor") || undefined,
          source: form.get("source") || undefined,
        }),
      });
      const data = (await res.json()) as { slug?: string; error?: string };
      if (!res.ok || !data.slug) {
        setError(data.error ?? "failed to create course");
        setBusy(false);
        return;
      }
      router.push(`/courses/${data.slug}`);
    } catch {
      setError("network error");
      setBusy(false);
    }
  }

  return (
    <form className="form-card" onSubmit={submit}>
      <div className="field">
        <label htmlFor="title">Title</label>
        <input id="title" name="title" type="text" required placeholder="Deep Learning and Computer Vision, HS 2026" />
      </div>
      <div className="field">
        <label htmlFor="slug">Folder name</label>
        <input id="slug" name="slug" type="text" pattern="[A-Za-z0-9][A-Za-z0-9._-]*" placeholder="auto from title" />
        <span className="hint">
          Directory under <code>data/</code> — letters, digits, dots, dashes.
        </span>
      </div>
      <div className="field">
        <label htmlFor="instructor">Instructor</label>
        <input id="instructor" name="instructor" type="text" placeholder="Sergey Nikolenko" />
      </div>
      <div className="field">
        <label htmlFor="source">Source link</label>
        <input id="source" name="source" type="url" placeholder="https://…" />
        <span className="hint">Course home page, if any.</span>
      </div>

      {error && <p className="form-error">{error}</p>}
      <div className="form-actions">
        <button className="btn btn-primary" type="submit" disabled={busy}>
          {busy ? "Creating…" : "Create course"}
        </button>
      </div>
    </form>
  );
}
