from django.urls import path

from apps.website.views import HomeTemplateView, AboutTemplateView, BlogTemplateView,\
    SidebarLTemplateView, SidebarRTemplateView, SingleTemplateView

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home_template'),
    path('about/', AboutTemplateView.as_view(), name='about_template'),
    path('blog/', BlogTemplateView.as_view(), name='blog_template'),
    path('sidebar-left/', SidebarLTemplateView.as_view(), name='sidebar-left'),
    path('sidebar-right/', SidebarRTemplateView.as_view(), name='sidebar-right'),
    path('single/', SingleTemplateView.as_view(), name='single'),

]