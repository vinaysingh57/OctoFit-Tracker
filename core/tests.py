from django.test import TestCase
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
	def test_create_user(self):
		user = User.objects.create(username='testuser', email='test@example.com')
		self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
	def test_create_team(self):
		team = Team.objects.create(name='Test Team')
		self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
	def test_create_activity(self):
		user = User.objects.create(username='testuser2', email='test2@example.com')
		activity = Activity.objects.create(user=user, activity_type='run', duration=30, calories_burned=200, date='2025-11-16')
		self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
	def test_create_workout(self):
		workout = Workout.objects.create(name='Pushups', difficulty='Easy', suggested_for='Beginner')
		self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
	def test_create_leaderboard(self):
		team = Team.objects.create(name='Leaderboard Team')
		leaderboard = Leaderboard.objects.create(team=team, total_points=100)
		self.assertEqual(leaderboard.total_points, 100)
