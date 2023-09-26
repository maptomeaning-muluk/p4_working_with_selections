# commonly used terms when working with selections

"""
Feature Class: A table containing an attribute field that stores geometry that defines shape of a feature
Feature Layer: An in-memory representation of the data in the feature class
Table : A storage container for rows that contain fields to store data
Table View: An in-memory representation of the data in a table

"""

import arcpy
import os
gdb_path = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"

restaurant_fc_path = os.path.join(gdb_path,restaurant_fc_name)

# converting feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_layer")


#all number of observations
pre_count = arcpy.GetCount_management("restaurant_layer")
print("The number of restaurants in wilson are:{}".format(pre_count[0]))

# selection of attriburtes where alcohol is served
arcpy.management.SelectLayerByAttribute("restaurant_layer", "NEW_SELECTION", "ALCOHOL = 1")
post_count = arcpy.GetCount_management("restaurant_layer")
print ("The restaurants which serve alcohol are {}".format(post_count[0]))

output_alcohol_restaurants = "Wilson_Restaurant_Alcohol"
output_alcohol_restaurants_path = os.path.join(gdb_path,output_alcohol_restaurants)

#converting the feature layer to feature class
arcpy.management.CopyFeatures("restaurant_layer", output_alcohol_restaurants_path)

print("process complete")