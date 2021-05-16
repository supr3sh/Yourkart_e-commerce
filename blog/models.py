from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    head0 = models.CharField(max_length=1000, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=1000, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=1000, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    pub_by = models.CharField(max_length=500, default="")
    thumbnail = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.title + str(self.post_id)