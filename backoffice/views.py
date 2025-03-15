from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def custom_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '/backoffice/')
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'register.html', {'form': form})

@login_required
@permission_required('mywebcv.can_edit_content', raise_exception=True)
def backoffice(request):
    return render(request, 'page.html')
def add_certificate(request):
    return render(request, 'add_certificate.html')