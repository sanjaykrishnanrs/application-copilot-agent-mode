import json
import logging
import os
from django.core.management.base import BaseCommand
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout

# Configure logging
logging.basicConfig(filename='/workspaces/application-copilot-agent-mode/octofit-tracker/backend/debug_output.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        logging.debug("Starting database population...")
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        test_data_path = os.path.join(base_dir, 'test_data.json')
        logging.debug(f"Resolved test data path: {test_data_path}")

        with open(test_data_path, 'r') as file:
            data = json.load(file)

        # Populate users
        for user_data in data['users']:
            user_data['name'] = user_data.pop('username')  # Map 'username' to 'name'
            logging.debug(f"Transformed user data: {user_data}")
            User.objects.get_or_create(**user_data)

        logging.debug("Database population completed.")
