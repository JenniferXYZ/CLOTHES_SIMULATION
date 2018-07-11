import maya.cmds as cmds
import os.path

#Get working directory and script location
sceneName = cmds.file( q = True, sn = True)
print (sceneName)
if os.path.exists(sceneName):
   # current folder 
   wrspFldr = os.path.dirname(sceneName)
   print (wrspFldr)
else:
   print "Cannot find current project directory" 
   
  
# projectDirectory = cmds.workspace(q = True, rd = True)
#if os.path.exists(wrspFldr + "scripts"):
 #   print(wrspFldr + "script")
#else:
  #  print "Cannot find current project directory" 
  
script_path = os.path.dirname(os.path.abspath( _file_ ))
if os.path.exists(script_path):
   print (script_path)
else:
   print "Cannot find current project directory" 