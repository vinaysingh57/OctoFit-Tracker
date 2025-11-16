import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.core.models import User, Team, Activity, Workout, Leaderboard

def create_test_data():
    # Users
    user1 = User.objects.create(name='Alice Smith', email='alice@example.com', team=team1)
    user2 = User.objects.create(name='Bob Jones', email='bob@example.com', team=team1)
    user3 = User.objects.create(name='Carol Lee', email='carol@example.com', team=team2)

    # Teams
    team1 = Team.objects.create(name='Team Alpha', description='Alpha team')
    team2 = Team.objects.create(name='Team Beta', description='Beta team')

    # Workouts
    workout1 = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
    workout2 = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')

    # Activities
    Activity.objects.create(user=user1, type='Pushups', duration=15, calories=100, date='2025-11-15')
    Activity.objects.create(user=user2, type='Running', duration=30, calories=250, date='2025-11-14')
    Activity.objects.create(user=user3, type='Pushups', duration=10, calories=70, date='2025-11-13')

    # Leaderboard
    Leaderboard.objects.create(team=team1, points=350, rank=1)
    Leaderboard.objects.create(team=team2, points=70, rank=2)

    print('Test data created.')

if __name__ == '__main__':
    create_test_data()
