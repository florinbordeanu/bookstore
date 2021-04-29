from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import SignUpForm
from store.models import Product


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('store:all_products')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


class ChangePassword(PasswordChangeView):
    template_name = 'accounts/login.html'
    success_url = '/books'


def search_books(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books = Product.objects.filter(title__icontains=searched)
        return render(request, 'accounts/search.html', {'searched': searched, 'books': books})
    else:
        return render(request, 'accounts/search.html', {})




