import requests

def fetch_files(token, repo, path):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/repos/{repo}/contents/{path}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        files = response.json()
        for file in files:
            file_name = file["name"]
            download_url = file["download_url"]
            response = requests.get(download_url, headers=headers)
            if response.status_code == 200:
                with open(file_name, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {file_name}")
            else:
                print(f"Failed to download: {file_name}")
    else:
        print(f"Failed to fetch files. Status Code: {response.status_code}")

def download_deps():
    try:
        subprocess.run(["pip3", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading dependencies: {e}")

        

def init_files(entry):
    with open('invoker_template', 'r') as fr:
        code = fr.read()
        with open('invoker.py', 'w') as fw:
            fw.write(code.format(name=entry))
    print('Initialised all files successfully')
    