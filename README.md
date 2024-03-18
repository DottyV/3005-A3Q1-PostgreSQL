# Student Database Application

This application connects to a PostgreSQL database to perform CRUD operations on a `students` table.

## Requirements

- Python 3.x
- PostgreSQL server running locally
- psycopg2 library (Python)

## Setup

1. Install psycopg2 library using pip:
"pip install psycopg2-binary"

2. Update the `db_params` configuration in `start.py` with your database connection details.

3. Ensure your PostgreSQL server is running and accessible.

### Clone the Repository

Clone this repo using the following command/link:

git clone https://github.com/DottyV/3005-A3Q1-PostgreSQL


## Running the Application

To run the application, navigate to the directory containing `start.py` and execute:

"start.py"
This will run the example operations defined at the end of the script. Comment out or remove these before running in a production environment.

## Functions

- `getAllStudents()`: Prints all student records to the console.
- `addStudent(first_name, last_name, email, enrollment_date)`: Adds a new student record.
- `updateStudentEmail(student_id, new_email)`: Updates the email for a given student ID.
- `deleteStudent(student_id)`: Deletes a student record based on student ID.

Replace the placeholders in the function calls with actual values to perform the operations on the database.

## Video Demo

- `Link 1 (First vid 9 min):` https://youtu.be/Ljv4P5VrkOQ
- `Link 2 (Second vid 5 min):` https://youtu.be/2-qtAiJrVKY
