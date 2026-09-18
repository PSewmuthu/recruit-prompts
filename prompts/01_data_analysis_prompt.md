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
