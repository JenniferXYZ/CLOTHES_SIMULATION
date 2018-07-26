import json
import sys
import os





def read_func() :
	json_data = open('C:/Users/Jennifer Zhang/Documents/CLOTHES_SIMULATION/textureData.json')
	data = json.load(json_data)

	print(data)

	json_data.close()


	# target = json.loads("C:/Users/Jennifer Zhang/Documents/CLOTHES_SIMULATION/textureData.json")


	print ("hi")
 




def main() :
	read_func()

if __name__ == '__main__':
	main()