from django.db import models


# Create your models here.
class Info(models.Model):
    Full_Name = models.CharField(max_length=100, null=True)
    university = models.CharField(max_length=100, null=True)
    topic = models.CharField(max_length=100, null=True)
    serial_no = models.CharField(max_length=100, unique=True)
    body = (
        ('Nadia Islam', 'Nadia Islam'),
        ('Laiba Tasnia', 'Laiba Tasnia'),
        ('Jahid Oyon', 'Jahid Oyon'),
        ('Anika Nargis', 'Anika Nargis'),
        ('Nusrat Meem', 'Nusrat Meem'),
        ('Mehenaj', 'Mehenaj'),
        ('Kheya', 'Kheya'),
    )
    editorial_body = models.CharField(max_length=100, choices=body, default='Nadia Islam')



    def __str__(self):
        return self.Full_Name


class EditorialBody(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)

    def __str__(self):
        return self.name
