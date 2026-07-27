import fs from "node:fs";
import path from "node:path";
import { Readable } from "node:stream";
import { pipeline } from "node:stream/promises";
import { NextResponse } from "next/server";
import { lectureDir } from "@/lib/courses";

/** Pipeline-expected filenames (app.transcribe reads video.mp4, app.conspect slides.pdf). */
const KIND_FILENAME: Record<string, string> = {
  video: "video.mp4",
  slides: "slides.pdf",
};

/** Streams the raw request body to <lecture-dir>/<video.mp4|slides.pdf> — no
 *  multipart, no buffering, so multi-GB lecture videos upload fine. */
export async function PUT(request: Request) {
  const url = new URL(request.url);
  const course = url.searchParams.get("course") ?? "";
  const lecture = url.searchParams.get("lecture") ?? "";
  const kind = url.searchParams.get("kind") ?? "";

  const filename = KIND_FILENAME[kind];
  if (!filename) return NextResponse.json({ error: "kind must be video or slides" }, { status: 400 });

  const dir = lectureDir(course, lecture);
  if (!dir) return NextResponse.json({ error: "lecture not found" }, { status: 404 });
  if (!request.body) return NextResponse.json({ error: "empty body" }, { status: 400 });

  const dest = path.join(dir, filename);
  const tmp = `${dest}.part`;
  try {
    await pipeline(
      Readable.fromWeb(request.body as import("node:stream/web").ReadableStream),
      fs.createWriteStream(tmp),
    );
    fs.renameSync(tmp, dest);
  } catch (e) {
    fs.rmSync(tmp, { force: true });
    return NextResponse.json({ error: e instanceof Error ? e.message : "upload failed" }, { status: 500 });
  }
  return NextResponse.json({ ok: true, file: filename });
}
