# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from demosite.forms import Member
def login(request):
    form = Member() 
    return render_to_response('demo/login.html', {
                              'form': form,                                                                                                                                
                        })


