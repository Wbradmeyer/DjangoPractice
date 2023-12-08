from django.shortcuts import render, redirect
from .models import Dojo
from .models import Ninja

# Create your views here.
def index(request):
    content = {
        'all_dojos': Dojo.objects.all()
    }
    print(content)
    return render(request, 'index.html', content)

def create_dojo(request):
    Dojo.objects.create(name = request.POST['name'], 
                        city = request.POST['city'], 
                        state = request.POST['state'])
    return redirect('/')

def create_ninja(request):
    this_dojo = Dojo.objects.get(id=request.POST['dojo_id'])
    Ninja.objects.create(first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        dojo = this_dojo)
    return redirect('/')

def delete_dojo(request, dojo_id):
    dojo_to_delete = Dojo.objects.get(id=dojo_id)
    dojo_to_delete.delete()
    return redirect('/')