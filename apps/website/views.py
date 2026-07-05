from django.shortcuts import render
from django.http import Http404
from django.views import View

from apps.website import content
from .helpers import get_nav_urls, attach_urls


class ContextPage(View):
    template_path = 'err.html'

    def get_context(self, request):
        return get_nav_urls(request)

    def get(self, request, format=None):
        context = self.get_context(request)
        return render(request, self.template_path, context={'context': context}, status=200)


class DetailsPage(View):
    template_path = 'err.html'
    url_suffix = 'None'

    def get_object(self, obj_id):
        raise NotImplementedError

    def get_context(self, request):
        return get_nav_urls(request)

    def get(self, request, format=None):
        obj = self.get_object(request.GET.get('id'))
        if obj is None:
            raise Http404('Not found')
        context = self.get_context(request)
        context.update({self.url_suffix: obj})
        return render(request, self.template_path, context={'context': context}, status=200)


class HomePage(ContextPage):
    template_path = 'website/home.html'

    def get_context(self, request):
        context = get_nav_urls(request)
        context.update({
            'short_bio': content.get_short_bio(),
            'services': attach_urls(content.get_services(), context['service_details']),
            'recent_works': attach_urls(content.get_works(), context['work_details']),
        })
        return context


class ServicesPage(ContextPage):
    template_path = 'website/services.html'

    def get_context(self, request):
        context = get_nav_urls(request)
        context.update({
            'services': attach_urls(content.get_services(), context['service_details']),
        })
        return context


class ServiceDetailsPage(DetailsPage):
    template_path = 'website/service_details.html'
    url_suffix = 'service_details'

    def get_object(self, obj_id):
        return content.get_service(obj_id)


class ProjectsPage(ContextPage):
    template_path = 'website/projects.html'

    def get_context(self, request):
        context = get_nav_urls(request)
        context.update({
            'projects': attach_urls(content.get_works(), context['work_details']),
        })
        return context


class WorkDetailsPage(DetailsPage):
    template_path = 'website/work_details.html'
    url_suffix = 'work_details'

    def get_object(self, obj_id):
        return content.get_work(obj_id)


class AboutPage(ContextPage):
    template_path = 'website/about.html'
