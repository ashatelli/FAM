import os
from fam_account.models import Transaction,Choice,Category

def populate():
    Automobile = Category.objects.get_or_create(category_list="Automobile")


    Choice.objects.get_or_create(choice_text=["AAA or Road Services","Fuel","Insurance","lease","Maintenance","Mileage","Registerion&Tax","Other"])
    Entertainment=Category.objects.get_or_create(category_list="Entertainment")
    Choice.objects.get_or_create(choice_text=["Concert","Movies","Party","Sports","other"])
    food = Category.objects.get_or_create(category_list = "Food")
    Choice.objects.get_or_create(choice_text= ["Groceries","Restaurant","Snack","Other"])

if __name__ == "__main__":
    print "Starting FAM populating script...."
    os.environ.setdefault('DJANGO_SETTING_MODULE','FAM/settings.py')
    #from fam_account.models import Transaction,Choice,Category
    populate()