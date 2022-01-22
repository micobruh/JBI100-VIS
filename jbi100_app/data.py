import pandas as pd
import plotly.express as px
import numpy as np
import re

def get_data():

    # Read data
    df = pd.read_csv("dataset.csv")

    # Any further data preprocessing can go here
    time_list = df['Time'].tolist()
    hour_list = [re.findall('([0-9]+)\:[0-9]+', i) for i in time_list]
    df['Hour'] = hour_list
    df['Hour'] = df['Hour'].str[0]

    # Redefine rows with unknown values
    df = df.replace(['?', -1, np.nan], 100000000)

    df = df.astype('str')

    # Replace numeric values to understandable strings
    df["Day_of_Week"].replace({"1": "Sunday", "2": "Monday", "3": "Tuesday", 
    "4": "Wednesday", "5": "Thursday", "6": "Friday", "7": "Saturday"}, inplace=True)

    df["1st_Road_Class"].replace({"1": "Motorway", "2": "A(M)", "3": "A", 
    "4": "B", "5": "C", "6": "100000000"}, inplace=True)

    df["Road_Type"].replace({"1": "Roundabout", "2": "One Way Street", "3": "Dual Carriageway", 
    "6": "Single Carriageway", "7": "Slip road", "9": "100000000"}, inplace=True)

    df["Speed_limit"].replace({"99": "100000000"}, inplace=True)

    df["Junction_Detail"].replace({"0": "Not at Junction or within 20 Metres", "1": "Roundabout", 
    "2": "Mini-Roundabout", "3": "T or Staggered Junction", "5": "Slip Road", "6": "Crossroads", 
    "7": "More than 4 Arms (Not Roundabout)", "8": "Private Drive or Entrance", "9": "Other Junction", 
    "99": "100000000"}, inplace=True)

    df["Junction_Control"].replace({"0": "Not at Junction or within 20 Metres", "1": "Authorised Person", 
    "2": "Auto Traffic Signal", "3": "Stop Sign", "4": "Give Way or Uncontrolled", 
    "9": "100000000"}, inplace=True)

    df["2nd_Road_Class"].replace({"1": "Motorway", "2": "A(M)", "3": "A", 
    "4": "B", "5": "C", "6": "100000000"}, inplace=True)

    df["Pedestrian_Crossing-Physical_Facilities"].replace({"0": "No Physical Crossing Facilities within 50 Metres", 
    "1": "Zebra", "4": "Pelican, Puffin, Toucan or Similar Non-Junction Pedestrian Light Crossing", 
    "5": "Pedestrian Phase at Traffic Signal Junction", "7": "Footbridge or Subway", "8": "Central Refuge", 
    "9": "100000000"}, inplace=True)

    df["Light_Conditions"].replace({"1": "Daylight", "4": "Darkness-Lights Lit", "5": "Darkness-Lights Unlit", 
    "6": "Darkness-No Lighting", "7": "Darkness-Lighting Unknown"}, inplace=True)

    df["Weather_Conditions"].replace({"1": "Fine No High Winds", "2": "Raining No High Winds", "3": "Snowing No High Winds", 
    "4": "Fine + High Winds", "5": "Raining + High Winds", "6": "Snowing + High Winds", 
    "7": "Fog or Mist", "8": "Other", "9": "100000000"}, inplace=True)

    df["Road_Surface_Conditions"].replace({"1": "Dry", "2": "Wet or Damp", "3": "Snow", 
    "4": "Frost or Ice", "5": "Flood over 3cm. Deep", "6": "Oil or Diesel", 
    "7": "Mud", "9": "100000000"}, inplace=True)

    df["Special_Conditions_at_Site"].replace({"0": "None", "1": "Auto Traffic Signal-Out", 
    "2": "Auto Signal Part Defective", "3": "Road Sign or Marking Defective or Obscured", 
    "4": "Roadworks", "5": "Road Surface Defective", "6": "Oil or Diesel", 
    "7": "Mud", "9": "100000000"}, inplace=True)

    df["Carriageway_Hazards"].replace({"0": "None", "1": "Vehicle Load on Road", 
    "2": "Other Object on Road", "3": "Previous Accident", 
    "4": "Dog on Road", "5": "Other Animal on Road", "6": "Pedestrian In Carriageway-Not Injured", 
    "7": "Any Animal in Carriageway (Except Ridden Horse)", "9": "100000000"}, inplace=True)

    df["Age_Band_of_Casualty"].replace({"1": "0-5", "2": "6-10", "3": "11-15", 
    "4": "16-20", "5": "21-25", "6": "26-35", "7": "36-45", "8": "46-55", "9": "56-65", 
    "10": "66-75", "11": "Over 75"}, inplace=True)

    df["Pedestrian_Location"].replace({"0": "Not a Pedestrian", "1": "Crossing on Pedestrian Crossing Facility", 
    "2": "Crossing in Zig-Zag Approach Lines", "3": "Crossing in Zig-Zag Exit Lines", 
    "4": "Crossing Elsewhere within 50m. of Pedestrian Crossing", "5": "In Carriageway, Crossing Elsewhere", 
    "6": "On Footway or Verge", "7": "On Refuge, Central Island or Central Reservation", 
    "8": "In Centre of Carriageway-Not on Refuge, Island or Central Reservation", "9": "In Carriageway, Not Crossing", 
    "10": "Others"}, inplace=True)

    df["Pedestrian_Movement"].replace({"0": "Not a Pedestrian", "1": "Crossing from Driver's Nearside", 
    "2": "Crossing from Nearside-Masked by Parked or Stationary Vehicle", "3": "Crossing from Driver's Offside", 
    "4": "Crossing from Offside-Masked by Parked or Stationary Vehicle", 
    "5": "In carriageway, Stationary-Not Crossing (Standing or Playing)", 
    "6": "In carriageway, Stationary-Not Crossing (Standing or Playing)-Masked by Parked or Stationary Vehicle", 
    "7": "Walking along in Carriageway, Facing Traffic", 
    "8": "Walking along in Carriageway, Back to Traffic", "9": "Others"}, inplace=True)

    df["Bus_or_Coach_Passenger"].replace({"0": "Not a Bus or Coach Passenger", "1": "Boarding", 
    "2": "Alighting", "3": "Standing Passenger", "4": "Seated passenger", "9": "100000000"}, inplace=True)

    df["Pedestrian_Road_Maintenance_Worker"].replace({"0": "No/Not Applicable", "1": "Yes", 
    "2": "Not Known", "3": "Probable"}, inplace=True)

    df["Casualty_IMD_Decile"].replace({"1": "Most Deprived 10%", "2": "More Deprived 10-20%", "3": "More Deprived 20-30%", 
    "4": "More Deprived 30-40%", "5": "More Deprived 40-50%", "6": "Less Deprived 40-50%", "7": "Less Deprived 30-40%", 
    "8": "Less Deprived 20-30%", "9": "Less Deprived 10-20%", "10": "Least Deprived 10%"}, inplace=True)

    df["Towing_and_Articulation"].replace({"0": "No Tow/Articulation", "1": "Articulated Vehicle", 
    "2": "Double or Multiple Trailer", "3": "Caravan", 
    "4": "Single Trailer", "5": "Other Tow", "9": "100000000"}, inplace=True)

    df["Vehicle_Manoeuvre"].replace({"1": "Reversing", "2": "Parked", "3": "Waiting to Go-Held Up", 
    "4": "Slowing or Stopping", "5": "Moving off", "6": "U-Turn", "7": "Turn Left", "8": "Waiting to Turn Left", 
    "9": "Turn Right", "10": "Waiting to Turn Right", "11": "Changing Lane to Left", "12": "Changing Lane to Right", 
    "13": "Overtaking Moving Vehicle-Offside", "14": "Overtaking Static Vehicle-Offside", "15": "Overtaking-Nearside", 
    "16": "Going Ahead Left-Hand Bend", "17": "Going Ahead Right-Hand Bend", "18": "Going Ahead Others", 
    "99": "100000000"}, inplace=True)

    df["Vehicle_Location-Restricted_Lane"].replace({"0": "On main C'Way-Not in Restricted Lane", 
    "1": "Tram/Light Rail Track", "2": "Bus Lane", "3": "Busway (Including Guided Busway)", 
    "4": "Cycle Lane (On Main Carriageway)", "5": "Cycleway or Shared Use Footway (Not Part of Main Carriageway)", 
    "6": "On Lay-By or Hard Shoulder", "7": "Entering Lay-by or Hard Shoulder", "8": "Leaving Lay-by or Hard Shoulder", 
    "9": "Footway (Pavement)", "10": "Not on Carriageway", "99": "100000000"}, inplace=True)

    df["Junction_Location"].replace({"0": "Not at or Within 20 Metres of Junction", 
    "1": "Approaching Junction or Waiting/Parked at Junction Approach", 
    "2": "Cleared Junction or Waiting/Parked at Junction Exit", "3": "Leaving Roundabout", 
    "4": "Entering Roundabout", "5": "Leaving Main Road", 
    "6": "Entering Main Road", "7": "Entering from Slip Road", "8": "Mid Junction-on Roundabout or on Main Road", 
    "9": "100000000"}, inplace=True)

    df["Hit_Object_in_Carriageway"].replace({"0": "None", "1": "Previous Accident", "2": "Road Works", 
    "4": "Parked Vehicles", "5": "Bridge (Roof)", "6": "Bridge (Side)", "7": "Bollard or Refuge", 
    "8": "Open Door of Vehicle", "9": "Central Island of Roundabout", "10": "Kerb", "11": "Other Object", 
    "12": "Any Animal (Except Ridden Horse)", "99": "100000000"}, inplace=True)

    df["Vehicle_Leaving_Carriageway"].replace({"0": "Did Not Leave Carriageway", "1": "Nearside", 
    "2": "Nearside and Rebounded", "3": "Straight Ahead at Junction", "4": "Offside on to Central Reservation", 
    "5": "Offside on to Central reservation + Rebounded", "6": "Offside-Crossed Central Reservation", "7": "Offside", 
    "8": "Offside and Rebounded", "9": "100000000"}, inplace=True)

    df["Hit_Object_off_Carriageway"].replace({"0": "None", "1": "Road Sign or Traffic Signal", "2": "Lamp Post", 
    "3": "Telegraph or Electricity Pole", "4": "Tree", "5": "Bus Stop or Bus Shelter", "6": "Central Crash Barrier", 
    "7": "Near/Offside Crash Barrier", "8": "Submerged in Water", "9": "Entered Ditch", "10": "Other Permanent Object", 
    "11": "Wall or Fence", "99": "100000000"}, inplace=True)

    df["1st_Point_of_Impact"].replace({"0": "Did Not Impact", "1": "Front", "2": "Back", 
    "3": "Offside", "4": "Nearside", "9": "100000000"}, inplace=True)

    df["Was_Vehicle_Left_Hand_Drive?"].replace({"1": "No", "2": "Yes", "9": "100000000"}, inplace=True)

    df["Journey_Purpose_of_Driver"].replace({"1": "Journey as Part of Work", "2": "Commuting to/from Work", 
    "3": "Taking Pupil to/from School", "4": "Pupil Riding to/from School", "5": "Other", "6": "100000000", 
    "15": "Other"}, inplace=True)

    df["Age_Band_of_Driver"].replace({"1": "0-5", "2": "6-10", "3": "11-15", 
    "4": "16-20", "5": "21-25", "6": "26-35", "7": "36-45", "8": "46-55", "9": "56-65", 
    "10": "66-75", "11": "Over 75"}, inplace=True)

    df["Propulsion_Code"].replace({"1": "Petrol", "2": "Heavy Oil", 
    "3": "Electric", "4": "Steam", "5": "Gas", "6": "Petrol/Gas (LPG)", 
    "7": "Gas/Bi-fuel", "8": "Hybrid Electric", "9": "Gas Diesel", "10": "New Fuel Technology", 
    "11": "Fuel Cells", "12": "Electric Diesel"}, inplace=True)

    df["Accident_Severity"].replace({"1": "Fatal", "2": "Serious", "3": "Slight"}, inplace=True)

    df["Pedestrian_Crossing-Human_Control"].replace({"0": "None within 50 Metres", 
    "1": "Control by School Crossing Patrol", "2": "Control by Other Authorised Person", "9": "100000000"}, inplace=True)

    df["Urban_or_Rural_Area"].replace({"1": "Urban", "2": "Rural", "3": "Unallocated"}, inplace=True)

    df["Did_Police_Officer_Attend_Scene_of_Accident"].replace({"1": "Yes", "2": "No", "3": "No"}, inplace=True)

    df["Casualty_Class"].replace({"1": "Driver or Rider", "2": "Passenger", "3": "Pedestrian"}, inplace=True)

    df["Sex_of_Casualty"].replace({"1": "Male", "2": "Female", "9": "100000000"}, inplace=True)

    df["Casualty_Severity"].replace({"1": "Fatal", "2": "Serious", "3": "Slight"}, inplace=True)

    df["Car_Passenger"].replace({"0": "Not Car Passenger", "1": "Front Seat Passenger", 
    "2": "Rear Seat Passenger", "9": "100000000"}, inplace=True)

    df["Casualty_Home_Area_Type"].replace({"1": "Urban Area", "2": "Small Town", "3": "Rural"}, inplace=True)

    df["Driver_Home_Area_Type"].replace({"1": "Urban Area", "2": "Small Town", "3": "Rural"}, inplace=True)

    return df
