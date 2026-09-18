# Live Groq API run - outputs

Model: `openai/gpt-oss-120b` · Sample posting used: `JP-013 - Junior Software Engineer`

## Data Analysis

```
Below is a concise, data‑driven look at the 20 job postings you shared.  
I’ve broken the analysis into three parts:

1. **High‑level statistics** – counts, averages, and distributions.  
2. **What the numbers tell us** – patterns, outliers, and “interesting” observations.  
3. **Actionable take‑aways** – ideas for recruiters, hiring managers, or anyone using this data.

---

## 1️⃣ High‑level statistics

| Metric | Value |
|--------|-------|
| **Total postings** | 20 |
| **Departments represented** | Engineering (5), Data & Analytics (4), Marketing (4), Human Resources (2), Sales (2), Finance (1), Operations (1), Customer Support (1), IT Support (1) |
| **Seniority distribution** | Junior: 6 (30 %)  <br>Mid: 8 (40 %)  <br>Senior: 5 (25 %)  <br>Intern: 1 (5 %) |
| **Employment type** | Full‑time: 17 (85 %)  <br>Part‑time: 1 (5 %)  <br>Contract: 2 (10 %) |
| **Remote‑type breakdown** | Remote (100 %): 5 (25 %)  <br>Hybrid: 9 (45 %)  <br>On‑site: 6 (30 %) |
| **Average salary (min‑max)** | **Min avg** = 115 k LKR <br>**Max avg** = 380 k LKR |
| **Average salary range width** | 71 k LKR (≈ 38 % of the midpoint) – fairly wide, especially for senior roles |
| **Experience required (mid‑point of range)** | Junior: 0‑2 yr (avg ≈ 1 yr) <br>Mid: 2‑6 yr (avg ≈ 4 yr) <br>Senior: 5‑9 yr (avg ≈ 7 yr) |
| **Most common required skill groups** | • Programming (Python, JavaScript) – 7 postings <br>• Cloud / DevOps (AWS, Kubernetes, Terraform) – 3 postings <br>• Data/Analytics (SQL, Power BI, Scikit‑learn) – 5 postings <br>• Design & Content (Figma, Adobe, SEO) – 4 postings |

### Salary by seniority (mid‑point of the advertised range)

| Seniority | Avg Min (LKR) | Avg Max (LKR) | Avg Mid‑point |
|-----------|--------------|--------------|---------------|
| Junior | 84 k | 124 k | **104 k** |
| Mid | 165 k | 236 k | **200 k** |
| Senior | 332 k | 440 k | **386 k** |
| Intern | 25 k | 35 k | **30 k** |

*All figures are simple arithmetic means; they do not account for currency conversion or cost‑of‑living adjustments.*

### Remote vs. On‑site salary comparison (mid‑point)

| Remote type | Avg Mid‑point (LKR) | # of roles |
|-------------|-------------------|------------|
| Fully Remote | 382 k | 5 |
| Hybrid | 226 k | 9 |
| On‑site | 166 k | 6 |

> **Observation:** Fully remote roles are, on average, **≈ 70 % higher** in advertised mid‑point salary than on‑site roles. The biggest driver is the concentration of senior data‑science/ML positions in the remote bucket.

---

## 2️⃣ What the numbers tell us (interesting findings)

| # | Insight | Why it matters |
|---|---------|----------------|
| **1** | **Engineering is the most represented department (25 % of all posts)** but only 5 of the 20 roles are senior‑level. | The company appears to be scaling its engineering bench (mid‑level & junior hires) while senior talent is being sourced elsewhere (e.g., remote data‑science roles). |
| **2** | **Data & Analytics roles are the highest‑paid** (average mid‑point ≈ 386 k LKR) and **all are remote**. | Indicates a strategic focus on data‑driven products and a willingness to pay a premium for remote talent in this niche. |
| **3** | **Hybrid work model dominates (45 %)**, especially for mid‑level engineering, product, and marketing roles. | Suggests the organization is transitioning away from strict on‑site work but still values in‑person collaboration for complex, cross‑functional work. |
| **4** | **Salary ranges are wide** (often > 30 % of the midpoint). For example, the Senior Data Scientist role spans 350 k–480 k LKR (≈ 37 % spread). | Wide bands may reflect flexibility for negotiation, but could also cause candidate uncertainty. Tightening ranges could improve transparency. |
| **5** | **Skill clustering** – Python appears in 4 different postings (Software Engineer, Senior Data Scientist, Senior ML Engineer, Data Analyst Intern). JavaScript/React appears only once (Junior Software Engineer). | Python is the de‑facto lingua franca for this company’s product & analytics stack, while front‑end work is still a niche need. |
| **6** | **Non‑technical roles (HR, Finance, Operations, Office Admin) are all on‑site** and have **lower salary mid‑points (≈ 170 k LKR)** compared with technical roles. | The company values physical presence for people‑operations and finance, possibly for compliance or cultural reasons. |
| **7** | **Internship pay is dramatically lower** (25 k–35 k LKR) but the role is on‑site in Kandy, not remote. | The company may be using the Kandy office as a talent pipeline for future full‑time hires. |
| **8** | **Sales & Business Development roles are hybrid and sit in the middle of the salary spectrum (160 k–220 k LKR)** despite being “revenue‑generating”. | This could indicate a more “cost‑center” view of sales, or that the company expects commissions to make up the bulk of compensation (note the Sales Executive description). |
| **9** | **Contract & Part‑time roles are limited** (Graphic Designer – contract; Content Writer – part‑time). Both are creative/marketing functions. | The firm prefers permanent staff for core product/engineering work, but uses flexible contracts for content creation, likely to keep the brand voice agile. |
| **10** | **Geographic concentration** – 14 of 20 roles list “Colombo, Sri Lanka” as the location, even when the remote type is “Hybrid”. | Colombo is the de‑facto hub; even hybrid roles expect occasional on‑site presence there. The few outliers (Galle, Kandy) are junior or support roles. |
| **11** | **Experience bands overlap** – e.g., a “Mid” Software Engineer asks for 2‑4 yr, while a “Junior” Software Engineer asks for 0‑2 yr. The overlap is intentional, but the salary bands for these two roles (180‑260 k vs. 130‑170 k) are well‑separated, reinforcing a clear progression path. | Good for internal career ladders; however, the “Mid” label on a role that also accepts 2 yr experience could cause confusion for candidates. |
| **12** | **MLOps and Model Deployment skills are explicitly required** (Senior ML Engineer, Senior Data Scientist). | The organization is moving beyond research‑only data science toward production‑grade ML pipelines. This is a relatively advanced requirement for a Sri Lankan market, justifying the higher remote salaries. |
| **13** | **Customer‑facing technical support (Customer Support Specialist) is fully remote and pays 95‑125 k LKR**, comparable to junior engineering roles. | The company values remote support talent and is willing to pay a premium for language/communication skills. |
| **14** | **Only one role mentions a “learning budget” (Software Engineer)** – a rare perk in the dataset. | Could be a differentiator for attracting senior engineers who value continuous learning. |
| **15** | **No explicit mention of benefits beyond salary** (e.g., health insurance, pension). | The posting style focuses on salary and work model; adding benefit details could improve attractiveness, especially for senior remote candidates. |

---

## 3️⃣ Actionable take‑aways

### For Recruiters / Hiring Managers
| Recommendation | Rationale |
|----------------|-----------|
| **Standardise salary ranges** – aim for a 20‑30 % spread instead of 35‑40 % for senior roles. | Reduces candidate confusion and speeds up negotiations. |
| **Highlight remote‑work premium** – especially for Data & Analytics and ML roles. | Candidates will see the clear financial upside of remote work and may be more willing to relocate or stay in Sri Lanka. |
| **Bundle “learning & development” perks** with senior engineering offers. | The Software Engineer posting already mentions a learning budget; extending this to senior engineers could improve offer acceptance. |
| **Create a “technical skill matrix”** to map required skills to seniority and salary bands. | Makes it easier to spot gaps (e.g., front‑end skills are under‑represented) and plan future hiring. |
| **Consider a “remote‑first” policy for data‑science/ML** and keep the higher salary bands. | The data shows remote roles command higher pay and attract senior talent; a remote‑first stance could reduce office‑space costs. |
| **Add benefit details** (health, pension, paid time off) to all postings. | Improves transparency and can offset lower salary offers for junior/on‑site roles. |
| **Leverage the Kandy office as a talent incubator** – turn the Data Analyst Intern into a pipeline for a full‑time analyst role after 6 months. | Low‑cost way to grow internal talent and improve retention. |
| **Re‑label “Mid” vs “Junior”** where experience overlap is high (e.g., 2 yr).** | Clearer labeling reduces candidate drop‑off due to perceived mis‑fit. |

### For Data‑Driven Decision‑Makers
| Insight | Potential Action |
|---------|------------------|
| **Engineering hires are heavily junior/mid** (80 % of engineering posts). | Plan for mentorship programs and a clear career ladder to retain talent. |
| **Remote senior talent is expensive** (average 382 k LKR). | Budget accordingly; consider a blended model where senior remote leads mentor on‑site junior staff. |
| **Marketing & Creative roles are the only contract/part‑time**. | If you need more flexibility, explore contract options for other non‑core functions (e.g., finance analysts for quarterly reporting). |
| **Sales compensation is heavily commission‑based** (base listed, “uncapped commission”). | Ensure commission structures are transparent and competitive to attract high‑performers. |
| **HR & Finance remain on‑site** despite overall hybrid trend. | Evaluate whether these functions could also benefit from hybrid or remote work to broaden talent pools. |

---

## Quick visual‑style summary (text‑only)

```
Department (count)      : Engineering (5)  Data & Analytics (4)  Marketing (4)  HR (2)  Sales (2)  Others (3)
Seniority distribution  : Junior 30% | Mid 40% | Senior 25% | Intern 5%
Remote type             : Remote 25% | Hybrid 45% | On‑site 30%
Avg. salary (mid‑point) : Junior 104k | Mid 200k | Senior 386k | Intern 30k
Top skills (freq)       : Python (4) | SQL (5) | Figma (2) | AWS (1) | Docker (2) | Selenium (1)
```

---

### TL;DR

* **Technical roles dominate** (especially mid‑level engineering) and are paid **2‑3×** more than non‑technical on‑site roles.  
* **Remote senior data‑science/ML positions command the highest salaries** and are the only fully remote senior jobs.  
* **Hybrid is the default work model** for most mid‑level product, engineering, and marketing roles.  
* **Salary ranges are wide** – tightening them could improve candidate experience.  
* **Skill clusters** (Python + SQL, Figma + design systems) reveal where the company’s product stack lives and where future hiring focus may be needed.

Feel free to let me know if you’d like deeper dives (e.g., correlation analysis, clustering of roles, or a mock salary‑budget model). Happy to help!
```

