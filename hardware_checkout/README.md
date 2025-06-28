# Hardware Checkout Tracker Web App

This is a minimal Django skeleton for tracking hardware loans, inventory status and service history.

## Features

- Inventory of hardware items with barcode IDs
- Checkout and checkin hardware to staff users
- Simple admin site to manage inventory and audit logs
- Placeholder views for exporting reports as Excel or PDF

## Setup

1. Install Python 3.11 and `pip`.
2. Install dependencies using the provided requirements file:
   ```bash
   pip install -r requirements.txt
   ```
   If you are in an environment without internet access, make sure the required
   packages (e.g. `Django` and `psycopg2-binary`) are available in your Python
   installation.
3. Configure PostgreSQL credentials using environment variables:
   - `POSTGRES_DB`
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_HOST`
   - `POSTGRES_PORT`
4. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
5. Access the site at `http://localhost:8000/`.

## Note

This repository contains only the basic skeleton of the application without third-party dependencies for PDF or Excel export. You can integrate packages such as `openpyxl` for Excel and `reportlab` or `weasyprint` for PDF.
