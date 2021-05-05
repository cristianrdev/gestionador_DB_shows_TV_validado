from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from datetime import date
from django.contrib import messages

# Create your views here.

def redireccionar(request):
    return redirect('/shows')

def listar_shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def nuevo_show(request):
    if request.method == 'GET':
        print('ES UN GET')
        return render(request, 'new_show.html')

    else:
        print('ES UN POST')
        # validacion
        errors = Show.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')

        else:
        #     guardar nuevo show
            new_show = Show.objects.create(
            title= request.POST['titulo'],
            network= request.POST['cadena'],
            release_date= request.POST['fecha_lanz'],
            description= request.POST['descripcion'],
                )
            return redirect('/shows/'+ str(new_show.id))

def detalle_show(request, id):
        context = {
            
            "pelicula" : Show.objects.get(id=id),
        }
        return render(request, 'detalle_show.html', context)

def editar_show(request, id):
    if request.method == 'GET':
        print('ES UN GET')
        
        context = {
            'show' : Show.objects.get(id=id),
        }

        return render(request, 'edit_show.html', context)

    else:
        print('ES UN POST')
        # validación acá
        errors = Show.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/' + id +'/edit')

        else:
            show_to_update = Show.objects.get(id=id)
            show_to_update.title = request.POST['titulo']
            show_to_update.network = request.POST['cadena']
            show_to_update.release_date = request.POST['fecha_lanz']
            show_to_update.description = request.POST['descripcion']
            show_to_update.save()

        return redirect('/shows/'+ str(show_to_update.id))





def borrar_show(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect('/shows')


# def TituloRepetido(request, titulo):
