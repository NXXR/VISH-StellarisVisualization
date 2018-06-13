# parseSave.py
#
# script to transform savegame-file into JSON file
# INPUT:    Stellaris gamestate file (filepath as command-line argument)
# OUTPUT:   JSON file at filepath/JSONdata/<IngameDateOfSave>.JSON

import sys
import re
import json
import os
from pathlib import Path

# import Regular Expressions Library
import RegExLib

# read file path out of command-line argument, throw exception if it doesn't exist
if len(sys.argv) < 2: raise NameError("File path missing (command-line argument)")
filePath = Path(sys.argv[1])
if not filePath.is_file():
    raise NameError("Error in file path: " + sys.argv[1])

# open file, read content into string and close file again
file = open(sys.argv[1], "r")
fileContent = file.read()
file.close()

# init output dict
output = {}

# extract date of save
match = RegExLib.saveDate.search(fileContent)
if match:
    output.update({"date" : match.group(1)})
else: raise NameError("Save Date not found")

# extract galactic_object array
galactic_objectArray = RegExLib.galactic_objectArray.search(fileContent)
if not galactic_objectArray: raise NameError("Galactic Object List not found")

# extract each galactic_object & index
galactic_objectMatch = RegExLib.galactic_object.findall(galactic_objectArray.group(0))
galactic_object = []
for (index, content) in galactic_objectMatch:

    # extract coordinates into sub-dict
    coordinateMatch = RegExLib.system_coordinate.search(content)
    coordinate = {"x" : coordinateMatch.group(1), "y" : coordinateMatch.group(2)}

    # extract name
    name = RegExLib.system_name.search(content).group(1)
    if RegExLib.specialName.search(name):   # handle names with NAME_
        name = name[5 : len(name)]          # cut off NAME_
        name = name.replace("_", " ")       # replace _ with blank

    # extract planets into sub-list
    planets = RegExLib.system_planets.findall(content)

    # extract hyperlanes into sub-list
    hyperlanes = RegExLib.system_hyperlane.findall(
        RegExLib.system_hyperlaneSection.search(content).group(0)  # match of hyperlane sub-section
    )

    # extract starbase
    starbase = RegExLib.system_starbase.search(content).group(1)
    if starbase == "4294967295":    # handle non starbases
        starbase = None             # replace with None

    # extract fleet_presence into sub-list
    fleet_presence = RegExLib.system_fleetPresences.search(content)
    if fleet_presence:
        fleet_presence = re.findall("\d+", fleet_presence.group(1))
    else:
        fleet_presence = None

    # extract bypasses into sub-list
    bypasses = RegExLib.system_bypasses.search(content)
    if bypasses:
        bypasses = re.findall("\d+", bypasses.group(1))
    else:
        bypasses = None

    # build galactic_object item
    galactic_object.append({
        "coordinate"    : coordinate,
        "name"          : name,
        "planets"       : planets,
        "hyperlanes"    : hyperlanes,
        "starbase"      : starbase,
        "fleet_presence": fleet_presence,
        "bypasses"      : bypasses
    })
output.update({"system" : galactic_object})  # merge galactic_objects as "system" into output

# extract starbases array
starbasesArray = RegExLib.starbasesArray.search(fileContent)
if not starbasesArray: raise NameError("Starbase List not found")

# extract each starbase & index
starbaseMatch = RegExLib.starbase.findall(starbasesArray.group(0))
starbase = []
for (index, content) in starbaseMatch:

    # extract level
    level = RegExLib.starbase_level.search(content).group(1)
    level = level[15 : len(level)]  # cut off starbase_level_

    # extract system
    system = RegExLib.starbase_system.search(content).group(1)

    # extract owner
    owner = RegExLib.starbase_owner.search(content).group(1)

    # build starbase item
    starbase.append({
        "level"     : level,
        "system"    : system,
        "owner"     : owner
    })
output.update({"starbase" : starbase})  # merge starbases into output

# extract planets array
planetsArray = RegExLib.planetsArray.search(fileContent)
if not planetsArray: raise NameError("Planet List not found")

# extract each planet & index
planetMatch = RegExLib.planet.findall(planetsArray.group(0))
planet = []
for (index, content) in planetMatch:

    # extract name
    name = RegExLib.planet_name.search(content).group(1)
    if RegExLib.specialName.search(name):   # handle names with NAME_
        name = name[5 : len(name)]          # cut off NAME_
        name = name.replace("_", " ")       # replace _ with blank

    # extract size
    size = RegExLib.planet_size.search(content).group(1)

    # extract bombardment date
    lastBombardment = RegExLib.planet_bombardment.search(content).group(1)
    if lastBombardment == "1.01.01":    # handle no bombardment
        lastBombardment = None          # replace with None

    # extract controller
    controller = RegExLib.planet_controller.search(content)
    if controller:
        controller = controller.group(1)
    else:
        controller = None

    # extract and count tiles
    tileCount = len(                                            # count elements in
        RegExLib.planet_tiles.findall(                          # matches of tiles in
            RegExLib.planet_tileList.search(content).group(0)   # tile list
        )
    )

    # extract surveyor
    surveyor = RegExLib.planet_surveyor.search(content)
    if surveyor:
        surveyor = surveyor.group(1)
    else:
        surveyor = None

    # extract and count pops
    popCount = RegExLib.planet_pops.search(content)
    if popCount:
        popCount = len(re.findall("\d+", popCount.group(1)))
    else:
        popCount = 0

    # extract colonization date
    colonized = RegExLib.planet_colonized.search(content)
    if colonized:
        colonized = colonized.group(1)
    else:
        colonized = None

    # extract army count
    armyCount = RegExLib.planet_armies.search(content)
    if armyCount:
        armyCount = len(re.findall("\d+", armyCount.group(1)))
    else:
        armyCount = 0

    # build planet item
    planet.append({
        "name"              : name,
        "size"              : size,
        "tile_count"        : tileCount,
        "owner"             : controller,
        "surveyor"          : surveyor,
        "pop_count"         : popCount,
        "army_count"        : armyCount,
        "colonization_date" : colonized,
        "last_bombardment": lastBombardment
    })
output.update({"planet" : planet})  # merge planets into output

########################################################################################################################
# Dump to console (for debug)
#
#json.dump(output, sys.stdout, indent=4)

########################################################################################################################
# Dump to JSON file in "filepath/JSON Data/<date>.json"
if not Path("./JSON Data").is_dir():
    os.mkdir(Path("./JSON Data"))
with open(Path("./JSON Data/" + output["date"] + ".json"), "w") as outputFile:
    json.dump(output, outputFile, indent=4)
    print("File " + outputFile.name + " created")