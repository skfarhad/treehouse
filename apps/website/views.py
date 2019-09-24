from django.shortcuts import render
from django.views import View
# from django.http import HttpResponseRedirect
from apps.portfolio.models import Service, WorkHistory


def render_context(request, template, context, status):
    return render(request, template, {'context': context}, status=status)


def render_context(request, template, context, status):
    return render(request, template, {'context': context}, status=status)


def get_url(request, prefix, uri):
    return request.build_absolute_uri(prefix + uri)


def get_nav_urls(request):
    # action_label = 'Login'
    # action_link = get_url(request, '/user/', 'login_api')
    # if request.user.is_authenticated:
    #     action_label = 'Logout'
    #     action_link = get_url(request, '/user/', 'logout_api')

    context = {
        'home': get_url(request, '/website/', 'home/'),
        'about': get_url(request, '/website/', 'about/'),
        'single': get_url(request, '/website/', 'single/'),
        'sidebar_left': get_url(request, '/website/', 'sidebar-left/'),
        'sidebar_right': get_url(request, '/website/', 'sidebar-right/'),
        'blog': get_url(request, '/website/', 'blog/'),
    }
    return context


class HomeTemplateView(View):

    def get(self, request, format=None):
        context = get_nav_urls(request)
        context.update({
            'services': Service.objects.all().values(),
            'recent_works': WorkHistory.objects.all().values()
        })
        return render_context(request, 'website/home.html', context, 200)


class BlogTemplateView(View):

    def get(self, request, format=None):
        context = get_nav_urls(request)
        return render_context(request, 'website/blog.html', context, 200)


class AboutTemplateView(View):

    def get(self, request, format=None):
        context = get_nav_urls(request)
        print(context)
        return render_context(request, 'website/about.html', context, 200)


class SingleTemplateView(View):

    def get(self, request, format=None):
        context = get_nav_urls(request)
        print(context)
        return render_context(request, 'website/single.html', context, 200)


class SidebarLTemplateView(View):

    def get(self, request, format=None):
        context = get_nav_urls(request)
        print(context)
        return render_context(request, 'website/sidebar-left.html', context, 200)


class SidebarRTemplateView(View):

    def get(self, request, format=None):
        context = get_nav_urls(request)
        print(context)
        return render_context(request, 'website/sidebar-right.html', context, 200)

