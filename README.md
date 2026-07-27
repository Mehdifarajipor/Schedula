# Schedula
### 1-About:
> Schedula is a backend service booking platform built with Django and Django Rest Framework.
> It enables customers to discover service providers, manage bookings and interact through a secure RESTful API.
___
### 2-Project Status: 
Under Development
___
### 3-Features:
#### Authentication
- User registration
- JWT authentication
- Login & Logout
- Token refresh
- User profile management
#### Provider Management
- Provider profile
- Public provider page
#### Service Management (In Progress)
- Create services
- Update services
- Delete services
#### Booking (Planned)
- Book a service
- Cancel booking
- Booking history
#### Reviews (Planned)
- Provider reviews
- Ratings
___
### 4-Tech Stack:
- Python
- Django
- Django Rest Framework
- PostgreSQL
- JWT Authentication
- Docker
- drf-spectacular
- React
___
### 5-Project Structure:
```
schedula/
|__ accounts/
|__ providers/
|__ services/
|__ bookings/
|__ reviews/
|__ config/
|__ manage.py
```
___
### 6-Installation
#### Clone the repository
```
git clone <repository-url>
cd schedula
```
#### Create virtual environment
```
python -m venv venv
```
#### Activate virtual environment
Linux/macOS
``` 
source .venv/bin/activate
```
Windows
``` 
.venv/Scripts/activate
```
#### Install dependencies
``` 
pip install -r requirements.txt
```
#### Apply migrations
``` 
python manage.py migrate
```
#### Run the server
``` 
python manage.py runserver
```
___
### 7- Environment variables
Create a ```.env``` file and configure your environment variables
___
### 8- API Documentation
OpenAPI Schema
``` 
/api/schema/
```
Swagger UI
``` 
/api/schema/swagger-ui/
```
ReDoc
``` 
/api/schema/redoc/
```
___
### 9- Roadmap
1. Authentication
2. Provider Profile
3. Service Management
4. Booking System
5. Payments
6. Reviews
7. Notifications
8. Docker Deployment
9. CI/CD
10. Automated Test
___
### 10-License
>This project is developed for learning and portfolio purposes

