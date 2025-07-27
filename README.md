# Vaccination Bot

This is a twitter bot built by Aabhas Amol, which will give you Covid Vaccination Availability details in your DMs for the said pincode.

The following Co-Win APIs have been used for the same:
https://apisetu.gov.in/public/api/cowin#/Appointment%20Availability%20APIs/calendarByDistrict
https://apisetu.gov.in/public/api/cowin#/Appointment%20Availability%20APIs/calendarByPin

The first API was used to generate a request which gave me all the PINCODES of all the vaccination centres present in Ranchi and Bangalore.

From the second API, I generated a request through which I got the JSON Object and extracted the basic details of the vaccination centres such as Name, Date, Vaccines Available, The Vaccine Administered, and pincode of the Vaccination center.

Using the said extracted data I designed a message that would display all the necessary details. 

The bot has a functionality of displaying vaccine availability data for a maximum of 7 days and iterates through every vaccination center providing said covid vaccination services.

The bot sends out timely updates for every center across India.

The twitter handle for the bot is @VaxUpdateBot and the link for the same is:
https://twitter.com/VaxUpdateBot

The aim of this bot was to provide assistance to those looking to get vaccinated, after-all India is undergoing the biggest vaccination drive in the world from 1st May, 2021.
It provides easy access to data and helps provides people with vaccination availability details.
