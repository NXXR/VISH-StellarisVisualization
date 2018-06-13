# RegExLib.py
#
# Collection of Regular Expressions used to dissect and reorganize Stellaris gamestate file

import re

# RegEx matching date of the save
saveDate = re.compile("\ndate=\"(\d+).\d+.\d+\"")
# ->    group1  date

# RegEx to check if name contains NAME_ and _
specialName = re.compile("NAME_")

########################################################################################################################
# RegEx matching galactic_object array
galactic_objectArray = re.compile("\ngalactic_object=[\s\S]+?\}\n\}")

# RegEx matching all galactic_object entries in array
galactic_object = re.compile("\n\t(\d+)=\{([\s\S]+?)\n\t\}")
# ->    group1  galactic_object index
# ->    group2  galactic_object content

# RegEx matching coordinates in galactic_object content
system_coordinate = re.compile("coordinate=\{\s+x=([-.\d]+)\s+y=([-.\d]+)")
# ->    group1  x coordinate
# ->    group2  y coordinate

# RegEx matching names in galactic_object content
system_name = re.compile("name=\"([\s\S]+?)\"")
# ->    group1  name

# RegEx matching planets in galactic_object content
system_planets = re.compile("planet=(\d+)")
# ->    group1  planet index

# RegEx matching hyperlane sub-section in galactic_object content
system_hyperlaneSection = re.compile("hyperlane=\{([\s\S]+?)\n\t\t\}")
# ->    group1  hyperlane sub-section content

# RegEx matching hyperlanes in hyperlane sub-section content
system_hyperlane = re.compile("{\s+to=(\d+)[\s\S]+?\n\t\t\t\}")
# ->    group1  hyperlane destination

# RegEx matching starbase in galactic_object content
system_starbase = re.compile("starbase=(\d+)")
# ->    group1  starbase index (4294967295 = no starbase)

# RegEx matching fleet_presence list
system_fleetPresences = re.compile("fleet_presence=\{\s+((?:\d+ )*)\s+\t\t\}")
# ->    group1  list of fleet indices separated by space

# RegEx matching bypasses list
system_bypasses = re.compile("bypasses=\{\s+((?:\d+ )*)\s+\t\t\}")
# ->    group1  list of bypass indices separated by space

########################################################################################################################
# RegEx matching starbases array
starbasesArray = re.compile("\nstarbases=[\s\S]+?\}\n\}")

# RegEx matching starbase entries in array
starbase = re.compile("\n\t(\d+)=\{([\s\S]+?)\n\t\}")
# ->    group1  starbase index
# ->    group2  starbase content

# RegEx matching level in starbase content
starbase_level = re.compile("level=\"([\w_]+)\"")
# ->    group1  level name

# RegEx matching system in starbase content
starbase_system = re.compile("system=(\d+)")
# ->    group1  home system index

# RegEx matching owner in starbase content
starbase_owner = re.compile("owner=(\d+)")
# ->    group1  owner country index

########################################################################################################################
# RegEx matching planet array
planetsArray = re.compile("\nplanet=\{[\s\S]+?\n\}")

# RegEx matching planet entries in array
planet = re.compile("\n\t(\d+)=\{([\s\S]+?orbital_deposit_tile=\d+)\t\}")
# ->    group1  planet index
# ->    group2  planet content

# RegEx matching name in planet content
planet_name = re.compile("\n\t\tname=\"([\s\S]+?)\"")
# ->    group1  planet name

# RegEx matching planet_size in planet content
planet_size = re.compile("planet_size=(\d+)")
# ->    group1  planet size

# RegEx matching last_bombardment in content
planet_bombardment = re.compile("last_bombardment=\"([\d.]+)\"")
# ->    group1  planet bombardment date

# RegEx matching controller in content
planet_controller = re.compile("controller=(\d+)")
# ->    group1  planet controller

# RegEx matching tiles array in content
planet_tileList = re.compile("tiles=\{[\s\S]+?\n\t\t\}")

# RegEx matching tile entries in array
planet_tiles = re.compile("\d+=\{[\s\S]+?\n\t\t\t\}")

# RegEx matching surveyed_by in content
planet_surveyor = re.compile("surveyed_by=(\d+)")
# ->    group1  planet surveyor

# RegEx matching pop list in content
planet_pops = re.compile("pop=\{\s+((?:\d+ )*)\s+\t\t\}")
# ->    group1  list of pops separated by space

# RegEx matching colonize_date in content
planet_colonized = re.compile("colonize_date=\"([\d.]+)\"")
# ->    group1  planet colonization date

# RegEx matching army list in content
planet_armies = re.compile("army=\{\s+((?:\d+ )*)\s+\t\t\}")
