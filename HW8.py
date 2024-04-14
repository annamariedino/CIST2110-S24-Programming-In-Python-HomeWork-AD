# HW8.py
# Author: Anna-Marie DiNofrio

# This homework will exapnd upon the code for Lab10.py. If you did not complete Lab10.py, you should do so before attempting this homework.

# Copy the code from Lab10.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)
import streamlit as st
import datetime as dt

# Streamlit title, subtitle, date, and button
st.title("Date Counter")
st.subheader("This is a simple date counter.")
date = st.date_input("Enter a date:")
button = st.button("Click Me")

# The calculate_days function from Lab10.py
def calculate_days(date):
    current_date = dt.datetime.now().date()
    difference = date - current_date
    return difference.days

print(calculate_days(date))

# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.
calculate_days_until_birthday = st.date_input("Enter your birthday:")
def calculate_days_until_birthday(birthday):
    """This function will take in the entered birthday and find the difference with todays date to return the amount of days until the birthday.
    Returns: days until birthday"""
    current_date = dt.datetime.now().date()
    difference = birthday - current_date
    return difference.days


def app():
    print("Running the app")

    try:
        if button:
            days = calculate_days_until_birthday(date)
            st.write(f"Days until the date: {days}")


# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)
def days_until_semester_ends(end_of_semester):
    """This function will take in the entered end of the semester and find the difference with todays date to return the amount of days until the end of the semester.
    Returns: days until end of semester"""
    current_date = dt.datetime.now().date()
    end_of_semester = dt.date(2023, 12, 8)
    difference = current_date - end_of_semester
    return difference.days
    

# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include
# an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE.
# new_years = dt.date(2025, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")

def days_until_new_years(new_years):
    """This function will take in the entered New Years Day and find the difference with todays date to return the amount of days until New Years Day.
    Returns: days until New Years Day"""
    new_years = dt.date(2025, 1, 1)
    current_date = dt.datetime.now().date()
    difference = current_date - new_years
    st.write("🎉")
    return difference.days

# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.

# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date.
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉
button = st.button("Days until New Year's Day")
try:
    if button:
        days = days_until_new_years(current_date)
        st.write(f"Days until New Year's Day: {days}")

# app function from Lab10.py


if __name__ == "__main__":
    app()
