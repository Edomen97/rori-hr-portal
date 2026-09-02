import os
from werkzeug.security import generate_password_hash

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'rori_hr.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads', 'cvs')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

    # HR admin credentials. Override with env vars before deploying publicly.
    HR_USERNAME = os.environ.get('HR_USERNAME', 'admin')
    HR_PASSWORD_HASH = os.environ.get('HR_PASSWORD_HASH') or generate_password_hash(
        os.environ.get('HR_PASSWORD', 'RoriHR2026')
    )
