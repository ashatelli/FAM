from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name= models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Choice(models.Model):
    category = models.ForeignKey(Category)
    name= models.CharField(max_length=200)

    def __unicode__(self):
        return self.category.name+'- ' + self.name



class Vendor(models.Model):
    name= models.CharField(max_length=200)

    def __unicode__(self):
        return self.name




class Transaction(models.Model):
    amount = models.FloatField(default=0)
    choice = models.ForeignKey(Choice)
    vendor = models.ForeignKey(Vendor)
    note = models.CharField(max_length=200)
    User = models.ForeignKey(User)
    def __unicode__(self):
       return self.choice.category+'-'+ str(self.amount)


       #return self.amount
#wehen we add amount 666 and note in amazon .it created transaction
#object... so to diplay our amazon
#def__unicode__ has implimented

