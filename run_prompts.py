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
import dotenv

dotenv.load_dotenv()

GROQ_MODEL = "llama-3.3-70b-versatile"  # free-tier model on Groq as of writing
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "data", "job_postings.csv")
PROMPTS_DIR = os.path.join(HERE, "prompts")
RESULTS_PATH = os.path.join(HERE, "results", "live_run_outputs.md")
