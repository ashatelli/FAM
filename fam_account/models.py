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
    choice = models.ForeignKey(Choice,blank= True, null=True)#parementer says that this field is not mandatory to fill in brower
    vendor = models.ForeignKey(Vendor)
    note = models.CharField(max_length=200,blank=True)#null is only requre for foreigh key
    User = models.ForeignKey(User)
    date = models.DateTimeField()
    def __unicode__(self):
       return str(self.choice)+'-'+ str(self.amount)# return line18



    #ef__unicode__(self):
    #return self.user,username
       #return self.amount
#wehen we add amount 666 and note in amazon .it created transaction
#object... so to diplay our amazon
#def__unicode__ has implimented

