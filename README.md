# Streamlit Spell Checker App

This is a lightweight web-based **spell checker** built using [Streamlit](https://streamlit.io/) and the [`pyspellchecker`](https://pypi.org/project/pyspellchecker/) library.

## Features

- Simple text input via a web UI
- Automatic spell correction of misspelled words
- Shows corrected output in a new text area
- Highlights which words were corrected (in logs)

## Demo
https://github.com/user-attachments/assets/e4245068-01e7-48ed-bcc6-88dd1478f58b

##  How It Works

This app uses the prebuilt Python library **`pyspellchecker`**, which uses a Levenshtein Distance algorithm and a frequency dictionary to suggest the most likely corrections for misspelled words.

## Requirements

Install dependencies using `pip`:

```bash
pip install streamlit pyspellchecker
````

## How to Run

In your terminal, run:

```bash
streamlit run app.py
```

## Example

Input:

```
this is a smple text with some erors.
```

Output:

```
this is a simple text with some errors.
```

## Dependencies

* [Streamlit](https://streamlit.io/)
* [pyspellchecker](https://pypi.org/project/pyspellchecker/)

## Further Ideas

* Highlight corrected words inline
* Show original vs corrected side-by-side
* Add language selection (if supported by the library)


