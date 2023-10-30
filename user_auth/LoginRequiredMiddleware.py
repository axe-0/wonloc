import re
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url)for url in settings.LOGIN_EXEMPT_URLS]
   

class LoginRequiredMiddleware(MiddlewareMixin):

    
    def process_request(self, request):
        if not hasattr(request, 'user') or not request.user.is_authenticated:
            print("The Login Required Middleware")
            path = request.path_info.lstrip('/')
            if not any(url_pattern.match(path) for url_pattern in EXEMPT_URLS):
                redirect_to = reverse('user_auth:login')
                return HttpResponseRedirect(redirect_to)
        else:
            print("Proceed to User login :)")            
                
