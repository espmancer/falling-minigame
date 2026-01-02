all: init run

init:
		pip install -r -q requirements.txt

run:
		python3 sample/main.py
