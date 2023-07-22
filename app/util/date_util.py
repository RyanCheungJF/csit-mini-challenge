from datetime import datetime

from werkzeug.exceptions import BadRequest


def formulate_date(date: str):
    """Converts a date as a string to a datetime object.

    Args:
        date: Date of yyyy-mm-dd format.

    Raises:
        BadRequest: When input does not follow the specified format.

    Returns:
        datetime: Datetime object used in Mongo date types.
    """
    try:
        date_arr = date.split("-")
        if len(date_arr) != 3:
            raise BadRequest("Date is not properly formatted!")
        yyyy, mm, dd = [int(i) for i in date_arr]
        return datetime(yyyy, mm, dd, 0, 0)
    except:
        raise BadRequest("Date is not properly formatted!")
