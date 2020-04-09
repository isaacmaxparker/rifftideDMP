from django_mako_plus import view_function, jscontext

@view_function
def process_request(request,divID=None):

    context={
        'div':divID
    }

    return request.dmp.render('about.html',context)
