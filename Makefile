# start local ELK
.PHONY: elk-local-up
elk-local-up:
	docker-compose -f ./compose/docker-compose-elk.yaml up -d

# stop local ELK
.PHONY: elk-local-down
elk-local-down:
	docker-compose -f ./compose/docker-compose-elk.yaml up -d

