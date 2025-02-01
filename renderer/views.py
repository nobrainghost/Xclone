from django.shortcuts import render,redirect


# Create your views here.
def render_timeline(request):
    return render(request, 'timeline.html')

def render_login_email(request):
    if request.method == 'POST':
        username=request.POST['username']
        # request.session['username'] = username
        response=redirect('login_password')
        response.set_cookie( 'username', 
            username, 
            max_age=300,  
            secure=False,   
            httponly=True, 
            samesite='Lax' 
        )
        return response
    return render(request, 'login_email.html')

def render_password_login(request):
    return render(request, 'password_login.html')

def render_profile(request):
    return render(request, 'profile_page.html')

def render_edit_profile(request):
    return render(request, 'edit_profile.html')