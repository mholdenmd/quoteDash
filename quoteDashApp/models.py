from django.db import models
from django.db.models.deletion import CASCADE

import re

class UsersMan(models.Manager):
    def i_am_the_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emlTaken = Users.objects.filter(email = postData['eml'])
        print(postData)
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) == 0:
            errors["FirstnameRequired"] = "First name is required"
        elif len(postData['fname']) < 2:
            errors["Firstnamelen"] = "First name must be aleast 2 characters long"
        if len(postData['lname']) == 0:
            errors["FirstnameRequired"] = "First name is required" 
        elif len(postData['lname']) < 2:
            errors["LastnameRequired"] = "Last name should be at least 3 characters long"
        if len(postData['eml']) == 0:
            errors["emlRequired"] = "Please add an email address"
        elif not EMAIL_REGEX.match(postData['eml']):    # test whether a field matches the pattern            
            errors['eml'] = "Invalid email address!"
        elif len(emlTaken)>0:
            errors['emlTaken'] = "This email is taken, Try again!"

        
        if len(postData['PW']) < 8:
            errors["PWRequired"] = "Password should be at least 8 characters long"
        return errors

    def loginVal(self, postData): 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        print(postData)   
        errors = {}

        emailMatch = Users.objects.filter(email = postData['eml'])
        if len(emailMatch) == 0:
            errors['emailNotfound'] = "This email address is not found"

        elif emailMatch[0].password != postData ['PW']:
            errors['PWwrong'] = "incorrect password"

        
        if len(postData['eml']) == 0:
            errors["descriptionRequired"] = "Please add an email address"
        elif not EMAIL_REGEX.match(postData['eml']):    # test whether a field matches the pattern            
            errors['eml'] = "Invalid email address!"
        return errors

    def updateVal(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emlTaken = Users.objects.filter(email = postData['Email'])
        errors = {}
        if len(postData['fname']) == 0:
            errors["FirstnameRequired"] = "First name is required"
        elif len(postData['fname']) < 2:
            errors["Firstnamelen"] = "First name must be aleast 2 characters long"
        if len(postData['lname']) == 0:
            errors["FirstnameRequired"] = "First name is required" 
        elif len(postData['lname']) < 2:
            errors["LastnameRequired"] = "Last name should be at least 3 characters long"
        if len(postData['Email']) == 0:
            errors["emlRequired"] = "Please add an email address"
        elif not EMAIL_REGEX.match(postData['Email']):    # test whether a field matches the pattern            
            errors['eml'] = "Invalid email address!"
        elif len(emlTaken)>0:
            errors['emlTaken'] = "This email is taken, Try again!"
        return errors

class QuoteMan(models.Manager):
    def quoteVal(self, postData):
        errors = {}

        if len(postData['AT']) == 0:
            errors["AuthorRequired"] = "Author name is required"

        elif len(postData['AT']) < 3:
            errors["AuthorLen"] = "Author name must be atleast 3 characters long"

        if len(postData['QT']) == 0:
            errors["QuoteRequired"] = "Quote is required"

        elif len(postData['QT']) < 10:
            errors["QuoteLen"] = "Quote must be atleast 10 characters long"

        return errors



# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersMan()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Quotes(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    posted_by = models.ForeignKey(Users, related_name="quotes_uploaded", on_delete = models.CASCADE)
    wholiked = models.ManyToManyField(Users, related_name="liked_quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteMan()


    def __str__(self):
        return f"<Quotes object: {self.title} ({self.id})>"







