# Rori Hotel Hawassa — Careers & Recruitment Portal

A Flask + SQLite HR system for Rori Hotel Hawassa covering the full recruitment flow:
candidate views a job → applies with CV → HR sees it on a dashboard → shortlist → interview → selected.

## Features

- Public site: Home, Careers / Job Openings, Job Details, Online Application with CV upload
- HR Admin (password-protected): Dashboard, Job Postings, Candidate Management, Interview
  Management, Reports
- Mobile responsive (Bootstrap 5)
- SQLite database (auto-created on first run, seeded with 3 sample jobs)

## Local setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`. HR login is at `/hr/login`.

**Default HR login:** `admin` / `RoriHR2026`
Change this before deploying publicly — see Environment Variables below.

## Environment variables

| Variable       | Purpose                                   | Default              |
|----------------|--------------------------------------------|----------------------|
| `SECRET_KEY`   | Flask session signing key                  | dev key (change it)  |
| `HR_USERNAME`  | HR admin username                          | `admin`               |
| `HR_PASSWORD`  | HR admin password (hashed at startup)      | `RoriHR2026`          |
| `DATABASE_URL` | Database connection string                 | local SQLite file    |

## Deploying to GitHub + Render

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit — Rori Hotel Hawassa Careers Portal"
   git branch -M main
   git remote add origin <your-empty-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com) → New → Web Service → connect your GitHub repo.
   - Render will detect `render.yaml` automatically (or set manually):
     - Build command: `pip install -r requirements.txt`
     - Start command: `gunicorn app:app`
   - Under Environment, set `HR_USERNAME` and `HR_PASSWORD` to your real credentials, and let
     `SECRET_KEY` auto-generate.
   - Deploy. Render gives you a live URL such as `https://rori-hr-portal.onrender.com`.

3. **Note on storage:** Render's free-tier filesystem is ephemeral — uploaded CVs and the SQLite
   file can be wiped on redeploy. For production use, add a Render persistent disk (Render
   dashboard → your service → Disks) mounted at `/instance` and `/static/uploads`, or move to a
   managed Postgres database + S3-style storage for CVs.

## Project structure

```
rori-hr-portal/
├── app.py               # app factory + seed data
├── config.py             # settings, HR credentials
├── extensions.py         # SQLAlchemy instance
├── models.py              # Job, Application models
├── routes/
│   ├── public.py          # home, careers, job detail, apply
│   └── admin.py            # HR login, dashboard, jobs, candidates, interviews, reports
├── templates/
│   ├── base.html, home.html, careers.html, job_detail.html, apply.html, apply_success.html
│   ├── partials/           # public_nav.html, admin_nav.html
│   └── admin/               # login, dashboard, jobs, candidates, candidate_detail, interviews, reports
├── static/css/style.css   # navy/gold branding
└── static/uploads/cvs/    # uploaded CV files
```

## Next steps for v2

- Replace placeholder hotel contact details and logo image in `templates/home.html`
- Add email notifications to candidates on status change
- Multi-admin accounts with roles instead of one shared HR login
- Export candidate reports to Excel/PDF
