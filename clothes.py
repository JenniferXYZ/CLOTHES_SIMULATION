import maya.cmds as cmds
import os.path
import sys


def get_working_dir () :
	#Get working directory and script location
	sceneName = cmds.file( q = True, sn = True)
	print (sceneName)
	if os.path.exists(sceneName):
	   # current folder 
	   wrspFldr = os.path.dirname(sceneName)
	   print (wrspFldr + "yay")
	   #if os.path.exists(wrspFldr+'test.obj'):
	       #print "Mesh exists"
	   #else:
	       #print "Cannot find mesh"
	else:
	   print "Cannot find current project directory" 
	 


def import_obj () :

	#import obj files  
	cmds.file(wrspFldr+'/test.obj', i = True, type = 'OBJ', iv = True, ra = True, ns = 'VR', mnc = True)
	cmds.select('VR:Mesh',r = True)
	cmds.rename('VR:Mesh' ,'Object1')

	#center the pivot and freeze transformation
	cmds.xform(cp = True)
	cmds.move(0,0,0, rpr = True)
	cmds.setAttr('Object1.rx', -90)
	cmds.makeIdentity('Object1', apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

	#reduce dimension
	cmds.select('Object1',r = True)
	cmds.polyReduce(ver = 1, p = 60.0)

	#UV editor better use GUI


# MAIN FUNCTION
def main():
	get_working_dir()
	import_obj()





if __name__ == '__main__':
	main()