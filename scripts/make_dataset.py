"""
Generates a synthetic (but realistic) job-postings dataset for a recruitment
agency context - used as the shared input data for all four prompts in this
prompt-engineering task.

The postings are original text written for this task (not scraped or
copied from any real job board), so there are no licensing/copyright concerns
with redistributing or publishing them.
"""

import csv
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")

# Create the data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

rows = [
    dict(
        id="JP-001", title="Software Engineer", department="Engineering",
        seniority_level="Mid", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=180000, salary_max=260000, currency="LKR",
        years_experience="2-4", required_skills="Python;Django;PostgreSQL;REST APIs;Docker",
        description=(
            "We are looking for a Software Engineer to join our growing product team. "
            "You will design, build, and maintain backend services that power our core "
            "platform, collaborate closely with product and QA, and help shape our "
            "engineering practices as we scale. The ideal candidate has hands-on "
            "experience building REST APIs in Python (Django or FastAPI), is comfortable "
            "with relational databases, and has some exposure to containerized "
            "deployments. You will participate in code reviews, write tests, and "
            "contribute to architecture discussions. We offer a hybrid work model, "
            "annual learning budget, and a supportive engineering culture that values "
            "clean code and mentorship over hero-culture overtime."
        )
    ),
    dict(
        id="JP-002", title="Senior Data Scientist", department="Data & Analytics",
        seniority_level="Senior", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Remote",
        salary_min=350000, salary_max=480000, currency="LKR",
        years_experience="5-8", required_skills="Python;Scikit-learn;SQL;A/B Testing;MLOps",
        description=(
            "Our Data & Analytics team is hiring a Senior Data Scientist to lead "
            "predictive modelling initiatives across churn, pricing, and demand "
            "forecasting. You will own projects end-to-end: framing the business "
            "problem, building and validating models, and partnering with engineering "
            "to ship them into production. We expect strong Python and SQL skills, "
            "experience running rigorous A/B tests, and familiarity with MLOps "
            "practices for model monitoring. You'll also mentor two junior data "
            "scientists and present findings directly to leadership. This is a fully "
            "remote role open to candidates anywhere in Sri Lanka, with quarterly "
            "in-person offsites."
        )
    ),
    dict(
        id="JP-003", title="Data Analyst Intern", department="Data & Analytics",
        seniority_level="Intern", employment_type="Internship",
        location="Kandy, Sri Lanka", remote_type="On-site",
        salary_min=25000, salary_max=35000, currency="LKR",
        years_experience="0", required_skills="Excel;SQL basics;Power BI;Statistics",
        description=(
            "A 6-month internship for a final-year undergraduate interested in data "
            "analytics. You will support the team by cleaning datasets, building "
            "simple dashboards in Power BI, and drafting weekly summary reports for "
            "stakeholders. No professional experience is required, but comfort with "
            "spreadsheets, basic SQL, and an interest in statistics is expected. This "
            "is a great first step for someone who wants to build a portfolio of real "
            "business analytics work under the guidance of a senior analyst. On-site "
            "presence in our Kandy office is required three days a week."
        )
    ),
    dict(
        id="JP-004", title="DevOps Engineer", department="Engineering",
        seniority_level="Mid", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=220000, salary_max=300000, currency="LKR",
        years_experience="3-5", required_skills="AWS;Kubernetes;Terraform;CI/CD;Linux",
        description=(
            "Join our platform team as a DevOps Engineer responsible for the "
            "reliability and scalability of our AWS-hosted infrastructure. You'll "
            "manage Kubernetes clusters, build and improve CI/CD pipelines, and "
            "codify infrastructure with Terraform. Strong Linux fundamentals and "
            "an on-call rotation mindset are essential. You will also work with "
            "security to harden our environments and reduce cloud spend through "
            "smarter autoscaling. Prior experience supporting a production system "
            "with real users is strongly preferred."
        )
    ),
    dict(
        id="JP-005", title="HR Business Partner", department="Human Resources",
        seniority_level="Senior", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="On-site",
        salary_min=250000, salary_max=320000, currency="LKR",
        years_experience="6-10", required_skills="Employee Relations;Performance Management;Labor Law;Coaching",
        description=(
            "We're seeking an experienced HR Business Partner to act as a strategic "
            "advisor to two of our business units. You will guide managers through "
            "performance management cycles, resolve employee relations issues with "
            "sound judgement, and ensure our practices comply with local labor law. "
            "The right candidate builds trust quickly, coaches leaders through "
            "difficult conversations, and can translate business goals into people "
            "strategy. This is an on-site role based at our Colombo head office, "
            "with occasional travel to regional branches."
        )
    ),
    dict(
        id="JP-006", title="Sales Executive", department="Sales",
        seniority_level="Junior", employment_type="Full-time",
        location="Galle, Sri Lanka", remote_type="On-site",
        salary_min=90000, salary_max=140000, currency="LKR",
        years_experience="1-2", required_skills="Cold Calling;CRM (HubSpot);Negotiation;B2B Sales",
        description=(
            "We're expanding our southern-region sales team and looking for an "
            "energetic Sales Executive to generate and close new B2B business. "
            "Responsibilities include cold outreach, running product demos, "
            "negotiating contracts, and maintaining accurate pipeline records in "
            "HubSpot. A base salary plus uncapped commission structure rewards "
            "top performers well beyond the listed range. Prior sales experience "
            "is a plus but not required for candidates who can demonstrate strong "
            "communication skills and resilience."
        )
    ),
    dict(
        id="JP-007", title="Marketing Manager", department="Marketing",
        seniority_level="Mid", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=200000, salary_max=270000, currency="LKR",
        years_experience="4-6", required_skills="Content Strategy;SEO;Google Analytics;Campaign Management",
        description=(
            "As Marketing Manager you will own our digital marketing calendar "
            "across content, SEO, and paid channels. You'll plan and execute "
            "campaigns, analyze performance in Google Analytics, and work with "
            "an external design agency to keep brand output consistent. We're "
            "looking for someone who can both write compelling copy and read a "
            "funnel report, translating data into next quarter's content plan. "
            "You'll manage one junior marketing executive directly."
        )
    ),
    dict(
        id="JP-008", title="Customer Support Specialist", department="Customer Support",
        seniority_level="Junior", employment_type="Full-time",
        location="Remote (Sri Lanka)", remote_type="Remote",
        salary_min=95000, salary_max=125000, currency="LKR",
        years_experience="0-2", required_skills="Zendesk;Written Communication;Troubleshooting;Empathy",
        description=(
            "Be the first point of contact for our customers via chat and email. "
            "You will troubleshoot product issues, escalate bugs to engineering "
            "with clear reproduction steps, and maintain a friendly, patient tone "
            "even in frustrating situations. We use Zendesk for ticketing and "
            "measure success by resolution time and customer satisfaction score, "
            "not just ticket volume. This role is fully remote with a rotating "
            "shift schedule covering Sri Lanka and UK business hours."
        )
    ),
    dict(
        id="JP-009", title="Product Manager", department="Product",
        seniority_level="Senior", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=320000, salary_max=420000, currency="LKR",
        years_experience="5-8", required_skills="Product Discovery;Roadmapping;SQL;Stakeholder Management",
        description=(
            "We're hiring a Senior Product Manager to own our core analytics "
            "product line. You will run discovery interviews with customers, "
            "prioritize a roadmap balancing technical debt and new features, and "
            "write clear specs that engineering can execute against without "
            "constant clarification. Comfort querying data directly in SQL to "
            "validate hypotheses is expected. You'll report to the Head of "
            "Product and work closely with design, engineering, and sales."
        )
    ),
    dict(
        id="JP-010", title="Graphic Designer", department="Marketing",
        seniority_level="Junior", employment_type="Contract",
        location="Colombo, Sri Lanka", remote_type="Remote",
        salary_min=70000, salary_max=110000, currency="LKR",
        years_experience="1-3", required_skills="Figma;Adobe Illustrator;Brand Guidelines;Social Media Design",
        description=(
            "We need a Graphic Designer on a 6-month contract to produce social "
            "media assets, presentation decks, and occasional print collateral. "
            "You'll work from our existing brand guidelines but should bring a "
            "sharp eye for what performs well on Instagram and LinkedIn. Deliver "
            "a mix of static and short animated assets in Figma and Adobe tools, "
            "turning around requests within a 48-hour SLA. Portfolio review is "
            "part of the interview process."
        )
    ),
    dict(
        id="JP-011", title="Content Writer", department="Marketing",
        seniority_level="Mid", employment_type="Part-time",
        location="Remote (Sri Lanka)", remote_type="Remote",
        salary_min=60000, salary_max=90000, currency="LKR",
        years_experience="2-4", required_skills="SEO Writing;Editing;Research;WordPress",
        description=(
            "Our blog needs a steady hand. This part-time Content Writer role "
            "involves researching and drafting two long-form articles per week "
            "on B2B SaaS topics, optimizing for SEO without sacrificing "
            "readability, and publishing directly through WordPress. You'll "
            "work from an editorial calendar set collaboratively with the "
            "Marketing Manager and receive feedback through tracked-change "
            "reviews. Prior experience writing for a technical or business "
            "audience is required."
        )
    ),
    dict(
        id="JP-012", title="Financial Analyst", department="Finance",
        seniority_level="Mid", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="On-site",
        salary_min=170000, salary_max=230000, currency="LKR",
        years_experience="3-5", required_skills="Excel Modeling;Forecasting;Variance Analysis;ERP Systems",
        description=(
            "We are hiring a Financial Analyst to support monthly close, "
            "budgeting, and forecasting cycles. You will build and maintain "
            "Excel models for departmental budgets, investigate variances "
            "against forecast, and prepare board-ready summaries. Experience "
            "with an ERP system (SAP or NetSuite) is a plus. Strong attention "
            "to detail and the ability to explain financial concepts to "
            "non-finance stakeholders are essential."
        )
    ),
    dict(
        id="JP-013", title="Junior Software Engineer", department="Engineering",
        seniority_level="Junior", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=130000, salary_max=170000, currency="LKR",
        years_experience="0-2", required_skills="JavaScript;React;Git;Problem Solving",
        description=(
            "A great first (or second) role for a developer who wants to grow "
            "on a small, collaborative team. You will build user-facing features "
            "in React under the guidance of senior engineers, participate in "
            "code review from day one, and gradually take on larger pieces of "
            "the codebase. We care more about your ability to reason through "
            "problems and learn quickly than about years on your CV. Recent "
            "graduates and bootcamp alumni are encouraged to apply."
        )
    ),
    dict(
        id="JP-014", title="Recruitment Consultant", department="Human Resources",
        seniority_level="Mid", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=140000, salary_max=190000, currency="LKR",
        years_experience="2-4", required_skills="Sourcing;Client Management;Interviewing;ATS Tools",
        description=(
            "As a Recruitment Consultant you will manage the full recruitment "
            "lifecycle for a portfolio of client accounts: sourcing candidates, "
            "screening resumes and conducting first-round interviews, and "
            "advising clients on market salary benchmarks. You'll use our ATS "
            "to track pipeline health and report weekly on time-to-fill metrics. "
            "This role suits someone who enjoys both people-facing work and the "
            "operational discipline of a structured pipeline."
        )
    ),
    dict(
        id="JP-015", title="QA Engineer", department="Engineering",
        seniority_level="Mid", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=180000, salary_max=240000, currency="LKR",
        years_experience="2-4", required_skills="Test Automation;Selenium;API Testing;Bug Tracking",
        description=(
            "We're looking for a QA Engineer to build out automated test "
            "coverage across our web application and public API. You will "
            "design test plans for new features, maintain a growing Selenium "
            "suite, and work closely with engineers to reproduce and triage "
            "reported bugs. A mindset of 'break it before customers do' paired "
            "with clear, reproducible bug reports will make you successful here."
        )
    ),
    dict(
        id="JP-016", title="Machine Learning Engineer", department="Data & Analytics",
        seniority_level="Senior", employment_type="Full-time",
        location="Remote (Sri Lanka)", remote_type="Remote",
        salary_min=380000, salary_max=500000, currency="LKR",
        years_experience="5-9", required_skills="PyTorch;Model Deployment;Docker;Feature Engineering",
        description=(
            "Our ML team needs a Senior Machine Learning Engineer to take models "
            "from notebook to production. You'll work with data scientists to "
            "productionize PyTorch models, build robust feature pipelines, and "
            "containerize services for reliable deployment. Strong software "
            "engineering fundamentals matter as much as ML knowledge here — we "
            "expect tested, maintainable code, not one-off scripts. Fully remote "
            "with occasional travel for team offsites."
        )
    ),
    dict(
        id="JP-017", title="Office Administrator", department="Operations",
        seniority_level="Junior", employment_type="Full-time",
        location="Kandy, Sri Lanka", remote_type="On-site",
        salary_min=65000, salary_max=90000, currency="LKR",
        years_experience="1-3", required_skills="Scheduling;Vendor Management;MS Office;Organization",
        description=(
            "We need a dependable Office Administrator to keep our Kandy branch "
            "running smoothly: managing supplies and vendor relationships, "
            "coordinating meeting schedules for leadership, and serving as the "
            "first point of contact for visitors. This role is highly varied "
            "day-to-day and suits someone who takes pride in a well-run office "
            "and enjoys being the person others rely on to get things sorted."
        )
    ),
    dict(
        id="JP-018", title="UI/UX Designer", department="Product",
        seniority_level="Mid", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=190000, salary_max=260000, currency="LKR",
        years_experience="3-5", required_skills="Figma;User Research;Prototyping;Design Systems",
        description=(
            "Join our product team as a UI/UX Designer responsible for turning "
            "rough problem statements into polished, tested interfaces. You will "
            "run light-weight user research, prototype flows in Figma, and "
            "maintain our growing design system so the product feels coherent "
            "as it scales. You'll partner closely with the Senior Product "
            "Manager and present design rationale directly to engineering."
        )
    ),
    dict(
        id="JP-019", title="Business Development Executive", department="Sales",
        seniority_level="Mid", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="Hybrid",
        salary_min=160000, salary_max=220000, currency="LKR",
        years_experience="3-5", required_skills="Partnerships;Market Research;Negotiation;Presentation",
        description=(
            "We are hiring a Business Development Executive to identify and "
            "close strategic partnerships that open new revenue channels. You "
            "will research target markets, build a business case for each "
            "opportunity, and lead negotiations through to signed agreements. "
            "This role requires equal parts analytical rigor and relationship-"
            "building instinct, and reports directly to the Head of Sales."
        )
    ),
    dict(
        id="JP-020", title="IT Support Technician", department="Engineering",
        seniority_level="Junior", employment_type="Full-time",
        location="Colombo, Sri Lanka", remote_type="On-site",
        salary_min=85000, salary_max=115000, currency="LKR",
        years_experience="0-2", required_skills="Windows/macOS Support;Networking Basics;Ticketing Systems;Hardware Troubleshooting",
        description=(
            "Our internal IT Support Technician keeps 80+ employees productive "
            "by resolving hardware and software issues quickly, managing laptop "
            "provisioning for new hires, and maintaining basic network "
            "infrastructure across our office. You'll triage tickets by "
            "priority, document recurring issues to reduce repeat tickets, and "
            "escalate complex networking problems to our outsourced IT partner."
        )
    )
]

fieldnames = [
    "id", "title", "department", "seniority_level", "employment_type",
    "location", "remote_type", "salary_min", "salary_max", "currency",
    "years_experience", "required_skills", "description"
]

with open(os.path.join(DATA_DIR, "job_postings.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"Wrote {len(rows)} job postings.")
