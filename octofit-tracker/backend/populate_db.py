import os
import sys

# Attempt to add the project's virtualenv site-packages so Django can be imported
# Virtualenv path: octofit-tracker/backend/venv
venv_base = os.path.join(os.path.dirname(__file__), 'venv')
if os.path.isdir(venv_base):
    lib_dir = os.path.join(venv_base, 'lib')
    if os.path.isdir(lib_dir):
        for entry in os.listdir(lib_dir):
            candidate = os.path.join(lib_dir, entry, 'site-packages')
            if os.path.isdir(candidate):
                sys.path.insert(0, candidate)
                break

try:
    import django  # type: ignore
except ImportError:
    print("Django is not installed in the current environment. To fix this, create and activate the project's virtualenv and install requirements:")
    print("  python3 -m venv octofit-tracker/backend/venv")
    print("  source octofit-tracker/backend/venv/bin/activate")
    print("  pip install -r octofit-tracker/backend/requirements.txt")
    raise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.core.models import User, Team, Activity, Workout, Leaderboard

def create_test_data():
    # Teams
    team1 = Team.objects.create(name='Team Alpha', description='Alpha team')
    team2 = Team.objects.create(name='Team Beta', description='Beta team')

    # Users
    user1 = User.objects.create(name='Alice Smith', email='alice@example.com', team=team1)
    user2 = User.objects.create(name='Bob Jones', email='bob@example.com', team=team1)
    user3 = User.objects.create(name='Carol Lee', email='carol@example.com', team=team2)

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
