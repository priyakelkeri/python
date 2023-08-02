import json

def load_weather_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def display_menu():
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

def get_user_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        return -1

def get_weather_by_date(weather_data):
    date = input("Enter the date (YYYY-MM-DD): ")
    for item in weather_data["list"]:
        if item["dt_txt"].startswith(date):
            print("Temperature for", item["dt_txt"], ":", item["main"]["temp"], "°C")
            return
    print("Weather data not available for the specified date.")

def get_wind_speed_by_date(weather_data):
    date = input("Enter the date (YYYY-MM-DD): ")
    for item in weather_data["list"]:
        if item["dt_txt"].startswith(date):
            print("Wind Speed for", item["dt_txt"], ":", item["wind"]["speed"], "m/s")
            return
    print("Wind Speed data not available for the specified date.")

def get_pressure_by_date(weather_data):
    date = input("Enter the date (YYYY-MM-DD): ")
    for item in weather_data["list"]:
        if item["dt_txt"].startswith(date):
            print("Pressure for", item["dt_txt"], ":", item["main"]["pressure"], "hPa")
            return
    print("Pressure data not available for the specified date.")

def main():
    file_path = "hourly.json"  # Replace with the actual file name and path if different
    weather_data = load_weather_data(file_path)

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            get_weather_by_date(weather_data)
        elif choice == 2:
            get_wind_speed_by_date(weather_data)
        elif choice == 3:
            get_pressure_by_date(weather_data)
        elif choice == 0:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
