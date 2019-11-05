from django.db import models

# Create your models here.
class paste(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=100, null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or str(self.id)
