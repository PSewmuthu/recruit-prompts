"""
Runs all four prompts (data analysis, summarization, classification,
content generation) against the job_postings.csv dataset using Groq's
free-tier API, and writes each response to results/live_run_outputs.md.

Setup:
    pip install requests
    export GROQ_API_KEY="your-free-key-from-console.groq.com" or add it to your .env file
Run:
    python run_prompts.py

Note: this script makes live network calls to api.groq.com, so it needs to
be run in an environment with outbound internet access and a valid key -
it will not run inside a network-restricted sandbox.
"""
import csv
import json
import os
import sys

import requests
import random
import dotenv

dotenv.load_dotenv()

GROQ_MODEL = "llama-3.3-70b-versatile"  # free-tier model on Groq as of writing
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "data", "job_postings.csv")
PROMPTS_DIR = os.path.join(HERE, "prompts")
RESULTS_PATH = os.path.join(HERE, "results", "live_run_outputs.md")


def call_groq_api(prompt: str, temperature: float = 0.3) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        sys.exit("Error: GROQ_API_KEY not set in environment variables or .env file.")

    resp = requests.post(
        GROQ_URL,
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": GROQ_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature
        },
        timeout=60
    )
    resp.raise_for_status()

    return resp.json()["choices"][0]["message"]["content"]


def load_dataset():
    with open(DATA_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def extract_prompt_body(md_path: str) -> str:
    """
    Pulls the final prompt templte out of the markdown file - 
    the text inside the last code block (```...```) in the file.
    """

    text = open(md_path, encoding='utf-8').read()
    blocks = text.split("```")
    code_blocks = blocks[1::2]

    return code_blocks[-1].strip() if code_blocks else ""


def main():
    os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)
    dataset = load_dataset()
    sample = random.choice(dataset)  # use for the single-posting prompts

    with open(DATA_PATH, encoding='utf-8') as f:
        full_dataset_text = f.read()

    outputs = {}

    # 1. Data Analysis Prompt - whole dataset
    p1 = extract_prompt_body(os.path.join(
        PROMPTS_DIR, "01_data_analysis_prompt.md"))
    outputs["data_analysis"] = call_groq_api(
        p1.replace("{dataset}", full_dataset_text))

    # 2. Summarization Prompt - one posting's description only
    p2 = extract_prompt_body(os.path.join(
        PROMPTS_DIR, "02_summarization_prompt.md"))
    outputs["summarization"] = call_groq_api(
        p2.replace("{description}", sample["description"]))

    # 3. Classification Prompt - description only, metadata withheld
    p3 = extract_prompt_body(os.path.join(
        PROMPTS_DIR, "03_classification_prompt.md"))
    outputs["classification"] = call_groq_api(p3.replace(
        "{description}", sample["description"]), temperature=0.1)

    # 4. Content Generation Prompt - full structured fields
    p4 = extract_prompt_body(os.path.join(
        PROMPTS_DIR, "04_content_generation_prompt.md"))
    fields_json = json.dumps(sample, indent=2)
    outputs["content_generation"] = call_groq_api(
        p4.replace("{fields}", fields_json))

    with open(RESULTS_PATH, "w", encoding='utf-8') as f:
        f.write("# Live Groq API run - outputs\n\n")
        f.write(
            f"Model: `{GROQ_MODEL}` · Sample posting used: `{sample['id']} - {sample['title']}`\n\n")
        for name, out in outputs.items():
            f.write(f"## {name.replace('_', ' ').title()}\n\n")
            f.write(f"```\n{out}\n```\n\n")

    print(f"Done! Outputs written to {RESULTS_PATH}")


if __name__ == "__main__":
    main()
