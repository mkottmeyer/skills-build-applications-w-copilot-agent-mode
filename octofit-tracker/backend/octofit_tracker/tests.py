from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T')
        u = User.objects.create(name='U', email='u@example.com', team=team)
        self.assertEqual(str(u), 'U')
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='desc', suggested_for='U')
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='L')
        l = Leaderboard.objects.create(team=team, points=10)
        self.assertEqual(l.points, 10)
    def test_activity_create(self):
        team = Team.objects.create(name='A')
        u = User.objects.create(name='A', email='a@example.com', team=team)
        a = Activity.objects.create(user=u, type='run', duration=10, calories=100, date='2025-12-10')
        self.assertEqual(a.type, 'run')
