#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: October 31, 2023
#This program makes a map of collsions in nyc!

import folium
import pandas as pd

inF = input('Enter input filename:')
outF = input('Enter output filename:')

collisions = pd.read_csv(inF)
collisions["LATITUDE"] = collisions["LATITUDE"].fillna(0)
collisions["LONGITUDE"] = collisions["LONGITUDE"].fillna(0)

mapCrash = folium.Map(location = [40.768731, -73.964915])

for index, row in collisions.iterrows():
    if row['LATITUDE'] != 0 and row['LONGITUDE'] != 0:
        lat = row["LATITUDE"]
        lon = row["LONGITUDE"]
        name = row["TIME"]
        newMarker = folium.Marker([lat, lon], popup=name)
        newMarker.add_to(mapCrash)

mapCrash.save(outfile=outF)
