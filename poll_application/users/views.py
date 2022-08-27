from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def signup(request):                                
    if request.method == "POST":
        f_name = request.POST.get('first_name')
        username = request.POST.get('first_name')       
        email = request.POST.get('email')
        password = request.POST.get('password')

        error = False       


        if User.objects.filter(username = username).exists():
            print("username already taken")                          # printing a message in terminal
            messages.error(request, "username already taken")
            error = True

        if User.objects.filter(email = email).exists():
            print("EMAIL already taken")
            messages.error(request, "Email already taken")
            error = True

        if error:
            return render(request, 'user/signup.html')      


        
        try:
            user = User.objects.create_user(    
                username = f_name,
                first_name = f_name,            
                email = email,
                password = password

            )

            user.save()     # saving the object into database

            
            messages.success(request, "Account created successfully. Login to continue.")
            return redirect('login')

        except Exception as e:
            print(e)

    return render(request, 'user/signup.html')



def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')     
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)     

        if user is not None:            # if existing user
            login(request, user)        # creates a session 
            context = {
                'user' : user,
            }
            return render(request, 'poll/index.html', context)    

        else:
            messages.error(request, "Invalid Credentials")


    return render(request, 'user/login.html')




def signout(request):
    logout(request)                 # session is expired, logout is inbuilt function
    return redirect('login')  

