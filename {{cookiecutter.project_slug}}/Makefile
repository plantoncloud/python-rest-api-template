.PHONY: build
build:
	pip3 install -r requirements.txt

.PHONY: build-image
build-image:
	docker build --platform linux/amd64 -t python-todo-api .

.PHONY: run
run:
	python3 app.py
