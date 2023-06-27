from pydantic import BaseModel


class SalesData(BaseModel):
    sales_type: str
    sales_date: str
    product_description: str
    product_price: str
    vendor_name: str
