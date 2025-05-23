from django.db import models


class Book(models.Model):
    RANK_CHOICES = [(i, str(i)) for i in range(1, 11)] 

    title = models.CharField(max_length=20)
    description = models.TextField()
    customer_review_rank = models.IntegerField(choices=RANK_CHOICES)
    author = models.CharField(max_length=15)
    author_profile_img = models.ImageField(upload_to="author_profiles/", blank=True)
    author_info = models.TextField()
    author_works = models.CharField(max_length=50)
    cover_image = models.ImageField(blank=True)
    audio_file = models.FileField(upload_to="tts/", blank=True, null=True)
