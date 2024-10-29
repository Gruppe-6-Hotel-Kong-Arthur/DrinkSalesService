# DrinkSalesService


```bash
docker build -t drinks_sales_service . && docker image prune -f
```

```bash
docker run -d \        
  -p 5006:5006 \
  --name drinks_sales_service \
  --network microservice-network \
  drinks_sales_service
```
docker run -d -p 5006:5006 --name drinks_sales_service --network microservice-network drinks_sales_service

