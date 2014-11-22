# Project:		mossPi
# Author:		Cecil O. Almonte (Cecilomar Design, Inc)
# Contact:		info@cecilomar.com
# Website:		http://www.cecilomar.com/
# GitHub:		https://github.com/cecilomar/mossPi.git
# Description:	Automatic Irrigation System for Raspberry Pi
import time


# Minimum Humidity: Minimum amount of humidity allowed in the soil.
min_humidity = 50

# Maximum Humidity: Maximum amount of humidity allowed in the soil.
max_humidity = 90

# Irrigation Time: for how long will the irrigation sytem run?
irrigation_time = 10

# Messages:
soil_status_ok = "Good"
soil_status_dry = "Dry"
soil_status_sat = "Saturated"


print("\n")
print("######################################################################")
print("mossPi START #########################################################")
print("######################################################################")
print("\n")


print("Getting Soil Humidity Readings...")
print("\n")
# Get Soil Humidity value from sensors
# [CODE] 


humidity = 49 #simulated
print("Humidity:")
print(humidity)
print("\n")


print("Sending humidity report to database...")
# [CODE] 
print("\n")


print("Soil Status:")

if humidity >= min_humidity and humidity <= max_humidity:
	print(soil_status_ok)
if humidity > max_humidity:
	print(soil_status_sat)
if humidity < min_humidity:
	print(soil_status_dry);
	print("\n")

	# START Irrigation
	# [CODE] 
	print("Irrigation Initiated")
	print("\n")

	# Wait irrigation_time (seconds)
	print("Irrigating for %d seconds" % irrigation_time)

	irrigation_time_left = irrigation_time
	while irrigation_time_left != 0:
		time.sleep(1)
		irrigation_time_left -= 1
		print("%s Seconds left..." % irrigation_time_left)
	
	# STOP Irrigation
	# [CODE] 
	print("\n")
	
	print("Irrigation Secured")
	print("\n")
	
	print("Sending irrigation report to database...")
	# [CODE] 
	
print("\n")

print("\n")
print("######################################################################")
print("mossPi END ###########################################################")
print("######################################################################")
print("\n")
