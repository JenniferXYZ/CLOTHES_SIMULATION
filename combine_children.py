import maya.cmds as cmds
import sys
import os
import fnmatch


def get_working_dir () :
	global wrspFldr
	
	#Get working directory and script location
	sceneName = cmds.file( q = True, sn = True)
	print (sceneName)
	if os.path.exists(sceneName):
	   # current folder    
	   wrspFldr = os.path.dirname(sceneName)
	   print (wrspFldr + "yay")
	else:
	   print "Cannot find current project directory" 

def process(fn): 

	
	cmds.file(wrspFldr + '//Models/man/raw/' + fn + '.obj', i = True, type = 'OBJ', iv = True, ra = True, ns = fn, mnc = False)

	# print (fn)
	# n = fn + ":Mesh"
	# print (n)

	# n = n.replace('"', "'") 

	tempn = fn + ":Mesh"
	cmds.select(tempn, r = True)

	cmds.xform(cp = True)
	cmds.move(0,0,0, rpr = True)
	cmds.rotate(-90, rotateX = True)
	cmds.scale(3,3,3, scaleXYZ = True)
	cmds.makeIdentity( apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

	cmds.file(wrspFldr + '//Models/man/process_1/' + fn + '_new.obj', f = True, op = "v = 0;", typ = "OBJexport", pr = True, es = True)

def cleanup(fn) :
	cmds.select(all = True)
	cmds.delete()
	boolfn = cmds.namespace(ex = fn)
	if (boolfn):
		cmds.namespace(rm = fn)







# MAIN FUNCTION
def main():
	
	print("Im here")
	get_working_dir ()

	listOfFiles = os.listdir(wrspFldr + '//Models/man/raw')
	pattern = "*.obj"

	if not listOfFiles:
		print ("no files")
		exit()

	for fp in listOfFiles:
 		if fnmatch.fnmatch(fp,pattern):
 	# fp = "tee_23.obj";
		 	no_ext_fn = os.path.splitext(os.path.basename(fp))[0];
			print(no_ext_fn)
			cleanup(no_ext_fn)
		 	process(no_ext_fn)

 	print ("end")




	
	# get_working_dir ()
	# process()


if __name__ == '__main__':
	main()