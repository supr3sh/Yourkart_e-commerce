from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    product_desc = models.CharField(max_length=1000)
    release_date = models.DateField()
    price = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to="shop/images", default="")
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    query = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    items_json = models.CharField(max_length=10000, default="")
    amount = models.IntegerField(max_length=100, default=0)
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " " + str(self.order_id)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..." + str(self.order_id)