from schemas import SalesData


def extract_sales_data_price(text):
    """
    This function extracts the sales data from a text.
    :param text:
    :return:
    """

    is_empty_text = len(text) == 0

    if is_empty_text:
        raise ValueError("EMPTY_TEXT_ERROR")

    sales_type = text[0]
    sales_date = text[1:26]
    product_description = text[26:56]
    vendor_name = text[66:86]
    product_price = text[56:66]

    if product_price != '':
        product_price = str(int(product_price) / 100)

    data = {
        "sales_type": sales_type.strip(),
        "sales_date": sales_date.strip(),
        "product_description": product_description.rstrip(),
        "product_price": product_price.strip(),
        "vendor_name": vendor_name.rstrip()
    }

    if any(value == "" for value in data.values()):
        raise ValueError("OBJECT_WITH_EMPTY_VALUES_ERROR")

    return data


def extract_sales_data_from_text_array(lines):
    """
    This function extracts the sales data from a text array.
    :param lines:
    :return:
    """

    results = []
    exceptions = []

    for index, line in enumerate(lines):
        try:
            data = extract_sales_data_price(line)
            results.append(SalesData(**data).dict())
        except Exception as e:
            # Handle validation errors or specific exceptions
            # You can choose to skip invalid lines or raise an exception
            exceptions.append(f"> Error processing line - {index + 1}: {line}")

    return {
        "results": results,
        "exceptions": exceptions,
    }


def convert_tuple_to_dict(data, columns):
    try:
        return dict(zip(columns, data))
    except Exception as e:
        print(f"Error converting tuple to dict: {e}")
        return {}
