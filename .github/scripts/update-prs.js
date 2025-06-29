const fs = require("fs");

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
})();
