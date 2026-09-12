import pandas as pd

from pipeline.transform import transform_customers


def test_email_lowercase():

    input_df = pd.DataFrame(
        {
            "customer_id": [1],
            "name": [
                "John Smith"
            ],
            "email": [
                "JOHN@EMAIL.COM"
            ],
            "city": [
                "Toronto"
            ],
            "updated_at": [
                "2026-09-10 10:00:00"
            ],
        }
    )

    result = transform_customers(
        input_df
    )

    assert (
        result.iloc[0]["email"]
        == "john@email.com"
    )

def test_customer_name():

    input_df = pd.DataFrame(
        {
            "customer_id": [1],
            "name": [
                "  john smith  "
            ],
            "email": [
                "john@email.com"
            ],
            "city": [
                "Toronto"
            ],
            "updated_at": [
                "2026-09-10 10:00:00"
            ],
        }
    )

    result = transform_customers(
        input_df
    )

    assert (
        result.iloc[0]["name"]
        == "John Smith"
    )

def test_city_format():

    input_df = pd.DataFrame(
        {
            "customer_id": [1],
            "name": [
                "John Smith"
            ],
            "email": [
                "john@email.com"
            ],
            "city": [
                "  PICKERING  "
            ],
            "updated_at": [
                "2026-09-10 10:00:00"
            ],
        }
    )

    result = transform_customers(
        input_df
    )

    assert (
        result.iloc[0]["city"]
        == "Pickering"
    )