# File: scripts/update_prs.py

import requests
from datetime import datetime

USERNAME = "ArjunJagdale"
REPO = "ArjunJagdale"
TOKEN = "${{ secrets.GITHUB_TOKEN }}"  # Used only in GitHub Actions

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {TOKEN}"
}

API_URL = f"https://api.github.com/search/issues?q=is:pr+author:{USERNAME}+is:open+repo:huggingface/datasets&sort=created&order=desc"

MARKER_START = "<!-- PRS:START -->"
MARKER_END = "<!-- PRS:END -->"


def fetch_recent_prs():
    response = requests.get(API_URL, headers=HEADERS)
    response.raise_for_status()
    prs = response.json()["items"][:5]
    lines = [
        f"- [{pr['title']}]({pr['html_url']})  ",
        f"  Opened on {datetime.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ').date()}"
        for pr in prs
    ]
    return "\n".join(lines)


def update_readme(pr_list):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    before = content.split(MARKER_START)[0] + MARKER_START
    after = MARKER_END + content.split(MARKER_END)[-1]
    new_content = f"{before}\n{pr_list}\n{after}"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    prs = fetch_recent_prs()
    update_readme(prs)
    print("✅ README updated with latest PRs.")
