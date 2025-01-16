import mysql.connector
import bcrypt

# Function to hash the password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

# Function to register a new user
def register_user(username, password):
    # Hash the password
    password_hash = hash_password(password)

    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost:3306",
        user="root",
        password="123456789",
        database="cred"
    )

    cursor = conn.cursor()

    # Insert the new user into the database
    try:
        insert_query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, password_hash))
        conn.commit()
        print("User registered successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    register_user(username, password)
