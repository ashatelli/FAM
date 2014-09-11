from django.contrib import admin
from fam_account.models import Transaction
from fam_account.models import Category
from fam_account.models import Vendor
from fam_account.models import Choice

from django.contrib.auth.models import User




admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Vendor)
#admin.site.register(User)
admin.site.register(Choice)