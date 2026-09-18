# Prompt 2 - Summarization

**Task:** Given one long job description, produce a scannable summary a busy
recruiter or hiring manager can read in under 10 seconds.

**Input:** a single posting's `description` field (plain text).

---

## v1 (first draft)

```
Summarize this job description in a few sentences:

{description}
```

**Problem observed when tested:** the "summary" was often nearly as long as
the original (one long paragraph restating most of the sentences), and it
mixed responsibilities, requirements, and perks together with no visual
structure - no faster to scan than the source text.
