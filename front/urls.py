from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.dashboard)
]

admin.site.site_header = 'CPE500 Level'
admin.site.index_title = 'CPE500 Level Administration'
admin.site.site_title = 'CPE500 Level Admin'
