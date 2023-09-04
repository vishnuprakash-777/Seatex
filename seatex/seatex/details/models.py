from django.db import models

class Details(models.Model):
    status = models.CharField(max_length=10)
    RegNo = models.CharField(max_length=15)

    def __str__(self):
        return self.RegNo
    

class RoomDetails(models.Model):
    roomno=models.IntegerField()
    rows=models.IntegerField()
    columns=models.IntegerField()
    noofbenches=models.IntegerField()
    benchstrength=models.IntegerField()

    def __str__(self):
        return f"{self.roomno}"
