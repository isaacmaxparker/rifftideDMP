from django.conf import settings
from django_mako_plus import view_function, jscontext
from account import models as amod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):

    if request.user.is_authenticated:

        if request.user.has_perm('account.editUsers'):
    
            users = amod.User.objects.filter(status="A")

            context = {
                'users':users
            }
            return request.dmp.render('users.html', context)
        else:
            return HttResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')