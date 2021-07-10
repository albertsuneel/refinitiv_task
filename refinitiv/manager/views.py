import json

from django.shortcuts import render, redirect
from .models import Manager, Branches, Rates
from user.models import User
from .forms import LoginForm, AddUserForm, RequestResponseForm
from passlib.hash import phpass


def auth_user(func):
    def inner1(request, *args, **kwargs):
        global user
        if 'user' in request.session:
            session_id = request.session['user']
            try:
                user = Manager.objects.get(email=session_id)
                return func(request, *args, **kwargs)
            except Exception as e:
                print(e)
                del request.session['user']
                return redirect(login)
        else:
            return redirect(login)
    return inner1


@auth_user
def home(request):
    requests = User.objects.all()
    request_count = User.objects.filter(status=0).count()
    all_count = User.objects.all().count()
    accepted_count = User.objects.filter(status=1).count()
    pending_count = User.objects.filter(status=0).count()
    rejected_count = User.objects.filter(status=2).count()
    buy = User.objects.filter(status=1, position='Buy').count()
    sell = User.objects.filter(status=1, position='Sell').count()
    return render(request, 'manager_home.html', {"user": user, "requests": requests, 'count': request_count,
                                                 'all': all_count, 'accepted': accepted_count, 'pending': pending_count,
                                                 'rejected': rejected_count, 'buy': buy, 'sell': sell})


@auth_user
def create_user(request):
    if request.method == "POST":
        my_form = AddUserForm(request.POST)
        if my_form.is_valid():
            name = my_form.cleaned_data['name']
            email = my_form.cleaned_data['email']
            password = my_form.cleaned_data['password']
            manager = Manager(name=name, email=email, password=phpass.encrypt(password))
            try:
                manager.save()
                return redirect(home)
            except Exception as e:
                print(e)
                return redirect(home)


@auth_user
def upload_info(request):
    if request.method == "POST":
        file = request.FILES.getlist('file')[0].read()
        data = json.loads(file.decode('utf8').replace("'", '"'))
        if 'branches' in data.keys():
            for branch in data['branches']:
                if Branches.objects.filter(branch_id=branch["id"]):
                    branch_data = Branches.objects.get(branch_id=branch["id"])
                    branch_data.name = branch["name"]
                    branch_data.address_line1 = branch["address"]["line1"]
                    branch_data.address_line2 = branch["address"]["line2"]
                    branch_data.address_line3 = branch["address"]["line3"]
                    branch_data.city = branch["address"]["city"]
                    branch_data.zip = branch["address"]["zip"]
                    branch_data.country = branch["address"]["country"]
                    branch_data.tel = branch["address"]["tel"]
                    try:
                        branch_data.save()
                    except Exception as e:
                        print(e)
                else:
                    branch_data = Branches(branch_id=branch["id"], name=branch["name"],
                                           address_line1=branch["address"]["line1"],
                                           address_line2=branch["address"]["line2"],
                                           address_line3=branch["address"]["line3"], city=branch["address"]["city"],
                                           zip=branch["address"]["zip"], country=branch["address"]["country"],
                                           tel=branch["address"]["tel"])
                    try:
                        branch_data.save()
                    except Exception as e:
                        print(e)
        if 'rates' in data.keys():
            for rate in data["rates"]:
                if Rates.objects.filter(currency=rate["currency"]):
                    rate_data = Rates.objects.get(currency=rate["currency"])
                    rate_data.rate = rate["rate"]
                    rate_data.spread = rate["spread"]
                    try:
                        rate_data.save()
                    except Exception as e:
                        print(e)
                else:
                    rate_data = Rates(currency=rate["currency"], rate=rate["rate"], spread=rate["spread"])
                    try:
                        rate_data.save()
                    except Exception as e:
                        print(e)
    return redirect(home)


def login(request):
    return render(request, 'login.html', {})


def login_submit(request):
    if request.method == "POST":
        # Get the posted form
        my_form = LoginForm(request.POST)

        if my_form.is_valid():
            email = my_form.cleaned_data['email']
            password = my_form.cleaned_data['password']
            if Manager.objects.filter(email=email):
                user_data = Manager.objects.get(email=email)
                password_store = user_data.password
                if phpass.verify(password, password_store):
                    request.session['user'] = email
                    return redirect(home)
                else:
                    return redirect(login)
            else:
                return redirect(login)
        else:
            return redirect(login)
    return redirect(login)


@auth_user
def logout(request):
    if 'user' in request.session:
        try:
            del request.session['user']
        except Exception as e:
            print(e)
            pass
    return redirect(login)


@auth_user
def request_inside(request):
    if request.method == "GET":
        transaction_id = request.GET["transaction_id"]
        data = User.objects.get(transaction_id=transaction_id)
        request_count = User.objects.filter(status=0).count()
        return render(request, 'request_inside.html', {'data': data, 'count': request_count})


@auth_user
def request_response(request):
    if request.method == "POST":
        my_form = RequestResponseForm(request.POST)

        if my_form.is_valid():
            id = my_form.cleaned_data['id']
            comments = my_form.cleaned_data['comments']
            status = my_form.cleaned_data['status']
            data = User.objects.get(transaction_id=id)
            data.status = int(status)
            data.comments = comments
            data.save()
            return redirect('/hq/requestInside/?transaction_id='+id)
        else:
            print(my_form.errors)

    return redirect(home)


@auth_user
def report(request):
    data = User.objects.filter(status=1)
    request_count = User.objects.filter(status=0).count()
    buy = 0
    sell = 0
    for row in data:
        if row.position == 'Buy':
            buy += int(row.amount)*float(row.fx_rate_spread)
        if row.position == 'Sell':
            sell += int(row.amount)*float(row.fx_rate_spread)
    return render(request, 'report.html', {'data': data, 'count': request_count, 'buy': buy, 'sell': sell})
