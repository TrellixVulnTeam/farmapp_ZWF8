from django.conf import settings
from django.http import HttpResponseRedirect

class AuthorizerMiddleware:

    def process_request(self, request):
        request.data = {}
        # Check for authentication
        if 'HTTP_AUTHORIZATION' in request.META:
            key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            try:
                user = Token.objects.get(key=key).user
                request.data['user'] = user
                request.user = user
            except:
                pass
        request.custom_data = request.data
        return None