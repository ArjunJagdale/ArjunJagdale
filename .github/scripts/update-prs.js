const fs = require("fs");
const { execSync } = require("child_process");

const SECTION_HEADER = "## 🛠️ Latest Open Source Work";
const USERNAME = "ArjunJagdale";
const REPO = "huggingface/datasets";

(async () => {
  const fetch = (await import("node-fetch")).default;

  const res = await fetch(`https://api.github.com/search/issues?q=type:pr+author:${USERNAME}+repo:${REPO}+is:public&sort=created&order=desc`);
  const data = await res.json();

  const items = data.items?.slice(0, 5) || [];

  const markdown = items
    .map(pr => `- [${pr.title} (#${pr.number})](${pr.html_url})`)
    .join("\n");

  const readme = fs.readFileSync("README.md", "utf-8");

  const updated = readme.replace(
    new RegExp(`${SECTION_HEADER}[\\s\\S]*?(?=\\n##|\\n---|\\n$)`, "g"),
    `${SECTION_HEADER}\n\n${markdown}`
  );

  fs.writeFileSync("README.md", updated);

  // Git commit and push logic
  execSync('git config user.name "github-actions[bot]"');
  execSync('git config user.email "github-actions[bot]@users.noreply.github.com"');
  execSync('git add README.md');
  try {
    execSync('git commit -m "chore: update recent PRs"');
  } catch (error) {
    // No changes to commit, so just exit
    console.log("No changes to commit");
    return;
  }

  const token = process.env.GH_PAT;
  if (!token) {
    throw new Error("GH_PAT environment variable not set");
  }
  execSync(`git push https://x-access-token:${token}@github.com/ArjunJagdale/ArjunJagdale.git HEAD:main`);
})();
