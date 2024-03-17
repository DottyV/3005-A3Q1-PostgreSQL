import psycopg2

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
    with psycopg2.connect(**db_params) as conn:             # Establishes a connection to the database
        with conn.cursor() as cur:                          # Opens a cursor to perform database operations
            cur.execute("SELECT * FROM students")           # Executes the SQL command
            for record in cur.fetchall():                   # Fetches all rows from the last executed statement
                print(record)                               # Prints each record

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cur:
            # Prepares the SQL command with placeholders for the insert operation
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                        (first_name, last_name, email, enrollment_date)) # Executes the insert command

# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cur:
            # Prepares the SQL command for updating the email based on student_id
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                        (new_email, student_id)) # Executes the update command

# Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,)) # Executes the delete command

# Example usage
# getAllStudents()
# addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
# addStudent('Alice', 'Johnson', 'alice.johnson@example.com', '2023-10-01')
# addStudent('Baker', 'Nooks', 'baker.nooks@example.com', '2022-11-05')
# addStudent('Jayear', 'Caldwell', 'jayear.caldwell@example.com', '2024-01-18')
# updateStudentEmail(1, 'john.doe@newexample.com')
# updateStudentEmail(27, 'leroy.lexis@newexample.com')
# updateStudentEmail(29, 'kapri.bill@newexample.com')
deleteStudent(28)
deleteStudent(30)
deleteStudent(27)
deleteStudent(29)
# deleteStudent(4)
# deleteStudent(15)
getAllStudents()