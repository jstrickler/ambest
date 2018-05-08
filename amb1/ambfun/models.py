from django.db import models

# Create your models here.

class Toast(models.Model):
    bread_type = models.CharField(max_length=32)
    butter = models.BooleanField()
    spread = models.CharField(max_length=32)

    def __str__(self):
        if self.butter:
            return 'Buttered {} with {}'.format(
                self.bread_type, self.spread
            )
        else:
            return '{} with {}'.format(
                self.bread_type, self.spread
            )
