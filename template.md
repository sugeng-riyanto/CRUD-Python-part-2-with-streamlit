# Lesson Process with Students

## Introduction to the Database
- **SQLite** is used as the database to store items and their associated information.
- A table named `items` is created, containing:
  - A unique ID for each item.
  - Name and description fields for textual data.
  - An image field to store image data as binary (BLOB).

## Creating the Database
- The database and table are initialized using the `init_db` function, which ensures the database structure is ready for CRUD operations.

## Adding Data
- Students learn to add records (name, description, and an optional image) into the database using the `add_item` function.
- Images are uploaded and converted into binary format before being stored in the database.

## Reading Data
- Students explore how to fetch and display records from the database using the `get_items` and `get_item_by_id` functions.
- For efficiency, the `get_items` function retrieves a list of items without loading their images.
- Images are displayed when detailed information for an item is requested.

## Updating Data
- The `update_item` function allows students to modify existing records.
- Students learn how to handle optional image updates (e.g., retaining the old image if a new one isn't uploaded).

## Deleting Data
- The `delete_item` function demonstrates how to remove records from the database by specifying their unique ID.

## Streamlit for UI
- Students interact with a user-friendly interface created using **Streamlit**.
- The interface has a sidebar with options (Create, Read, Update, Delete) to perform respective operations.
- Input fields and buttons are used to gather data and trigger database actions.

## Working with Images
- Students learn about image processing with Python's **PIL** library.
- Images are read from binary data in the database and displayed using **Streamlit**.
