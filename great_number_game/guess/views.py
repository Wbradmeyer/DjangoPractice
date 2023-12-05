from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'secret_number' not in request.session:
        request.session['secret_number'] = random.randint(1, 100)
        request.session['count'] = 5
        request.session['message'] = None
        request.session['correct'] = False
    return render(request, 'index.html')

def guess_number(request):
    if request.session['count'] == 0: return redirect('/')
    if request.session['secret_number'] == int(request.POST['guess']):
        request.session['message'] = 'That was the number! Play again.'
        request.session['correct'] = True
        request.session['count'] = 0
        return redirect('/')
    elif request.session['secret_number'] < int(request.POST['guess']):
        request.session['message'] = 'Too high!'
        request.session['count'] -= 1
    else:
        request.session['message'] = 'Too low!'
        request.session['count'] -= 1
    if request.session['count'] == 0 and request.session['correct'] == False:
        request.session['message'] = 'Game over!'
    return redirect('/')

def destroy_session(request):
    del request.session['secret_number']
    del request.session['count']
    del request.session['message']
    return redirect('/')