from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth import logout
from .forms import SignupForm

def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render (request, 'main/index.html',{
        'cateories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'main/contact.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')

def privacy(request):
    """Renders the Privacy Policy page."""
    return render(request, 'main/privacy.html')

def terms(request):
    """Renders the Terms of Use page."""
    return render(request, 'main/terms.html')

def signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'main/signup.html',{
        'form' : form
    })
def custom_logout_view(request):
    """Handles logging out and redirects to the homepage."""
    # This check is technically not required since the URL pattern is usually secured
    # but it ensures the action is only performed on a POST request.
    if request.method == 'POST':
        logout(request)
        return redirect('main:index') # Redirect to the homepage URL name

    # Fallback/security: If someone tries GET, redirect them away
    return redirect('main:index')
