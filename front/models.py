from django.db import models

SEMESTER_CHOICES = (
    ("1", "1st"),
    ("2", "2nd"),
)


class Semester(models.Model):
    current_semester = models.CharField(
        max_length=3, choices=SEMESTER_CHOICES, default=1)
    current_semester_time_table = models.ImageField()

    class Meta:
        verbose_name_plural = 'Semester'

    def __str__(self):
        return "1st Semester" if int(self.current_semester) == 1 else "2nd Semester"


class Update(models.Model):
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Info: {self.message[:20]}..."


class Course(models.Model):
    course_code = models.CharField(max_length=30)

    def __str__(self):
        return self.course_code


class Material(models.Model):
    material = models.FileField()
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True, related_name="material")

    def __str__(self):
        return self.course.course_code if self.course else "---"
