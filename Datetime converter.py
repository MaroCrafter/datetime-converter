import datetime
from pyperclip import copy

def main():
  print("Welcome to the Date/Time to Timestamp converter!")
  print("Please enter the date and time you would like to convert below!")
  print("Enter the format you would like to have! Here are the available options with examples:\n1: 07/10/2021\n2: July 10, 2021 1:21 PM\n3: 1:21 PM\n4: July 10, 2021\n5: Saturday, July 10, 2021 1:21 PM\n6: 6 minutes ago\n7: 1:21:08 PM")
  
  # Get the date and time input from the user
  date_input = input("Date (YYYY-MM-DD): ")
  time_input = input("Time (HH:MM:SS): ")
  format_input = input("Format number:")
  
  # Combine the date and time input into a single string
  datetime_input = f"{date_input} {time_input}"
  
  # Convert the string to a datetime object
  datetime_obj = datetime.datetime.strptime(datetime_input, "%Y-%m-%d %H:%M:%S")
  
  # Convert the datetime object to a timestamp
  timestamp = datetime_obj.timestamp()
  timestamp = int(timestamp)
  print(timestamp)
  
  # Print the timestamp
  print(f"Timestamp: {timestamp}")
  if format_input == "1":
    print(f"Timestamp discord-ready (and put into the clipboard): <t:{timestamp}:d>")
    copy(f"<t:{timestamp}:d>")
  elif format_input == "2":
    print(f"Timestamp discord-ready (and put into the clipboard): <t:{timestamp}:f>")
    copy(f"<t:{timestamp}:f>")
  elif format_input == "3":
    print(f"Timestamp discord-ready (and put into the clipboard): <t:{timestamp}:t>")
    copy(f"<t:{timestamp}:t>")
  elif format_input == "4":
    print(f"Timestamp discord-ready (and put into the clipboard): <t:{timestamp}:D>")
    copy(f"<t:{timestamp}:D>")
  elif format_input == "5":
    print(f"Timestamp discord-ready (and put into the clipboard): <t:{timestamp}:F>")
    copy(f"<t:{timestamp}:F>")
  elif format_input == "6":
    print(f"Timestamp discord-ready (and put into the clipboard): <t:{timestamp}:R>")
    copy(f"<t:{timestamp}:R>")
  elif format_input == "7":
    print(f"Timestamp discord-ready (and put into the clipboard): <t:{timestamp}:T>")
    copy(f"<t:{timestamp}:T>")

if __name__ == "__main__":
  main()
  noinput = input("You can close this program now.")