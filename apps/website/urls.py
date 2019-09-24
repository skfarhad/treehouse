from django.urls import path

from apps.website.views import HomePage, AboutPage, BlogPage,\
    SidebarLeftPage, SidebarRightPage, BlogPostPage, \
    ServiceDetailsPage, WorkDetailsPage

urlpatterns = [
    path('', HomePage.as_view(), name='home_template'),
    path('home/', HomePage.as_view(), name='home_template'),
    path('about/', AboutPage.as_view(), name='about_template'),
    path('blog/', BlogPage.as_view(), name='blog_template'),
    path('sidebar-left/', SidebarLeftPage.as_view(), name='sidebar-left'),
    path('sidebar-right/', SidebarRightPage.as_view(), name='sidebar-right'),
    path('blog-post/', BlogPostPage.as_view(), name='blog-post'),
    path('service-details/', ServiceDetailsPage.as_view(), name='service-details'),
    path('work-details/', WorkDetailsPage.as_view(), name='work-details'),

]
