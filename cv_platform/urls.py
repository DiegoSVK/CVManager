from django.urls import path
from .views import platform_view, delete_resume, preview
from accounts.views import logout_view

urlpatterns=[
    path('',platform_view,name='cv_platform'),
    path('delete_resume/<int:resume_id>/',delete_resume,name='delete_resume'),
    path('preview/<int:resume_id>/',preview,name='preview'),
    path('logout/',logout_view,name='logout'),
]