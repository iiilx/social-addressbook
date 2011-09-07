from django.http import Http404, HttpResponseForbidden as Http403, HttpResponse

WHITE_LIST = ['']

class WhiteList(object):
    def process_request(self, request):
        ip = request.META['REMOTE_ADDR']
        if ip not in WHITE_LIST:
            raise Http404 #return HttpResponse(ip) # raise Http404
        else:
            return None


