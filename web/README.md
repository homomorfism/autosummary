# web — course study app (TypeScript)

Next.js successor to the Flask `app/web`: a wiki-style study platform over the
repo's `data/` directory. Courses → course page (instructor, source, lecture
& materials table from `info.md`) → lecture conspect (server-rendered KaTeX,
table of contents) → self-check quiz → results → question statistics.

```bash
npm install
npm run dev        # http://localhost:3000
npm run build && npm start
```

## Deploy (Docker)

`make deploy` from the repo root rsyncs `web/` + `data/` (no media, no
node_modules) + `docker-compose.prod.yml` to the VPS and runs
`docker compose -f docker-compose.prod.yml up -d --build` there.

The compose file publishes no ports: the container (named `lectorium`) joins
the external `proxy` docker network and Caddy terminates TLS, e.g.:

```
lectorium.example.com {
    reverse_proxy lectorium:3000
}
```

The image (`web/Dockerfile`, multi-stage, Next standalone) contains only the
app — course content and `quiz_results.db` stay in the bind-mounted `data/`
directory, so redeploys keep attempts and newly synced conspects/quizzes
appear without a restart.

## Data contract

- Content comes from `../data/<course>/<lecture>/` — a lecture appears when it
  has a `conspect.md`; `quiz.json` enables the quiz. `../data/<course>/info.md`
  (title, `- **Instructor:** …` bullets, markdown lecture table) drives the
  course page; lectures found on disk but missing from the table are appended.
- Attempts are stored in the **same SQLite DB as the Python stack**
  (`../data/quiz_results.db`): identical schema and a byte-identical
  `question_id` hash (`src/lib/db.ts` mirrors `app/db.py`). The E3 loop —
  `uv run python -m app.quality … --retire --regenerate` — keeps working over
  attempts recorded here. `src/lib/quality.ts` ports the same item analysis
  for the live stats page.
- Overrides: `DATA_DIR`, `QUIZ_DB_PATH` env vars.

## Layout

- `src/lib/` — `courses.ts` (discovery + info.md parsing), `db.ts` (better-sqlite3),
  `quiz.ts`, `quality.ts` (p-value / point-biserial / rejection rule),
  `markdown.ts` (remark/rehype + KaTeX; display math in list items is stashed
  and rendered directly, same trick as `app/web`).
- `src/app/` — routes: `/`, `/courses/[course]`, `/courses/[course]/[lecture]`
  (+ `/quiz`, `/stats`), `/results/[id]`, `POST /api/attempts` (grades
  server-side; the client never sees correct answers).
