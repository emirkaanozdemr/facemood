IMAGE_NAME = facemood

all: build

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it --rm $(IMAGE_NAME)

test:
	docker run -it --rm $(IMAGE_NAME) python -m unittest discover

clean:
	docker rmi $(IMAGE_NAME)

interactive:
	docker run -it --rm $(IMAGE_NAME) /bin/bash
