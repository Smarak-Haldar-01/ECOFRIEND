from django.shortcuts import render,HttpResponse
from db_admin.models import login_details
import datetime

_view_symbols = """
  1. -1 states that there is a db error
"""

def home(request):
    return render(request, 'home/home.html', {'title': 'HOME | ECO-Friend'})

def login_signin_home(request):

  if 'user_id' in request.session or 'user_email' in request.session:

    return render(request, 'admin/home.html', {'title':'Dashboard-A | ECO-Friend'})
  
  return render(request, 'home/login_signin.html', {'title':'Login-Signin | ECO-Friend'})

def login_action(request):

  if request.method == 'POST':

    email = request.POST['email']
    password = request.POST['password']

    try:

      login_object = login_details.objects.get(email=email, password=password)

      if len(login_object) > 0:

        request.session['user_email'] = email

        request.session['user_id'] = login_object.id

        if login_object.user_type == 1: #1-Admin / 2-Dealer  / 3-Seller

          try:

            login_object.last_login = datetime.datetime.now()

            login_object.save()

          except Exception as E:

            print(E)
            return HttpResponse(-1)
          
          else:

            return render(request, 'admin/home.html', {'title':'HOME | ECO-Friend'})

        elif login_object.user_type == 2:

          pass

        else:

          pass

    except Exception as E:
      print(E)

  
  return render(request, 'home/login_signin.html', {'title':'Login-Signin | ECO-Friend'})

def dashboard(request):  
    return render(request, 'home/dashboard.html', {'title': 'Dashboard | ECO-Friend'})  # Ensure the template exists
