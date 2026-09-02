import os
from flask import Flask

from config import Config
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

    db.init_app(app)

    from routes.public import public_bp
    from routes.admin import admin_bp
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()
        seed_data()

    return app


def seed_data():
    from models import Job

    if Job.query.count() > 0:
        return

    jobs = [
        Job(
            title='Front Desk Agent',
            department='Guest Services',
            location='Hawassa, Ethiopia',
            job_type='Full-time',
            summary="Be the first face our guests see. Manage check-in, check-out, and guest "
                    "requests with warmth and precision.",
            responsibilities="Welcome guests and manage check-in / check-out\n"
                              "Handle reservations, billing, and guest inquiries\n"
                              "Coordinate with housekeeping and food & beverage teams\n"
                              "Resolve guest concerns promptly and professionally",
            requirements="Diploma in Hotel Management or related field\n"
                         "1+ years front office experience preferred\n"
                         "Fluent in Amharic and English\n"
                         "Friendly, well-presented, and detail-oriented",
        ),
        Job(
            title='Chef de Partie',
            department='Food & Beverage',
            location='Hawassa, Ethiopia',
            job_type='Full-time',
            summary="Own a section of our kitchen and help deliver a dining experience that "
                    "matches Rori Hotel's standards.",
            responsibilities="Prepare and present dishes to hotel quality standards\n"
                              "Supervise commis chefs within your section\n"
                              "Maintain hygiene and food-safety standards\n"
                              "Manage stock and minimize waste",
            requirements="Culinary certification or equivalent experience\n"
                         "2+ years kitchen experience, hotel/restaurant setting\n"
                         "Knowledge of both local and international cuisine\n"
                         "Able to work shifts including weekends and holidays",
        ),
        Job(
            title='Sales & Marketing Executive',
            department='Sales & Marketing',
            location='Hawassa, Ethiopia',
            job_type='Full-time',
            summary="Grow Rori Hotel's presence with corporate clients, travel partners, "
                    "and event organizers.",
            responsibilities="Identify and pursue new business and partnership opportunities\n"
                              "Manage relationships with travel agencies and corporate accounts\n"
                              "Support marketing campaigns across digital and print channels\n"
                              "Prepare sales reports and forecasts",
            requirements="Degree in Marketing, Business, or related field\n"
                         "2+ years sales experience, hospitality a plus\n"
                         "Strong communication skills in Amharic and English\n"
                         "Confident, target-driven, and organized",
        ),
    ]
    db.session.add_all(jobs)
    db.session.commit()


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
 