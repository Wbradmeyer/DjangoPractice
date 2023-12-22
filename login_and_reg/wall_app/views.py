from django.shortcuts import render, redirect
from .models import Message
from .models import Comment
from user_app.models import User

# Create your views here.
def display_wall(request):
    content = {
        'all_messages': Message.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'wall.html', content)

def create_message(request):
    this_user = User.objects.get(id=request.POST['user_id'])
    Message.objects.create(message = request.POST['message'],
                        user = this_user)
    return redirect('/wall')

def create_comment(request):
    this_user = User.objects.get(id=request.POST['user_id'])
    this_message = Message.objects.get(id=request.POST['message_id'])
    Comment.objects.create(comment = request.POST['comment'],
                        user = this_user,
                        message = this_message)
    return redirect('/wall')

def delete_message(request, message_id):
    message_to_delete = Message.objects.get(id=message_id)
    message_to_delete.delete()
    return redirect('/wall')

def delete_comment(request, comment_id):
    comment_to_delete = Comment.objects.get(id=comment_id)
    comment_to_delete.delete()
    return redirect('/wall')