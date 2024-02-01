import json
from datetime import datetime, timedelta

def calculate_time_difference_in_minutes(date_str, time_str):
    input_time = datetime.strptime(time_str, "%H:%M")
    input_date = datetime.strptime(date_str, "%Y-%m-%d")

    current_datetime = datetime.now()

    input_datetime = datetime(
        year=input_date.year,
        month=input_date.month,
        day=input_date.day,
        hour=input_time.hour,
        minute=input_time.minute
    )

    time_difference = current_datetime - input_datetime
    minutes_difference = int(time_difference.total_seconds() / 60)
    #minutes_difference = int((time_difference.total_seconds() % 3600) / 60)

    return minutes_difference

def get_user_by_id(user_data, user_id):
    for user in user_data.get("users", []):
        if user.get("id") == user_id:
            return user
    return None


def save_to_file(data):
    # Specify the file path where you want to save the data
    file_path = "food_data.json"

    # Open the file in append mode and write the data
    with open(file_path, 'w') as file:
        json.dump(data, file)
        file.write('\n')  # Add a new line for each entry