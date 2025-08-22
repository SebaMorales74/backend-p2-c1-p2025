from django.http import HttpResponse

def inicio(request):
    nombre = "Sebastian Morales"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")