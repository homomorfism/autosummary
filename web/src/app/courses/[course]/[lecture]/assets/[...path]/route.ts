import fs from "node:fs";
import path from "node:path";
import { NextResponse } from "next/server";
import { lectureDir } from "@/lib/courses";

/** Lecture-dir subdirectories the conspect may embed from, with allowed types. */
const SERVABLE: Record<string, Record<string, string>> = {
  slides_images: { ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg" },
};

const FILENAME_RE = /^[A-Za-z0-9][A-Za-z0-9._-]*$/;

interface Props {
  params: Promise<{ course: string; lecture: string; path: string[] }>;
}

/** Serves conspect assets (rendered slide PNGs) from the lecture directory. */
export async function GET(_request: Request, { params }: Props) {
  const { course, lecture, path: parts } = await params;

  const dir = lectureDir(course, lecture);
  if (!dir || parts.length !== 2) return NextResponse.json({ error: "not found" }, { status: 404 });

  const [subdir, filename] = parts;
  const types = SERVABLE[subdir];
  const type = types?.[path.extname(filename).toLowerCase()];
  if (!type || !FILENAME_RE.test(filename)) {
    return NextResponse.json({ error: "not found" }, { status: 404 });
  }

  const file = path.join(dir, subdir, filename);
  if (!fs.existsSync(file)) return NextResponse.json({ error: "not found" }, { status: 404 });

  return new NextResponse(new Uint8Array(fs.readFileSync(file)), {
    headers: {
      "Content-Type": type,
      "Cache-Control": "public, max-age=3600",
    },
  });
}
