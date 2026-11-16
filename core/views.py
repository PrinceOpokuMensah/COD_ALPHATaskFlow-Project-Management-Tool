
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Task, TaskComment


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created. Please sign in.")
        return redirect("login")

    return render(request, "register.html", {
        "form": form,
        "brand": "TaskFlow"
    })


@login_required
def home(request):
    projects = Project.objects.filter(
        members=request.user
    ).distinct().order_by("-created_at")

    return render(request, "home.html", {
        "projects": projects,
        "brand": "TaskFlow"
    })


@login_required
def create_project(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            project = Project.objects.create(
                name=name,
                description=request.POST.get("description", ""),
                owner=request.user
            )
            project.members.add(request.user)
            messages.success(request, "Project created.")

    return redirect("home")


@login_required
def board(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk,
        members=request.user
    )

    tasks = project.tasks.select_related("assignee").all()

    return render(request, "board.html", {
        "project": project,
        "tasks": tasks,
        "members": project.members.all(),
        "brand": "TaskFlow"
    })


@login_required
def create_task(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk,
        members=request.user
    )

    if request.method == "POST":
        title = request.POST.get("title", "").strip()

        if title:
            assignee_id = request.POST.get("assignee")
            assignee = None

            if assignee_id:
                assignee = User.objects.filter(
                    pk=assignee_id,
                    team_projects=project
                ).first()

            Task.objects.create(
                project=project,
                title=title,
                description=request.POST.get("description", ""),
                priority=request.POST.get("priority", "medium"),
                status=request.POST.get("status", "todo"),
                assignee=assignee,
                due_date=request.POST.get("due_date") or None
            )

            messages.success(request, "Task created successfully.")

    return redirect("board", pk=pk)


@login_required
def update_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        project__members=request.user
    )

    if request.method == "POST":
        task.status = request.POST.get("status", task.status)
        task.priority = request.POST.get("priority", task.priority)
        task.save()

    return redirect("board", pk=task.project_id)


@login_required
def add_member(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        person = User.objects.filter(
            username=request.POST.get("username")
        ).first()

        if person:
            project.members.add(person)
            messages.success(request, "Member added.")
        else:
            messages.error(request, "No user found with that username.")

    return redirect("board", pk=pk)


@login_required
def add_comment(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        project__members=request.user
    )

    if request.method == "POST":
        body = request.POST.get("body", "").strip()

        if body:
            TaskComment.objects.create(
                task=task,
                author=request.user,
                body=body
            )

    return redirect("board", pk=task.project_id)
