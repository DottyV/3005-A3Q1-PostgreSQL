import psycopg2
from psycopg2 import errors

# Database connection parameters
db_params = {
    'database': 'school_db',
    'user': 'postgres',
    'password': 'Quebec',
    'host': 'localhost',
    'port': 5432
}

#  Retrieves all records from the students table.
def getAllStudents():
    try:
        with psycopg2.connect(**db_params) as conn:             # Establishes a connection to the database
            with conn.cursor() as cur:                          # Opens a cursor to perform database operations
                cur.execute("SELECT * FROM students")           # Executes the SQL command
                for record in cur.fetchall():                   # Fetches all rows from the last executed statement
                    print(record)                               # Prints each record
    except Exception as e:
        print(f"An error occurred: {e}")

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                # Prepares the SQL command with placeholders for the insert operation
                cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                            (first_name, last_name, email, enrollment_date)) # Executes the insert command
                conn.commit()  # Commit changes
    except errors.UniqueViolation:
        print(f"An error occurred: A student with the email '{email}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    try:
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                # Prepares the SQL command for updating the email based on student_id
                cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                            (new_email, student_id)) # Executes the update command
                if cur.rowcount == 0:
                    print(f"No student found with ID {student_id}")
                else:
                    conn.commit()  # Commit changes
    except errors.UniqueViolation:
        print(f"An error occurred: Another student with the email '{new_email}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    try:
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,)) # Executes the delete command
                if cur.rowcount == 0:
                    print(f"No student found with ID {student_id}")
                else:
                    conn.commit()  # Commit changes
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# getAllStudents()
# addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
# addStudent('Alice', 'Johnson', 'alice.johnson@example.com', '2023-10-01')
# addStudent('Baker', 'Nooks', 'baker.nooks@example.com', '2022-11-05')
# addStudent('Jayear', 'Caldwell', 'jayear.caldwell@example.com', '2024-01-18')
# updateStudentEmail(1, 'felix.doe@newexample.com')
# updateStudentEmail(31, 'felix.doe@newexample.com')
# updateStudentEmail(33, 'kapri.bill@newexample.com')
# deleteStudent(28)
# deleteStudent(30)
# deleteStudent(33)
# deleteStudent(32)
# deleteStudent(4)
# deleteStudent(15)
getAllStudents()