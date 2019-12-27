from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as smod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):

    if request.user.is_authenticated:

        if request.user.has_perm('account.editUsers'):
            
            if request.method == 'POST':
                    print("IN THE IF")
                    user = smod.User()
                    user.first_name=request.POST['firstName']
                    user.last_name=request.POST['lastName']
                    user.username=request.POST['userName']
                    user.voicePart=request.POST['voicePart']
                    user.set_password(request.POST['password'])
                    user.save()
                    print("IN THE IF")
                    return HttpResponseRedirect('/adminportal/users/')
            print("OUT THE IF")
            return request.dmp.render('newUser.html')
        else:
            return HttpResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')