import requests
import os
import re

GH_USERNAME = os.getenv("GH_USERNAME", "ArjunJagdale")
GH_TOKEN = os.getenv("GH_PAT")  # ✅ Match your GitHub Actions secret

headers = {"Authorization": f"token {GH_TOKEN}"} if GH_TOKEN else {}

url = f"https://api.github.com/search/issues?q=type:pr+author:{GH_USERNAME}+repo:huggingface/datasets+is:public&sort=created&order=desc"
response = requests.get(url, headers=headers)
data = response.json()
items = data.get("items", [])[:5]

markdown_lines = [f"- [{item['title']} (#{item['number']})]({item['html_url']})" for item in items]
markdown = "\n".join(markdown_lines)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

pattern = r"(## 🛠️ Latest Open Source Work\n\n)([\s\S]*?)(?=\n##|\n---|\n$)"
new_readme = re.sub(pattern, rf"\1{markdown}", readme)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
