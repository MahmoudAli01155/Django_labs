from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
# from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import ListView

# Create your views here.


class List(ListView):
    model = MyUser

class Loginview(View):
    def get(self,req):
        return render(req, 'Login.html')
    def post(self,req):
        u = MyUser.objects.filter(username=req.POST['username'], password=req.POST['password'])
        authuser = authenticate(username=req.POST['username'], password=req.POST['password'])
        print(authuser)
        if (u[0] is not None and authuser is not None):
            req.session['userid'] = u[0].id
            req.session['username'] = u[0].username
            login(req, authuser)
            return HttpResponseRedirect('/')
        else:
            context = {}
            context['error'] = 'username or password wong'
            return render(req, 'Login.html', context)



# create my registration
def myregister2(req):
    if(req.method=='POST'):
        x=MyUser.objects.create(
            username=req.POST['username'],
            password=req.POST['password'],
            email=req.POST['email']
        )
        User.objects.create_superuser(username=req.POST['username']
                                      , password=req.POST['password'],
                                      email=req.POST['email'])

        req.session['userid']=x.id
        req.session['username']=x.username

        return  render(req,'catagory/Add.html')
    else:
        return render(req, 'Register.html' )



# create my logout
def mylogout2(req):
    req.session.clear()
    return HttpResponseRedirect('Login')


# create my  login
# @require_http_methods(['GET','POST'])
# def mylogin2(req):
#     if (req.method == 'GET'):
#         return render(req, 'Login.html')
#     else:
#         u = MyUser.objects.filter(username=req.POST['username'], password=req.POST['password'])
#         authuser=authenticate(username=req.POST['username'],password=req.POST['password'])
#         print(authuser)
#         if (u[0] is not None and authuser is not None):
#             req.session['userid'] = u[0].id
#             req.session['username'] = u[0].username
#             login(req,authuser)
#             return HttpResponseRedirect('/')
#         else:
#             context = {}
#             context['error'] = 'username or password wong'
#             return render(req, 'Login.html', context)
