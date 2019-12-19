from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as pmod

@view_function
def process_request(request):

    scores = pmod.Score.objects.filter(status='A')

    context = {
       'Scores':scores
    }
    return request.dmp.render('index.html', context)