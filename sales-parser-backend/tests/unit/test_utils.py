import pytest

from src.schemas import SalesData
from src.utils import extract_sales_data_price, extract_sales_data_from_text_array, convert_tuple_to_dict


@pytest.fixture
def data_example():
    return "12022-01-15T19:20:30-03:00CURSO DE BEM-ESTAR            0000012750JOSE CARLOS"


def test_extract_data(data_example):
    """
    Should correctly extract the data from a valid text.
    :param data_example:
    :return:
    """

    result = extract_sales_data_price(data_example)
    assert result == {
            "sales_type": "1",
            "sales_date": "2022-01-15T19:20:30-03:00",
            "product_description": "CURSO DE BEM-ESTAR",
            "product_price": "127.5",
            "vendor_name": "JOSE CARLOS"
        }


def test_extract_data_with_spaces(data_example):
    """
    Should correctly extract the data from a valid text with spaces.
    :param data_example:
    :return:
    """

    text_with_spaces = data_example + "  "
    result = extract_sales_data_price(text_with_spaces)

    assert result == {
            "sales_type": "1",
            "sales_date": "2022-01-15T19:20:30-03:00",
            "product_description": "CURSO DE BEM-ESTAR",
            "product_price": "127.5",
            "vendor_name": "JOSE CARLOS"
        }


def test_extract_data_with_incomplete_text():
    """
    Should raise an error when the text is incomplete.
    :return:
    """

    incomplete_data = "1"

    with pytest.raises(ValueError) as exception_info:
        extract_sales_data_price(incomplete_data)
    assert str(exception_info.value) == "OBJECT_WITH_EMPTY_VALUES_ERROR"


def test_extract_data_with_empty_text():
    """
    Should raise an error when the text is empty.
    :return:
    """
    incomplete_data = ""

    with pytest.raises(ValueError) as exception_info:
        extract_sales_data_price(incomplete_data)
    assert str(exception_info.value) == "EMPTY_TEXT_ERROR"


def test_extract_sales_data_from_text_array():
    """
    Should correctly extract the data from a valid text array.
    :return:
    """

    lines = [
        "12022-01-15T19:20:30-03:00CURSO DE BEM-ESTAR            0000012750JOSE CARLOS",
        "12021-12-03T11:46:02-03:00DOMINANDO INVESTIMENTOS       0000050000MARIA CANDIDA",
        "3INVALID_LINE",
        "22022-01-16T14:13:54-03:00CURSO DE BEM-ESTAR            0000012750THIAGO OLIVEIRA"
    ]

    expected_results = [
        SalesData(
            sales_type="1",
            sales_date="2022-01-15T19:20:30-03:00",
            product_description="CURSO DE BEM-ESTAR",
            product_price="127.5",
            vendor_name="JOSE CARLOS"
        ),
        SalesData(
            sales_type="1",
            sales_date="2021-12-03T11:46:02-03:00",
            product_description="DOMINANDO INVESTIMENTOS",
            product_price="500.0",
            vendor_name="MARIA CANDIDA"
        ),
        SalesData(
            sales_type="2",
            sales_date="2022-01-16T14:13:54-03:00",
            product_description="CURSO DE BEM-ESTAR",
            product_price="127.5",
            vendor_name="THIAGO OLIVEIRA"
        )
    ]

    results = extract_sales_data_from_text_array(lines)

    assert len(results['results']) == len(expected_results)

    for result, expected_result in zip(results['results'], expected_results):
        assert result['sales_type'] == expected_result.sales_type
        assert result['sales_date'] == expected_result.sales_date
        assert result['product_description'] == expected_result.product_description
        assert result['product_price'] == expected_result.product_price
        assert result['vendor_name'] == expected_result.vendor_name


def test_convert_tuple_to_dict():
    data = (1, 'John', 'Doe')
    columns = ['id', 'first_name', 'last_name']
    expected_result = {'id': 1, 'first_name': 'John', 'last_name': 'Doe'}
    assert convert_tuple_to_dict(data, columns) == expected_result

    data = (42, 'Alice')
    columns = ['age', 'name']
    expected_result = {'age': 42, 'name': 'Alice'}
    assert convert_tuple_to_dict(data, columns) == expected_result

    data = (100,)
    columns = ['value']
    expected_result = {'value': 100}
    assert convert_tuple_to_dict(data, columns) == expected_result
