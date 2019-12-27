from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as smod
from django.http import HttpResponseRedirect


@view_function
def process_request(request, score:smod.Score):

    if request.user.is_authenticated:

        if request.user.has_perm('account.editScores'):
            
            scores = smod.Score.objects.filter(status="A",name=score.name).order_by('name').delete()


            return HttpResponseRedirect('/adminportal/scores/')
        else:
            return HttpResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')