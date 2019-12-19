from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as smod
from django.http import HttpResponseRedirect


@view_function
def process_request(request, score:smod.Score):

    if request.user.is_authenticated:

        if request.user.has_perm('account.editScores'):
            
            scores = smod.Score.objects.filter(status="A",name=score.name).order_by('name')

            if request.method == 'POST':

                for score in scores:
                    score.name=request.POST['scoreName']
                    score.allURL=request.POST['allURL']
                    score.partURL=request.POST['partURL'+ str(score.id)]
                    score.save()

                return HttpResponseRedirect('/adminportal/scores/')
            

            context = {
                'scores':scores
            }
            return request.dmp.render('editScore.html', context)
        else:
            return HttpResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')