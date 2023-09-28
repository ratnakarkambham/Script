from django.db import models

# Create your models here.



# Create your models here.

class Test(models.Model):
    test_uid = models.AutoField(primary_key=True)
    data = models.TextField()

    class Meta:
        managed = True
        db_table = 'test'
        #app_label = 'screenwriting'


class Screenplay(models.Model):
    screenplay_uid = models.BigAutoField(primary_key=True)
    title = models.TextField()
    success_percentage = models.FloatField()
    ip_address = models.TextField()
    geo_location = models.TextField()
    status = models.TextField()
    file_path = models.TextField()
    file_size = models.IntegerField()
    user_uid = models.BigIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    created_by = models.BigIntegerField()
    modified_by = models.BigIntegerField()
    language_uid = models.SmallIntegerField()
    #tenant_uid = models.ForeignKey(Tenant, on_delete=models.RESTRICT, to_field='tenant_uid', db_column='tenant_uid')
    process_time = models.BigIntegerField()
    failure_reason = models.TextField()

    class Meta:
        managed = True
        db_table = 'screenplay'
  

# api/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
