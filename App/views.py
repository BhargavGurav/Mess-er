from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import cache_control 
from django.contrib import messages 
from .models import *
import requests 
from datetime import datetime, timedelta, date

# from django.contrib.gis.utils import GeoIP
# from ip2geotools.databases.noncommercial import DbIpCity

# Create your views here.

def home(request):
    

    # try:
    #     response = DbIpCity.get(ip, api_key='free')
    #     location = response.country + " | " + response.city
    # except:
    #     location = "Not known"

    # print(location)

    details = [[i,j] for i,j in zip(MessOwner.objects.all(), MessMenu.objects.all())]
    # mess_owners = MessOwner.objects.all()
    # for i in MessMenu.objects.all():
    #     # print(i)
    #     details.append([i, MessOwner.objects.get(user=i.user.user)])
    
    context = {}
    context['owner_detail'] = details
    print(details)

    # context['city'] = city

    # api_key = 'aa2652a772d0410cbaf300ff7982e6da'
    # api_url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip}'
    # response = requests.get(api_url)
    # print(response.content)
    return render(request, 'home.html', context)

def saveContactus(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        contactus = Contact(email=email, message=msg)
        contactus.save()
        messages.success(request, 'Got your message. Thank you for contacting.')
        return HttpResponseRedirect('/')

    
@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        # print(username, password)
        
        if User.objects.filter(username=username):  
            usr = authenticate(username=username, password=password)
            if usr:
                login(request, usr)
                messages.success(request, 'Login successful.')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Wrong username or password.')
                return HttpResponseRedirect('loginUser')
        else:
            messages.error(request, 'No user found.')
            return HttpResponseRedirect('/')
            

def aboutus(request):
    return render(request, 'about_us.html')


@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mess = request.POST.get('mess-name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        state = request.POST.get('state')
        district = request.POST.get('district')
        address = request.POST.get('address')
        password = request.POST.get('password')

        
        if len(password) < 8:
            messages.error(request, 'Password must be 8 character long.')
            return HttpResponseRedirect('/')

        if not any(x.isdigit() for x in password):
            messages.error(request, 'Password must contain at least one digit.')
            return HttpResponseRedirect('/')

        if not any(x.islower() for x in password):
            messages.error(request, 'Password must contain at least one small letter.')
            return HttpResponseRedirect('/')

        if not any(x.isupper() for x in password):
            messages.error(request, 'Password must contain at least one capital letter.')
            return HttpResponseRedirect('/')

        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = fname
            user.last_name = lname
            user.is_staff = True
            user.save()

            mess_owner = MessOwner(user=user, mess=mess, contact=mobile, state=state, district=district, address=address)
            mess_owner.save()
            mess_menu = MessMenu(user=mess_owner)
            mess_menu.save()

            messages.success(request, 'Registered successfully')
            return HttpResponseRedirect('/')

    return render(request, 'register.html')

@login_required(login_url='loginUser')
@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def profile(request):
    logged_user = MessOwner.objects.get(user=request.user)
    context = {}
    context['owner'] = logged_user


    if request.method == 'POST':
        item1 = request.POST.get('item1')
        item2 = request.POST.get('item2')
        item3 = request.POST.get('item3')
        item4 = request.POST.get('item4')
        item5 = request.POST.get('item5')
        item6 = request.POST.get('item6')
        item7 = request.POST.get('item7')
        item8 = request.POST.get('item8')
        item9 = request.POST.get('item9')
        item10 = request.POST.get('item10')

        mess_menu = MessMenu.objects.get(user=logged_user)
        mess_menu.item1 = item1
        mess_menu.item2 = item2
        mess_menu.item3 = item3
        mess_menu.item4 = item4
        mess_menu.item5 = item5
        mess_menu.item6 = item6
        mess_menu.item7 = item7
        mess_menu.item8 = item8
        mess_menu.item9 = item9
        mess_menu.item10 = item10
        mess_menu.save()
        messages.success(request, 'Menu Updated successfully')
        return HttpResponseRedirect('/')

    mess_menu = MessMenu.objects.get(user=logged_user)
    context['menu'] = mess_menu
    return render(request, 'profile.html', context)

@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def requestedProfile(request, id):
    context = {}
    id = str(int(id) + 1)
    requestUser = User.objects.get(id=id)
    owner = MessOwner.objects.filter(user=requestUser).first()
    context['requestUser'] = requestUser
    context['owner'] = owner
    return render(request, 'requestedProfile.html', context)

@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def registerCustomer(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        contact = request.POST.get('mobile')
        email = request.POST.get('email')
        mess = request.POST.get('mess-name')
        type = request.POST.get('type')
        registration = datetime.today().strftime("%Y-%m-%d")

        if type == '':
            messages.error(request, 'Please select type')
            return HttpResponseRedirect('/')
        if type == 'veg':
            per_month = 2500
        else:
            per_month = 3000
        
        messOwner = MessOwner.objects.get(mess=mess)
        print("\n\n\n\nHere \n", full_name, email, contact, mess, type, registration, per_month)
        customer = Customer(full_name=full_name, email=email, contact=contact, mess=messOwner, type=type, registration=registration, per_month=per_month)
        customer.save()
        messages.success(request, 'Registered successfully')
        return HttpResponseRedirect('/')

@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def customers(request, id):

    context = {}
    # print(id)
    requestUser = User.objects.get(id=id)
    # print("\n\nhere", requestUser)

    owner = MessOwner.objects.filter(user=requestUser).first()
    # print("\n\nhere",  owner.mess)

    customers = Customer.objects.filter(mess=owner)

    # print("\n\nhere", requestUser, owner, customers)

    # context['requestUser'] = requestUser
    # context['owner'] = owner

    context['data'] = customers
    # print("here is list : ", customers)
    return render(request, 'customers.html', context)

@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def attendance(request, id):
    customer = Customer.objects.get(id=id)
    attendance = Attendance.objects.filter(customer=customer)
    # print(attendance)
    if request.method == 'POST':
        date_ = request.POST.get('date')
        lunch =  request.POST.get('lunch')
        dinner =  request.POST.get('dinner')
        # print('-'*10, lunch, dinner, '-'*10)
        lunch = True if lunch == 'on' else False
        dinner = True if dinner == 'on' else False

        date_ = str(date_)
        date_ = date_[0:3] + date_[5:]
        date_ = datetime.strptime(str(date_) , "%b %d, %Y").strftime('%Y-%m-%d')
        att = Attendance(customer=customer, date=date_, morning=lunch, evening=dinner)
        att.save()
        messages.success(request, 'Saved')
        return HttpResponseRedirect(f'/attendance/{id}')

    context = {}
    list_dates = []
    try:
        last_attendance =  Attendance.objects.filter(customer=customer).last()
        print('-'*10, last_attendance.date, '-'*10)
    except:
        print('-'*10, 'Not found', '-'*10)
    if last_attendance:
        registration_date, registration_month, registration_year = [last_attendance.date.strftime('%d'), last_attendance.date.strftime('%m'), last_attendance.date.strftime('%Y')]
        registration_date = date(int(registration_year), int(registration_month), int(registration_date))
        registration_date += timedelta(days=1)
    else:
        registration_date, registration_month, registration_year = [customer.registration.strftime('%d'), customer.registration.strftime('%m'), customer.registration.strftime('%Y')]
        registration_date = date(int(registration_year), int(registration_month), int(registration_date))
        
    today_date, todays_month, todays_year = [datetime.today().strftime('%d'), datetime.today().strftime('%m'), datetime.today().strftime('%Y')]
    todays_date = date(int(todays_year), int(todays_month), int(today_date))

    isSame = False
    try:
    # user = User.objects.get(user=request.user)
        mess = MessOwner.objects.get(user=request.user)
        print( mess, customer.mess)
        if str(mess.mess) == str(customer.mess):
            isSame = True
    except:
        print('Error')
    
    i = registration_date
    while i <= todays_date:
        list_dates.append(i)
        i += timedelta(days=1)

    # print('\n'*5)
    # print(list_dates, isSame)
    # print('\n'*5)
    context['customer'] = customer
    context['dates'] = list_dates
    context['isSame'] = isSame
    context['attendance'] = attendance

    return render(request, 'attendance.html', context)


@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def requestedCustomer(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'requestCustomer.html', {'customer' : customer})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutuser(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return HttpResponseRedirect('/')


