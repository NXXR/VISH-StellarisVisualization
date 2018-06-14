# processAllSaves.py
#
# script to unzip .sav files and rename gamestate to date

import os
import zipfile
import subprocess
import sys
import json

print("Beginning savegame extraction and parsing:")
# unzip saves and call parseSave.py to generate JSON Data
for file in os.listdir("./Test Files"):

    # find all .sav files in directory
    if file.endswith(".sav"):

        # extract date and build filename <date>.stellarissave
        filename = file[9:19] + ".stellarissave"

        # unzip gamestate file
        zipref = zipfile.ZipFile("./Test Files/"+file, "r")
        zipref.extract("gamestate", "./Test Files")
        zipref.close()

        # rename/replace file to <date>.stellarissave
        os.replace("./Test Files/gamestate", "./Test Files/" + filename)
        print(file, "extracted and renamed to:", filename)

        # run parseSave.py with filepath as parameter
        returnCode = subprocess.run([sys.executable, "parseSave.py", "./Test Files/" + filename]).returncode
        if returnCode == 0:
            print(filename, "successfully parsed")
        else: raise NameError("Save parse returned: " + str(returnCode) + "instead of 0");

print("\n Compiling superfile for Visualization.html")
# merge JSON Data into superData.json containing all data
superfile = open("./JSON Data/superData.json", "w", encoding="utf-8")
superdata = []
for file in os.listdir("./JSON Data"):

    # find all .json files except superData.json itself
    if file.endswith(".json") and not file == "superData.json":
        with open("./JSON Data/" + file, "r") as inputfile:

            # append .json to end of superdata
            superdata.append(json.load(inputfile))
            print(file, "dumped")

# dump superData to file
json.dump(superdata, superfile, indent=2)
print("\n============================================")
print("Superfile created, Visualization.html ready!")
superfile.close()
