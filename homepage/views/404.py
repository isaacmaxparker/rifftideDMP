from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    return request.dmp.render('404.html')
