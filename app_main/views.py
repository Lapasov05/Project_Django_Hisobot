from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from .forms import CostForm
from .models import Cost
from datetime import datetime, timedelta
from django.db.models import Q, Sum
from .models import Cost


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    full_name = request.user.get_full_name()
    Chiqim_list = Cost.objects.filter(owner_id=request.user,transaction_type='Chiqim')  # Use 'user' instead of 'owner_id'
    Kirim_list = Cost.objects.filter(owner_id=request.user,transaction_type='Kirim')  # Use 'user' instead of 'owner_id'

    context = {
        "full_name": full_name,
        'Kirim': Kirim_list,
        'Chiqim':Chiqim_list
    }

    return render(request, 'app_main/home.html', context)

    return render(request, 'app_main/home.html', context)


# @login_required
# def chiqim_get_costs_within_7_days(request):
#     costs_list = Cost.objects.filter(owner_id=request.user)  # Use 'user' instead of 'owner_id'
#     print(f"Costs for user {request.user}: {costs_list}")
#
#     context = {
#         'costs': costs_list  # Ensure the context variable matches your template usage
#     }
#
#     return render(request, 'app_main/home.html', context)

@login_required()
def get_cost_info(request,cost_id):
    cost = get_object_or_404(Cost, id=cost_id, owner_id=request.user)
    context = {
        'Cost': cost
    }

    return render(request, 'app_main/cost_info.html', context)



@login_required
def add_cost(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        transaction_type = request.POST.get('transaction_type')

        if name and amount and transaction_type:  # Ensure all fields are filled
            cost = Cost.objects.create(
                name=name,
                amount=amount,
                transaction_type=transaction_type,
                owner_id=request.user
            )
            cost.save()
            return redirect('/costs/')  # Redirect to the costs page after adding

    return render(request, 'app_main/add_cost.html')  # Render a form for adding costs


@login_required
def update_cost(request, cost_id):
    cost = get_object_or_404(Cost, id=cost_id, owner_id=request.user)

    if request.method == 'POST':
        form = CostForm(request.POST, instance=cost)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the list of costs
    else:
        form = CostForm(instance=cost)

    return render(request, 'app_main/update_cost.html', {'form': form, 'cost': cost})


@login_required
def delete_cost(request, cost_id):
    cost = get_object_or_404(Cost, id=cost_id, owner_id=request.user)
    if request.method == 'POST':
        cost.delete()
        return redirect('/')  # Redirect to the list of costs after deletion
    return render(request, 'app_main/confirm_delete.html', {'cost': cost})


def chiqim_get_costs_within_7_days(request):
    # Get the current date
    today = datetime.now().date()

    # Calculate the date 7 days ago
    seven_days_ago = today - timedelta(days=7)

    # Filter costs added within the last 7 days
    costs_within_7_days_chiqim = Cost.objects.filter(
        Q(created__date__gte=seven_days_ago) & Q(created__date__lte=today) & Q(transaction_type='Chiqim')
    )
    summa = costs_within_7_days_chiqim.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'app_main/chiqim_7_days.html', {
        'costs_within_7_days_chiqim': costs_within_7_days_chiqim,
        'summa': summa
    })


def chiqim_get_costs_within_30_days(request):
    # Get the current date
    today = datetime.now().date()

    # Calculate the date 30 days ago
    seven_days_ago = today - timedelta(days=30)

    # Filter costs added within the last 30 days
    costs_within_30_days_chiqim = Cost.objects.filter(
        Q(created__date__gte=seven_days_ago) & Q(created__date__lte=today) & Q(transaction_type='Chiqim')
    )
    summa = costs_within_30_days_chiqim.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'app_main/chiqim_30_days.html', {
        'costs_within_30_days_chiqim': costs_within_30_days_chiqim,
        'summa': summa
    })

def kirim_get_costs_within_7_days(request):
    # Get the current date
    today = datetime.now().date()

    # Calculate the date 7 days ago
    seven_days_ago = today - timedelta(days=7)

    # Filter costs added within the last 7 days
    costs_within_7_days_kirim = Cost.objects.filter(
        Q(created__date__gte=seven_days_ago) & Q(created__date__lte=today) & Q(transaction_type='Kirim')
    )
    summa = costs_within_7_days_kirim.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'app_main/chiqim_7_days.html', {
        'costs_within_7_days_chiqim': costs_within_7_days_kirim,
        'summa': summa
    })


def kirim_get_costs_within_30_days(request):
    # Get the current date
    today = datetime.now().date()

    # Calculate the date 30 days ago
    seven_days_ago = today - timedelta(days=30)

    # Filter costs added within the last 30 days
    costs_within_30_days_kirim = Cost.objects.filter(
        Q(created__date__gte=seven_days_ago) & Q(created__date__lte=today) & Q(transaction_type='Kirim')
    )
    summa = costs_within_30_days_kirim.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'app_main/kirim_30_days.html', {
        'costs_within_30_days_kirim': costs_within_30_days_kirim,
        'summa': summa
    })