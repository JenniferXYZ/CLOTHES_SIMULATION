import json
import sys
import os
import maya.cmds as cmds

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
	 

def read_func() :
	json_data = open(wrspFldr + '/textureData.json')
	data = json.load(json_data)
	item_num = len(data)
	# print (item_num)

	for i in range(0,item_num-1):
		path = data[i]["pathfolder"]
		R = data[i]["r"]
		G = data[i]["g"]
		B = data[i]["b"]
		


	# print(data)
	# print(data[0]["r"])

	# print(data[0]["b"])


	# target = json.loads("C:/Users/Jennifer Zhang/Documents/CLOTHES_SIMULATION/textureData.json")


	# print ("hi")
 
	json_data.close()



def main() :
	get_working_dir()
	read_func()

if __name__ == '__main__':
	main()