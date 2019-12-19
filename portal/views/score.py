from django.conf import settings
from django_mako_plus import view_function, jscontext
from portal import models as pmod

@view_function
def process_request(request, score:pmod.Score, part:int):

    score = pmod.Score.objects.get(id=score.id)
    if part == 1:
        url = score.partURL
    else:
        url = score.allURL



    context = {
       'Url':url,
       'title':score.name,
    }
    return request.dmp.render('score.html', context)