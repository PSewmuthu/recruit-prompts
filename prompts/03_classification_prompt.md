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

## v2 (improved)

```
You are an ATS auto-tagging engine. Classify the job posting below and
respond with ONLY a single JSON object - no markdown fences, no
commentary before or after.

Choose exactly one value per field from these fixed lists:
- department: ["Engineering", "Data & Analytics", "Human Resources",
  "Sales", "Marketing", "Customer Support", "Product", "Finance",
  "Operations"]
- seniority_level: ["Intern", "Junior", "Mid", "Senior", "Lead"]
- employment_type: ["Full-time", "Part-time", "Contract", "Internship"]

For years_experience, extract the number/range stated or implied in the
text (e.g. "2-4"); use "0" if it reads as entry-level with no experience
mentioned.

JSON schema (fill every field, use these exact keys):
{
  "department": string,
  "seniority_level": string,
  "employment_type": string,
  "years_experience": string,
  "confidence": number,        // 0.0-1.0, your certainty in this classification
  "justification": string      // ONE short sentence citing the phrase(s) that drove the decision
}

If the text is genuinely ambiguous between two values, pick the more likely
one and lower the confidence score accordingly rather than hedging in the
text fields.

Job posting:
{description}
```

**Why this is better:** constraining every categorical field to a fixed
enum makes the output machine-parseable and directly comparable to ground
truth for accuracy scoring; the `confidence` field lets a real ATS route
low-confidence cases to a human instead of silently mis-tagging them; the
`justification` field makes the model's reasoning auditable in one glance
without bloating the output. See `/results/test_results_and_iterations.md`
for accuracy against the dataset's true labels.
