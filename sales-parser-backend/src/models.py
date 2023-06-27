import sqlalchemy as sa
from database import metadata

sales_table = sa.Table(
    "sales",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("sales_type", sa.String(1)),
    sa.Column("sales_date", sa.String(26)),
    sa.Column("product_description", sa.String(31)),
    sa.Column("product_price", sa.String(10)),
    sa.Column("vendor_name", sa.String(20)),
)