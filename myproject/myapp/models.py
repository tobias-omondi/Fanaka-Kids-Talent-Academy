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

    
class Message (models.Model):
    parent_name = models.CharField(max_length=30 )
    message = models.TextField(null=False , blank=False)
    phone_number = models.CharField( max_length=15,
     validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')]
    )

    def __str__(self):
        return f"{self.parent_name}: {self.message}"
    

# class Game (models.Model) :
#     PLAYER_CHOICES = [
#         ('AI', 'Artificial Intelligence'),
#         ('PLAYER', 'Another Player'),
#     ]
#     student = models.ForeignKey(Student, related_name ='chess_games', on_delete=models.CASCADE)
#     opponent_type = models.CharField(max_length=10, choices=PLAYER_CHOICES)
#     opponent = models.ForeignKey (Student, null=True , blank=True , on_delete=models.SET_NULL , related_name= 'oppenents_games' )
#     result_choices = [
#         ('WIN', 'Win'),
#         ('LOSS', 'Loss'),
#         ('DRAW', 'Draw'),
#     ]
#     results = models.CharField(max_length=5, choices=result_choices)
#     date_played = models.DateTimeField(default=now) 

    
#     def __str__(self):
#         return f"Game on {self.date_played} - {self.student.username} vs {self.opponent_type}"

#     class Meta:
#         ordering = ['-date_played']  


    






