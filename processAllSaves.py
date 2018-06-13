# processAllSaves.py
#
# script to unzip .sav files and rename gamestate to date

import os
import zipfile
import subprocess
import sys
import json

# unzip saves and call parseSave.py to generate JSON Data
for file in os.listdir("./Test Files"):
    if file.endswith(".sav"):                                                                                           # find all .sav files in directory
        filename = file[9:19] + ".stellarissave"                                                                        # extract date
        zipref = zipfile.ZipFile("./Test Files/"+file, "r")
        zipref.extract("gamestate", "./Test Files")                                                                     # unzip gamestate file
        zipref.close()
        os.replace("./Test Files/gamestate", "./Test Files/" + filename)                                                # rename/replace file to <date>.stellarissave
        print(file, "extracted and renamed to:", filename)
        returnCode = subprocess.run([sys.executable, "parseSave.py", "./Test Files/" + filename]).returncode            # run parseSave with file
        if returnCode == 0:
            print(filename, "successfully parsed")
        else: raise NameError("Save parse returned: " + str(returnCode) + "instead of 0");
        print("\n")

# merge JSON Data into superData.json containing all data
superfile = open("./JSON Data/superData.json", "w", encoding="utf-8")
superdata = []
for file in os.listdir("./JSON Data"):
    if file.endswith(".json") and not file == "superData.json":
        with open("./JSON Data/" + file, "r") as inputfile:
            superdata.append(json.load(inputfile))
            print(file, "dumped")
json.dump(superdata, superfile, indent=2)
print("Superfile created")
superfile.close()