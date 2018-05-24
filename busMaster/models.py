from django.db import models

# Create your models here.

class routeMaster(models.Model):
    rid=models.AutoField(primary_key=True)
    rname=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.rname


class stopMaster(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.sname

class routeStop(models.Model):
    rsid=models.AutoField(primary_key=True)
    stop_id=models.ForeignKey(stopMaster, on_delete=models.CASCADE)
    route_id=models.ForeignKey(routeMaster, on_delete=models.CASCADE)
    stopNum=models.IntegerField(default=1)
    class Meta:
        unique_together=(('stop_id','route_id','stopNum'),)
    # def __str__(self):
    #    return self.route_id,self.stop_id,self.stopNum
