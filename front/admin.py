from django.contrib import admin

from .models import (
    Course,
    Material,
    Notification,
    Semester
)

admin.site.register([Course, Material, Notification, Semester])
