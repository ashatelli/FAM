from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext

from fam_account.models import *
# import * imports all the models

def user_trans (request):
    context = RequestContext(request)
    context_dict = {'user_trans': user_trans}
    return render_to_response('fam_account/user_trans.html', context_dict,context)


def index(request):
    context = RequestContext(request)
    context_dict = {'variable_name': "WELCOME TO FAM WEBSITE"}
    return render_to_response('fam_account/index.html', context_dict, context)


def list(request,id):
    context = RequestContext(request)
    transaction_list = Transaction.objects.order_by('choice__category__name')
    context_dict = {
        'transactions': transaction_list,
        'id':id,
        }
    return render_to_response('fam_account/list.html', context_dict, context)

def category_list(request,id):
     if request.method=="POST":
        choice=request.POST["category"]
        print choice
        total_transaction = Transaction.objects.get(pk=id)
        c = Choice.objects.get(pk=choice)
        #print c
        total_transaction.choice=c
        total_transaction.save()


        return redirect('total_transaction', id=id)
     else:

        context = RequestContext(request)
        category_list = Choice.objects.all()
        context_dict = {
            'category_list': category_list,
            'id':id,
            }
        return render_to_response('fam_account/category_list.html', context_dict, context)


def uncategory_list(request,id):
    context = RequestContext(request)
    uncategory_list = Transaction.objects.filter(choice__isnull=True)
    #uncategory_list= Transaction.objects.all()
    context_dict = {
        'uncategory_list': uncategory_list,
        'id': id,
        }
    return render_to_response('fam_account/uncategory_transaction_list.html', context_dict, context)


def total_transaction(request, id):
    context = RequestContext(request)
    total_transaction = Transaction.objects.get(pk=id)
    context_dict = {
        'total_transaction ': total_transaction,
        'id': id,
        'amount': total_transaction.amount,
        'date' :total_transaction.date,
        'choice':total_transaction.choice,
        # in green words we can pul out in templates

    }

    return render_to_response('fam_account/total_transaction.html', context_dict, context)


def edit_amount(request,id ):
    if request.method=="POST":
        amount=request.POST["amount"]
        print amount
        total_transaction = Transaction.objects.get(pk=id)
        total_transaction.amount= amount
        total_transaction.save()
        return redirect('total_transaction', id=id)


    else:

        context = RequestContext(request)
        total_transaction = Transaction.objects.get(pk=id)
        context_dict = {
            'transaction': total_transaction,
            'id' : id,

            }
        return render_to_response('fam_account/edit_amount.html', context_dict, context)


def vendor(request,id):
    context = RequestContext(request)
    vendor= Vendor.objects.all()
    context_dict = {
        'vendor': vendor,
        'id':id,
        }
    return render_to_response('fam_account/vendor.html', context_dict, context)

def add_vendor(request,id):
    context = RequestContext(request)
    context_dic = {
        'add_vendor':add_vendor,
        'id': id,
        }
    return render_to_response('fam_account/add_vendor.html',context_dic,context)


