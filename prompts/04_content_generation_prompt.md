# Prompt 4 - Content Generation

**Task:** Given a posting's structured fields, generate a LinkedIn-ready job
ad that will actually attract applicants - the kind of content a recruiter
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

**Problem observed when tested:** generic corporate-brochure tone ("We are
seeking a talented individual to join our dynamic team!"), no salary or
location surfaced even though both were provided, no call-to-action, and
no hashtags - i.e. missing the specific things that actually make a job
post perform on LinkedIn.
