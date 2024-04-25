from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    return render(request, 'index.html')

@login_required(login_url="login")
def accordion(request):

    return render(request, 'base/accordion.html')


@login_required(login_url="login")
def breadcrumb(request):
    return render(request, 'base/breadcrumb.html')


@login_required(login_url="login")
def cards(request):
    return render(request, 'base/cards.html')


@login_required(login_url="login")
def carousel(request):
    return render(request, 'base/carousel.html')


@login_required(login_url="login")
def collapse(request):
    return render(request, 'base/collapse.html')


@login_required(login_url="login")
def list_group(request):
    return render(request, 'base/list-group.html')


@login_required(login_url="login")
def navs_tabs(request):
    return render(request, 'base/navs-tabs.html')


@login_required(login_url="login")
def pagination(request):
    return render(request, 'base/pagination.html')


@login_required(login_url="login")
def placeholders(request):
    return render(request, 'base/placeholders.html')



@login_required(login_url="login")
def popovers(request):
    return render(request, 'base/popovers.html')



@login_required(login_url="login")
def progress(request):
    return render(request, 'base/progress.html')


@login_required(login_url="login")
def spinners(request):
    return render(request, 'base/spinners.html')


@login_required(login_url="login")
def tables(request):
    return render(request, 'base/tables.html')


@login_required(login_url="login")
def tooltips(request):
    return render(request, 'base/tooltips.html')


@login_required(login_url="login")
def charts(request):
    return render(request, 'charts.html')


@login_required(login_url="login")
def widgets(request):
    return render(request, 'widgets.html')


@login_required(login_url="login")
def colors(request):
    return render(request, 'colors.html')



@login_required(login_url="login")
def typography(request):
    return render(request, 'typography.html')


@login_required(login_url="login")
def checks_radios(request):
    return render(request, 'forms/checks-radios.html')


@login_required(login_url="login")
def floating_labels(request):
    return render(request, 'forms/floating-labels.html')


@login_required(login_url="login")
def form_control(request):
    return render(request, 'forms/form-control.html')




@login_required(login_url="login")
def input_group(request):

    return render(request, 'forms/input-group.html')



@login_required(login_url="login")
def layout(request):
    return render(request, 'forms/layout.html')


@login_required(login_url="login")
def range(request):
    return render(request, 'forms/range.html')



@login_required(login_url="login")
def select(request):
    return render(request, 'forms/select.html')


@login_required(login_url="login")
def validation(request):
    return render(request, 'forms/validation.html')



@login_required(login_url="login")
def button_group(request):
    return render(request, 'buttons/button-group.html')



@login_required(login_url="login")
def buttons(request):
    return render(request, 'buttons/buttons.html')



@login_required(login_url="login")
def dropdowns(request):
    return render(request, 'buttons/dropdowns.html')


@login_required(login_url="login")
def coreui_icons_brand(request):
    return render(request, 'icons/coreui-icons-brand.html')


@login_required(login_url="login")
def coreui_icons_flag(request):
    return render(request, 'icons/coreui-icons-flag.html')


@login_required(login_url="login")
def coreui_icons_free(request):
    return render(request, 'icons/coreui-icons-free.html')



@login_required(login_url="login")
def alerts(request):
    return render(request, 'notifications/alerts.html')


@login_required(login_url="login")
def badge(request):
    return render(request, 'notifications/badge.html')


@login_required(login_url="login")
def modals(request):
    return render(request, 'notifications/modals.html')


@login_required(login_url="login")
def toasts(request):
    return render(request, 'notifications/toasts.html')


#auth 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
           
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error_message': 'Username already exists'})
           
            if User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'error_message': 'Email already exists'})
           
            user = User.objects.create_user(username=username, email=email, password=password)
           
            return redirect('login')  
        else:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        error_message = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('index')





def custom_404(request, exception):
    return render(request, '404.html', status=404)

