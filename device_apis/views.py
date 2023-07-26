from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return HttpResponse("hello world, you're at the device store.",status=200)