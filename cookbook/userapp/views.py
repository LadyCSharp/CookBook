from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import RegistrationForm

from .models import BookUser, Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):
    model = BookUser
    template_name = 'userapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')


class ProfileListView(ListView):
    model = Profile
    template_name = 'userapp/profile_list.html'
    paginate_by = 10



# детальная информация
class ProfileDetailView(DetailView):
    fields = '__all__'
    model = Profile
    template_name = 'userapp/profile_detail.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Profile, pk=self.id)


# создание тега
class ProfileCreateView(LoginRequiredMixin, CreateView):
    # form_class =
    fields = '__all__'
    model = Profile
    success_url = reverse_lazy('users:login')
    template_name = 'userapp/profile_create.html'

    def post(self, request, *args, **kwargs):
        """
        Пришел пост запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    model = Profile
    success_url = reverse_lazy('users:login')
    template_name = 'userapp/profile_create.html'


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'userapp/profile_delete.html'
    model = Profile
    success_url = reverse_lazy('users:login')