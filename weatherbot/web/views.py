from msilib.schema import Error

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from users.models import User

from . import bot
from .forms import RegForm


def index(request):
    post_list = User.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    main = True
    return render(
        request,
        'index.html',
        {'page': page, 'index': main}
    )


def register(request, user_id):
    header = 'Изменение размера изображения'
    card = 'Редактирование изображения'
    action = 'Изменить'
    user = get_object_or_404(User, pk=user_id)
    form = RegForm(
        request.POST or None,
        files=request.FILES or None,
        instance=user
    )
    if form.is_valid():
        reg_user = form.save(commit=False)
        tg_id = form.cleaned_data['tg_id']
        if tg_id:
            reg_user.status = True
        reg_user.save()
        return redirect('index')
    return render(
        request,
        'register.html',
        {'image': user, 'form': form, 'user_id': user_id,
         'header': header, 'card': card,
         'action': action}
    )


def weather(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user.status is True:
        tg_id = user.tg_id
        bot.tg_bot(tg_id)
        return redirect('index')
    raise Error(message='Сначала зарегистрируйтесь в боте')
