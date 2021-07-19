from django.db import models


class Show(models.Model):
    show_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.CharField(max_length=255)
    popularity = models.CharField(max_length=255)
    votes = models.IntegerField()
    release_year = models.DateField()

    def __str__(self):
        return self.name


class ShowDetail(models.Model):
    show_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.CharField(max_length=255)
    popularity = models.CharField(max_length=255)
    release_year = models.DateField()
    release_date_first_epi = models.DateField()
    total_epi = models.IntegerField()
    gender = models.TextField()
    # gender = models.ManyToManyField('Gender')

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=255)


class Reviews(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    avatar_path = models.CharField(max_length=255)
