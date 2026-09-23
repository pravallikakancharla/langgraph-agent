from langchain_core.tools import tool
from datetime import datetime


@tool
def get_day(date: str) -> str:
    """Return the day of the week for a date in YYYY-MM-DD format."""

    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")

        return date_object.strftime("%A")

    except ValueError:
        return "Invalid date. Use YYYY-MM-DD format."