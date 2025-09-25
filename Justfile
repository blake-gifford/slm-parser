set quiet

chat:
  docker compose run --rm app

down:
  docker compose down

build: 
  docker compose build --no-cache
