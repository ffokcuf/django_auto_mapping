from inspect import getmembers, isfunction, getmodule, getfullargspec
from django.conf.urls import include
from django.urls import path


def auto_mapping(base, mod, custom=None):
    if not custom:
        custom = {}
    views = getmembers(mod, isfunction)
    views = [t for t in views if getmodule(t[1]) == mod]
    urls = []
    for name, view in views:
        if name in custom:
            u = custom[name]
        else:
            annotations = getfullargspec(view).annotations
            u = r''
            u += name + "/"
            for param_name, param_type in annotations.items():
                if param_name != 'request':
                    u += '<%s:%s>/' % (param_type.__name__, str(param_name))
        urls.append(path(u, view))
    return path(base, include(urls))
