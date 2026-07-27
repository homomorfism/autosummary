"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

/** PUT a file with upload progress (fetch has no progress events). */
function putFile(url: string, file: File, onProgress: (pct: number) => void): Promise<void> {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open("PUT", url);
    xhr.upload.onprogress = (e) => {
      if (e.lengthComputable) onProgress(Math.round((e.loaded / e.total) * 100));
    };
    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) resolve();
      else {
        try {
          reject(new Error((JSON.parse(xhr.responseText) as { error?: string }).error ?? `upload failed (${xhr.status})`));
        } catch {
          reject(new Error(`upload failed (${xhr.status})`));
        }
      }
    };
    xhr.onerror = () => reject(new Error("network error during upload"));
    xhr.send(file);
  });
}

export function NewLectureForm({ course }: { course: string }) {
  const router = useRouter();
  const [busy, setBusy] = useState(false);
  const [status, setStatus] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function submit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(null);
    setBusy(true);
    const form = new FormData(e.currentTarget);
    const videoFile = form.get("videoFile") as File | null;
    const slidesFile = form.get("slidesFile") as File | null;
    const hasVideoFile = !!videoFile?.size;
    const hasSlidesFile = !!slidesFile?.size;

    try {
      setStatus("Creating lecture…");
      const res = await fetch("/api/lectures", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          course,
          title: form.get("title"),
          videoUrl: form.get("videoUrl") || undefined,
          slidesUrl: form.get("slidesUrl") || undefined,
          hasVideoFile,
          hasSlidesFile,
        }),
      });
      const data = (await res.json()) as { lecture?: string; error?: string };
      if (!res.ok || !data.lecture) {
        setError(data.error ?? "failed to create lecture");
        setBusy(false);
        setStatus(null);
        return;
      }

      const upload = (kind: "video" | "slides", file: File) =>
        putFile(
          `/api/upload?course=${encodeURIComponent(course)}&lecture=${encodeURIComponent(data.lecture!)}&kind=${kind}`,
          file,
          (pct) => setStatus(`Uploading ${kind}… ${pct}%`),
        );
      if (hasVideoFile) await upload("video", videoFile!);
      if (hasSlidesFile) await upload("slides", slidesFile!);

      router.push(`/courses/${course}`);
      router.refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "something went wrong");
      setBusy(false);
      setStatus(null);
    }
  }

  return (
    <form className="form-card" onSubmit={submit}>
      <div className="field">
        <label htmlFor="title">Lecture title</label>
        <input id="title" name="title" type="text" required placeholder="Introduction to machine learning" />
      </div>

      <fieldset className="fieldset">
        <legend>Video</legend>
        <div className="field">
          <label htmlFor="videoUrl">Link</label>
          <input id="videoUrl" name="videoUrl" type="url" placeholder="https://www.youtube.com/watch?v=…" />
        </div>
        <div className="field">
          <label htmlFor="videoFile">File</label>
          <input id="videoFile" name="videoFile" type="file" accept="video/*" />
          <span className="hint">
            Saved as <code>video.mp4</code> in the lecture folder — the transcription input.
          </span>
        </div>
      </fieldset>

      <fieldset className="fieldset">
        <legend>Slides</legend>
        <div className="field">
          <label htmlFor="slidesUrl">Link</label>
          <input id="slidesUrl" name="slidesUrl" type="url" placeholder="https://…/slides.pdf" />
        </div>
        <div className="field">
          <label htmlFor="slidesFile">File (PDF)</label>
          <input id="slidesFile" name="slidesFile" type="file" accept="application/pdf" />
          <span className="hint">
            Saved as <code>slides.pdf</code> — the second summarization source.
          </span>
        </div>
      </fieldset>

      {error && <p className="form-error">{error}</p>}
      <div className="form-actions">
        <button className="btn btn-primary" type="submit" disabled={busy}>
          {busy ? "Working…" : "Add lecture"}
        </button>
        {status && busy && <span className="form-status">{status}</span>}
      </div>
    </form>
  );
}
