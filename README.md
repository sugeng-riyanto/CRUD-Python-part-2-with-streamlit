

# CRUD Application with SQLite and Images

This project is a simple CRUD (Create, Read, Update, Delete) application built with **Python**, **Streamlit**, and **SQLite3**. It allows users to manage items with basic details (name and description) and an optional image.

## Features

1. **Create**: Add a new item with a name, description, and optional image.
2. **Read**: View the list of items and see details, including uploaded images.
3. **Update**: Modify an item's name, description, and optionally update its image.
4. **Delete**: Remove an item from the database.

## Technologies Used

- **Python**: Programming language used to implement the application logic.
- **Streamlit**: Framework for building the web-based interface.
- **SQLite3**: Database to store items, descriptions, and images.
- **Pillow**: Library to handle images in Python.

## Prerequisites

Make sure you have the following installed:
- Python 3.8 or above
- pip (Python package manager)

## Installation

1. Clone this repository or download the script.
2. Install the required libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run script_name.py
   ```

   Replace `script_name.py` with the name of your Python script.

## How to Use

1. **Start the Application**:
   - Run the Streamlit app as described above.
   - The web interface will open in your browser.

2. **Navigate the Menu**:
   - Use the sidebar menu to switch between the options: Create, Read, Update, Delete.

3. **Perform Actions**:
   - **Create**:
     - Enter a name, add a description, and optionally upload an image.
     - Click "Add Item" to save it.
   - **Read**:
     - View the list of items.
     - Click "View Details" to see an item's full details and image.
   - **Update**:
     - Select an item from the dropdown to edit.
     - Modify the name, description, or upload a new image.
     - Click "Update Item" to save changes.
   - **Delete**:
     - Select an item from the dropdown to delete.
     - Click "Delete Item" to remove it.

4. **View Images**:
   - Uploaded images are displayed in the "Read" section when viewing item details.

## File Structure

```
.
├── script_name.py        # Main Python script
├── requirements.txt      # List of dependencies
└── README.md             # Documentation
```

## Example Screenshots

1. **Create New Item**
   - Add details and an optional image to create an item.

2. **View Items**
   - See all items listed, and view detailed information for each.

3. **Update Item**
   - Modify item details and optionally upload a new image.

4. **Delete Item**
   - Remove an item from the database permanently.

## Notes

- Uploaded images are stored as BLOB data in the SQLite database.
- SQLite is lightweight and requires no setup, making it perfect for small applications.

## Contribution

If you want to improve or add new features to this project:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

## License

This project is open-source and free to use.

---

Enjoy learning CRUD operations with Python and Streamlit!
#
