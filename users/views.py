import secrets

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from dz_5_curs import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        token = secrets.token_hex(11)

        user = form.save(commit=False)
        user.token = token
        user.is_active = False
        user.save()

        send_mail(
            subject='Регистрация',
            message=f'Авторизация удалась.  {token}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def verification_view(request):
    if request.method == 'POST':
        input_key = request.POST.get('token')
        try:
            user = User.objects.get(token=input_key)
            user.is_active = True
            user.save()
        except User.DoesNotExist:
            return render(request, 'users/fail_verif.html')
        return render(request, 'users/success_valid.html')
    return render(request, 'users/verification.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def recovery_view(request):
    if request.method == 'POST':
        input_email = request.POST.get('email')

        user = User.objects.get(email=input_email)
        user_password = secrets.token_hex(11)

        user.set_password(user_password)
        user.save()

        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш новый пароль  {user_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
    return render(request, 'users/recovery.html')

