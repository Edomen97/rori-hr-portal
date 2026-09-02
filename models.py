from datetime import datetime
from extensions import db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), default='Hawassa, Ethiopia')
    job_type = db.Column(db.String(50), default='Full-time')
    summary = db.Column(db.Text, nullable=False)
    responsibilities = db.Column(db.Text)   # newline-separated bullet points
    requirements = db.Column(db.Text)       # newline-separated bullet points
    status = db.Column(db.String(20), default='open')  # open / closed
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)

    applications = db.relationship(
        'Application', backref='job', cascade='all, delete-orphan', lazy=True
    )

    def resp_list(self):
        return [r.strip() for r in (self.responsibilities or '').split('\n') if r.strip()]

    def req_list(self):
        return [r.strip() for r in (self.requirements or '').split('\n') if r.strip()]


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    cover_letter = db.Column(db.Text)

    cv_filename = db.Column(db.String(255))   # stored under static/uploads/cvs
    cv_link = db.Column(db.String(500))       # optional external link instead

    status = db.Column(db.String(20), default='applied')
    # applied -> shortlisted -> interview -> selected / rejected

    applied_date = db.Column(db.DateTime, default=datetime.utcnow)

    interview_date = db.Column(db.String(20))
    interview_time = db.Column(db.String(20))
    interview_location = db.Column(db.String(255))
    interview_notes = db.Column(db.Text)
