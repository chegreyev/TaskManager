from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        PLANNING =  'planning',  _('PL')
        ACTIVE =    'active',      _('AC')
        CONTROL =   'control',    _('CL')
        COMPLETE =  'complete',  _('CE')

    title = models.CharField(max_length=255)
    description = models.TextField()
    performer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='performers')
    observer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='observers')
    status = models.CharField(
        max_length=8,
        choices=TaskStatus.choices
    )
    started_at = models.DateField(auto_now=True)
    planning_completed_at = models.DateField(null=True)
    completed_at = models.DateField(null=True)


class ChangingStatus(models.Model):

    class TaskStatus(models.TextChoices):
        PLANNING =  'planning',  _('PL')
        ACTIVE =    'active',      _('AC')
        CONTROL =   'control',    _('CL')
        COMPLETE =  'complete',  _('CE')

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='tasks')
    previous_status = models.CharField(max_length=255, null=True)
    next_status = models.CharField(
        max_length=8,
        choices=TaskStatus.choices
    )
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()
    users = models.ManyToManyField(User)
