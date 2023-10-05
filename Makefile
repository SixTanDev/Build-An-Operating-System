build:
	docker build -t my_asyncio -f ./docker/Dockerfile .

run:
	docker run -v `pwd`:/app --name my_asyncio my_asyncio

start:
	docker start my_asyncio

stop:
	docker stop my_asyncio

restart:
	docker restart my_asyncio

interact:
	docker exec -it my_asyncio /bin/bash

delete: stop
	docker rm my_asyncio; docker rmi my_asyncio

delete_cnt:
	docker rm my_asyncio

.PHONY: build run start stop restart interact delete delete_cnt
