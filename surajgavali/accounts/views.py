from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            #log the user in

            login(request,user)
            return redirect('articles:home')
    
    else:
        signup_form = UserCreationForm()

    return render(request,'accounts/signup.html',{'signup_form':signup_form})

def login_view(request):

    if request.method == 'POST':

        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            #login the user
            user = login_form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:home')

    else:
        login_form = AuthenticationForm()
    
    
    return render(request,'accounts/login.html',{'login_form' : login_form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:home')