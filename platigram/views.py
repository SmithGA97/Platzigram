"""Vista del platzigram"""
from django.http import HttpResponse
from django.http import JsonResponse
#utilities
from datetime import datetime

def hello_world(request):
    """Funcion"""
    now=datetime.now().strftime('%b %dth, %Y -%H:%M hrs')
    return HttpResponse('Oh, Hola, Current time server is {now}'.format(now=now))

def sort_integers(request):
    """Return a Json with sorted"""
    
    #print(request)
    #numbers=request.GET['numbers']
    #import pdb; pdb.set_trace()
    numbers=map(lambda x : int(x), request.GET['numbers'].split(","))# el split me devuelve una lista ya que el map recibe una función y una lista
    
    return JsonResponse({"numbers": sorted(numbers, key=int) }, json_dumps_params={'indent':6} )

def say_hi(request, name, age): # la forma en la que django responde una solicitud reuqest,
    """return a greetign"""
    if age < 12 :
        message = f"Sorry {name} , no eres bienvenido"
    else:
        message = f"Hola {name}, Bienvenido a Platzigram"
    return HttpResponse(message)