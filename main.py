from Utils.github import sync_github_folder

# Example usage:
owner = "xivapi"
repo = "ffxiv-datamining"
folder_path = "csv"
local_path = "./csv"
branch = "master"
token = None  # Add your personal access token if needed for private repositories

sync_github_folder(owner, repo, folder_path, local_path, branch, token)