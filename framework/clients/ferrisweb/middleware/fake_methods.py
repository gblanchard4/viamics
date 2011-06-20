
class FakeHttpMiddleware:
    """Allows us to use a '_method' or other field in a POSTed form to simulate PUT and DELETE methods of HTTP. This seems to be a growing convention to get around the limitation of browsers, used in both Django and Rails.

    By using _method, browser forms can call all the HTTP methods to fully use an api."""

    def process_request(self, request):
        if request.method == 'POST' and "_method" in request.POST:
            request._method = request.POST["_method"].upper()
        else:
            request._method = request.method
        return None
            
