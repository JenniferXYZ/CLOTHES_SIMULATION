import maya.cmds as cmds
import os.path
import sys
import json



def get_working_dir () :
	global wrspFldr
	#Get working directory and script location
	sceneName = cmds.file( q = True, sn = True)
	print (sceneName)
	if os.path.exists(sceneName):
	   # current folder    
	   wrspFldr = os.path.dirname(sceneName)
	   # print (wrspFldr + "yay")
	else:
	   print "Cannot find current project directory" 
	 
def load_json() :
	json_data = open(wrspFldr + '/textureData.json')
	global data
	# target to parse
	data = json.load(json_data)
	global item_num
	# number of items
	item_num = len(data)

	json_data.close()
	print("file loaded")



def import_obj (fn,rel_path) :

	#import obj files  
	cmds.file( wrspFldr + '/Models/' + rel_path + fn + '.obj', i = True, type = 'OBJ', iv = True, ra = True, ns = fn, mnc = True)
	

	global tempfn
	tempfn = fn + ":Mesh"

	cmds.select(tempfn,r = True)

	#center the pivot and freeze transformation

	cmds.xform(cp = True)
	cmds.move(0,0,0, rpr = True)
	# cmds.rotate(-90, rotateX = True)
	cmds.scale(3,3,3, scaleXYZ = True)
	cmds.makeIdentity( apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)


#Object_List is a list of strings
def modify_tex (fn,R,G,B) :

	#create and assign texture
	textureA = cmds.shadingNode("lambert", asShader = True, name = "TextureA")
	cmds.setAttr(textureA + ".color", float(R/255),float(G/255),float(B/255))#grey
	textureASG = cmds.sets( renderable = True, noSurfaceShader = True, empty = True, name = 'TextureASG')


	cmds.select(tempfn, r = True)	
	cmds.defaultNavigation(connectToExisting = True, source = "TextureA", destination = "TextureASG")
	cmds.sets(e = True, forceElement = "TextureASG")


def export_fbx(fn) :
# 	# cmds.select(ado = True)
	cmds.select(tempfn, r = True)	

	# need to choose a folder for output
	cmds.file(wrspFldr + '//OUTPUT/' + fn + '.fbx', f = True, op = "v = 0;", typ = "FBX export", pr = True, es = True)


def cleanup(fn) :
	cmds.select(all = True)
	cmds.delete()
	boolfn = cmds.namespace(ex = fn)
	if (boolfn):
		cmds.namespace(rm = fn)



# MAIN FUNCTION
def main():
	print("Start")
	


	get_working_dir()
	load_json()

	for i in range(item_num):
		
		filename = data[i]["name"]	#filename without extension
		path = data[i]["pathfolder"] # reletive to wrspFldr
		R = data[i]["r"]	# range: 0 - 255
		G = data[i]["g"]
		B = data[i]["b"]

		cleanup(filename)
		import_obj(filename,path)
		# print(wrspFldr + '/Models/' + path + filename + '.obj')
		modify_tex(filename,R,G,B)
		export_fbx(filename)

	print ("End")


if __name__ == '__main__':
	main()