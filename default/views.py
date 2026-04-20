from django.shortcuts import render, redirect
from default.models import check_form

def home(request):
    if not request.session.get('user_id'):
        return redirect('login')
    messages_data = check_form.objects.all().order_by('-created_at')
    context = {
        'username': request.session.get('username'),
        'messages_data': messages_data,
    }
    return render(request, 'main/home.html', context)
