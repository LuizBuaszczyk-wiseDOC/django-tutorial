from django.http import HttpResponse

def cookie(request):
    resp = HttpResponse()
    resp.set_cookie('dj4e_cookie', '2a203bc5', max_age=1000)
    return resp

def myview(request):
    if not request.COOKIES:
        resp = cookie(request)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    return resp

