from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    context = {

    }
    return request.dmp.render('music.html', context)