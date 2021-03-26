Stellaris Savegame Visualization
================================
###### Version 1.0

(PDF version of the visualization poster)[VISH-Sheet.pdf]

#### How-To generate the Visualization ####
1. Move the .sav files from your Stellaris savegame folder to the "Test Files" folder in this directory.
    - if you are using the SaveScoop.py script, you can also set the destination to the "Test Files" folder.
2. Run the processAllSaves.py script
    - the script will:
    1. extract and rename the gamestate files from the .sav archive
    2. parse the gamestate into a .json file located in the new folder "JSON Data"
    3. combine the .json files in superData.json
3. When the script is finished, you can launch the [Visualization.html](Visualization.html)
    - (if no galayx map is diplayed use the slider to update the year)

#### Quickstart ####
This project already comes with a sample superData.json so you can immediately start the [Visualization.html](Visualization.html) to view the sample.

#### How-To use the Visualization ####
- The slider updates the chart with a particular year
- The "Node Color Modification" Radio Buttons allow different coloration of the galaxy.
    - "Countries" categorizes the systems into groups owned by a Country (first 14. Thereafter, minor factions are colored white).
    - "Starbases" paints starbases according to their level into the galaxy (white to red)
    
- The Infobox at the bottom shows available Info on the selected System (Systems can be selected and deselected by clicking on them).
- Systems can be Compared by selecting one normally and the second one while shift is pressed down.

#### Additional Information ####
- The json data structure documentation can be found in the (JSON-Documentation)[JSON-Documentation.md] file.
- The used Regular Expressions can be found in the (RegExLib)[RegExLib.py] file
