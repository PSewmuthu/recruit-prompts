# Prompt Engineering - Recruitment Job Postings

A prompt-engineering exercise built around a realistic recruitment-agency
use case: given a dataset of open job postings, four prompts handle **data
analysis**, **summarization**, **classification**, and **content
generation** - the kind of work a recruiter actually does with a stack of
job orders every week.

## Why this use case

The task asked for four general-purpose prompt types on any dataset. This
project ties them together around one coherent workflow instead of four
unrelated toy examples, and picks a domain (recruitment) that's directly
relevant to real hiring-team work.

## Folder structure

```
data/
  job_postings.csv          20 synthetic-but-realistic job postings
prompts/
  01_data_analysis_prompt.md        market brief across all postings
  02_summarization_prompt.md        scannable TL;DR of one posting
  03_classification_prompt.md       auto-tag dept/seniority/type as JSON
  04_content_generation_prompt.md   LinkedIn job ad from structured fields
results/
  results_summary.md                v1 vs v2 outputs + evaluation for each
  live_run_outputs.md               latest outputs from a live Groq API run
scripts/
  make_dataset.py            regenerates data/job_postings.csv
run_prompts.py               runs the 4 final prompts live via Groq's API
README.md                    this file
```

## The dataset

`data/job_postings.csv` - 20 postings spanning 9 departments (Engineering,
Data & Analytics, HR, Sales, Marketing, Customer Support, Product,
Finance, Operations), 4 seniority levels, and 4 employment types. Each row
has structured fields (title, department, seniority, salary range,
location, remote type, required skills) plus a full free-text
`description`, so the same record can be used both as structured input
(prompts 1 and 4) and as text-only input for a genuine text-classification
test (prompt 3). The postings are original text written for this
assignment - not scraped from a real job board - so there's no licensing
concern with including or publishing them.

## Each prompt, and how it was tested

Every prompt in `/prompts` documents its own **v1 → v2 iteration**: the
first draft, the specific quality problem observed when run against the
dataset, and the refined final version. The full before/after outputs
(not just descriptions of them) are in
`results/results_summary.md`, along with an evaluation of each v2 output.
The latest live API responses are recorded separately in
`results/live_run_outputs.md`.

**The pattern that held across all four prompts:** the v1 drafts were
open-ended ("summarize this," "analyze this") and produced plausible but
low-utility output - vague, inconsistent length, or not machine-parseable.
Every v2 fix was a **structural constraint** - a fixed section list, a hard
word cap, an output JSON schema, a required confidence score - not a
change to the underlying task. That's the main takeaway of this exercise:
for these four task types, the biggest quality lever isn't rephrasing the
ask, it's constraining the shape of the answer.

## Reproducing / re-testing the prompts live

`run_prompts.py` runs all four final (v2) prompts against the dataset
using [Groq's free-tier API](https://console.groq.com) (OpenAI-compatible,
no cost for the model used here):

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your key, or set it in your shell:

```bash
export GROQ_API_KEY="your-key-from-console.groq.com"
```

On Windows PowerShell, use:

```powershell
$env:GROQ_API_KEY = "your-key-from-console.groq.com"
```

Then run:

```bash
python run_prompts.py
```

This writes fresh outputs to `results/live_run_outputs.md`. The data-analysis
prompt receives the full CSV. The summarization and classification prompts
receive only the randomly selected posting's description; classification is
not given the posting's metadata. The content-generation prompt receives all
structured fields from that same selected posting. The sample is selected
anew on each run, so the three single-posting outputs may vary. To use a
different model, change `GROQ_MODEL` at the top of the script.

**Note on how this submission itself was tested:** the outputs documented
in `results_summary.md` were produced by directly executing
each prompt against the sample data (v1 and v2, side by side) rather than
through a live API call, since the environment used to assemble this
submission has network access to a fixed allow-list that doesn't include
`api.groq.com`. `run_prompts.py` is provided precisely so the same v2
prompts can be independently re-run against the live API - the prompts
themselves are unchanged between the two testing paths.

## Key learnings

1. **Constrain the output shape, not just the task.** Every meaningful
   quality jump came from specifying sections, word limits, or a JSON
   schema - not from better task phrasing.
2. **Ban known failure modes explicitly.** Naming clichés to avoid
   ("rockstar," "dynamic environment") or rules to follow ("don't invent
   requirements not in the text") removed specific, predictable errors
   that vaguer instructions didn't catch.
3. **Ask for a confidence signal on judgment calls.** For classification
   especially, a confidence score turns a black-box guess into something
   a human reviewer can triage.
4. **Ground evaluation in checkable numbers.** Where possible (data
   analysis, classification), outputs were checked against an independent
   calculation or the dataset's true labels rather than judged by feel
   alone.
