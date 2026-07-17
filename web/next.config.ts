import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Self-contained build for Docker: .next/standalone runs with `node server.js`,
  // no node_modules install needed in the runtime image.
  output: "standalone",
};

export default nextConfig;
