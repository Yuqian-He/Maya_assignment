from maya import cmds
import random
import os
import os

def path(Path) :
    # Get the current working directory of the script
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, Path)
    return file_path

#create function
def creatObjects(mode, numObjects=5):
    objList=[]

    # create a number of objects of the given type
    for n in range(numObjects):
        if mode == 'Type01':
            obj=cmds.file(path("modeling\Jerry Perkins Gear 1.obj"), i=True, options="mo=1;lo=1", pr=True,namespace='Type1_', returnNewNodes=True)
        elif mode == 'Type02':
            obj=cmds.file(path("modeling\Jerry Perkins Gear 2.obj"), i=True, options="mo=1;lo=1", pr=True,namespace='Type1_', returnNewNodes=True)
        elif mode == 'Type03':
            obj=cmds.file(path("modeling\Jerry Perkins Gear 3.obj"), i=True, options="mo=1;lo=1", pr=True,namespace='Type1_', returnNewNodes=True)
        elif mode == 'Type04':
            obj=cmds.file(path("modeling\Jerry Perkins Gear 4.obj"), i=True, options="mo=1;lo=1", pr=True,namespace='Type1_', returnNewNodes=True)
        elif mode == 'Type05':
            obj=cmds.file(path("modeling\Jerry Perkins Gear 5.obj"), i=True, options="mo=1;lo=1", pr=True,namespace='Type1_', returnNewNodes=True)
        elif mode == 'Type06':
            obj=cmds.file(path("modeling\Jerry Perkins Gear 6.obj"), i=True, options="mo=1;lo=1", pr=True,namespace='Type1_', returnNewNodes=True)
        elif mode == 'Type07':
            obj=cmds.file(path("modeling\Jerry Perkins Gear 7.obj"), i=True, options="mo=1;lo=1", pr=True,namespace='Type1_', returnNewNodes=True)
        elif mode == 'Type08':
            obj=cmds.file(path("modeling\Jerry Perkins Gear 8.obj"), i=True, options="mo=1;lo=1", pr=True,namespace='Type1_', returnNewNodes=True)
        else: cmds.error("I don't know what to create")
        print (obj)
        objList.append(obj[0])

    cmds.select(objList)
    #print(file_path)
    #print (obj)

#random function
def randomize(objList=None, minValue=0, maxValue=10,mode='Absolute',axes='xyz'):
    if objList is None:
        objList=cmds.ls(selection=True)
    
    for obj in objList:
        for axis in axes :
            current=0
            if mode=='Relative' :
                current=cmds.getAttr(obj+'.t%s' % axis)
            val=current+random.uniform(minValue,maxValue)
            cmds.setAttr(obj+'.t%s' % axis, val)

def showWindow() :
    Window()

#maya interface
class Window():
      def __init__(self):
          self.window = "MR_Window"
          self.title = "Generator"
          self.size = (200,400)
        
          #close old window is open
          if cmds.window(self.window, exists = True):
              cmds.deleteUI(self.window, window = True)
              
          #create new window
          self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
          
          cmds.columnLayout(adjustableColumn = True)
          cmds.text(label='Generator Random Gears',font='boldLabelFont')
          cmds.separator(height=9)
          cmds.intSliderGrp( "numObjects",field=True, label='number of objects', minValue=0, maxValue=10, fieldMinValue=0, fieldMaxValue=20, value=1 )
          
          #type of gears
          #cmds.text(label=' type', backgroundColor=(0.42,0.42,0.42), align='left', height=18, recomputeSize=True)
          frame=cmds.frameLayout(label="Choose an object type")
          column = cmds.gridLayout(numberOfColumns=4,cellWidth=80, cellHeight=20)
          cmds.radioCollection("objectCreationType")
          cmds.radioButton(label="Type01")
          cmds.radioButton(label="Type02", select=True)
          cmds.radioButton(label="Type03")
          cmds.radioButton(label="Type04")
          cmds.radioButton(label="Type05")
          cmds.radioButton(label="Type06")
          cmds.radioButton(label="Type07")
          cmds.radioButton(label="Type08")

          #different position of gears
          cmds.setParent(frame)
          cmds.frameLayout(label="Choose your position range")
          cmds.gridLayout(numberOfColumns=4, cellWidth=80)

          cmds.text(label='MIN')
          for axis in 'xyz':
            cmds.floatField("%sAxisFieldMin" % axis,value=random.uniform(0,10))

          cmds.text(label='MAX')
          for axis in 'xyz':
            cmds.floatField("%sAxisFieldMax" % axis,value=random.uniform(0,10))
        
          cmds.setParent(frame)
          cmds.frameLayout(label="Choose your random mode")
          cmds.rowLayout(numberOfColumns=2)
          cmds.radioCollection("randomMode")
          cmds.radioButton(label='Absolute', select=True)
          cmds.radioButton(label='Relative')

          cmds.setParent(frame)
          cmds.separator(height=5)
          cmds.gridLayout(numberOfColumns=2, cellWidth=200)
          #cmds.rowLayout(numberOfColumns=2, columnAlign=(1, 'center'))
          cmds.button(label="Create",align='center',command=onCreateClick)
          cmds.button(label="Randomize",align='center',command=onRandomClick)

          #display new window
          cmds.showWindow()

#create button
def onCreateClick(*args) :
    radio=cmds.radioCollection("objectCreationType", query=True, select=True)
    mode=cmds.radioButton(radio, query=True,label=True)
    numObjects=cmds.intSliderGrp("numObjects",query=True,value=True)

    creatObjects(mode, numObjects)
    onRandomClick()

#random button
def onRandomClick(*args) :
     radio=cmds.radioCollection("randomMode", query=True, select=True)
     mode=cmds.radioButton(radio, query=True,label=True)

     for axis in 'xyz' :
        minval = cmds.floatField("%sAxisFieldMin" % axis, query=True,value=True)
        maxval = cmds.floatField("%sAxisFieldMax" % axis, query=True,value=True)
        randomize(minValue=minval,maxValue=maxval,mode=mode,axes=axis)