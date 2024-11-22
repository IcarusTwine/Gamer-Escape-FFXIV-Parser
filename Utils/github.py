import os
import hashlib
import requests

def list_github_files(owner, repo, path='', branch='master', token=None):
	headers = {}
	if token:
		headers['Authorization'] = f'token {token}'
	
	url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
	response = requests.get(url, headers=headers)
	
	if response.status_code == 200:
		return response.json()
	else:
		print(f"Error: {response.status_code} - {response.json().get('message')}")
		return []

def calculate_git_blob_sha(filepath):
	with open(filepath, 'rb') as f:
		content = f.read()
	blob_header = f"blob {len(content)}\0".encode('utf-8')
	blob_data = blob_header + content
	return hashlib.sha1(blob_data).hexdigest()

def download_file(url, output_path, token=None):
	headers = {}
	if token:
		headers['Authorization'] = f'token {token}'
	
	with requests.get(url, headers=headers, stream=True) as response:
		if response.status_code == 200:
			with open(output_path, 'wb') as file:
				for chunk in response.iter_content(chunk_size=8192):
					file.write(chunk)
		else:
			print(f"Failed to download {url}: {response.status_code} - {response.reason}")

def sync_github_folder(owner, repo, folder_path, local_path, branch='master', token=None):
	files = list_github_files(owner, repo, folder_path, branch, token)
	if 'type' in files:
		file_name = files['name']
		file_sha = files['sha']
		local_file_path = os.path.join("./", file_name)
		
		if os.path.exists(local_file_path):
			local_blob_sha = calculate_git_blob_sha(local_file_path)
			if local_blob_sha == file_sha:
				print(f"File '{file_name}' is up-to-date. Skipping download.")
		else:
			print(f"Downloading {file_name} to {local_file_path}")
			download_file(files['download_url'], local_file_path, token)
	else:
		os.makedirs(local_path, exist_ok=True)
		for file in files:
			if file['type'] == 'file':
				file_name = file['name']
				file_sha = file['sha']
				local_file_path = os.path.join(local_path, file_name)
				
				if os.path.exists(local_file_path):
					local_blob_sha = calculate_git_blob_sha(local_file_path)
					if local_blob_sha == file_sha:
						print(f"File '{file_name}' is up-to-date. Skipping download.")
						continue
				
				print(f"Downloading {file_name} to {local_file_path}")
				download_file(file['download_url'], local_file_path, token)
			
			elif file['type'] == 'dir':
				subfolder_path = os.path.join(folder_path, file['name'])
				subfolder_local_path = os.path.join(local_path, file['name'])
				sync_github_folder(owner, repo, subfolder_path, subfolder_local_path, branch, token)
