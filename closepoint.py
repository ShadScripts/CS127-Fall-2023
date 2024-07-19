#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: October 31, 2023
#This program makes a map of collsions in nyc!

import folium
import pandas as pd

def getData():
    df = input('Enter input filename:')
    return (df)

def getColumnNames():
    latName = input('Whats the column name for Latitude: ')
    lonName = input('Whats the column name for Longitude')
    return (latName, lonName)

def getLocale():
    lat = input('Whats your current latitude')
    lon = input("Whats your current longitude")
    return (lat, lon)


def computeDist(x1, y1, x2, y2):
    d = (x1 - x2)**2 + (y1 - y2)**2
    return (d)

def dotAllPoints(cMap, df, latCol, lonCol):
    for i, row in df.iterrows():
        folium.CircleMarker(location=[row[latCol], row[lonCol]], radius=4, color='red').add_to(cMap)

def markAndFindClosest(cMap, df, latCol, lonCol, cLat, cLon):
    """
    Goes through the list of points, marking each with a circle marker.
    Finds the closest point using the computeDist() function and
    Returns the lat and lon of closest point.
    """

    # Find closest marker:
    df['Dist'] = df[[latCol, lonCol]].apply(lambda row: computeDist(*row, cLat, cLon), axis=1)
    minRow = df[df['Dist'] == df['Dist'].min()]

    # Make a marker for the closest point:
    folium.Marker(location=[float(minRow[latCol]), float(minRow[lonCol])],
                  popup="Closest").add_to(cMap)
    # Make a marker for the starting point
    folium.Marker(location=[cLat, cLon],
                  popup="You Are Here",
                  icon=folium.Icon(color='red')).add_to(cMap)


def writeMap(cMap):
    """
    Writes the inputted map, cMap, to the file specified by the user.
    """
    outF = input('Enter output file: ')
    cMap.save(outfile=outF)


def main():
    dataF = getData()
    latColName, lonColName = getColumnNames()
    lat, lon = getLocale()
    cityMap = folium.Map(location=[lat, lon], tiles='cartodbpositron', zoom_start=11)
    dotAllPoints(cityMap, dataF, latColName, lonColName)
    markAndFindClosest(cityMap, dataF, latColName, lonColName, lat, lon)
    writeMap(cityMap)


if __name__ == "__main__":
    main()