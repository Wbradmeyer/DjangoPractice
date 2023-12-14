from django.shortcuts import render, redirect
from .models import Show

# Create your views here.

# Create methods
def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    created_show =Show.objects.create(title = request.POST['title'],
                                    network = request.POST['network'],
                                    desc = request.POST['desc'],
                                    release = request.POST['release'])
    return redirect(f'/shows/{created_show.id}')

# Read methods
def index(request):
    return redirect('/shows')

def dashboard(request):
    content = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'dashboard.html', content)

def one_show(request, show_id):
    content = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'display_show.html', content)

# Update methods
def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    content = {
        'show': show,
    }
    return render(request, 'edit_show.html', content)

def update_show(request, show_id):
    show_to_update = Show.objects.get(id=show_id)
    show_to_update.title = request.POST['title']
    show_to_update.network = request.POST['network']
    show_to_update.desc = request.POST['desc']
    if request.POST['release']:
        show_to_update.release = request.POST['release']
    show_to_update.save()
    return redirect(f'/shows/{show_id}')

# Delete methods
def delete_show(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')