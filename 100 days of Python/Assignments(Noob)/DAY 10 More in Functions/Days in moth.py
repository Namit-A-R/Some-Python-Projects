def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return("Leap year.")
            else:
                return("Not leap year.")
        else:
            return("Leap year.")
    else:
        return("Not leap year.")


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == "Leap year." and month == 2:
        return 29
    else:
        if month < 13 and month > 0:
            return month_days[month - 1]
        else:
            print("Invalid month")
            return ""


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
