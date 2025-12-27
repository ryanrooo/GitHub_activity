import os
import sys
import logging
import argparse
import requests
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

def fetch_github_activity(username: str) -> List[Dict[str, Any]]:
    """Fetch recent activity for a GitHub user."""
    url = f'https://api.github.com/users/{username}/events'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data for {username}: {e}")
        sys.exit(1)

def format_event(event: Dict[str, Any]) -> str:
    """Format a single event into a readable string."""
    try:
        event_type = event.get('type')
        repo_name = event.get('repo', {}).get('name')
        payload = event.get('payload', {})

        if event_type == 'PushEvent':
            commit_count = len(payload.get('commits', []))
            return f"- Pushed {commit_count} commits to {repo_name}"
        elif event_type == 'IssuesEvent':
            action = payload.get('action')
            return f"- {action.capitalize()} a new issue in {repo_name}"
        elif event_type == 'WatchEvent':
            if payload.get('action') == 'started':
                return f"- Starred {repo_name}"
        elif event_type == 'CreateEvent':
            ref_type = payload.get('ref_type')
            if ref_type == 'repository':
                return f"- Created repository {repo_name}"
            else:
                return f"- Created {ref_type} in {repo_name}"
        elif event_type == 'PullRequestEvent':
            action = payload.get('action')
            return f"- {action.capitalize()} pull request in {repo_name}"
        else:
            return f"- {event_type} in {repo_name}"
    except (KeyError, AttributeError):
        return None
    return None

def main():
    parser = argparse.ArgumentParser(description='Get GitHub activity')
    parser.add_argument('username', type=str, help='GitHub username')
    args = parser.parse_args()

    activity = fetch_github_activity(args.username)
    
    print("Output:")
    for event in activity:
        formatted_message = format_event(event)
        if formatted_message:
            print(formatted_message)

if __name__ == '__main__':
    main()

