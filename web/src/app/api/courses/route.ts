import { NextResponse } from "next/server";
import { createCourse } from "@/lib/manage";

interface CourseBody {
  title: string;
  slug?: string;
  instructor?: string;
  source?: string;
}

export async function POST(request: Request) {
  let body: CourseBody;
  try {
    body = (await request.json()) as CourseBody;
  } catch {
    return NextResponse.json({ error: "invalid JSON" }, { status: 400 });
  }
  if (typeof body.title !== "string") {
    return NextResponse.json({ error: "title is required" }, { status: 400 });
  }

  try {
    const { slug } = createCourse(body);
    return NextResponse.json({ slug }, { status: 201 });
  } catch (e) {
    return NextResponse.json({ error: e instanceof Error ? e.message : "failed" }, { status: 400 });
  }
}
