import maya.cmds as cmds
import sys
import os

#Get working directory and script location
sceneName = cmds.file( q = True, sn = True)
print (sceneName)
if os.path.exists(sceneName):
   # current folder 
   wrspFldr = os.path.dirname(sceneName)
else:
   print "Cannot find current project directory" 


 
def psource(module):

    file = os.path.basename( module )
    dir = os.path.dirname( module )

    toks = file.split( '.' )
    modname = toks[0]

    # Check if dirrectory is really a directory
    if( os.path.exists( dir ) ):

    # Check if the file directory already exists in the sys.path array
        paths = sys.path
        pathfound = 0
        for path in paths:
            if(dir == path):
                pathfound = 1

    # If the dirrectory is not part of sys.path add it
        if not pathfound:
            sys.path.append( dir )

    # exec works like MEL's eval but you need to add in globals()
    # at the end to make sure the file is imported into the global
    # namespace else it will only be in the sc ope of this function
    exec ('import ' + modname) in globals()

    # reload the file to make sure its up to date
    exec( 'reload( ' + modname + ' )' ) in globals()

    # This returns the namespace of the file imported
    return modname

# When you import a file you must give it the full path
psource( wrspFldr + '/combine_children.py' )

combine_children.main()