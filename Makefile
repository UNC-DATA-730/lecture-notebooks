.PHONY: build-image run-lab get-url stop-notebook

NAME = $(shell basename $(PWD))_$(shell id -u)
CONTAINER_ID = $(shell docker ps -aqf "name=$(NAME)")

build-image:
	docker build -t $(shell basename $(PWD)) .

run-lab: run-lab.sh
	IMAGE=$(shell basename $(PWD)) ./$<

get-url:
	docker exec $(NAME) jupyter lab list 2>&1 | sed s/$(CONTAINER_ID)/localhost/g

stop-lab:
	docker stop $(NAME) || echo "Already stopped."
