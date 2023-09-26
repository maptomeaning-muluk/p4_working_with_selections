import arcpy
import os
gdb_path = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
hist_fc_name = "Wilson_Histdist"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
hist_fc_path = os.path.join(gdb_path,hist_fc_name)
# converting feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_layer")
arcpy.management.MakeFeatureLayer(hist_fc_path, "hist_dist_layer")

arcpy.management.SelectLayerByLocation("restaurant_layer", "WITHIN_A_DISTANCE","hist_dist_layer", "500 feet")
post_count = arcpy.GetCount_management("restaurant_layer")
print(post_count[0])
#apply selection
arcpy.management.SelectLayerByLocation

output_resto_histdist = "Resto_within_500feet"
output_resto_histdist_path = os.path.join(gdb_path,output_resto_histdist)
arcpy.management.CopyFeatures("restaurant_layer", output_resto_histdist_path)
