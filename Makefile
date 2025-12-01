# Nombre de la app y stack
APP_NAME=irina
STACK_NAME=irina
STACK_FILE=stack.yml

# ⚠ Cambia <OWNER> por el usuario de GitHub de la chica, ej: lizirina (todo minúsculas)
IMAGE=ghcr.io/lizirina/irina-app:1.0.5

build:
	docker build -t $(APP_NAME):latest .

deploy:
	docker stack deploy --with-registry-auth -c $(STACK_FILE) $(STACK_NAME)

logs:
	docker service logs -f $(STACK_NAME)_$(APP_NAME)

rm:
	docker stack rm $(STACK_NAME)

ps:
	docker service ls

restart:
	make rm
	sleep 5
	make build
	make deploy