import os
import pytest
import sqlite3

from fastapi.testclient import TestClient
from models import sales_table
from src.main import app
from utils import convert_tuple_to_dict

client = TestClient(app)

root_dir = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(os.getcwd(), "app.db")


@pytest.fixture(autouse=True)
def clean_all_data():
    """
    Clean all data from the database.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect(sql_path)
    cursor = connection.cursor()

    # Delete all data from the database
    cursor.execute("DELETE FROM sales")
    connection.commit()

    # Close the database connection
    cursor.close()
    connection.close()


def test_upload_file_with_valid_txt_file():
    """
    Should correctly store the data from a valid file and validate it in the database.
    """
    file_path = os.path.join(root_dir, "resources/sales_data_valid.txt")

    files = {
        "files": ("sales_data_valid.txt", open(file_path, "rb"), "text/plain")
    }

    response = client.post("/upload_file/", files=files)
    assert response.status_code == 201

    # Connect to the SQLite database
    connection = sqlite3.connect(sql_path)
    cursor = connection.cursor()

    # Retrieve the stored data from the database
    cursor.execute("SELECT * FROM sales")
    stored_data = cursor.fetchall()

    # Assert the stored data matches the expected values
    assert len(stored_data) == 1  # Assuming only one row is stored

    stored_data = convert_tuple_to_dict(
        stored_data[0],
        sales_table.columns.keys()
    )

    expected_data = {'id': 1, 'sales_type': '1', 'sales_date': '2022-01-15T19:20:30-03:00',
                     'product_description': 'CURSO DE BEM-ESTAR', 'product_price': '127.5',
                     'vendor_name': 'JOSE CARLOS'}

    assert stored_data == expected_data

    # Close the database connection
    cursor.close()
    connection.close()


def test_upload_file_with_invalid_file_extension():
    """
    Should not store the data from an invalid file (file extension not allowed).
    :return:
    """
    file_path = os.path.join(root_dir, "resources/sales_data_csv.csv")

    files = {
        "files": ("sales_data_csv.csv", open(file_path, "rb"), "text/csv")
    }

    response = client.post("/upload_file/", files=files)

    assert response.status_code == 400
    assert response.json() == {"detail": "Only .txt files are allowed"}

    # Connect to the SQLite database
    connection = sqlite3.connect(sql_path)
    cursor = connection.cursor()

    # Retrieve the stored data from the database
    cursor.execute("SELECT * FROM sales")
    stored_data = cursor.fetchall()

    # Assert the stored data matches the expected values
    assert len(stored_data) == 0  # Assuming only one row is stored

    # Close the database connection
    cursor.close()
    connection.close()


def test_upload_file_with_empty_file():
    """
    Should not store the data from an invalid file (empty file).
    :return:
    """
    file_path = os.path.join(root_dir, "resources/sales_data_empty.txt")

    files = {
        "files": ("sales_data_empty.txt", open(file_path, "rb"), "text/plain")
    }

    response = client.post("/upload_file/", files=files)
    assert response.status_code == 400
    assert response.json() == {"detail": "The file is empty"}

    # Connect to the SQLite database
    connection = sqlite3.connect(sql_path)
    cursor = connection.cursor()

    # Retrieve the stored data from the database
    cursor.execute("SELECT * FROM sales")
    stored_data = cursor.fetchall()

    # Assert the stored data matches the expected values
    assert len(stored_data) == 0  # Assuming only one row is stored

    # Close the database connection
    cursor.close()
    connection.close()


def test_upload_file_with_invalid_line_format():
    """
    Should not store the data from an invalid file (invalid data).
    :return:
    """
    file_path = os.path.join(root_dir, "resources/sales_data_invalid.txt")

    files = {
        "files": ("sales_data_invalid.txt", open(file_path, "rb"), "text/plain")
    }

    response = client.post("/upload_file/", files=files)
    assert response.status_code == 201

    # Connect to the SQLite database
    connection = sqlite3.connect(sql_path)
    cursor = connection.cursor()

    # Retrieve the stored data from the database
    cursor.execute("SELECT * FROM sales")
    stored_data = cursor.fetchall()

    # Assert the stored data matches the expected values
    assert len(stored_data) == 0  # Assuming only one row is stored

    # Close the database connection
    cursor.close()
    connection.close()
