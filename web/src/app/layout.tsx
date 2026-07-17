import type { Metadata } from "next";
import Link from "next/link";
import "katex/dist/katex.min.css";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "Lectorium", template: "%s · Lectorium" },
  description: "Course notes and self-check quizzes generated from lecture recordings.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <div className="site-header-inner">
            <Link href="/" className="brand">
              <span className="brand-mark">❧</span>Lectorium
            </Link>
            <span className="brand-tagline">course notes &amp; self-check quizzes</span>
          </div>
        </header>
        <main className="container">{children}</main>
        <footer className="site-footer">Generated from lecture recordings by the autosummary pipeline.</footer>
      </body>
    </html>
  );
}
