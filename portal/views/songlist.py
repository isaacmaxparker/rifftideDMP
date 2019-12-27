from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as pmod
from account import models as amod
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage

@view_function
def process_request(request):

   if request.user.is_authenticated:

      if request.user.has_perm('account.seePortal'):
         currentUser = amod.User.objects.get(id=request.user.id)
         scores = pmod.Score.objects.filter(status='A',part=currentUser.voicepart).order_by('name')
         
         i = 0
         for score in scores:
            if i % 2 != 0:
               score.is_dark = True
            else:
               score.is_dark = False
            i = i+1
         

         context = {
            'Scores':scores,
            'message':'NONE'
         }
         return request.dmp.render('songlist.html', context)
      else:
         return HttpResponseRedirect('/account/errors/')

   return HttpResponseRedirect('/account/login/')

@view_function
def requestScore(request, score:pmod.Score):

    if request.user.is_authenticated:

        if request.user.has_perm('account.viewScores'):

            score = pmod.Score.objects.get(id=score.id)
            
            send_mail(
                'SCORE IS BEING REQUESTED',
                '' + request.user.first_name + ' is requesting an individual part for ' + score.name,
                'riffnotifs@gmail.com',
                ['rifftideacapella@gmail.com'],
                fail_silently=False,
            )

            msg = EmailMessage('Request Callback',
                              'Here is the message.', to=['rifftideacapella@gmail.com'])
            msg.send()

            currentUser = amod.User.objects.get(id=request.user.id)
            scores = pmod.Score.objects.filter(status='A',part=currentUser.voicepart).order_by('name')

            context = {
                'Scores':scores,
                'message':'ERROR 4141324234. Request could not be sent, text Isaac and request your part'
            }
            return request.dmp.render('songlist.html', context)


        else:
            return HttpResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')