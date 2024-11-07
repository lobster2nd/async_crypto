up:
	docker compose up -d

down:
	docker compose down && docker network prune --force

restart: down up


logs:
	docker compose logs -f
