.PHONY: install test pipeline query report clean

install:
	pip install -r requirements.txt

test:
	pytest

pipeline:
	py src/pipeline.py

query:
	py src/query.py

report:
	py src/report.py

clean:
	Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
	Remove-Item -Recurse -Force src\__pycache__ -ErrorAction SilentlyContinue
	Remove-Item -Recurse -Force test\__pycache__ -ErrorAction SilentlyContinue