counties = ["Arapahoe","Denver","Jefferson"]

# Simple if
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# If with and
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
    
# If with or
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
    
# When you run the following code, what is printed to the screen? 

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
    
#for county in counties:
#    print(county)
    
#for i in range(len(counties)):
#    print(counties[i])

#for county, voters in counties_dict.items():
#    print(f'{county} county has {voters} voters.')    