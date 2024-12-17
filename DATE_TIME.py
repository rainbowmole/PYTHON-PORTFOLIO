import datetime

timezones = {'GMT': 0, 'EST': -5, 'PST': 7, 'IST': 5.5}
def parse_datetime(input_datetime):
    try:
        parse_datetime = datetime.datetime.strptime(input_datetime, '%Y-%m-%d %H:%M:%S')
        return parse_datetime
    except ValueError:
        print("Error: Invalid date/time format.")
    return None
def convert_timezone(datetime_obj, original_offset, target_offset):
    try:
        offset_difference = original_offset - target_offset
        converted_datetime = datetime_obj + datetime.timedelta(hours=offset_difference)
        return converted_datetime
    except:
        print("Error: Unknown Timezone.")
    return None
def perform_date_arithmetic(input_date, days):
    try:
        input_date = datetime.datetime.strptime(input_date, '%Y-%m-%d')
        resultant_date = input_date + datetime.timedelta(days=days)
        return resultant_date.strftime('%B %d, %Y')
    except ValueError:
        print("Error: Invalid Date Format. ")
    return None
def format_datetime(input_datetime, format_choice):
    try:
        input_datetime = datetime.datetime.strptime(input_datetime, '%Y-%m-%d %H:%M:%S')
        if format_choice == 1:
            formatted_datetime = input_datetime.strftime('%m/%d/%Y %I:%M %p')
        if format_choice == 2:
            formatted_datetime = input_datetime.strftime('%d/%m/%Y %I:%M %p')
        if format_choice == 3:
            formatted_datetime = input_datetime.strftime('%Y-%m-%d %I:%M %p')
        else:
            print("Error: Invalid Format Choice.")
            return None
        return formatted_datetime
    except ValueError:
        print("Error: Invalid Date/Time Format.")
        return None
def main():
    print("\nWelcome to the Python DateTime Utility")
    while True:
        print("\n1. Parse Date/Time")
        print("2. Convert Timezones")
        print("3. Perform Date arithmetic")
        print("4. Format Date/Time")
        print("5. Exit\n")

        choice = input("Please enter your choice: ")

        if choice == '1':
            print("\n-- Parse Date/Time --\n")
            input_datetime = input("Enter a date/time (e.g, YYYY-MM-DD HH:MM:SS): ")
            parsed_datetime = parse_datetime(input_datetime)

            if parsed_datetime:
                print("Parsed Date/Time: ", parsed_datetime.strftime('%B %d, %Y %I:%M %p'))

        elif choice == '2':
            print("\n-- Convert Timezones --\n")
            orginal_datetime = input("Enter the original date/time (e.g, YYYY-MM-DD HH:MM:SS): ")
            orginal_timezone = input("enter the original timezone (e.g., GMT, EST): ")
            target_timezone = input('Enter the target timezone (e.g., PST, IST): ')
            orignal_offset = timezones.get(orginal_timezone)
            target_offset = timezones.get(target_timezone)

            if original_offset is not None and target_offset is not None:
                convert_datetime = convert_timezone(parse_datetime(orginal_datetime), orignal_offset, target_offset)
                if convert_datetime:
                    print("Converted Date/Time: ", convert_datetime.strftime('%B %d, %Y %I:%M %p'), f'{target_timezone}')

        elif choice == '3':
            print("\n-- Perform Date Arithmetic --\n")
            input_datetime = input("Enter a date (YYYY-MM-DD): ")
            input_date = input("Enter the number of days to add/subtract: ")
            resultant_date = perform_date_arithmetic(input_date, days)

            if resultant_date:
                print("Resultant Date: ", resultant_date)

        elif choice == '4':
            print("\n-- Format Date/time --\n")
            input_datetime = input("Enter a date/time (YYYY-MM-DD HH:MM:SS): ")
            format_choice = int(input("Choose a format (1. MM/DD/YYYY, 2. DD/MM/YYYY, 3. YYYY-MM-DD): "))
            formatted_datetime = format_datetime(input_datetime, format_choice)

            if formatted_datetime:
                print("Formatted Date/Time: ", formatted_datetime)

        elif choice == '5':
            print("\nThank you for using the Python DateTime Utility")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == '__main__':
    main()