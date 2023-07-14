Set-ExecutionPolicy Unrestricted -Scope Process -Force
py -m venv venv
py .\set_dir.py
venv\scripts\activate
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
exit
