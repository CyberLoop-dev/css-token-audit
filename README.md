<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0d9488&height=170&section=header&text=CSS%20Token%20Audit&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="CSS Token Audit banner">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=21&pause=900&color=2DD4BF&center=true&vCenter=true&width=700&lines=Find%20unused%20and%20undefined%20CSS%20custom%20properties" alt="Animated project title">
</p>
<p align="center">
<a href="https://github.com/CyberLoop-dev/css-token-audit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CyberLoop-dev/css-token-audit?style=flat-square" alt="License"></a>
<img src="https://img.shields.io/badge/language-Python-0d9488?style=flat-square" alt="Python">
<a href="https://github.com/CyberLoop-dev/css-token-audit/stargazers"><img src="https://img.shields.io/github/stars/CyberLoop-dev/css-token-audit?style=flat-square" alt="Stars"></a>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/css-token-audit?style=flat-square" alt="Last commit">
</p>
<p align="center"><img src="assets/icon.svg" width="520" alt="CSS Token Audit illustration"></p>

## 🧭 Overview
Audit CSS custom properties to find duplicate definitions, unused tokens, and var() references that have no definition.

## ✨ Features
- 🎨 Find custom properties declared more than once.
- 🔎 Detect var() references without a matching definition.
- 🧹 List tokens that are defined but never referenced.
- ⚙️ Run locally with Python's standard library.

## 🖥️ Demo
~~~bash
python main.py examples/styles.css
~~~
Try it with the included sample input or your own local files.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/css-token-audit.git
cd css-token-audit
python main.py examples/styles.css
~~~

## 🧰 Tech Stack
- Python 3.10+
- re, pathlib, argparse, collections (standard library)

## 🗂️ Folder Structure
~~~text
css-token-audit/\n├── assets/icon.svg\n├── examples/styles.css\n├── tests/test_main.py\n├── LICENSE\n├── README.md\n├── main.py\n└── requirements.txt
~~~

## 🗺️ Roadmap
- [ ] Add JSON output for CI integrations.
- [ ] Improve parsing around nested CSS functions and preprocessors.

## 🤝 Contributing
Issues and focused pull requests are welcome. Add tests for behavior changes and keep the project easy to run locally.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer"></p>
