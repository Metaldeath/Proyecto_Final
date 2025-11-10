from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

@login_required
def inbox(request):
    mensajes = request.user.mensajes_recibidos.order_by('-creado')
    return render(request, 'messaging/inbox.html', {'mensajes': mensajes})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.emisor = request.user
            msg.save()
            return redirect('messaging:inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send.html', {'form': form})
