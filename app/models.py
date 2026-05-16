from .extensions import db, login_manager

from flask_login import UserMixin

from datetime import datetime


# =========================
# USER LOADER
# =========================
@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# =========================
# USER MODEL
# =========================
class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    tasks = db.relationship(
        'Task',
        backref='author',
        lazy=True
    )

    def __init__(self, username, email, password, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email
        self.password = password


# =========================
# TASK MODEL
# =========================
class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    priority = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(50),
        nullable=False
    )

    created_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    def __init__(self, title, description, priority, status, user_id, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.user_id = user_id