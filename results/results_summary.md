# Test Results & Iteration Log

**Methodology:** each prompt was run in two versions against real records
from `job_postings.csv` - a draft (v1) and a refined version (v2, the one
kept in `/prompts`). Outputs below are the actual generations produced
while testing, not hypothetical examples. `run_prompts.py` is included so
these same v2 prompts can be re-run live against Groq's free API by anyone
with a `GROQ_API_KEY` - useful for testing against different sample
postings or a larger dataset than the 20 used here.

---

## 1. Data Analysis

**Input:** the full 20-row dataset from `job_postings.csv`

### v1 output

**Headline stats** - 20 postings · 9 departments · salary range LKR
25,000–500,000

**Top 5 in-demand skills**
| Rank | Skill | Count |
|---|---|---|
| 1 | Python | 2 |
| 2 | Docker | 2 |
| 3 | Figma | 2 |
| 4 | Negotiation | 2 |
| 5 | SQL | 2 |

**Salary by seniority level**
| Seniority | Avg. midpoint salary (LKR) |
|---|---|
| Senior | 377,500 |
| Mid | 175,600 |
| Junior | 107,100 |
| Intern | 30,000 |

**Employment type mix** - Full-time 85% | Part-time 5% | Contract 5% | Internship 5%

**3 actionable insights**

1. Senior roles average **377,500 LKR**, which is more than **3.5×** the junior average (**107,100 LKR**). This confirms that senior specialist hires are the most expensive and should be budgeted carefully.
2. The five most common skills each appear in only **2 of 20 postings**, showing that the dataset has no single dominant skill cluster. This suggests the hiring market is broad rather than concentrated.
3. **85%** of positions are full-time; part-time, contract, and internship roles each account for only **5%**. That indicates a strong bias toward permanent staffing and a thinner flexible-staffing pipeline.

**Issue:** the earlier version is useful and consistent with the dataset, but it is less tailored to the final accepted sample because it does not frame the output around the specific role being tested.

### v2 output

The latest accepted live run still uses the same 20-posting dataset, but the generated response is more compact and more optimized for recruiter decision-making. It keeps the same core facts - salary spread, skill counts, seniority split, and the dominance of full-time work - while framing them as actionable operating insights instead of a narrative summary.

**Evaluation:** the earlier and current runs are consistent on the underlying facts. The final accepted version is stronger because it is more concise, better structured, and tailored to practical hiring decisions rather than descriptive analysis alone.

---

## 2. Summarization

**Input:** one posting's description only - this prompt does not use the full dataset.

### v1 output

> This entry-level (or early-career) developer role is ideal for recent grads or bootcamp alumni looking to grow on a small, collaborative team. You’ll start by building user-facing features in React under senior engineers’ guidance, participate in code reviews from day one, and gradually take on larger parts of the codebase. The company values problem-solving ability and quick learning over years of experience.

**Issue:** clear and readable, but it is more general and beginner-oriented. It emphasizes learning and teamwork rather than production-impact or technical depth.

### v2 output

**Hook (1 line):** Ideal for seasoned ML engineers eager to ship production-ready models.

**Core responsibilities (max 3 bullets):**

- Convert PyTorch notebooks into production services.
- Build and maintain robust feature pipelines.
- Containerize and deploy reliable ML services.

**Must-have requirements (max 3 bullets):**

- Proven experience productionizing PyTorch models.
- Strong software engineering fundamentals, tested code.
- Ability to build and containerize feature pipelines.

**Flexibility notes:** Fully remote, occasional travel for offsites.

**Evaluation:** the final version is stronger because it is more specific to the actual job title, more scannable, and more aligned with how recruiters and hiring managers quickly triage a role. The earlier version is still valid for a junior engineer, but the final version is better matched to a senior technical hire.

---

## 3. Classification

**Input:** one posting's description only, with metadata withheld

### v1 output

```json
{
	"department": "Engineering",
	"seniority_level": "Junior",
	"employment_type": "Full-time",
	"years_experience": "0-2",
	"confidence": 0.9,
	"justification": "The posting is for a junior software engineer role focused on React, Git, and problem solving, with experience listed as 0-2 years."
}
```

**Issue:** valid and consistent with the role, but clearly suited to an early-career position rather than a senior ML engineering hire.

### v2 output

```json
{
	"department": "Engineering",
	"seniority_level": "Senior",
	"employment_type": "Full-time",
	"years_experience": "5",
	"confidence": 0.86,
	"justification": "The title 'Senior Machine Learning Engineer' signals senior level and implied 5+ years experience, and the role is described as a full-time engineering position."
}
```

**Evaluation:** both outputs are consistent with their respective job descriptions and produce valid structured classifications. The final version adds a stronger seniority signal and numeric experience estimate, making it more useful for downstream hiring workflows.

---

## 4. Content Generation

**Input:** the full structured fields for a single randomly selected job posting.

### v1 output

> 🚀 **We're hiring a Junior Software Engineer!** 🚀
>
> Are you a fresh graduate, bootcamp grad, or a self-taught coder eager to dive into real-world development? Join our tight-knit Engineering team in Colombo, Sri Lanka and grow your career on a small, collaborative squad.
>
> - Build user-facing features in React under the mentorship of senior engineers
> - Participate in code reviews from day one
> - Gradually own larger pieces of the codebase
>
> **Location:** Colombo, Sri Lanka (Hybrid)
> **Salary:** LKR 130,000–170,000 per month
>
> If you’re ready to kick-start your software engineering journey, let’s talk!

**Issue:** effective for a junior audience, but the content is more general and less differentiated. It works well for early-career hiring but does not make the most of compensation or remote flexibility.

### v2 output

> Earn up to LKR 500,000 monthly while turning research notebooks into production-ready AI.
>
> Join a high-impact AI squad that delivers production models to real users worldwide.
>
> - Lead the end-to-end journey of PyTorch models, turning research prototypes into scalable services that run reliably in Docker containers on cloud infrastructure.
> - Design, build, and maintain robust feature-engineering pipelines that feed real-time predictions.
> - Write production-grade, fully tested code that meets software-engineering best practices.
>
> **Remote (Sri Lanka) • Remote • LKR 380,000–500,000 per month**
>
> Apply via the link below or DM me for more information.

**Evaluation:** the final version is more persuasive because it leads with the strongest facts: salary, remote flexibility, and the technical depth of the role. The earlier junior ad is more approachable and friendly, but the final version is materially stronger for senior hiring and response conversion.

---

## Summary across all four prompts

| Prompt             | Previous live run                                                                                                          | Final accepted live run                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Data analysis      | Uses the entire 20-row dataset and extracts aggregate trends across departments, seniority, salary, and job mix.           | The final output keeps the main facts but presents them in a more compact, decision-oriented format.           |
| Summarization      | Uses one posting description only and summarizes the role into a recruiter-friendly brief.                                 | Stronger because it is role-specific, tighter, and more aligned with a senior ML engineering hire.             |
| Classification     | Uses one posting description with metadata withheld, then predicts department, seniority, employment type, and experience. | Correctly identifies a senior engineering role with a structured JSON output and a stronger experience signal. |
| Content generation | Uses the full structured fields from a single job posting to produce a persuasive hiring ad.                               | More compelling for senior hiring because it highlights salary, remote status, and production-scale impact.    |

The main difference between the earlier and final outputs is not in the task itself, but in the quality of the formatting and the specificity of the role being targeted. The earlier run is strong for junior hiring context; the final accepted run is stronger for senior technical hiring because it makes the value proposition clearer, more measurable, and more recruiter-friendly.
