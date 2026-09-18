# Prompt 3 - Classification

**Task:** Given only the free-text `description` of a posting (no metadata),
classify it into department, seniority level, and employment type - the
kind of auto-tagging an ATS would run on an inbound job order - and output
strict, parseable JSON.

**Input:** a single posting's `description` field (plain text only - the
structured fields are hidden so this genuinely tests classification from
text, and can be checked against the dataset's real labels for accuracy).

---

## v1 (first draft)

```
Classify this job posting: department, seniority, and employment type.

{description}
```

**Problem observed when tested:** free-text answers like "This looks like a
mid-to-senior engineering role, possibly full-time" - not parseable by
downstream code, categories didn't match a fixed taxonomy (so "mid-to-
senior" can't be filtered against), and there was no confidence signal to
flag uncertain cases for human review.
