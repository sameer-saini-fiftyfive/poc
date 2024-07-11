from django.http.response import HttpResponse

def home(request):
    return HttpResponse("This is home data!!")
