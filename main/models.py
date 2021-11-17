from django.db import models


class PostItem(models.Model):
    postTitle = models.CharField(max_length=300)
    postAuthor = models.CharField(max_length=200)
    postDate = models.DateField()
    postHeader = models.CharField(max_length=400)
    postSection = models.CharField(max_length=5000)

    def __str__(self):
        return self.postTitle


class ResumeItem(models.Model):
    JobCompanyName = models.CharField(max_length=300)
    JobPositionName = models.CharField(max_length=300)
    JobStart = models.DateField()
    JobEnd = models.DateField()
    JobDescription = models.CharField(max_length=5000)
    JobDetail0 = models.CharField(max_length=5000, default="")
    JobDetail1 = models.CharField(max_length=5000, default="")
    JobDetail2 = models.CharField(max_length=5000, default="")
    JobDetail3 = models.CharField(max_length=5000, default="")
    JobDetail4 = models.CharField(max_length=5000, default="")
    JobDetail5 = models.CharField(max_length=5000, default="")
    JobDetail6 = models.CharField(max_length=5000, default="")
    JobDetail7 = models.CharField(max_length=5000, default="")
    JobDetail8 = models.CharField(max_length=5000, default="")
    JobDetail9 = models.CharField(max_length=5000, default="")


    def __str__(self):
        return self.JobPositionName+'-'+self.JobCompanyName



