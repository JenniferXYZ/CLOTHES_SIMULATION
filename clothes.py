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
	cmds.file( wrspFldr + '//' + filename + '.obj', i = True, type = 'OBJ', iv = True, ra = True, ns = 'VR', mnc = True)
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

'''buggy'''
def double_sided() :
	cmds.select('Object1',r = True)
	dup = cmds.duplicate('Object1')
	cmds.rename('Object1_dup')
	cmds.select('Object1_dup',r = True)
	cmds.polyNormal(normalMode = 0, ch = True)
	#Now we have two objects, Object1 and Object1_dup
	#Needs to assign texture to both


#Object_List is a list of strings
def modify_tex () :

	#create and assign texture
	textureA = cmds.shadingNode("lambert", asShader = True, name = "TextureA")
	cmds.setAttr(textureA + ".color", 0.5,0.78,0.28)#grey
	textureASG = cmds.sets( renderable = True, noSurfaceShader = True, empty = True, name = 'TextureASG')

	#get all objects in scene
	cmds.select(ado = True)
	Object_List = cmds.ls(selection = True)

	for item in Object_List :
		cmds.select(item,r = True)
		cmds.defaultNavigation(connectToExisting = True, source = "TextureA", destination = "TextureASG")
		cmds.sets(e = True, forceElement = "TextureASG")


def export_fbx() :
	cmds.select(ado = True)
	cmds.file(wrspFldr + '//' + filename + '.fbx', f = True, op = "v = 0;", typ = "FBX export", pr = True, es = True)



# MAIN FUNCTION
def main():
	
	#get_working_dir()
	#import_obj()
	# double_sided()


	# modify_tex()
	export_fbx()
	print "Here"


if __name__ == '__main__':
	main()