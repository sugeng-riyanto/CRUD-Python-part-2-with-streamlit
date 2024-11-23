import sqlite3
import streamlit as st
from PIL import Image
import io

# Database setup
def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            image BLOB
        )
    ''')
    conn.commit()
    conn.close()

def add_item(name, description, image_file):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    if image_file:
        image_data = image_file.read()
    else:
        image_data = None
    cursor.execute('''
        INSERT INTO items (name, description, image) VALUES (?, ?, ?)
    ''', (name, description, image_data))
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description FROM items")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_item_by_id(item_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description, image FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_item(item_id, name, description, image_file=None):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    if image_file:
        image_data = image_file.read()
        cursor.execute('''
            UPDATE items
            SET name = ?, description = ?, image = ?
            WHERE id = ?
        ''', (name, description, image_data, item_id))
    else:
        cursor.execute('''
            UPDATE items
            SET name = ?, description = ?
            WHERE id = ?
        ''', (name, description, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

# Streamlit app
st.title("CRUD Application with SQLite and Images")

init_db()

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Add New Item")
    name = st.text_input("Name")
    description = st.text_area("Description")
    image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if st.button("Add Item"):
        add_item(name, description, image_file)
        st.success("Item added successfully!")

elif choice == "Read":
    st.subheader("View Items")
    items = get_items()
    for item in items:
        st.write(f"ID: {item[0]}")
        st.write(f"Name: {item[1]}")
        st.write(f"Description: {item[2]}")
        if st.button(f"View Details {item[0]}"):
            item_detail = get_item_by_id(item[0])
            if item_detail[3]:
                image = Image.open(io.BytesIO(item_detail[3]))
                st.image(image, caption=item_detail[1])
            st.write(f"Name: {item_detail[1]}")
            st.write(f"Description: {item_detail[2]}")

elif choice == "Update":
    st.subheader("Update Item")
    items = get_items()
    item_id = st.selectbox("Select Item to Update", [item[0] for item in items])
    if item_id:
        item_detail = get_item_by_id(item_id)
        new_name = st.text_input("Name", item_detail[1])
        new_description = st.text_area("Description", item_detail[2])
        new_image_file = st.file_uploader("Upload New Image (optional)", type=["png", "jpg", "jpeg"])
        if st.button("Update Item"):
            update_item(item_id, new_name, new_description, new_image_file)
            st.success("Item updated successfully!")

elif choice == "Delete":
    st.subheader("Delete Item")
    items = get_items()
    item_id = st.selectbox("Select Item to Delete", [item[0] for item in items])
    if st.button("Delete Item"):
        delete_item(item_id)
        st.success("Item deleted successfully!")
