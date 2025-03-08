from django.db import models

# Create your models here.

class Tablessnort(models.Model):
    ID = models.AutoField(primary_key=True)
    alert = models.CharField(max_length=1000, null=True)
    Prediction_ml = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'tablessnort'



class Tableossec(models.Model):
    num = models.AutoField(primary_key=True)
    rule_level = models.IntegerField(null=True, default=None)
    rule_comment = models.CharField(max_length=255, null=True, default=None)
    rule_sidid = models.IntegerField(null=True, default=None)
    rule_firedtimes = models.IntegerField(null=True, default=None)
    rule_groups = models.CharField(max_length=255, null=True, default=None)
    location = models.CharField(max_length=300, null=True, default=None)
    hostname = models.CharField(max_length=300, null=True, default=None)
    program_name = models.CharField(max_length=300, null=True, default=None)
    decoder_desc = models.TextField(null=True, default=None)
    agent_name = models.CharField(max_length=255, null=True, default=None)
    timestamp = models.DateTimeField(null=True, default=None)
    logfile = models.CharField(max_length=300, null=True, default=None)
    id = models.CharField(max_length=255, null=True, default=None)
    prediction_ml = models.CharField(max_length=50, null=True, default=None)

    class Meta:
        db_table = 'tableossec'

