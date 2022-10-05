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
              Casualty_IMD_Decile = df.Casualty_IMD_Decile.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                  value = ["Most Deprived 10%", "More Deprived 10-20%", "More Deprived 20-30%", "More Deprived 30-40%", 
                           "More Deprived 40-50%", "Less Deprived 40-50%", "Less Deprived 30-40%", "Less Deprived 20-30%", 
                           "Less Deprived 10-20%", "Least Deprived 10%"]                   
              ),
              Towing_and_Articulation = df.Towing_and_Articulation.replace(
                  to_replace = ["0", "1", "2", "3", "4", "5", "9"],
                  value = ["No Tow/Articulation", "Articulated Vehicle", "Double or Multiple Trailer", "Caravan", 
                           "Single Trailer", "Other Tow", "100000000"]
              ), 
              Vehicle_Manoeuvre = df.Vehicle_Manoeuvre.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "99"],
                  value = ["Reversing", "Parked", "Waiting to Go-Held Up", "Slowing or Stopping", "Moving off", "U-Turn", "Turn Left", 
                           "Waiting to Turn Left", "Turn Right", "Waiting to Turn Right", "Changing Lane to Left", "Changing Lane to Right", 
                           "Overtaking Moving Vehicle-Offside", "Overtaking Static Vehicle-Offside", "Overtaking-Nearside", 
                           "Going Ahead Left-Hand Bend", "Going Ahead Right-Hand Bend", "Going Ahead Others", "100000000"]
              ),
              Vehicle_Location-Restricted_Lane = df.Vehicle_Location-Restricted_Lane.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "99"],
                  value = ["On main C'Way-Not in Restricted Lane", "Tram/Light Rail Track", "Bus Lane", "Busway (Including Guided Busway)", 
                           "Cycle Lane (On Main Carriageway)", "Cycleway or Shared Use Footway (Not Part of Main Carriageway)", 
                           "On Lay-By or Hard Shoulder", "Entering Lay-by or Hard Shoulder", "Leaving Lay-by or Hard Shoulder", 
                           "Footway (Pavement)", "Not on Carriageway", "100000000"]                 
              ),
              Junction_Location = df.Junction_Location.replace(
                  to_replace = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  value = ["Not at or Within 20 Metres of Junction", "Approaching Junction or Waiting/Parked at Junction Approach", 
                           "Cleared Junction or Waiting/Parked at Junction Exit", "Leaving Roundabout", "Entering Roundabout", 
                           "Leaving Main Road", "Entering Main Road", "Entering from Slip Road", 
                           "Mid Junction-on Roundabout or on Main Road", "100000000"]                 
              ),
              Hit_Object_in_Carriageway = df.Hit_Object_in_Carriageway.replace(
                  to_replace = ["0", "1", "2", "4", "5", "6", "7", "8", "9", "10", "11", "12", "99"],
                  value = ["None", "Previous Accident", "Road Works", "Parked Vehicles", "Bridge (Roof)", "Bridge (Side)", 
                           "Bollard or Refuge", "Open Door of Vehicle", "Central Island of Roundabout", "Kerb", "Other Object", 
                           "Any Animal (Except Ridden Horse)", "100000000"]                  
              ),
              Vehicle_Leaving_Carriageway = df.Vehicle_Leaving_Carriageway.replace(
                  to_replace = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  value = ["Did Not Leave Carriageway", "Nearside", "Nearside and Rebounded", "Straight Ahead at Junction", 
                           "Offside on to Central Reservation", "Offside on to Central reservation + Rebounded", 
                           "Offside-Crossed Central Reservation", "Offside", "Offside and Rebounded", "100000000"]                  
              ),
              Hit_Object_off_Carriageway = df.Hit_Object_off_Carriageway.replace(
                  to_replace = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "99"],
                  value = ["None", "Road Sign or Traffic Signal", "Lamp Post", "Telegraph or Electricity Pole", "Tree", 
                           "Bus Stop or Bus Shelter", "Central Crash Barrier", "Near/Offside Crash Barrier", 
                           "Submerged in Water", "Entered Ditch", "Other Permanent Object", "Wall or Fence", "100000000"]                  
              ),
              1st_Point_of_Impact = df.1st_Point_of_Impact.replace(
                  to_replace = ["0", "1", "2", "3", "4", "9"],
                  value = ["Did Not Impact", "Front", "Back", "Offside", "Nearside", "100000000"]                      
              ),
              Was_Vehicle_Left_Hand_Drive? = df.Was_Vehicle_Left_Hand_Drive?.replace(
                  to_replace = ["1", "2", "9"],
                  value = ["No", "Yes", "100000000"]                      
              ),
              Journey_Purpose_of_Driver = df.Journey_Purpose_of_Driver.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "15"],
                  value = ["Journey as Part of Work", "Commuting to/from Work", "Taking Pupil to/from School", 
                           "Pupil Riding to/from School", "Other", "100000000", "Other"]
              ),
              Age_Band_of_Driver = df.Age_Band_of_Driver.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
                  value = ["0-5", "6-10", "11-15", "16-20", "21-25", "26-35", "36-45", "46-55", "56-65", "66-75", "Over 75"]
              ),
              Propulsion_Code = df.Propulsion_Code.replace(
                  to_replace = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                  value = ["Petrol", "Heavy Oil", "Electric", "Steam", "Gas", "Petrol/Gas (LPG)", "Gas/Bi-fuel", "Hybrid Electric", 
                           "Gas Diesel", "New Fuel Technology", "Fuel Cells", "Electric Diesel"]
              ),
              Accident_Severity = df.Accident_Severity.replace(
                  to_replace = ["1", "2", "3"],
                  value = ["Fatal", "Serious", "Slight"]
              ),
              Pedestrian_Crossing-Human_Control = df.Pedestrian_Crossing-Human_Control.replace(
                  to_replace = ["0", "1", "2", "9"],
                  value = ["None within 50 Metres", "Control by School Crossing Patrol", "Control by Other Authorised Person", "100000000"]
              ),
              Urban_or_Rural_Area = df.Urban_or_Rural_Area.replace(
                  to_replace = ["1", "2", "3"]
                  value = ["Urban", "Rural", "Unallocated"]
              ),
              Did_Police_Officer_Attend_Scene_of_Accident = df.Did_Police_Officer_Attend_Scene_of_Accident.replace(
                  to_replace = ["1", "2", "3"],
                  value = ["Yes", "No", "No"]
              ),
              Casualty_Class = df.Casualty_Class.replace(
                  to_replace = ["1", "2", "3"],
                  value = ["Driver or Rider", "Passenger", "Pedestrian"]
              ),
              Sex_of_Casualty = df.Sex_of_Casualty.replace(
                  to_replace = ["1", "2", "9"],
                  value = ["Male", "Female", "100000000"]                  
              ),
              Casualty_Severity = df.Casualty_Severity.replace(
                  to_replace = ["1", "2", "3"],
                  value = ["Fatal", "Serious", "Slight"]                    
              ),
              Car_Passenger = df.Car_Passenger.replace(
                  to_replace = ["0", "1", "2", "9"],
                  value = ["Not Car Passenger", "Front Seat Passenger", "Rear Seat Passenger", "100000000"]                  
              ),
              Casualty_Home_Area_Type = df.Casualty_Home_Area_Type.replace(
                  to_replace = ["1", "2", "3"],
                  value = ["Urban Area", "Small Town", "Rural"]                              
              ),
               Driver_Home_Area_Type = df.Driver_Home_Area_Type.replace(
                  to_replace = ["1", "2", "3"],
                  value = ["Urban Area", "Small Town", "Rural"]                              
              )             
          )

    return df
