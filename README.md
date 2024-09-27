# Automated Seating Arrangement in Examination Hall

This project automates the seating arrangement process in examination halls. It provides an efficient solution for managing seating arrangements in educational institutions, reducing administrative workload, and ensuring fairness in seat allocation.

## Features
- **Automated Seat Allocation**: Uses the Graph Coloring Algorithm to ensure no adjacent seating of students with similar registration numbers.
- **CSV Data Handling**: Allows uploading student details via CSV files for processing.
- **Export to Excel**: Generates seating arrangements and exports them as Excel files for easy distribution.
- **User-Friendly Interface**: Simple and intuitive interface for managing seating arrangements.

## Table of Contents
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Backend Overview](#backend-overview)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

## Technology Stack
- **Programming Language**: Python 3.7
- **Framework**: Django (Backend framework)
- **Database**: SQLite (For lightweight data storage)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)

## Installation

### Prerequisites
- Python 3.7 or higher
- Pip (Python package manager)

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/vishnuprakash-777/seatex.git
    cd seatex
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Run database migrations:
    ```bash
    python manage.py migrate
    ```

4. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

5. Open the application in your browser at `http://127.0.0.1:8000/`.

## Usage

1. **Upload Student Data**: Use the provided form to upload a CSV file containing student information.
2. **View Seating Arrangement**: The backend will process the uploaded data and generate a seating plan.
3. **Export Seating Plan**: Download the seating arrangement in Excel format for further distribution.

## Backend Overview

- **CSV Handling**: Upload CSV files with student details (name, registration number, etc.) for processing.
- **Seating Allocation Algorithm**: Implemented using Python, the Graph Coloring Algorithm ensures no students with the same registration prefix are seated next to each other.
- **Database**: Data is stored in an SQLite database using Django's ORM.
- **API Endpoints**: Django provides RESTful APIs for data submission (CSV upload) and retrieval (seating arrangement results).

## Testing

To run tests:
```bash
python manage.py test
