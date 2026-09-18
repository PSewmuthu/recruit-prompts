# Prompt 4 — Content Generation

**Task:** Given a posting's structured fields, generate a LinkedIn-ready job
ad that will actually attract applicants — the kind of content a recruiter
needs to post multiple times a week and can't hand-write from scratch
every time.

**Input:** one posting's structured fields (title, department, seniority,
location, remote_type, salary range, required_skills, description).

---

## v1 (first draft)

```
Write a LinkedIn post advertising this job:

{fields}
```
