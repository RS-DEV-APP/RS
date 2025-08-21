.PHONY: up down logs seed demo test

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f

seed:
	docker compose exec api python -m app.utils.seed

demo:
	docker compose exec api python -m app.utils.demo_schedule

test:
	docker compose exec api pytest -q
