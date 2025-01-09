from django.http import HttpRequest


def set_useragent_on_request_middleware(get_response):
    def middleware(request: HttpRequest):
        request.user_agent = request.META.get('HTTP_USER_AGENT')
        response = get_response(request)
        return response

    return middleware