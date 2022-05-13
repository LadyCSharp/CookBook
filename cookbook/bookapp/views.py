from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Recipes
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def main_view(request):
    posts = Recipes.objects.all()
    return render(request, 'bookapp/index.html', context={'posts': posts})



def create_recipe(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Ваш сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, 'bookapp/create.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'bookapp/create.html', context={'form': form})

def post(request, id):
    post = get_object_or_404(Recipes, id=id)
    return render(request, 'bookapp/post.html', context={'post': post})