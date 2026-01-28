from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Solo2View(LoginRequiredMixin, View):
    def get(self, request):
        msg = request.session.get('msg', False)
        if (msg) : del(request.session['msg'])
        return render(request, 'solo2/index.html', {'message': msg})

    def post(self, request):
        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        msg = f"Your result is {field2}  {field1}"
        request.session['msg'] = msg
        return redirect(request.path)