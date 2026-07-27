import { NextResponse } from "next/server";
import { addLecture } from "@/lib/manage";

interface LectureBody {
  course: string;
  title: string;
  videoUrl?: string;
  slidesUrl?: string;
  hasVideoFile?: boolean;
  hasSlidesFile?: boolean;
}

export async function POST(request: Request) {
  let body: LectureBody;
  try {
    body = (await request.json()) as LectureBody;
  } catch {
    return NextResponse.json({ error: "invalid JSON" }, { status: 400 });
  }
  if (typeof body.course !== "string" || typeof body.title !== "string") {
    return NextResponse.json({ error: "course and title are required" }, { status: 400 });
  }

  try {
    const { lecture } = addLecture(body);
    return NextResponse.json({ lecture }, { status: 201 });
  } catch (e) {
    return NextResponse.json({ error: e instanceof Error ? e.message : "failed" }, { status: 400 });
  }
}
