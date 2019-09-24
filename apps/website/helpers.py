
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
        'blog_post': get_url(request, '/website/', 'blog-post/'),
        'sidebar_left': get_url(request, '/website/', 'sidebar-left/'),
        'sidebar_right': get_url(request, '/website/', 'sidebar-right/'),
        'blog': get_url(request, '/website/', 'blog/'),
        'service_details': get_url(request, '/website/', 'service-details/'),
        'work_details': get_url(request, '/website/', 'work-details/'),
    }
    return context


def get_objs_with_url(ObjModel, root):
    obj_list = []
    obj_qs = ObjModel.objects.all().values()
    for obj in obj_qs:
        obj.update({
            'url': root + '?id=' + str(obj['id'])
        })
        obj_list.append(obj)
    return obj_list
