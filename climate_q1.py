import matplotlib.pyplot as plt
import sqlite3
        
years = []
co2 = []
temp = []

# Define connection and cursor
connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

# Fetch values from database
cursor.execute("SELECT * FROM ClimateData")
results = cursor.fetchall()

# Populate Python lists with corresponding values
for record in results:
    years.append(record[0])
    co2.append(record[1])
    temp.append(record[2])


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 

