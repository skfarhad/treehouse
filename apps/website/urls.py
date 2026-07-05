from django.urls import path

from apps.website.views import HomePage, ExperiencePage, EducationPage, \
    SkillsPage, ProjectsPage, ServicesPage, ServiceDetailsPage, WorkDetailsPage

urlpatterns = [
    path('', HomePage.as_view(), name='home_template'),
    path('home/', HomePage.as_view(), name='home_template'),
    path('experience/', ExperiencePage.as_view(), name='experience_template'),
    path('education/', EducationPage.as_view(), name='education_template'),
    path('skills/', SkillsPage.as_view(), name='skills_template'),
    path('projects/', ProjectsPage.as_view(), name='projects_template'),
    path('services/', ServicesPage.as_view(), name='services_template'),
    path('service-details/', ServiceDetailsPage.as_view(), name='service-details'),
    path('work-details/', WorkDetailsPage.as_view(), name='work-details'),
]
