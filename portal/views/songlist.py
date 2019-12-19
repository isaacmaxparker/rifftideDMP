from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as pmod
from account import models as amod
from django.http import HttpResponseRedirect

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
            'Scores':scores
         }
         return request.dmp.render('songlist.html', context)
      else:
         return HttpResponseRedirect('/account/errors/')

   return HttpResponseRedirect('/account/login/')