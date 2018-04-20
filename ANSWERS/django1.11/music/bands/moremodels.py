from django.db import models
# these are the enhanced models that DO have the
# extra code from chapter 9

class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=32)
    genre = models.ForeignKey(Genre)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.name

    def get_genre(self):
        return self.genre.name.upper()

    class Meta():
        ordering = [Band.genre]
