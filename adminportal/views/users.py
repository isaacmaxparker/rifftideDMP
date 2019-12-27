from django.conf import settings
from django_mako_plus import view_function, jscontext
from account import models as amod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):

    if request.user.is_authenticated:

        if request.user.has_perm('account.editUsers'):
            
            if request.method == 'POST':

                users = amod.User.objects.filter(status="A")

                for user in users:
                        user.first_name=request.POST['firstName'+str(user.id)]
                        user.last_name=request.POST['lastName'+str(user.id)]
                        user.username=request.POST['userName'+str(user.id)]
                        user.voicepart=request.POST['voicePart'+str(user.id)]

                        if user.voicepart == 'Soprano':
                            user.priority = 1
                        if user.voicepart == 'Mezzo':
                            user.priority = 2
                        if user.voicepart == 'Alto':
                            user.priority = 3
                        if user.voicepart == 'Contralto':
                            user.priority = 4
                        if user.voicepart == 'Tenor':
                            user.priority = 5
                        if user.voicepart == 'Baritone':
                            user.priority = 6
                        if user.voicepart == 'Bass':
                            user.priority = 7
                        if user.voicepart == 'Beatbox':
                            user.priority = 8


                        user.save()





            users = amod.User.objects.filter(status="A").order_by('priority')

            context = {
                'users':users
            }
            return request.dmp.render('users.html', context)
        else:
            return HttResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')