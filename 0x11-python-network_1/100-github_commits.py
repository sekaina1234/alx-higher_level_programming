#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./100-github_commits.py <repository name> <owner name>")
    sys.exit(1)

repo_name = sys.argv[1]
owner_name = sys.argv[2]

# URL for the GitHub API to fetch commits
url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

try:
    # Make a GET request to fetch the commits
    response = requests.get(url)
    response.raise_for_status()

    # Parse the response JSON to get commit information
    commits = response.json()

    # Display the 10 most recent commits
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid JSON response")
