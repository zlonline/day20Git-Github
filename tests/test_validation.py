import pandas as pd
import pytest

from pipeline.validation import validate_customers


def test_duplicate_customer_id():

    df = pd.DataFrame(
        {
            "customer_id": [
                1,
                1
            ],
            "name": [
                "John",
                "John"
            ],
            "email": [
                "john@email.com",
                "john@email.com"
            ],
            "city": [
                "Toronto",
                "Toronto"
            ],
            "updated_at": [
                "2026-09-10 10:00:00",
                "2026-09-10 11:00:00"
            ],
        }
    )

    with pytest.raises(
        ValueError,
        match="Duplicate customer_id found"
    ):

        validate_customers(
            df
        )

def test_null_customer_id():

    df = pd.DataFrame(
        {
            "customer_id": [
                1,
                None
            ],
            "customer_name": [
                "John",
                "Mary"
            ],
            "email": [
                "john@email.com",
                "mary@email.com"
            ],
            "city": [
                "Toronto",
                "Pickering"
            ],
            "updated_at": [
                "2026-09-10 10:00:00",
                "2026-09-10 11:00:00"
            ],
        }
    )

    with pytest.raises(
        ValueError
    ):

        validate_customers(
            df
        )

def test_missing_email_column():

    df = pd.DataFrame(
        {
            "customer_id": [1],
            "name": [
                "John"
            ],
            "city": [
                "Toronto"
            ],
            "updated_at": [
                "2026-09-10 10:00:00"
            ],
        }
    )

    with pytest.raises(
        ValueError,
        match="Missing column: email"
    ):

        validate_customers(
            df
        )

def test_null_email():

    df = pd.DataFrame(
        {
            "customer_id": [1],
            "name": ["John"],
            "email": [None],
            "city": ["Toronto"],
            "updated_at": [
                "2026-09-10 10:00:00"
            ],
        }
    )

    with pytest.raises(
        ValueError,
        match="email contains NULL"
    ):

        validate_customers(
            df
        )