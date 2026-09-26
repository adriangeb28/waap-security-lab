.PHONY: up down ml test fixtures
up:
	docker compose up -d --build

down:
	docker compose down

ml:
	python3 waap/ml/make_normal_traffic.py
	python3 waap/ml/features.py
	python3 waap/ml/train.py
	python3 waap/ml/evaluate.py

test:
	python#3 -m compileall -q app waap scripts
	python3 scripts/test_rasp.py
