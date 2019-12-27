from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as smod
from django.http import HttpResponseRedirect


@view_function
def process_request(request, user:smod.User):

    if request.user.is_authenticated:

        if request.user.has_perm('account.editUsers'):
            
            users = smod.User.objects.filter(status="A",name=user.name).order_by('name').delete()


            return HttpResponseRedirect('/adminportal/users/')
        else:
            return HttpResponseRedirect('/account/errors/')

    return HttpResponseRedirect('/account/login/')