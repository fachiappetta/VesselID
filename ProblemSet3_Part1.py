#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (f'{mountain}, formerly \nknown as "{nickname}" \nis {elevation}\' above sea level.')


#%% Task 2

#assign a variable named dataFolder to the string object that reads “W:\859_data\tri_state" 
dataFolder = "W:\859_data\\tri_state"

#Creates a list object called dataList containing the following string objects:
dataList = ["roads.shp", "road_types.dbf", "naip_imagery.tif"]

#Assigns a variable named userItem and sets it to the string “streams.shp”.
userItem = "streams.shp"

#Adds the userItem string object to the dataList list.
dataList.append(userItem)

#Loops through each item in the dataList list, and for for each object prints 
#the full Windows path of each dataset, created by concatenating the dataFolder
#string with the item in the dataList. 

for item in dataList:
	print(f'{dataFolder}\{item}')
	
#%% Task3

# Creates an empty list variable named userNumbers.
userNumbers = []	
	
#Iterates the following process three times (using the range() function and a for loop):
for i in range(0,3):
	input_int = input("Enter an integer: ") #Uses the input() function to ask the user to “Enter an integer:”.
	userNumbers.append(int(input_int)) #Adds the user supplied integer to the userNumbers list created in 3.1.

userNumbers.sort() #Sorts the userNumbers in ascending numeric order.
print(userNumbers[-1]) #Prints the highest value in the userNumbers, i.e., the last value when sorted, to the interactive window.	
	
#%% Challenge

# Creates an empty list variable named userNumbers.
userNumbers = []	
	
#Iterates the following process three times (using the range() function and a for loop):
for i in range(0,3):
	input_int = input("Enter an integer: ") #Uses the input() function to ask the user to “Enter an integer:”.
	userNumbers.append(int(input_int)) #Adds the user supplied integer to the userNumbers list created in 3.1.

userNumbers.sort(reverse = True) #Sorts the userNumbers in ascending numeric order.
print(userNumbers) #modify it so that it sorts the userNumbers, but this time in descending numeric order, and then prints the entire contents of the list.
	
		

