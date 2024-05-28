from django.http import HttpResponse


# Create your views here.


def landing_page(request):
    message = 'Welcome to Worker Demo App!'
    return HttpResponse(message)
