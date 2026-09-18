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

## v2 (improved)

```
You are helping a recruiter triage job descriptions quickly. Summarize the
job description below into EXACTLY this format, nothing more:

**Hook (1 line):** a single sentence capturing who this role is for and
why it's interesting - not a restated title.

**Core responsibilities (max 3 bullets):** the actual day-to-day work,
most important first. Each bullet ≤ 12 words.

**Must-have requirements (max 3 bullets):** only hard requirements
explicitly stated (skills, years of experience, tools). Do not invent
requirements that aren't in the text. Each bullet ≤ 10 words.

**Flexibility notes (1 line, optional):** mention remote/hybrid/on-site or
contract length ONLY if the source text specifies it; omit this line
entirely if not mentioned.

Hard limits: total output under 80 words. No preamble, no restating the
job title as a heading, no closing remarks.

Job description:
{description}
```

**Why this is better:** the fixed word/bullet caps force real compression
instead of paraphrase-at-the-same-length; splitting responsibilities from
requirements matches how a recruiter actually scans a JD; explicitly
banning invented requirements avoids hallucinated must-haves that could
mislead a hiring decision. See `/results/test_results_and_iterations.md`
for before/after outputs on a real posting from the dataset.
