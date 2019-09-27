from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    return HttpResponseRedirect('/store/index/')

@view_function
def gettime(request):
    context = {
        'now': datetime.now(),
    }
    return request.dmp.render('gettime.html', context)