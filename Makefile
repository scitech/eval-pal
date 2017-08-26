.PHONY: build run shell

build:
	docker-compose build

run:
	docker-compose up -d

logs:
	docker-compose logs -f

shell:
	docker exec -it evalpal_evalpal_1 /bin/bash
