from django.urls import path

from apps.website.views import HomePage, AboutPage, ServicesPage, \
    ProjectsPage, ServiceDetailsPage, WorkDetailsPage

urlpatterns = [
    path('', HomePage.as_view(), name='home_template'),
    path('home/', HomePage.as_view(), name='home_template'),
    path('about/', AboutPage.as_view(), name='about_template'),
    path('services/', ServicesPage.as_view(), name='services_template'),
    path('projects/', ProjectsPage.as_view(), name='projects_template'),
    path('service-details/', ServiceDetailsPage.as_view(), name='service-details'),
    path('work-details/', WorkDetailsPage.as_view(), name='work-details'),
]
