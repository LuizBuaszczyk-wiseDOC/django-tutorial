from django.http import HttpResponse

# Create your views here.
def myview(request):
    resp = HttpResponse()
    resp.set_cookie('dj4e_cookie', '2a203bc5', max_age=1000)
    return resp
