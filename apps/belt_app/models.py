from __future__ import unicode_literals
from django.db import models
from ..login_reg_app.models import User
from datetime import datetime

class ApptManager(models.Manager):
    def validate(self, data):
        errors = []

        if not data["date"]:
            errors.append("Date is required")
        # elif data["date"] < str(datetime.today()):
        #     errors.append("Travel Date must not be in the past")

        if not data["time"]:
            errors.append("Time is required")

        if not data["tasks"]:
            errors.append("Tasks field is required")

        response = {}

        if not errors:
            response['added'] = True
        else:
            response['added'] = False
            response['errors'] = errors
        return response

class Appt(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False)
    time = models.TimeField(auto_now_add=False, auto_now=False)
    tasks = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_appt = models.ForeignKey(User, related_name='appts_of_user')
    all_users = models.ManyToManyField(User, related_name='all_appts')

    objects = ApptManager()
