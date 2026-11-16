from django.db import models
from django.contrib.auth.models import User
class Project(models.Model):
    name=models.CharField(max_length=140); description=models.TextField(blank=True); owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="owned_projects"); members=models.ManyToManyField(User,related_name="team_projects",blank=True); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
class Task(models.Model):
    STATUS=[("backlog","Backlog"),("todo","To do"),("progress","In progress"),("review","Review"),("done","Done")]
    PRIORITY=[("low","Low"),("medium","Medium"),("high","High"),("urgent","Urgent")]
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="tasks"); title=models.CharField(max_length=180); description=models.TextField(blank=True); assignee=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True); status=models.CharField(max_length=20,choices=STATUS,default="todo"); priority=models.CharField(max_length=20,choices=PRIORITY,default="medium"); due_date=models.DateField(null=True,blank=True); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
class TaskComment(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name="comments"); author=models.ForeignKey(User,on_delete=models.CASCADE); body=models.TextField(max_length=1000); created_at=models.DateTimeField(auto_now_add=True)
