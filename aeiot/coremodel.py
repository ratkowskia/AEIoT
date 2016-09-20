from __future__ import unicode_literals

#from django.db import models
from django.db import models
from django.core.urlresolvers import reverse


#from google.appengine.ext import ndb


class Supplier(models.Model): # todo
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Consumer(models.Model):  # todo
    name = models.CharField(max_length=200)


class DataFormat(models.Model):  # todo
    name = models.CharField(max_length=200)
    semantics = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class DataCollection(models.Model):
    name = models.CharField(max_length=200)

class DataSet(DataCollection):
    data_name = models.CharField(max_length=200)

class ResultSet(DataCollection):
    result_name = models.CharField(max_length=200)

class Resource(models.Model):
    name = models.CharField(max_length=200)

class Storage(Resource):
    mb = models.FloatField

class CPU(Resource):
    cycles = models.FloatField

class Billing(models.Model):
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier)
    consumer = models.ForeignKey(Consumer)

class Algorithm(models.Model):
    name = models.CharField(max_length=200)
    semantics = models.CharField(max_length=200)
    source_code = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier)
    input_format = models.ForeignKey(DataFormat, related_name="alg_input_format")
    output_format = models.ForeignKey(DataFormat, related_name="alg_otuput_format")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('aeiot:algorithm-detail', kwargs={'pk': self.pk})

class AlgorithmExecution(models.Model):
    consumer = models.ForeignKey(Consumer)
    algorithm = models.ForeignKey(Algorithm)
    result_set = models.ForeignKey(ResultSet)
    data_set = models.ForeignKey(DataSet)
    resource = models.ForeignKey(Resource)

class BillingRecord(models.Model):
    billing = models.ForeignKey(Billing)
    resource = models.ForeignKey(Resource)
    algorithm_execution = models.ForeignKey(AlgorithmExecution)
    amount = models.FloatField