# Prompt 1 - Data Analysis

**Task:** Given the full `job_postings.csv` dataset, produce a recruiter-facing
market analysis: in-demand skills, salary benchmarks, and actionable insights.

**Input:** the entire dataset (as CSV text or a JSON array of records).

---

## v1 (first draft)

```
You are a data analyst. Here is a dataset of job postings. Analyze it and
tell me what you find interesting.

{dataset}
```

**Problem observed when tested:** output was a rambling, unstructured wall of
text - a few real observations buried among generic filler ("this dataset
shows a variety of roles"), no numbers pulled out, and nothing a recruiter
could act on directly. Different runs emphasized different things, so it
wasn't reliably comparable across the whole team.

## v2 (improved)

```
You are a recruitment data analyst preparing a weekly market brief for the
hiring team. You will be given a dataset of open job postings as CSV.

Analyze the dataset and return a report with exactly these five sections,
in this order:

1. **Headline stats** - total postings, number of departments, and the
   overall salary range (min–max, in the dataset's currency).
2. **Top 5 in-demand skills** - count how often each skill in
   `required_skills` appears across all postings (skills are semicolon-
   separated). Present as a ranked markdown table: rank, skill, count.
3. **Salary by seniority level** - average of (salary_min + salary_max)/2
   for each seniority_level, sorted highest to lowest, as a markdown table.
4. **Employment type mix** - a one-line breakdown of what % of postings are
   Full-time / Part-time / Contract / Internship.
5. **3 actionable insights** - each insight must reference a specific number
   from the data (not a vague trend) and end with a one-sentence
   recommendation for the recruiting team.

Rules:
- Do not editorialize outside the five sections above.
- If a calculation can't be done from the given fields, say so explicitly
  instead of guessing.
- Keep the whole report under 350 words excluding tables.

Dataset:
{dataset}
```
