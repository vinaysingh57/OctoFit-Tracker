import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

def create_test_data():
    # Users
    user1 = User.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith')
    user2 = User.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Jones')
    user3 = User.objects.create(username='carol', email='carol@example.com', first_name='Carol', last_name='Lee')

    # Teams
    team1 = Team.objects.create(name='Team Alpha', description='Alpha team', members=[user1, user2])
    team2 = Team.objects.create(name='Team Beta', description='Beta team', members=[user3])

    # Workouts
    workout1 = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy', suggested_for='Beginner')
    workout2 = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium', suggested_for='Intermediate')

    # Activities
    Activity.objects.create(user=user1, activity_type='Pushups', duration=15, calories_burned=100, date='2025-11-15')
    Activity.objects.create(user=user2, activity_type='Running', duration=30, calories_burned=250, date='2025-11-14')
    Activity.objects.create(user=user3, activity_type='Pushups', duration=10, calories_burned=70, date='2025-11-13')

    # Leaderboard
    Leaderboard.objects.create(team=team1, total_points=350)
    Leaderboard.objects.create(team=team2, total_points=70)

    print('Test data created.')

if __name__ == '__main__':
    create_test_data()