## Summarization

```
This entry‑level (or early‑career) developer role is ideal for recent grads or bootcamp alumni looking to grow on a small, collaborative team. You’ll start by building user‑facing features in React under senior engineers’ guidance, participate in code reviews from day one, and gradually take on larger parts of the codebase. The company values problem‑solving ability and quick learning over years of experience.
```

## Classification

```
**Department:** Engineering – Front‑End / Software Development  

**Seniority:** Junior (entry‑level, first or second role)  

**Employment Type:** Full‑time, permanent (standard employee position)  
```

## Content Generation

```
🚀 **We're hiring a Junior Software Engineer!** 🚀  

Are you a fresh graduate, bootcamp grad, or a self‑taught coder eager to dive into real‑world development? Join our tight‑knit Engineering team in **Colombo, Sri Lanka** and grow your career on a small, collaborative squad.

### What you’ll do
- Build user‑facing features in **React** under the mentorship of senior engineers  
- Participate in code reviews from day one  
- Gradually own larger pieces of the codebase as you level up  
- Solve problems, learn fast, and make an impact from the start  

### What we’re looking for
- 0‑2 years of experience (recent grads & bootcamp alumni welcome)  
- Strong fundamentals in **JavaScript**, **React**, **Git**, and **problem solving**  
- A passion for learning and a collaborative mindset  

### The basics
- **Location:** Colombo, Sri Lanka (Hybrid – office + remote)  
- **Employment type:** Full‑time  
- **Salary:** LKR 130,000 – 170,000 per month  
- **Team:** Engineering (Junior level)  

If you’re ready to kick‑start your software engineering journey in a supportive environment, let’s talk!  

🔗 **Apply now:** [Insert application link]  
📩 Have questions? DM me or drop a comment below.

#Hiring #JuniorSoftwareEngineer #React #JavaScript #ColomboJobs #TechCareers #Engineering #HybridWork #CareerStart #WeAreHiring
```

