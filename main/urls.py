
from django.conf.urls import patterns, include, url


from django.http import HttpResponse

def ping_view(request):
    # ...

    return HttpResponse('{"ping":"pong"}', content_type="application/json")

urlpatterns = patterns(r'',

    #url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'ping/', ping_view),
)
