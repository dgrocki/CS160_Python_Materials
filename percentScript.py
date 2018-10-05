total = 0.0;                    #declare variable to hold total data points
bad = 0.0;                      #declare variable to hold bad data points

filename = input("Please enter your filename with the extention (ex. out.txt): ")

file = open(filename, "r")      #open our file 

for line in file:               #for every line in the file (line is a variable that is created in the scope of this loop and will automatically be given the next line on each iteration) 
    total+=1;                   #increment total number of lines
    if float(line) > 4.8:       #if we have a bad datapoint
        bad+=1                  #increment bad datapoints

percent = '%.2f'%(bad*100/total)    #calculate percent and truncate extra digits

print("Total Data Points: " + str(total))
print("Total Points Over 4.8 degrees: " + str(bad))
print( str(percent) + "% of the time the ramp angle was over 4.8 degrees")
