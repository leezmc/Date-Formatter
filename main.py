# Purpose: Converts input of date into long form and international short form. 
# Author:  Michael Lee
# Date: 25 January 2023

# defines numbers to months 
def dateLongForm(inputDate):
    months = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    monthLLong = months[inputDate[:2]]
    dayLLong = int(inputDate[3:5])
    yearLong = inputDate[6:]
    return (f"{monthLLong} {dayLLong}, {yearLong}")
# reorders user input date
def internationalShortForm(inputDate):
    return inputDate[3:5] + "-" + inputDate[:2] + "-" + inputDate[-2:]
# asks user for date
if __name__ == "__main__":
    inputDate = input("Enter a date in the following format (mm/dd/yyyy): ")
    print("Date long form:", dateLongForm(inputDate))
    print("International short form:", internationalShortForm(inputDate))
