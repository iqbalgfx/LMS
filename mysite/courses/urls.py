from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
# course views
    path('', views.course_list, name='course_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:course>/',
        views.course_detail,
        name='course_detail'),
]