# Import necessary libraries
import sqlite3  # For SQLite database operations
import streamlit as st  # For creating the web application interface
from PIL import Image  # For image handling
import io  # For working with binary streams (used for image handling)

# Database setup function
def init_db():
    # Connect to SQLite database (creates 'data.db' if it doesn't exist)
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # Create a table named 'items' if it doesn't exist already
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique ID for each item
            name TEXT NOT NULL,                   -- Name of the item (required)
            description TEXT,                     -- Description of the item
            image BLOB                            -- Binary data for storing images
        )
    ''')
    conn.commit()  # Save the changes
    conn.close()  # Close the connection to the database

# Function to add a new item to the database
def add_item(name, description, image_file):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # If an image is uploaded, read its binary data; otherwise, set it to None
    image_data = image_file.read() if image_file else None
    # Insert the item details into the 'items' table
    cursor.execute('''
        INSERT INTO items (name, description, image) VALUES (?, ?, ?)
    ''', (name, description, image_data))
    conn.commit()  # Save the changes
    conn.close()  # Close the connection

# Function to fetch all items from the database (without images for efficiency)
def get_items():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # Select the ID, name, and description of all items
    cursor.execute("SELECT id, name, description FROM items")
    rows = cursor.fetchall()  # Fetch all rows from the query
    conn.close()
    return rows

# Function to fetch details of a single item by ID (including the image)
def get_item_by_id(item_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # Select the details of a specific item
    cursor.execute("SELECT id, name, description, image FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()  # Fetch the row corresponding to the item ID
    conn.close()
    return row

# Function to update an existing item in the database
def update_item(item_id, name, description, image_file=None):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # If a new image is provided, update it along with name and description
    if image_file:
        image_data = image_file.read()
        cursor.execute('''
            UPDATE items
            SET name = ?, description = ?, image = ?
            WHERE id = ?
        ''', (name, description, image_data, item_id))
    else:
        # Update only name and description if no new image is provided
        cursor.execute('''
            UPDATE items
            SET name = ?, description = ?
            WHERE id = ?
        ''', (name, description, item_id))
    conn.commit()  # Save the changes
    conn.close()

# Function to delete an item from the database by ID
def delete_item(item_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # Delete the item with the specified ID
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()  # Save the changes
    conn.close()

# Streamlit app interface starts here
st.title("CRUD Application with SQLite and Images")  # App title

init_db()  # Initialize the database (create table if not exists)

# Sidebar menu options for navigation
menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)  # User selects an action from the sidebar

# If the user selects 'Create' from the menu
if choice == "Create":
    st.subheader("Add New Item")  # Subheading for the Create section
    name = st.text_input("Name")  # Input field for the item's name
    description = st.text_area("Description")  # Input field for the item's description
    # File uploader for images (optional)
    image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if st.button("Add Item"):  # Button to trigger adding the item
        add_item(name, description, image_file)  # Add the item to the database
        st.success("Item added successfully!")  # Confirmation message

# If the user selects 'Read' from the menu
elif choice == "Read":
    st.subheader("View Items")  # Subheading for the Read section
    items = get_items()  # Fetch all items from the database
    for item in items:
        # Display each item's ID, name, and description
        st.write(f"ID: {item[0]}")
        st.write(f"Name: {item[1]}")
        st.write(f"Description: {item[2]}")
        # Button to view details of a specific item
        if st.button(f"View Details {item[0]}"):
            item_detail = get_item_by_id(item[0])  # Fetch item details
            if item_detail[3]:  # If an image is available, display it
                image = Image.open(io.BytesIO(item_detail[3]))
                st.image(image, caption=item_detail[1])
            # Display the name and description
            st.write(f"Name: {item_detail[1]}")
            st.write(f"Description: {item_detail[2]}")

# If the user selects 'Update' from the menu
elif choice == "Update":
    st.subheader("Update Item")  # Subheading for the Update section
    items = get_items()  # Fetch all items
    # Dropdown to select an item to update
    item_id = st.selectbox("Select Item to Update", [item[0] for item in items])
    if item_id:
        item_detail = get_item_by_id(item_id)  # Fetch item details
        # Pre-filled input fields for updating name and description
        new_name = st.text_input("Name", item_detail[1])
        new_description = st.text_area("Description", item_detail[2])
        # Optional file uploader for a new image
        new_image_file = st.file_uploader("Upload New Image (optional)", type=["png", "jpg", "jpeg"])
        if st.button("Update Item"):  # Button to trigger the update
            update_item(item_id, new_name, new_description, new_image_file)
            st.success("Item updated successfully!")  # Confirmation message

# If the user selects 'Delete' from the menu
elif choice == "Delete":
    st.subheader("Delete Item")  # Subheading for the Delete section
    items = get_items()  # Fetch all items
    # Dropdown to select an item to delete
    item_id = st.selectbox("Select Item to Delete", [item[0] for item in items])
    if st.button("Delete Item"):  # Button to confirm deletion
        delete_item(item_id)  # Delete the selected item
        st.success("Item deleted successfully!")  # Confirmation message
