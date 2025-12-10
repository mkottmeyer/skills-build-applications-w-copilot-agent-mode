from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections using Djongo's raw connection
        from django.db import connection
        db = connection.cursor().db_conn.client[connection.settings_dict['NAME']]
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.workouts.drop()
        db.leaderboard.drop()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Workouts
        workouts = [
            Workout(name='Web Swinging', description='Swing through the city.', suggested_for='Spider-Man'),
            Workout(name='Armor Training', description='Train in the Iron Man suit.', suggested_for='Iron Man'),
            Workout(name='Amazon Strength', description='Strength training for Wonder Woman.', suggested_for='Wonder Woman'),
            Workout(name='Stealth Moves', description='Stealth and agility for Batman.', suggested_for='Batman'),
        ]
        for workout in workouts:
            workout.save()

        # Activities
        Activity.objects.create(user=users[0], type='Swinging', duration=60, calories=500, date=timezone.now())
        Activity.objects.create(user=users[1], type='Flying', duration=45, calories=400, date=timezone.now())
        Activity.objects.create(user=users[2], type='Strength', duration=30, calories=350, date=timezone.now())
        Activity.objects.create(user=users[3], type='Stealth', duration=50, calories=300, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=900)
        Leaderboard.objects.create(team=dc, points=650)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with superhero test data.'))
