from datetime import datetime

def transform_date(input_date: str) -> str:
    input_format = "%d %B %Y"

    date_object = datetime.strptime(input_date, input_format)

    output_format = "%Y-%m-%d"

    output_date = date_object.strftime(output_format)

    return output_date
