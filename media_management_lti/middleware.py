from media_manager.lti import LTILaunchError
#from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

class LtiExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, LTILaunchError):
            logger.error(exception.message)
            return HttpResponse('LTI Error. Please try relaunching the tool.')
        else:
            return None
