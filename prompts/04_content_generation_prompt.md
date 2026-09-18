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

## v2 (improved)

```
You are a recruitment marketer writing LinkedIn job ads that get clicks
and applications, not generic corporate copy. Using the structured job
data below, write a LinkedIn post with this exact structure:

1. **Hook line** (max 15 words) - lead with the most attractive concrete
   detail (salary, remote flexibility, or standout responsibility) - never
   start with "We are looking for" or "Join our team."
2. **2-3 short bullets** - what makes this role specifically worth
   applying to, drawn from the description (not the job title restated).
3. **Practical facts line** - location, remote_type, and salary range,
   stated plainly (candidates skip posts that hide this).
4. **Call to action** - one sentence telling the reader exactly what to do
   (e.g. "DM me or apply via the link below").
5. **3-5 hashtags** - mix of role, industry, and location tags (e.g.
   #SriLankaJobs), lowercase-free, no spaces inside a tag.

Tone: professional but warm, human-written - not a listicle, not
overhyped ("rockstar," "ninja," "fast-paced dynamic environment" are
banned words). Total length: 120-170 words including hashtags.

Job data:
{fields}
```
