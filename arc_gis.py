import arcpy
import os

gdb_path = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Selections\ProProject_Selections.gdb"

restaurant_fc_name = "Wilson_Restaurants"
hist_fc_name = "Wilson_Histdist"
crime_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
hist_fc_path = os.path.join(gdb_path,hist_fc_name)
crime_fc_path = os.path.join(gdb_path,crime_fc_name)

arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_layer")
arcpy.management.MakeFeatureLayer(hist_fc_path, "hist_dist_layer")
arcpy.management.MakeFeatureLayer(crime_fc_path, "crime_dist_layer")
arcpy.management.SelectLayerByAttribute("restaurant_layer", "SUBSET_SELECTION", "ALCOHOL = 1")
arcpy.management.SelectLayerByLocation("restaurant_layer", "WITHIN_A_DISTANCE","hist_dist_layer", "1000 feet","SUBSET_SELECTION" )
arcpy.management.SelectLayerByLocation("crime_dist_layer","WITHIN_A_DISTANCE","restaurant_layer","500 feet","SUBSET_SELECTION")
arcpy.management.SelectLayerByAttribute("crime_dist_layer", "SUBSET_SELECTION", "ALCOHOL > 0")

post_count = arcpy.GetCount_management("crime_dist_layer")
print ("The count of alcohol related crimes {}".format(post_count[0]))

