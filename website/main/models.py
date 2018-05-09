from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django_mysql.models import JSONField, Model
from django.contrib.postgres.fields import JSONField

def default_coursePlan():
	return { "Fall 2018": [], "Spring 2019" : [] }

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
	challenge = models.PositiveSmallIntegerField(default=4)
	hrsPerWeek = models.PositiveSmallIntegerField(default=24)
	coursePlan = JSONField()#default = default_coursePlan)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


class Courses(models.Model):
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    crse = models.TextField(db_column='Crse', blank=True, null=True)  # Field name made lowercase.
    courseoverall = models.FloatField(db_column='CourseOverall', blank=True, null=True)  # Field name made lowercase.
    hoursperwkinclclass = models.TextField(db_column='HoursPerWkInclClass', blank=True, null=True)  # Field name made lowercase.
    challenge = models.FloatField(db_column='Challenge', blank=True, null=True)  # Field name made lowercase.
    howmuchlearned = models.FloatField(db_column='HowMuchLearned', blank=True, null=True)  # Field name made lowercase.
    crstitle = models.TextField(db_column='CrsTitle', blank=True, null=True)  # Field name made lowercase.
    index = models.AutoField(db_column='index', primary_key=True)

    class Meta:
        managed = False
        db_table = 'courses'



# {"Fall 2018": [list of classes], "Spring 2019": [list of classes]}