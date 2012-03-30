# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from formapp.forms import LoginForm, RegisterForm
from formapp.models import Register

def loginn(request):
    def errorHandle(error):
        form = LoginForm()
        return render_to_response('fapp/login.html', {
                          'error' : error,
                          'form' : form,
        })
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username = request.POST['username']
            password = request.POST['password']
            user = Register.objects.filter(username=username, password=password)
            if user:
                login_user = user.get()
                request.session['mbr_id']=login_user.id
                return render_to_response('fapp/logged_in.html', {
                            'username': username,
                            })
            else:
                # Return an 'invalid login' error message.
                error = u'invalid login'
                return errorHandle(error)
        else:
            error = u'Username and Password should not be empty'
            return errorHandle(error)
    else:
        form = LoginForm() # An unbound form
        return render_to_response('fapp/login.html', {
                'form': form,
                })

def register(request):
    def errorHandle(error):
        form = RegisterForm()
        return render_to_response('fapp/register.html', {
                          'error' : error,
                          'form' : form,
        })
    if request.method == 'POST': # If the form has been submitted...
        form = RegisterForm(request.POST) # A form bound to the POST data
        register_obj = Register()
        if form.is_valid(): # All validation rules pass
            username = request.POST['username']
            password = request.POST['password']
            user = Register.objects.filter(username=username, password=password)
            if not user:
                register_obj.username = request.POST['username']
                register_obj.password = request.POST['password']
                register_obj.email = request.POST['email']
                register_obj.save()
                return render_to_response('fapp/register_in.html', {
                            'username': register_obj.username,
                         })
            else:
                error = u'User already exist'
                return errorHandle(error)
        else:
            error = u'Fields should not empty'
            return errorHandle(error)
    else:
        form = RegisterForm() # An unbound form
        return render_to_response('fapp/register.html', {
                'form': form,
                })

def home(request):
    def errorHandle(error):
        form = LoginForm()
        return render_to_response('fapp/login.html', {
                          'error' : error,
                          'form' : form,
        })
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username = request.POST['username']
            password = request.POST['password']
            user = Register.objects.filter(username=username, password=password)
            if user:
                return render_to_response('fapp/logged_in.html', {
                            'username': username,
                            })
            else:
                # Return an 'invalid login' error message.
                error = u'invalid login'
                return errorHandle(error)
        else:
            error = u'Username and Password should not be empty'
            return errorHandle(error)
    else:
        form = LoginForm() # An unbound form
        return render_to_response('fapp/login.html', {
                'form': form,
                })
