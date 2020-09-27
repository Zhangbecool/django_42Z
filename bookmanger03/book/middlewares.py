from django.utils.deprecation import MiddlewareMixin

class TestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('请求前会执行')

    def process_response(self, request, response):

        print('响应前执行')

        return response