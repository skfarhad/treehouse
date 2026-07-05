def get_url(request, prefix, uri):
    return request.build_absolute_uri(prefix + uri)


def get_nav_urls(request):
    return {
        'home': get_url(request, '/website/', 'home/'),
        'about': get_url(request, '/website/', 'about/'),
        'services_url': get_url(request, '/website/', 'services/'),
        'service_details': get_url(request, '/website/', 'service-details/'),
        'work_details': get_url(request, '/website/', 'work-details/'),
    }


def attach_urls(objs, root):
    """Return copies of the content dicts with a detail-page ``url`` added."""
    return [
        dict(obj, url=root + '?id=' + str(obj['id']))
        for obj in objs
    ]
