from django.shortcuts import render
from django.views import View
# from django.http import HttpResponseRedirect
from apps.portfolio.models import Service, WorkHistory
from apps.website.models import Paragraph
from apps.website.config import PARA_DICT
from .helpers import get_objs_with_url, get_nav_urls


class ContextPage(View):
    template_path = 'err.html'

    def get_context(self, request):
        return get_nav_urls(request)

    def get(self, request, format=None):
        context = self.get_context(request)
        return render(request, self.template_path, {'context': context}, 200)


class DetailsPage(View):
    ObjModel = None
    template_path = 'err.html'
    url_suffix = 'None'

    def get_context(self, request):
        return get_nav_urls(request)

    def get(self, request, format=None):
        # print(request)
        obj_id = request.GET.get('id', False)
        obj_values = self.ObjModel.objects.filter(id=obj_id).values()[0]
        context = self.get_context(request)
        context.update({
            self.url_suffix: obj_values
        })
        # print(context)
        return render(request, self.template_path, {'context': context}, 200)


class HomePage(ContextPage):
    template_path = 'website/home.html'

    def get_context(self, request):
        context = get_nav_urls(request)
        short_bio = Paragraph.objects.filter(
            type=PARA_DICT['Short-Bio']
        )[0]

        context.update({
            'short_bio': short_bio.text,
            'services': get_objs_with_url(
                Service, context['service_details']
            ),
            'recent_works': get_objs_with_url(
                WorkHistory, context['work_details']
            )
        })
        return context


class ServiceDetailsPage(DetailsPage):
    ObjModel = Service
    template_path = 'website/service_details.html'
    url_suffix = 'service_details'


class WorkDetailsPage(DetailsPage):
    ObjModel = WorkHistory
    template_path = 'website/work_details.html'
    url_suffix = 'work_details'


class BlogPage(ContextPage):
    template_path = 'website/blog.html'


class AboutPage(ContextPage):
    template_path = 'website/about.html'


class BlogPostPage(ContextPage):
    template_path = 'website/blog_post.html'


class SidebarLeftPage(View):
    template_path = 'website/sidebar-left.html'


class SidebarRightPage(View):
    template_path = 'website/sidebar-right.html'


