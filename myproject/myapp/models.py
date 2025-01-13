from django.db import models

class Student (models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=120)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

    pass

class Image_Gallery (models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title

    pass

class Videos_Gallery (models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True )
    Videos = models.FileField(upload_to='videos_gallery/')

    def __str__(self):
        return self.title

    pass

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
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    pass

class Ranking (models.Model):
    username = models.ForeignKey(Student, related_name='ranking', on_delete=models.CASCADE)
    game_played = models.IntegerField()
    games_won = models.IntegerField()
    games_lost = models.IntegerField()
    games_drawn = models.IntegerField()
    point_taken = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.username.username}' Ranking"
    






