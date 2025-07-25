# identify (Requirements , features) & design the database

## Requirements

### 1. Models to Implement
- **Customer**
  - `id` (auto)
  - `name`
  - `phone_number`
- **Order**
  - `id` (auto)
  - `tracking_number` (unique)
  - `customer` (FK → Customer)
  - `status` (CREATED → PICKED → DELIVERED)
  - `created_at`, `updated_at`
- **OrderTrackingEvent** *(bonus)*
  - `order` (FK → Order)
  - `status`
  - `timestamp`
  - `comment`

### 2. Features
- **Order Creation**  
  - Validate unique `tracking_number`
  - Automatically assign `customer` from the authenticated user
- **Order Listing**  
  - List all orders
  - Filter by `status`
  - Search by `customer` name or `tracking_number`
- **Order Detail**  
  - Retrieve a single order, including its tracking events
- **Order Update**  
  - Only allow valid status transitions:  
    `CREATED → PICKED → DELIVERED`
- **Order Delete**  
  - Soft‑delete an order (keep history)

- **OrderTrackingEvent**  
  - Record each status change with timestamp & comment  
- **Pagination** on the orders list endpoint  
- **Role‑based Permissions** (`admin` vs `customer`)  
- **JWT‑based Auth** (Register / Login / Logout)  
- **Automated Tests** for models, serializers, views  
- **OpenAPI/Swagger** docs
  
## SQL and Database Design

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
