from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from fam_account.models import Transaction
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
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render_to_response('fam_account/category_list.html',context_dict ,context)

