from django.db import models

# Create your models here.
class Register(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    GOAL_CHOICES = [
        ('lose_weight', 'Lose Weight'),
        ('gain_muscle', 'Gain Muscle'),
        ('maintain', 'Maintain Weight'),
        ('improve_endurance', 'Improve Endurance'),
        ('general_fitness', 'General Fitness'),
    ]

    name         = models.CharField(max_length=100)
    password=      models.CharField(max_length=15)
    gender       = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email        = models.EmailField(blank=True, null=True)
    phone        = models.CharField(max_length=15, blank=True, null=True)
    age          = models.IntegerField()
    height       = models.FloatField()          # cm
    weight       = models.FloatField()          # kg
    fitness_goal = models.CharField(max_length=30, choices=GOAL_CHOICES)
    created_at   = models.DateTimeField(auto_now_add=True)

class FitnessVideo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='fitness/%Y/%m/')
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
# models.py
from django.db import models
from django.conf import settings

class FitnessRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    distance_km = models.FloatField(default=0.0)
    steps = models.PositiveIntegerField(default=0)
    calories = models.PositiveIntegerField(default=0)
    recorded_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f"{self.user or 'Anon'} - {self.steps} steps"