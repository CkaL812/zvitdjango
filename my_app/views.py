from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User as DjangoUser
from django.views.generic import TemplateView

from .models import Users, Photos
from .forms import CreateAccountForm


# === ГОЛОВНА СТОРІНКА ===
class IndexView(TemplateView):
    template_name = 'my_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photos.objects.all()
        return context


# === НАТИСКАННЯ НА ІКОНКУ КОРИСТУВАЧА ===
class UserIconClickView(View):
    def post(self, request):
        return redirect('login')

    def get(self, request):
        return redirect('index')


# === ЛОГІН КОРИСТУВАЧА ===
class LoginView(View):
    template_name = 'my_app/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # Перевірка на порожні поля
        if not email or not password:
            return render(request, self.template_name, {
                'error_message': 'Введіть email і пароль.'
            })

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return render(request, self.template_name, {
                'error_message': 'Користувача не знайдено.'
            })

        # Перевіряємо пароль
        if not user.check_password(password):
            return render(request, self.template_name, {
                'error_message': 'Невірний пароль.'
            })

        # Сесія користувача
        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        request.session['user_name'] = f"{user.first_name} {user.last_name}"

        # Якщо користувач — суперюзер Django
        if DjangoUser.objects.filter(email=user.email, is_superuser=True).exists():
            return redirect('/admin/')
        else:
            return redirect('index')


# === СТВОРЕННЯ АККАУНТА ===
class CreateAccountView(View):
    template_name = 'my_app/create_account.html'

    def get(self, request):
        form = CreateAccountForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Акаунт створено успішно! Тепер увійдіть у систему.")
            return redirect('login')
        else:
            messages.error(request, "Будь ласка, перевірте правильність введених даних.")
            return render(request, self.template_name, {'form': form})


# === СТОРІНКА КАТЕГОРІЇ ПРОДУКТІВ ===
class ProductCategoryView(View):
    template_name = 'my_app/products.html'

    def get(self, request, category):
        products = Photos.objects.filter(title_name_ev=category)
        categories = {
            'business': 'Business Meeting',
            'party': 'Party',
            'wedding': 'Wedding',
            'casual': 'Casual Walk',
        }
        category_title = categories.get(category, 'Products')
        return render(request, self.template_name, {
            'category': category_title,
            'products': products
        })
