from django.urls import path

from . import views

#if we give namespace to url pattern, then in template we can say cohorts:detail
#decoupling
app_name = 'cohorts'
urlpatterns = [
    # ex: /cohorts/
    path('', views.index, name='index'),
    # ex: /cohorts/5/
    path('<int:cohort_id>/', views.detail, name='detail'),
]