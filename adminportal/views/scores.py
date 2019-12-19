from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as smod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):

    if request.user.is_authenticated:

        if request.user.has_perm('account.editScores'):
    
            scores = smod.Score.objects.filter(status="A").order_by('name').distinct('name')

            context = {
                'scores':scores
            }
            return request.dmp.render('scores.html', context)
        else:
            return HttResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')