# Markdown Generator

This directory contains various ways of creating Markdown for your site. In general, filenames that end with `.ipynb` or `.py` are similar, but may contain different documentation or are intended to be run from with GitHub when deploying your site.

## Python Scripts

The .py files are Python scripts that that can be run from the command line (ex., `python3 publications.py publications.csv`) with the objective of also ensuring that they have reduced requirements for packages, which may allow them to run when deploying your site from within GitHub.

## Jupyter Notebooks

These .ipynb files are Jupyter notebook files that convert a TSV containing structured data about talks (`talks.tsv`) or presentations (`presentations.tsv`) into individual markdown files that will be properly formatted for the academicpages template. The notebooks contain a lot of documentation about the process.

## Talk map

After talks exist in `_talks/`, regenerate the interactive map with:

```bash
# from the repo root
uv run python markdown_generator/talkmap.py
```

Or execute `talkmap.ipynb` from this directory. Output is written to the repo-root `talkmap/` folder (served by the site). Executed notebook dumps such as `talkmap_out.ipynb` are gitignored.
