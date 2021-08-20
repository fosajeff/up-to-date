from django.contrib import admin

from .models import (
    Course,
    Material,
    Update,
    Semester
)

admin.site.register([Course, Material, Update, Semester])
