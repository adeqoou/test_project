from .forms import *
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView


# Доступ к продукту пользователь будет получать через авторизацию и регистрацию
class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegForm
    success_url = 'index'
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class LoginUserView(LoginView):
    template_name = 'users/authorization.html'
    form_class = LoginUserForm
    success_url = 'index'
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)