from django.db import models


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name

