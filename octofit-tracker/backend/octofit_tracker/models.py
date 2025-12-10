from djongo import models

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None, editable=False, null=False)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None, editable=False, null=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', null=True, blank=True)
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None, editable=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', null=True, blank=True)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None, editable=False, null=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None, editable=False, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard', null=True, blank=True)
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
