# 1. SQL and Database Design

![Image](https://github.com/user-attachments/assets/14f48459-31fa-427f-90b3-f69c5871ca6b)

## Database Schema

**1- Entities:**
- customers
- orders
- order_tracking_events

```sql
CREATE TABLE customers (
    id             SERIAL PRIMARY KEY,
    name           VARCHAR(100) NOT NULL,
    phone_number   VARCHAR(20)  NOT NULL
);

CREATE TABLE orders (
    id              SERIAL PRIMARY KEY,
    tracking_number VARCHAR(50)  NOT NULL UNIQUE,
    customer_id     INTEGER      NOT NULL,
    status          VARCHAR(20)  NOT NULL,
    created_at      TIMESTAMP    NOT NULL DEFAULT now(),
    updated_at      TIMESTAMP    NOT NULL DEFAULT now(),

);

CREATE TABLE order_tracking_events (
    id        SERIAL PRIMARY KEY,
    order_id  INTEGER     NOT NULL,
    status    VARCHAR(20) NOT NULL,
    timestamp TIMESTAMP   NOT NULL DEFAULT now(),
    comment   TEXT,
 
);
```
