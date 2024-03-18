# Student Database Application

This application connects to a PostgreSQL database to perform CRUD operations on a `students` table.

## Requirements

- Python 3.x
- PostgreSQL server running locally
- psycopg2 library (Python)

## Database Setup with pgAdmin 4

Before running the application, you need to set up the `students` table in your PostgreSQL database. Here's how to do it with pgAdmin 4:

1. **Create the Database:**
   - Open pgAdmin 4 and connect to your PostgreSQL server.
   - Right-click on 'Databases', then select 'Create' and click 'Database'.
   - Enter a name for your database, i used `school_db`, and click 'Save'.

2. **Create the Table:**
   - With your new database selected in pgAdmin, open the 'Query Tool' from the toolbar.
   - Locate the SQL file in the `database/` directory of the cloned repository.
   - Open the SQL file in the Query Tool or copy and paste the SQL script directly into the Query Tool window.
   - Run the script to create the `students` table and insert the initial records.

After these steps, the database and table are ready to be used by the Python application.

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
