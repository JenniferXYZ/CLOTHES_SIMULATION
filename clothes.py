import maya.cmds as cmds
import os.path
import sys


#Global Variable
filename = "test"

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
	 


def import_obj () :

	#import obj files  
	cmds.file( wrspFldr + '//' + filename + '.obj', i = True, type = 'OBJ', iv = True, ra = True, ns = filename, mnc = True)
	
	tempfn = filename + ":Mesh"

	cmds.select(tempfn,r = True)

	#center the pivot and freeze transformation

	cmds.xform(cp = True)
	cmds.move(0,0,0, rpr = True)
	cmds.rotate(-90, rotateX = True)
	cmds.scale(3,3,3, scaleXYZ = True)
	cmds.makeIdentity( apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)


#Object_List is a list of strings
def modify_tex () :

	#create and assign texture
	textureA = cmds.shadingNode("lambert", asShader = True, name = "TextureA")
	cmds.setAttr(textureA + ".color", 0.5,0.78,0.28)#grey
	textureASG = cmds.sets( renderable = True, noSurfaceShader = True, empty = True, name = 'TextureASG')

	#get all objects in scene
	# cmds.select(ado = True)
	
	# global Object_List
	# Object_List = cmds.ls(selection = True)
	cmds.select(tempfn, r = True)	
	cmds.defaultNavigation(connectToExisting = True, source = "TextureA", destination = "TextureASG")
	cmds.sets(e = True, forceElement = "TextureASG")

	# for item in Object_List :
	# 	cmds.select(item,r = True)
	# 	cmds.defaultNavigation(connectToExisting = True, source = "TextureA", destination = "TextureASG")
	# 	cmds.sets(e = True, forceElement = "TextureASG")

# def sewing_pieces() :
# 	cmds.polyUnite(Object_List, n = 'result')

# def export_fbx() :
# 	# cmds.select(ado = True)
	cmds.select(tempfn, r = True)	
	cmds.file(wrspFldr + '//' + filename + '.fbx', f = True, op = "v = 0;", typ = "FBX export", pr = True, es = True)


def cleanup(fn) :
	cmds.select(all = True)
	cmds.delete()
	boolfn = cmds.namespace(ex = fn)
	if (boolfn):
		cmds.namespace(rm = fn)



# MAIN FUNCTION
def main():
	
	# get_working_dir()
	cleanup(filename)
	# import_obj()
	# double_sided()
	modify_tex()
	# sewing_pieces()
	export_fbx()
	print "Here"


if __name__ == '__main__':
	main()