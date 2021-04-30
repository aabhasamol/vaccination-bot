# Vaccination Bot

This is a twitter bot which will give you Covid Vaccination Availability details for Ranchi - PINCODE - 834001

The following Co-Win API has been used for the same:
https://apisetu.gov.in/public/api/cowin#/Appointment%20Availability%20APIs/calendarByPin

From here I got the JSON Object and extracted the basic details of the vaccination centres such as Name, Date, Vaccines Available, The Vaccine Administered and its cost.

Using the said extracted data I designed a tweet which would display all the necessary details. If the vaccine was free, the cost of the vaccine wouldn't be displayed. If there was no vaccine information provided then the price and vaccine information were made equivalent to null.

The bot has a functionality of displaying vaccine availability data for a maximum of 7 days and iterates through every vaccination center providing said covid vaccination services.

The bot sends out timely updates every 8 hours for every center across Ranchi in the said PINCODE which is of Ranchi Urban.

The twitter handle for the bot is @VaxUpdateBot and the link for the same is:
https://twitter.com/VaxUpdateBot

The aim of this bot was to provide assistance to those looking to get vaccinated, after-all India is undergoing the biggest vaccination drive in the world from 1st May, 2021.
It provides easy access to data and helps provides people with vaccination availability details.
