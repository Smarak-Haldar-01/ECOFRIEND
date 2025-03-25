from django.db import models

class login_details(models.Model):
  name = models.CharField(null=False, blank=False, max_length=250)
  email = models.TextField(null=False, blank=False)
  password = models.CharField(max_length=100, null=False, blank=False)
  user_type = models.IntegerField(null=False, blank=False)
  last_login = models.DateTimeField(null=True, blank=True)
  last_logout = models.DateTimeField(null =True, blank = True)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)