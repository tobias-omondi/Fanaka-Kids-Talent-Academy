from django.db import models
# from django.utils.timezone import now
# from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password

class Student (models.Model):
    # fullname = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, null=True, blank=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    registration_date = models.DateField(auto_now_add=True)

    def save(self , *args, **kwargs):
        if not self.pk: #hashing on creation
            self.password = make_password (self.password)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Image_Gallery(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title or self.image.name or "Untitled Image"


class Videos_Gallery(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='videos_gallery/')  # Renamed for clarity

    def __str__(self):
        return self.title or self.video.name or "Untitled Video"



class Blog (models.Model):
    image = models.FileField(upload_to='blog/', null=True, blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField(null=False, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    pass

class Events (models.Model):
    image = models.ImageField(upload_to='events_image/')
    title = models.CharField(max_length=30)
    description = models.TextField()
    event_date = models.TextField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    pass

class Ranking(models.Model):
    username = models.ForeignKey(Student, related_name='rankings', on_delete=models.CASCADE)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
    games_lost = models.IntegerField(default=0)
    games_drawn = models.IntegerField(default=0)
    points_taken = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username.username}'s Ranking"

    @property
    def win_ratio(self):
        total_games = self.games_won + self.games_lost + self.games_drawn
        return self.games_won / total_games if total_games > 0 else 0

    @property
    def total_points(self):
        return self.games_won * 3 + self.games_drawn  # 3 points for a win and 1 for a draw

    
class Message (models.Model):
    parent_name = models.CharField(max_length=30 )
    email = models.EmailField(max_length=200 , null= True , blank= True)
    message = models.TextField(null=False , blank=False)

    def __str__(self):
        return f"{self.parent_name}: {self.message}"
    

    






