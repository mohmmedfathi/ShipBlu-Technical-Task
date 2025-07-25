# ShipBlu Technical Task


<div>

<h3 align="center"> Customer & Orders API

  <p align="center">
      
</div>


## Table of Contents

- [Overview](#overview)
- [Built With](#built-with)
- [Installation](#installation)
- [Solution Steps](#solution-steps)
  - [Section 1: General Coding & Problem Solving](#section-1-general-coding--problem-solving)
  - [Section 2: API Design & Implementation](#section-2-api-design--implementation)
- [Documentation](#documentation)
- [Assumptions and Design Decisions](#assumptions-and-design-decisions)
- [TODO](#todo)


## Overview

A Django REST Framework-based API for managing customer accounts, creating and tracking orders, handling order status transitions, and enforcing business rules. It includes robust user authentication and provides clean, consistent API responses.


## Built With

* ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
* ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
* ![Django REST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)


## Installation

- Python ≤ 3.10.6  
- Pip ≤ 22.0.2  
- Python virtual environment

```bash
# 1. Clone the repo
git clone git@github.com:your-username/ShipBlu-Technical-Task.git
cd ShipBlu-Technical-Task

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install requirements
pip install -r requirements.txt

# 5. Migrate models
python manage.py migrate

# 6. Run development server
python manage.py runserver
```

## Solution steps

1. [Section 1: General Coding & Problem Solving](docs/project_starter.md)
   - identify the requirement
   - set the features
   - Design a database schema 
   - write sql for database


3. [Section 2: API Design & Implementation](docs/api.md)
   - JWT-based Auth (Register, Login, Logout)
   - Order CRUD with soft delete
   - Automatic status tracking via OrderTrackingEvent
   - Filter/search by customer, status, tracking number
     
## Documentation

https://documenter.getpostman.com/view/22971205/2sB34oDHyi

## Assumptions-and-Design-Decisions
**Project Structure**: Organized as a multi-app Django project (users, orders, core) to maintain separation of concerns and scalability.

**Custom User Model**:
Implemented a custom user model to support future flexibility (roles, phone login). 

**Soft Delete Implementation**: Used deleted_at timestamp instead of hard deletion to preserve data integrity and allow for recovery.

**Order Status Transitions**: Enforced logical order status transitions (CREATED → PICKED → DELIVERED) through validation to maintain business rules.

**JWT Authentication**: Used Simple JWT for stateless token-based authentication, supporting login, logout, and secure endpoint access.

**Order Tracking Events**: Added OrderTrackingEvent model to record order status changes with timestamps and comments for tracking history.
**Filtering and Pagination**: Added filtering by status and customer, and search by tracking_number and pagination .


## TODO
- **APIs Rate Limiting**

[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://docs.djangoproject.com/en/3.2/
[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://docs.python.org/3/
