from datetime import datetime
from json import JSONEncoder
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import models


@csrf_exempt
def submit_income(request):
    # todo : valid data user might be fake token might be fake and amount
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    models.Income.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok'
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_expense(request):
    # todo : valid data user might be fake token might be fake and amount
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    models.Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok'
    }, encoder=JSONEncoder)