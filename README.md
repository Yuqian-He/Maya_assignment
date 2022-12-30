# Overall idea
In order to expedite the process of generating and positioning various mechanical components, including gears, in my Maya scene, I have developed a script utilizing Python. This script consists of two main parts: a modeling component and a Python script component. The primary function of this script is to generate random models from a specified modeling file and randomly position them with different scale within the scene. This script allows me to efficiently create and place these elements in a randomized manner, ultimately saving time and effort in my workflows.

# where to use
In my Maya project, the main scene depicts a corner of an abandoned kitchen. Within this scene, there are numerous abandoned mechanical components scattered across the table, floor, and shelves. To create these components and position them in a realistic and varied manner, I use my script that randomly places them within a designated area within the scene.

# how to start my scripts
Prior to beginning, please download the necessary [modeling file and script](https://github.com/Yuqian-He/Maya_assignment.git) and place them in Maya scripts folder. Once this has been completed, open the Maya scene and navigate to the Script Editor by selecting **Window > General Editors > Script Editor** from the top menu. This will open the Script Editor window. Please remember to change executer source language to Python and type:

```python
import gearsGenerator
import importlib
importlib.reload(gearsGenerator)
gearsGenerator.showWindow()
```

Once you have completed, you may save it to the shelf by selecting **File > Save Script to Shelf** from the top menu of the Script Editor window. You may then provide a meaningful name for the script and save it. This will create a button for the script on the shelf, which you can then click at any time to run the script.

# how to use
My interface consists of four main parts: a field for selecting the desired number of objects, a menu for choosing the type of object, a field for specifying the range of positions to be used, and a toggle for enabling or disabling different random mode. By entering the desired values in these fields and clicking the 'CREATE' or 'RANDOMIZE' button, the user can generate a varying number of objects of the chosen type, with randomly determined positions within the specified range.
