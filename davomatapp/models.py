from django.db import models
from django.contrib.auth.models import User

class Xodim(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=255)
    bolim = models.CharField(max_length=255)
    telefon_raqami = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.ism} {self.familiya}"

class Davomat(models.Model):
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE)
    boshlash_vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.xodim.ism} - {self.boshlash_vaqti}"




