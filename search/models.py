from django.db import models

# Create your models here.
class Maize_cluster(models.Model):
    id = models.AutoField(primary_key=True)
    chromosome=models.IntegerField()
    cluster_start=models.IntegerField()
    cluster_end=models.IntegerField()
    strand=models.CharField(max_length=10)
    pac = models.IntegerField()
    pac_suppoort = models.IntegerField()
    cluster_support = models.IntegerField()
    region = models.CharField(max_length=20)
    gene_id = models.CharField(max_length=20)
    transcript_id = models.CharField(max_length=20)
    distance = models.CharField(max_length=20)
    transcript_code = models.CharField(max_length=10)
    gene_cord = models.CharField(max_length=20)
    utr_length = models.IntegerField()
    gene_biotype = models.CharField(max_length=10)
    cluster_size = models.IntegerField()
    number_pas = models.IntegerField()


def __str__(self):
    return self.gene_id






