import random
import string
from jira import JIRA
import json
import os
from os.path import dirname as up


def find_config_file(file_config):
    cur_dir = up(up(os.path.abspath(__file__)))
    config_location = os.path.join(cur_dir, file_config)
    with open(config_location) as f:
        return json.load(f)
class Utiles():

    def generate_random_string(length=10):
        """Generate a random string of specified length."""
        # Define the characters to choose from
        characters = string.ascii_letters
        # Generate the random string
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def create_jira_issue(summary, description):
        # Create JIRA issue with relevant information
        private_config = find_config_file('config.json')
        token = private_config['jira_token'][6:]
        email = private_config['jira_email']
        jira_url = private_config['jira_url']
        project_token = private_config['project_token']

        auth_jira = JIRA(
            basic_auth=(email, token),
            options={'server': jira_url}
        )
        issue_dict = {
            'project': {'key': project_token},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Bug'},
        }

        # Create the issue
        auth_jira.create_issue(fields=issue_dict)
