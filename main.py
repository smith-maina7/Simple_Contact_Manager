import sqlite3

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create a table to store contacts
# Sample data for employee contacts
employee_contacts = [
    ("John Doe", 30, "johndoe@example.com", "123-456-7890"),
    ("Jane Smith", 25, "janesmith@example.com", "987-654-3210"),
    ("Alice Johnson", 35, "alicej@example.com", "555-123-4567"),
    ("Bob Brown", 40, "bobbrown@example.com", "444-987-6543"),
    ("Charlie Davis", 28, "charlied@example.com", "333-222-1111"),
    ("Emily Clark", 32, "emilyc@example.com", "222-333-4444"),
    ("Frank Harris", 45, "frankh@example.com", "111-222-3333"),
    ("Grace Lee", 29, "gracel@example.com", "666-555-4444"),
    ("Henry Wilson", 50, "henryw@example.com", "777-888-9999"),
    ("Ivy Martinez", 27, "ivym@example.com", "888-777-6666"),
    ("Jack White", 31, "jackw@example.com", "999-000-1111"),
    ("Karen Hall", 36, "karenh@example.com", "000-111-2222"),
    ("Liam Young", 33, "liamy@example.com", "123-321-4567"),
    ("Mia King", 24, "miak@example.com", "456-654-7890"),
    ("Nathan Scott", 38, "nathans@example.com", "789-987-1234"),
    ("Olivia Adams", 26, "oliviaa@example.com", "321-123-6547"),
    ("Paul Baker", 42, "paulb@example.com", "654-456-9870"),
    ("Quinn Carter", 34, "quinnc@example.com", "987-789-3210"),
    ("Rachel Evans", 29, "rachele@example.com", "111-333-5555"),
    ("Steve Turner", 37, "stevet@example.com", "222-444-6666")
]
# Create the contacts table
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS contacts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         email TEXT NOT NULL UNIQUE, 
#         phone TEXT NOT NULL UNIQUE
#     )
#  """)


# # Insert sample data into the contacts table
# cursor.executemany("""
#     INSERT INTO contacts
#     (name, age, email, phone)
#     VALUES (?, ?, ?, ?) 
#  """, employee_contacts)
# conn.commit()

# # Query the contacts table
# cursor.execute("SELECT * FROM contacts")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


# # Finding contacts containing the letters 'LI'
# cursor.execute("SELECT * FROM contacts WHERE name LIke '%li%'")
# rows =cursor.fetchall()
# for row in rows:
#     print(row)

# Updating a contacts
# getting the contact id to update
# email_to_update = "bobbrown@example.com"
# cursor.execute("SELECT id FROM contacts WHERE email = ?", (email_to_update,))
# result = cursor.fetchone()

# if result:
#     contact_id = result[0]
#     cursor.execute("""
#      UPDATE contacts
#      SET email = ?
#      WHERE id = ?              
#     """, ("bob_bob@nonatll.com", contact_id))
#     conn.commit()
#     print(f"Contact with ID {contact_id} updated successfully.")
#     cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
#     updated_contact = cursor.fetchone() 
#     if updated_contact:
#         print("Updated contact:", updated_contact)
#     else:
#         print("User not found.")
# else:
#     print("Contact not found.")

# Deleting a contact
email_of_contact_to_delete = "miak@example.com"
cursor.execute("SELECT id FROM contacts WHERE email = ?", (email_of_contact_to_delete,))
result = cursor.fetchone()

if result: 
    contact_id = result[0]
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    print(f"Contact with ID {contact_id} deleted successfully.")
else:
    print("Contact not found.")

#closing the connection
cursor.close()
conn.close()