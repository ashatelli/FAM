from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from fam_account.models import Transaction,Choice
#from fam_account.models import User


def index(request):
    context = RequestContext(request)
    context_dict={'variable_name' : "WELCOME TO FAM WEBSITE"}
    return render_to_response('fam_account/index.html',context_dict,context)

def list(request):
    context = RequestContext(request)
    transaction_list = Transaction.objects.order_by('choice__category__name')
    context_dict = {'transactions': transaction_list}
    return render_to_response('fam_account/list.html',context_dict ,context)

def category_list(request):
    context = RequestContext(request)
    category_list = Choice.objects.all()
    context_dict = {'categories': category_list}
    return render_to_response('fam_account/category_list.html',context_dict ,context)

def uncategory_list(request):
    context = RequestContext(request)
    uncategory_list= Transaction.objects.filter(choice__isnull=True)
    #uncategory_list= Transaction.objects.all()
    context_dict= {'uncategory_list': uncategory_list}
    return render_to_response('fam_account/uncategory_transaction_list.html',context_dict,context)

def total_transaction(request):
    context = RequestContext(request)
    total_transaction= Transaction.objects.order_by('choice__category__amount')
    context_dict = {'total_transaction ':total_transaction}
    return render_to_response('fam_account/total_transaction.html',context_dict,context)

def edit_amount(request):
    context = RequestContext(request)
    context_dict = {'calculator': edit_amount}
    return render_to_response('fam_account/edit_amount.html',context_dict,context)

def vendor(request):
    context = RequestContext(request)
    context_dict={'vendor':vendor}
    #vendor_list= vendor.objects.all()
    return render_to_response('fam_account/vendor.html',context_dict,context)
