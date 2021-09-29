
#%% PART 2

#Create a dictionary listing the attributes of each vessel listed in the transshipment_vessels file
#Loop through the records in the loitering_events... dataset, and for each 
#vessel observed within a defined geographic region, print information about the vessel.


#%% Task 4.1  Reading in the data and displaying the column headers


#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2 Splitting the header string into a list of column names and extracting index values

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",") #this gives me a /n at the end of imo

#if we want to strip imo---
#converted_list = []
#for element in headerItems:
    #converted_list.append(element.strip())
#print(converted_list)

#List the index of the mmsa, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi") 
name_idx = headerItems.index("shipname") 
fleet_idx = headerItems.index("fleet_name") 

#Print the values
print(mmsi_idx,name_idx,fleet_idx)


#%% Task 4.3 Iterating through the data lines and adding values to a dictionary
#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for line in lineList:
	if line.isnumeric == False or line.startswith(","):
		continue
#Split the data into values
	lines_split = line.split(",")

	#Extract the mmsi value from the list using the mmsi_idx value
	mmsi = lines_split[mmsi_idx]
	#Extract the fleet value
	fleet = lines_split[fleet_idx]
	#Adds info to the vesselDict dictionary
	vesselDict[mmsi] = fleet
	
#%% Task 4.4: Using your dictionary
vesselID = "258799000"

vessel_mmsi = vesselDict.get(vesselID)

print(f'Vessel # {vesselID} flies the flag of {vessel_mmsi}')

	  
	  
#%% TASK 5

	  
#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#List the index of the transshipment_mmsi, starting & ending latitude, and starting longitude
transshipment_mmsi_idx = headerItems.index("transshipment_mmsi") 
starting_latitude_idx = headerItems.index("starting_latitude") 
ending_latitude_idx = headerItems.index("ending_latitude") 
ending_longitude_idx  = headerItems.index("ending_longitude") 
starting_longitude_idx  = headerItems.index("starting_longitude") 

#create set outside of for loop
mmsi_set = set()

#Iterate through all lines (except the header) in the data file:
for line in lineList:
	if line.startswith("t"):
		continue
#Split the data into values
	lines_split = line.split(",")
#Store the transshipment_mmsi, starting & ending latitude, and starting longitude 
#values into their own respective variables (e.g. mmsi = ...)
	transshipment_mmsi = lines_split[transshipment_mmsi_idx]
	starting_latitude = lines_split[starting_latitude_idx]
	ending_latitude = lines_split[ending_latitude_idx]
	ending_longitude = lines_split[ending_longitude_idx]
	starting_longitude = lines_split[starting_longitude_idx]
	
#Examines the starting and ending latitude (the 2nd and 4th columns in the csv) 
#to determine whether the event crosses the equator, passing from the southern hemisphere to the north.
#Examines the starting longitude to see whether it falls between 165°E and 170°E.
	PASS_POINT_LAT = 0 
	LOWER_LIM_ENDING_LONG = 165
	UPPER_LIM_ENDING_LONG = 170
	
	#if starting latitude is less than 0 (southern hem)
	#and ending latitude is greater than 0 (northern hem)
	#and ending long is greater than 165
	#and ending long is greater than 170
	if float(starting_latitude) < PASS_POINT_LAT \
	and float(ending_latitude) > PASS_POINT_LAT \
	and float(ending_longitude) > LOWER_LIM_ENDING_LONG \
	and float(ending_longitude) < UPPER_LIM_ENDING_LONG: 
		mmsi_set.add(transshipment_mmsi)
		
#If both the latitude and longitude constraints are true, then use the value 
#of the transmission_mmsi for the current line to query the vesselsDict 
#created above to print the vessel’s mmsi and its fleet.

if len(mmsi_set) == 0:
    print ("No vessels met criteria")
else:
	for mmsi in mmsi_set:
		mmsi_country = vesselDict.get(mmsi)
		print(f'Vessel #{mmsi} flies the flag of {mmsi_country}')

