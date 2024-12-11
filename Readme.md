1. Clone the repository.
2. Install dependencies.

`pip install -r requirements.txt`

3. Run migrations.

`python manage.py makemigrations`
`python manage.py migrate`

4. Start the server.

`python manage.py runserver`

5. Create a user.

`pyton manage.py createsuperuser`

6. Log in with admin panel.

7. Use basic auth with your username and password to auth the user during requests. Recommend to test with postman.

API Endpoints
1. Create Expense:

**POST** `/api/expenses/`

Request body:

`{
    "title": "Lunch",
    "amount": 10.50,
    "date": "2024-12-01",
    "category": "Food",
}`

2. Update expense:
   
**PUT** or **PATCH**  `/api/expenses/{id}/`

Request body:

**PATCH**
`{"amount": 11.50}`

**PUT**
`{
    "title": "Updated Title",
    "amount": 20.00,
    "date": "2024-12-02",
    "category": "Travel"
}`

3. Delete expense:
   
**DELETE**  `/api/expenses/{id}/`

4. List Expenses by Date Range:

**GET**` /api/expenses-by-date/?start_date=2024-01-01&end_date=2024-12-31`

5. Category Summary:

**GET** `/api/category-summary/?month=2024-12`

