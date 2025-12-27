# GitHub Activity Fetcher

A simple command-line interface (CLI) tool to fetch and display recent activity for a GitHub user.

## Features

- Fetches recent public events for a specified GitHub user.
- Displays activity in a human-readable format.
- Supports various event types:
  - Push commits
  - Issue creation and comments
  - Starred repositories
  - Repository and branch creation
  - Pull requests

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ryanrooo/GitHub_activity.git
   cd GitHub_activity
   ```

2. (Optional) Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script by providing a GitHub username as an argument:

```sh
python main.py <username>
```

### Example

```sh
python main.py kamranahmedse
```

**Output:**
```
Output:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
```

## Project Structure

- `main.py`: The main script handling API requests and formatting.
- `requirements.txt`: List of Python dependencies.
