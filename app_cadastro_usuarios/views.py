from django.shortcuts import get_object_or_404, render
from .models import User
# from django.views.decorators.http import require_http_methods


def home(request):
    return render(request, 'users/home.html')


# @require_http_methods(['GET', 'POST'])
def users(request):
    new_user = User()

    if request.method == 'POST':
        new_user.name = request.POST.get('name')
        new_user.age = request.POST.get('age')
        new_user.save()
        
    users = {
        'users': User.objects.all()
    }
    
    return render(request, 'users/users.html', users)


def user_update(request, id):
    user = get_object_or_404(User, pk=id)
    
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.save()
        
        users = {
            'users': User.objects.all()
        }
        
        return render(request, 'users/users.html', users)
        
    user = {
        'user': User.objects.get(pk=id)
    }

    return render(request, 'users/user_update.html', user)


def user_delete(request, id):
    if request.method == 'POST':
        user_to_delete = get_object_or_404(User, pk=id)
        user_to_delete.delete()
        
        users = {
            'users': User.objects.all()
        }

        return render(request, 'users/users.html', users)
    
    user = {
        'user': User.objects.get(pk=id)
    }

    return render(request, 'users/user_delete.html', user)