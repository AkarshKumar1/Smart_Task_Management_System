from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from .models import Task

from .extensions import db, socketio

from .analytics import task_analytics


main = Blueprint('main', __name__)


# =========================
# DASHBOARD
# =========================
@main.route('/')
@login_required
def dashboard():

    tasks = Task.query.filter_by(
        user_id=current_user.id
    ).all()

    task_data = []

    for task in tasks:

        task_data.append({
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status
        })

    analytics = task_analytics(task_data)

    return render_template(
        'dashboard.html',
        tasks=tasks,
        analytics=analytics
    )


# =========================
# ADD TASK FORM
# =========================
@main.route('/add-task', methods=['POST'])
@login_required
def add_task_form():

    title = request.form.get('title')

    description = request.form.get('description')

    priority = request.form.get('priority')

    status = request.form.get('status')

    task = Task(
        title=title,
        description=description,
        priority=priority,
        status=status,
        user_id=current_user.id
    )

    db.session.add(task)

    db.session.commit()

    socketio.emit(
        'new_task',
        {
            "title": task.title
        }
    )

    flash(
        "Task added successfully!",
        "success"
    )

    return redirect(
        url_for('main.dashboard')
    )


# =========================
# DELETE TASK
# =========================
@main.route('/api/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    socketio.emit(
        'task_deleted',
        {
            "task_id": task.id
        }
    )

    return jsonify({
        "message": "Task deleted successfully"
    })