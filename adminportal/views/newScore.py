from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as smod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):

    if request.user.is_authenticated:

        if request.user.has_perm('account.editScores'):
            
           
            if request.method == 'POST':
                voices = ['Soprano','Mezzo','Alto','Contralto','Tenor','Baritone','Bass','Beatbox']
                for i in range(8):
                    score = smod.Score()
                    score.name=request.POST['scoreName']
                    score.allURL=request.POST['allURL']
                    score.partURL=request.POST['partURL'+ str(i)]
                    print(voices[i])
                    score.part=voices[i]
                    score.save()

                return HttpResponseRedirect('/adminportal/scores/')

            return request.dmp.render('newScore.html')
        else:
            return HttpResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')