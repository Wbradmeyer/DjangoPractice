from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'visits' in request.session:
        request.session['visits'] = 1
    else:
        request.session['visits'] += 1

    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request, 'index.html')

def destroy(request):
    del request.session['visits']
    del request.session['count']
    return redirect('/')

def add_two_to_count(request):
    request.session['count'] += 1
    return redirect('/')

def add_custom_to_count(request):
    request.session['count'] += int(request.POST['add_count']) - 1
    return redirect('/')