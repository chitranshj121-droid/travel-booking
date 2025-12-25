import streamlit as st
from datetime import datetime
import pandas as pd

# Date
current_date = datetime.now().date()



st.title("✈️ Travel & Ticket Booking Dashboard")
st.write("Current Date:", current_date)
st.write("Welcome to your trusted travel and ticketing partner.")

# User details
st.header("Passenger Details")
name = st.text_input("Enter your name")
passport = st.text_input("Enter your passport number")
age = st.number_input("Enter your age", min_value=0, max_value=120)

if age != 0 and age < 18:
    st.error("Bookings are allowed only for individuals aged 18 and above.")
    st.stop()

# Data
train = ["RAJDHANI EXPRESS", "JAN SHATABDI", "VANDE BHARAT", "GARIB RATH", "GATIMAN"]
venues = ["Jaipur-Delhi", "Delhi-Jaipur", "Banglore-Mumbai", "Mumbai-Kota", "Goa-Lonavala"]
price = [355, 567, 198, 241, 134]

flights = ["INDIGO", "VISTARA", "EMIRATES", "AIR INDIA", "SWISS"]
venues2 = ["Delhi-Dubai", "Banglore-Tokyo", "Mumbai-Switzerland", "Jaipur-Banglore", "Thailand-Mumbai"]
price2 = [1233, 8444, 3555, 958, 1312]

# Menu
st.header("Booking Menu")
option = st.radio("Choose booking type:", ["Trains", "Flights"])

# Train Booking
if option == "Trains":
    st.subheader("Available Trains")
    train_df = pd.DataFrame({
        "Train": train,
        "Route": venues,
        "Price": price
    })
    st.table(train_df)

    selected_train = st.selectbox("Select a train", train)

    if st.button("Book Train"):
        st.success(f"✅ {selected_train} booked successfully for tomorrow!")

# Flight Booking
if option == "Flights":
    st.subheader("Available Flights")
    flight_df = pd.DataFrame({
        "Flight": flights,
        "Route": venues2,
        "Price": price2
    })
    st.table(flight_df)

    selected_flight = st.selectbox("Select a flight", flights)

    if st.button("Book Flight"):
        st.success(f"✅ {selected_flight} booked successfully for tomorrow!")

st.footer = st.write("Thank you for visiting us. Have a pleasant journey! 🌍")
st.footer = st.write("CHITRANSH J(DATA ANALYST) APPLE PARK ")
st.footer = st.write("Special thanks goes to:")
st.footer = st.write("BIRENDRA SINGH ")
st.footer = st.write("TANISHKA SHARMA")
st.footer = st.write("DIVYANSHI JAIN")
st.footer = st.write("FOR RUNNING ADDS MAIL TO- chitranshj121@gmail.com)



