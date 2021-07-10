from django.shortcuts import render, redirect
from manager.models import Branches, Rates
from .models import User
from .forms import RequestForm, RequestEditForm
from django.utils.crypto import get_random_string


def index(request):
    return render(request, 'index.html', {})


def new_request(request):
    branches = Branches.objects.all()
    rates = Rates.objects.all()
    return render(request, 'request.html', {"branches": branches, "rates": rates})


def request_submit(request):
    if request.method == "POST":
        my_form = RequestForm(request.POST)
        if my_form.is_valid():
            transaction_id = get_random_string(length=12)
            name = my_form.cleaned_data['name']
            position = my_form.cleaned_data['position']
            currency = my_form.cleaned_data['currency']
            amount = my_form.cleaned_data['amount']
            branch = my_form.cleaned_data['branch']
            rate_data = Rates.objects.get(currency=currency)
            fx_rate_hq = rate_data.rate
            fx_rate_spread = fx_rate_hq+(rate_data.spread/2) if position == "Buy" else fx_rate_hq-(rate_data.spread/2)
            request_data = User(transaction_id=transaction_id, name=name, position=position, currency=currency,
                                amount=amount, branch_id=branch, comments="", status=0, fx_rate_hq=fx_rate_hq,
                                fx_rate_spread=round(fx_rate_spread, 3))
            request_data.save()
            return render(request, 'response.html', {"transaction_id": transaction_id})
        else:
            print(my_form.errors())
    return redirect(index)


def transaction_inside(request):
    if request.method == "GET":
        transaction_id = request.GET["transaction_id"]
        branches = Branches.objects.all()
        rates = Rates.objects.all()
        data = User.objects.get(transaction_id=transaction_id)
        return render(request, 'transaction_inside.html', {'data': data, 'branches': branches, 'rates': rates})
    return redirect(index)


def edit_request(request):
    if request.method == "POST":
        my_form = RequestEditForm(request.POST)
        if my_form.is_valid():
            transaction_id = my_form.cleaned_data['id']
            data = User.objects.get(transaction_id=transaction_id)
            data.name = my_form.cleaned_data['name']
            data.position = position = my_form.cleaned_data['position']
            data.currency = currency = my_form.cleaned_data['currency']
            data.amount = my_form.cleaned_data['amount']
            data.branch_id = my_form.cleaned_data['branch']
            rate_data = Rates.objects.get(currency=currency)
            data.fx_rate_hq = fx_rate_hq = rate_data.rate
            data.fx_rate_spread = round(fx_rate_hq+(rate_data.spread/2) if position == "Buy"
                                        else fx_rate_hq-(rate_data.spread/2), 3)
            data.status = 0
            data.comments = ""
            data.save()
            return render(request, 'response.html', {"transaction_id": transaction_id})
        else:
            print(my_form.errors())
    return redirect(index)

