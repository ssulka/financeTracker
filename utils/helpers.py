import datetime

def format_currency(amount):
    """Format a number as currency."""
    return "${:,.2f}".format(amount)

def calculate_percentage(part, whole):
    """Calculate the percentage of part out of whole."""
    if whole == 0:
        return 0
    return (part / whole) * 100

def parse_date(date_str, date_format="%Y-%m-%d"):
    """Parse a date string into a datetime object."""
    try:
        return datetime.datetime.strptime(date_str, date_format)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Expected format: {date_format}")