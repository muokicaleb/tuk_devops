# Define default make command
all: install test

# Command to install dependencies
install:
	pip install -r ./requirements.txt

# Command to run tests
test:
	pytest test_main.py

# Command to build and push docker image
build_push:
	docker build -t muoki/tukdevops:$(SERVICE_NAME) .
	docker push muoki/tukdevops:$(SERVICE_NAME)

