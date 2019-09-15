from django.conf.urls import include, url

try:
    from djcelery.views import apply
    urlpatterns = [
        url(r'^apply/(?P<task_name>.+?)/', apply, name='celery-apply'),
        url(r'^celery/', include('djcelery.urls')),
    ]
except ImportError:
    urlpatterns = []
