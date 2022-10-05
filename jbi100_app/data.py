import pandas as pd
import plotly.express as px
import numpy as np
import re

def get_data():

    # Read data
    df = pd.read_csv("dataset.csv")

    # Any further data preprocessing can go here
    df = (df
          .assign(
              Hour = [re.findall('([0-9]+)\:[0-9]+', i) for i in df['Time'].tolist()].str[0]
          )
          .replace(
              # Redefine rows with unknown values
              to_replace = ['?', -1, np.nan], 
              replace = 100000000
          )
          .astype('str')
          .assign(
              # Replace numeric values to understandable strings 
              Day_of_Week = df.Day_of_Week.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7"], 
                  value = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
              ),
              1st_Road_Class = df.1st_Road_Class.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6"], 
                  value = ["Motorway", "A(M)", "A", "B", "C", "100000000"]
              ),
              Road_Type = df.Road_Type.replace(
                  to_replace = ["1", "2", "3", "6", "7", "9"], 
                  value = ["Roundabout", "One Way Street", "Dual Carriageway", "Single Carriageway", "Slip road", "100000000"]                  
              ),
              Speed_limit = df.Speed_limit.replace(
                  to_replace = "99",
                  value = "100000000"
              ),
              Junction_Detail = df.Junction_Detail.replace(
                  to_replace = ["0", "1", "2", "3", "5", "6", "7", "8", "9", "99"], 
                  value = ["Not at Junction or within 20 Metres", "Roundabout", "Mini-Roundabout", "T or Staggered Junction", 
                           "Slip Road", "Crossroads", "More than 4 Arms (Not Roundabout)", "Private Drive or Entrance", 
                           "Other Junction", "100000000"]                 
              ),
              Junction_Control = df.Junction_Control.replace(
                  to_replace = ["0", "1", "2", "3", "4", "9"], 
                  value = ["Not at Junction or within 20 Metres", "Authorised Person", "Auto Traffic Signal", "Stop Sign", 
                           "Give Way or Uncontrolled", "100000000"]                         
              ),
              2nd_Road_Class = df.1st_Road_Class.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6"], 
                  value = ["Motorway", "A(M)", "A", "B", "C", "100000000"]
              ),
              Pedestrian_Crossing-Physical_Facilities = df.Pedestrian_Crossing-Physical_Facilities.replace(
                  to_replace = ["0", "1", "4", "5", "7", "8", "9"], 
                  value = ["No Physical Crossing Facilities within 50 Metres", "Zebra", 
                           "Pelican, Puffin, Toucan or Similar Non-Junction Pedestrian Light Crossing", 
                           "Pedestrian Phase at Traffic Signal Junction", "Footbridge or Subway", "Central Refuge", "100000000"]                    
              ),
              Light_Conditions = df.Light_Conditions.replace(
                  to_replace = ["1", "4", "5", "6", "7"],
                  value = ["Daylight", "Darkness-Lights Lit", "Darkness-Lights Unlit", "Darkness-No Lighting", "Darkness-Lighting Unknown"]
              ),
              Weather_Conditions = df.Weather_Conditions.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  value = ["Fine No High Winds", "Raining No High Winds", "Snowing No High Winds", "Fine + High Winds", 
                           "Raining + High Winds", "Snowing + High Winds", "Fog or Mist", "Other", "100000000"]
              ),
              Road_Surface_Conditions = df.Road_Surface_Conditions.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7", "9"],
                  value = ["Dry", "Wet or Damp", "Snow", "Frost or Ice", "Flood over 3cm. Deep", "Oil or Diesel", "Mud", "100000000"]
              ),
              Special_Conditions_at_Site = df.Special_Conditions_at_Site.replace(
                  to_replace = ["0", "1", "2", "3", "4", "5", "6", "7", "9"],
                  value = ["None", "Auto Traffic Signal-Out", "Auto Signal Part Defective", "Road Sign or Marking Defective or Obscured", 
                           "Roadworks", "Road Surface Defective", "Oil or Diesel", "Mud", "100000000"]                  
              ),
              Carriageway_Hazards = df.Carriageway_Hazards.replace(
                  to_replace = ["0", "1", "2", "3", "4", "5", "6", "7", "9"],
                  value = ["None", "Vehicle Load on Road", "Other Object on Road", "Previous Accident", "Dog on Road", 
                           "Other Animal on Road", "Pedestrian In Carriageway-Not Injured", 
                           "Any Animal in Carriageway (Except Ridden Horse)", "100000000"]
              ),
              Age_Band_of_Casualty = df.Age_Band_of_Casualty.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
                  value = ["0-5", "6-10", "11-15", "16-20", "21-25", "26-35", "36-45", "46-55", "56-65", "66-75", "Over 75"]
              ),
              Pedestrian_Location = df.Pedestrian_Location.replace(
                  to_replace = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                  value = ["Not a Pedestrian", "Crossing on Pedestrian Crossing Facility", "Crossing in Zig-Zag Approach Lines", 
                           "Crossing in Zig-Zag Exit Lines", "Crossing Elsewhere within 50m. of Pedestrian Crossing", 
                           "In Carriageway, Crossing Elsewhere", "On Footway or Verge", "On Refuge, Central Island or Central Reservation", 
                           "In Centre of Carriageway-Not on Refuge, Island or Central Reservation", "In Carriageway, Not Crossing", "Others"]                  
              ),
              Pedestrian_Movement = df.Pedestrian_Movement.replace(
                  to_replace = ["0", "1", "2", "3", "4", "5", "6", "7", "8"],
                  value = ["Not a Pedestrian", "Crossing from Driver's Nearside", "Crossing from Nearside-Masked by Parked or Stationary Vehicle", 
                           "Crossing from Driver's Offside", "Crossing from Offside-Masked by Parked or Stationary Vehicle", 
                           "In carriageway, Stationary-Not Crossing (Standing or Playing)", 
                           "In carriageway, Stationary-Not Crossing (Standing or Playing)-Masked by Parked or Stationary Vehicle", 
                           "Walking along in Carriageway, Facing Traffic", "Walking along in Carriageway, Back to Traffic", "Others"]                   
              ),
              Bus_or_Coach_Passenger = df.Bus_or_Coach_Passenger.replace(
                  to_replace = ["0", "1", "2", "3", "4", "9"],
                  value = ["Not a Bus or Coach Passenger", "Boarding", "Alighting", "Standing Passenger", "Seated passenger", "100000000"]
              ),
              Pedestrian_Road_Maintenance_Worker = df.Pedestrian_Road_Maintenance_Worker.replace(
                  to_replace = ["0", "1", "2", "3"],
                  value = ["No/Not Applicable", "Yes", "Not Known", "Probable"]
              )
          )

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
