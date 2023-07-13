# https://stackoverflow.com/questions/59097339/package-and-clone-a-python-venv
import os
import json
venv_dir = "/venv"
cwd = os.getcwd()
cwd = cwd.replace("\\","/")
cwd += venv_dir
dir_path = {
    "path": cwd
}
with open('path.json', 'w', encoding='utf-8') as f:
    json.dump(dir_path, f, ensure_ascii=False, indent=4)


