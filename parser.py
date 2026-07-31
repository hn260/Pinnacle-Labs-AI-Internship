import pdfplumber
import re
import pandas as pd


def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                text += txt + "\n"
    return text


def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not Found"


def extract_phone(text):
    match = re.search(r'(\+91[- ]?)?[6-9]\d{9}', text)
    return match.group(0) if match else "Not Found"


def extract_name(text):
    lines = text.split("\n")
    return lines[0] if lines else "Not Found"


def extract_skills(text):
    skills = pd.read_csv("skills.csv", header=None)[0].tolist()

    found = []

    for skill in skills:
        if skill.lower() in text.lower():
            found.append(skill)

    return list(set(found))
