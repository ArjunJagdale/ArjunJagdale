<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=7AA2F7&center=true&vCenter=true&width=800&lines=AI+Engineer+%7C+Building+ML+Systems+That+Ship;Open+Source+Contributor+%40+Hugging+Face;Deep+Learning+%7C+Computer+Vision+%7C+NLP)](https://git.io/typing-svg)

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-7AA2F7?style=for-the-badge&logo=github&logoColor=white)](https://arjunjagdale.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/arjun-jagdale)
[![Email](https://img.shields.io/badge/Email-Reach%20Out-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:arjunjagdale14@gmail.com)
[![LeetCode](https://img.shields.io/badge/LeetCode-Solve-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://www.leetcode.com/u/ArjunJagdale/)

</div>

---

## 👋 About Me

**Turning research into production-ready ML systems.** I'm an AI engineer who codes at the intersection of deep learning research and production engineering.

---

## 🔥 What I'm Working On

- 🚀 **Contributing to Hugging Face** — datasets & dataset-viewer libraries (7 merged PRs)
- 🧠 **Research** — Published paper on Retrieval-Augmented Systems with Dynamic Learning
- 🛠️ **Building** — Production ML pipelines with real-time inference and GPU optimization
- 📚 **Learning** — Parameter-efficient methods, vision-language models, cloud-native deployments

---

## 🛠️ Tech Arsenal

<div align="center">

### Languages & Core
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### ML & AI Frameworks
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-FFD21F?style=for-the-badge&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![LangChain](https://img.shields.io/badge/🦜_LangChain-121212?style=for-the-badge)
![LlamaIndex](https://img.shields.io/badge/🦙_LlamaIndex-1A1B26?style=for-the-badge)

### Cloud & DevOps
![IBM Cloud](https://img.shields.io/badge/IBM_Cloud-1261FE?style=for-the-badge&logo=ibmcloud&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

### Tools & Libraries
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

</div>

---

## 🌟 Open Source Contributions

<div align="center">

![PRs](https://img.shields.io/badge/Merged_PRs-7-success?style=for-the-badge&logo=github)
![Repos](https://img.shields.io/badge/Repositories-2-blue?style=for-the-badge&logo=github)
![Impact](https://img.shields.io/badge/Lines_Changed-500%2B-orange?style=for-the-badge&logo=git)

**Active contributor to Hugging Face** focusing on datasets infrastructure, compatibility fixes, and developer experience

</div>

### 📦 huggingface/datasets

<table>
<tr>
<td width="10%">
<img src="https://img.shields.io/badge/MERGED-8957E5?style=for-the-badge" />
</td>
<td width="90%">

**[#7831](https://github.com/huggingface/datasets/pull/7831) • Fix ValueError in train_test_split with NumPy 2.0+**

Resolved compatibility issue with NumPy 2.0+ by wrapping stratify column array access with `np.asarray()`. Maintains backward compatibility with NumPy 1.x while fixing array copy errors.

`bug-fix` `compatibility` `numpy`

</td>
</tr>

<tr>
<td width="10%">
<img src="https://img.shields.io/badge/MERGED-8957E5?style=for-the-badge" />
</td>
<td width="90%">

**[#7648](https://github.com/huggingface/datasets/pull/7648) • Fix misleading docstring examples across multiple methods**

Updated docstrings for `add_column()`, `select_columns()`, `select()`, `filter()`, `shard()`, and `flatten()` to clarify that these methods return new datasets instead of modifying in-place. Significantly improves API documentation clarity.

`documentation` `api-improvement` `datasets`

</td>
</tr>

<tr>
<td width="10%">
<img src="https://img.shields.io/badge/MERGED-8957E5?style=for-the-badge" />
</td>
<td width="90%">

**[#7623](https://github.com/huggingface/datasets/pull/7623) • Fix: Raise error when data_dir and data_files are missing**

Added validation check in FolderBasedBuilder to prevent silent fallback to current directory when loading folder-based datasets without required parameters. Improves user experience by catching errors early.

`bug-fix` `validation` `datasets`

</td>
</tr>
</table>

### 🔍 huggingface/dataset-viewer

<table>
<tr>
<td width="10%">
<img src="https://img.shields.io/badge/MERGED-8957E5?style=for-the-badge" />
</td>
<td width="90%">

**[#3223](https://github.com/huggingface/dataset-viewer/pull/3223) • Add support for Date features in Croissant schema**

Implemented support for Date, UTCDate, and UTCTime features in Croissant schema generation. Automatically infers correct dataType (sc:Date, sc:Time, or sc:DateTime) based on format string.

`feature` `croissant` `schema`

</td>
</tr>

<tr>
<td width="10%">
<img src="https://img.shields.io/badge/MERGED-8957E5?style=for-the-badge" />
</td>
<td width="90%">

**[#3219](https://github.com/huggingface/dataset-viewer/pull/3219) • Refactor: Replace get_empty_str_list with CONSTANT.copy**

Eliminated shared mutable default values in dataclass fields by replacing helper functions with explicit constant copies. Makes configuration behavior more explicit and prevents subtle bugs.

`refactor` `best-practices` `config`

</td>
</tr>

<tr>
<td width="10%">
<img src="https://img.shields.io/badge/MERGED-8957E5?style=for-the-badge" />
</td>
<td width="90%">

**[#3218](https://github.com/huggingface/dataset-viewer/pull/3218) • Test: Add unit tests for get_previous_step_or_raise**

Implemented comprehensive unit tests for cache retrieval function covering successful cache hits, missing cache scenarios, and error status handling. Improves code coverage and reliability.

`testing` `unit-tests` `coverage`

</td>
</tr>

<tr>
<td width="10%">
<img src="https://img.shields.io/badge/MERGED-8957E5?style=for-the-badge" />
</td>
<td width="90%">

**[#3206](https://github.com/huggingface/dataset-viewer/pull/3206) • Refactor: Use HfApi.update_repo_settings for gated datasets**

Removed redundant custom implementations of `update_repo_settings()` across test utilities by leveraging official huggingface_hub API. Cleaned up **222 lines of code** while maintaining full functionality.

`refactor` `code-cleanup` `testing`

</td>
</tr>
</table>

<div align="center">

[![View All Contributions](https://img.shields.io/badge/View_All_Contributions-7AA2F7?style=for-the-badge&logo=github&logoColor=white)](https://arjunjagdale.github.io/OSS.github.io/)

</div>


---

## 📚 Research & Publications

**[Retrieval-Augmented System with Dynamic Learning from Web Content](https://papers.ssrn.com/abstract_id=5223831)**  
Published research on RAG systems that dynamically learn from web content, combining retrieval mechanisms with adaptive learning strategies.

---

## 💬 Let's Connect

<div align="center">

**Building something interesting?** I'm always open to collaborating on ML research, open source contributions, or production ML systems.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/arjun-jagdale)
[![Email](https://img.shields.io/badge/Email-arjunjagdale14@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:arjunjagdale14@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-arjunjagdale.github.io-7AA2F7?style=for-the-badge&logo=github&logoColor=white)](https://arjunjagdale.github.io/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Solve_Problems-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://www.leetcode.com/u/ArjunJagdale/)

</div>
