# About
Take your leetcode problems offline. Generates pdfs, html files and starter code files for each problem in `config.py`'s `LIST_OF_QUESTIONS` list. Currently it is set to the Blind 75 list `blind_75_links.txt`.

Uses the Leetcode's GraphQL API to get the problem description and starter code. This repo is a modification of https://github.com/raiyansayeed/leetcode-download-questions

# Configuration
You can change the list used, default language and file extension for the starter code in `config.py`.
The output directory is set to `output/` by default. Sub directories are created for each classification of problem as denoted with the "~" in the problem list. Each question is saved in a sub directory of its classification.

# Dependencies
See `requirements.txt` for Python dependencies. 

> **NOTE** This project uses https://pypi.org/project/pdfkit/ to convert HTML to PDF. You must install wkhtmltopdf, for MacOS you can install via brew: `brew install homebrew/cask/wkhtmltopdf`. 

# Usage
```
pip install -r requirements.txt
python main.py
```

# Notes
The code is not able to download paid questions.