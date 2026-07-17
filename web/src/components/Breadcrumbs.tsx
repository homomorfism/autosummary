import Link from "next/link";
import { Fragment } from "react";

export interface Crumb {
  label: string;
  href?: string;
}

export function Breadcrumbs({ crumbs }: { crumbs: Crumb[] }) {
  return (
    <nav className="breadcrumbs" aria-label="Breadcrumb">
      <Link href="/">Courses</Link>
      {crumbs.map((crumb, i) => (
        <Fragment key={i}>
          <span className="sep">/</span>
          {crumb.href ? <Link href={crumb.href}>{crumb.label}</Link> : <span>{crumb.label}</span>}
        </Fragment>
      ))}
    </nav>
  );
}
