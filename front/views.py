from django.shortcuts import render
from .models import Update, Course, Semester, Material


def dashboard(request):
    updates = Update.objects.filter(
        is_active=True).order_by('-date_added')
    courses = Course.objects.all()
    semester = Semester.objects.all()
    materials = Material.objects.all()

    context = {
        'updates': updates,
        'courses': courses,
        'materials': materials
    }

    if semester.exists():
        semester = semester[0]
        current_semester = "1st Semester Time-table" if int(
            semester.current_semester) == 1 else "2nd Semester Time-table"
        current_semester_time_table = semester.get_image_url
        context.update({'current_semester': current_semester,
                        'current_semester_time_table': current_semester_time_table, })

    return render(request, template_name="index.html", context=context)
