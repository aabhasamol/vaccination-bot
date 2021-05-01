# Vaccination Bot

This is a twitter bot which will give you Covid Vaccination Availability details for Ranchi and Bangalore.

The following Co-Win APIs have been used for the same:
https://apisetu.gov.in/public/api/cowin#/Appointment%20Availability%20APIs/calendarByDistrict
https://apisetu.gov.in/public/api/cowin#/Appointment%20Availability%20APIs/calendarByPin

The first API was used to generate a request which gave me all the PINCODES of all the vaccination centres present in Ranchi and Bangalore.

From the second API, I generated a request through which I got the JSON Object and extracted the basic details of the vaccination centres such as Name, Date, Vaccines Available, The Vaccine Administered and its cost.

Using the said extracted data I designed a tweet which would display all the necessary details. If the vaccine was free, the cost of the vaccine would be displayed as zero. If there was no vaccine information provided then the price and vaccine information were made equivalent to null.

The bot has a functionality of displaying vaccine availability data for a maximum of 7 days and iterates through every vaccination center providing said covid vaccination services.

The bot sends out timely updates every 8 hours for every center across Ranchi and Bangalore in the said PINCODE.

The twitter handle for the bot is @VaxUpdateBot and the link for the same is:
https://twitter.com/VaxUpdateBot

The aim of this bot was to provide assistance to those looking to get vaccinated, after-all India is undergoing the biggest vaccination drive in the world from 1st May, 2021.
It provides easy access to data and helps provides people with vaccination availability details.
