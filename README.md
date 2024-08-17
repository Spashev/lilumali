## Start application
``python3 main.py``

## FastAPI
http://localhost:8000/swagger <br>
<h4>Нужно создать company и budget</h4>

### Company
```bash
curl -X 'POST' \
  'http://localhost:8000/company/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "bookit"
}'
```

### Budget
```bash
curl -X 'POST' \
  'http://localhost:8000/budget/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "month": "Mart",
  "income": 1200,
  "consumption": 100,
  "profit": 1000,
  "kpn": 311,
  "company_id": 1
}'
```

``src/app/core/config.py:4`` Нужно указать ``TELEGRAM_BOT_TOKEN`` <br>
Токен можно получить у https://t.me/BotFather

