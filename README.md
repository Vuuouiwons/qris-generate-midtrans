# Midtrans Payment Gateway Examples

## Payment api with curl (base)

```
curl -X POST \
  https://api.midtrans.com/v2/charge \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic <YOUR SERVER KEY ENCODED in Base64>' \
  -H 'X-Override-Notification: <YOUR BACKEND URL TO RECEIVE NOTIFICATION>' \
  -d '{
  "payment_type": "qris",
  "transaction_details": {
    "order_id": "order102",
    "gross_amount": 789000
  }
}'
```