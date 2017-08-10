from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class NewsAndUpdate(models.Model):
    POSTER_CHOICES = (
        ('Glenn Paul Gara', 'Glenn Paul Gara'),
        ('Isaiah Evans Villa Abrille', 'Isaiah Evans Villa Abrille'),
        ('Seth Jasper Napalit', 'Seth Jasper Napalit'),
        ('Neil Ivan Palacios', 'Neil Ivan Palacios'),
        ('Christine Joy Busalanan', 'Christine Joy Busalanan'),
        ('Jesmar James Rama', 'Jesmar James Rama'),
        ('Reno Marco Fandiño', 'Reno Marco Fandiño'),
        ('Quinn Ray Anthony Intrepido', 'Quinn Ray Anthony Intrepido'),
        ('Mark Kenneth Jimenez', 'Mark Kenneth Jimenez'),
        ('Arch Renzo Falconi', 'Arch Renzo Falconi'),
        ('Elven Earl Tsuruoka', 'Elven Earl Tsuruoka'),
        ('Nikko Tulang', 'Nikko Tulang'),
        ('Villa Abrille and Co.', 'TANOM Group'),
        ('Napalit and Co.', 'HALANG Group'),
        ('Palacios and Co.', 'Explore Davao Group'),
    )

    CATEGORY_CHOICES = (
        ('News', 'News'),
        ('Update', 'Update'),
        ('Event', 'Event'),
        ('Article', 'Article'),
        ('Project', 'Project'),
    )

    NU_Poster = models.CharField(max_length=100, choices=POSTER_CHOICES, default='Glenn Paul Gara')
    NU_Category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='News')
    NU_Title = models.CharField(max_length=250)
    NU_Content = RichTextField()
    NU_Logo = models.FileField()
    NU_Posted = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.NU_Title + ' - ' + self.NU_Content

class Message(models.Model):
    M_Name = models.CharField(max_length=1000)
    M_Email = models.CharField(max_length=1000)
    M_Message = models.TextField()

    def __str__(self):
        return self.M_Name + ' - ' + self.M_Email