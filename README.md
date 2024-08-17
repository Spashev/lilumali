### Deploy docker project
```
make install
make start
```

### Make migration files
```
alembic revision --autogenerate -m 'some comment'
```

### Run migrations
```
alembic upgrade head 
```
