import re
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url)for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware(MiddlewareMixin):
   
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required Middleware"

        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')

            if not any(url_pattern.match(path) for url_pattern in EXEMPT_URLS):
                redirect_to = settings.LOGIN_URL

            return HttpResponseRedirect(redirect_to)
                
            
