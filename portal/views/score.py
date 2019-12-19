from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as pmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request, score:pmod.Score, part:int):

    if request.user.is_authenticated:

        if request.user.has_perm('account.viewScores'):

            score = pmod.Score.objects.get(id=score.id)
            if part == 1:
                url = score.partURL
            else:
                url = score.allURL

            score.views = score.views + 1
            score.save()

            context = {
            'Url':url,
            'title':score.name,
            }
            return request.dmp.render('score.html', context)
        else:
            return HttpResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')