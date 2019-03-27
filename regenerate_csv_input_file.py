import os

def createDescCsvFile():
	datasetFolderPath = 'E:\\Thesis\\Skeleton dataset\\NTU RGB+D Dataset\\nturgb+d_skeletons'
	file = open("desc.csv", "w")
	brokenFileList = open("samples_with_missing_skeletons_fixed.txt", "r").read()
	rowData = []
	startFrame = 1
	endFrame = 0
	for i in range(7):
		rowData.append("")
	for f in os.listdir(datasetFolderPath):
		if f not in brokenFileList:
			print("processing file : " + f)
			datasetFilePath = os.path.join(datasetFolderPath, f)
			dataFile = open(datasetFilePath, "r").readlines()
			data = re.findall('[0-9]+', f)
			startFrame = endFrame + 1
			endFrame = endFrame + int(dataFile[0])
			rowData[0] = rowData[0] + str(int(data[0])) + ','
			rowData[1] = rowData[1] + str(int(data[1])) + ','
			rowData[2] = rowData[2] + str(int(data[2])) + ','
			rowData[3] = rowData[3] + str(int(data[3])) + ','
			rowData[4] = rowData[4] + str(int(data[4])) + ','
			rowData[5] = rowData[5] + str(startFrame) + ','
			rowData[6] = rowData[6] + str(endFrame) + ','
	rowData[0] = rowData[0][:-1]
	rowData[1] = rowData[1][:-1]
	rowData[2] = rowData[2][:-1]
	rowData[3] = rowData[3][:-1]
	rowData[4] = rowData[4][:-1]
	rowData[5] = rowData[5][:-1]
	rowData[6] = rowData[6][:-1]
	print(rowData[0])
	for i in range(7):
		file.write(rowData[i] + '\n')
	file.close()
			
def createSklCsvFile_3_25_2():
	datasetFolderPath = 'E:\\Thesis\\Skeleton dataset\\NTU RGB+D Dataset\\nturgb+d_skeletons'
	file = open("skl_2.csv", "w")
	brokenFileList = open("samples_with_missing_skeletons_fixed.txt", "r").read()
	rowData = ""
	lineNumer = 0
	for f in os.listdir(datasetFolderPath):
		if f not in brokenFileList:
			print("processing file : " + f)
			datasetFilePath = os.path.join(datasetFolderPath, f)
			dataFile = open(datasetFilePath, "r").readlines()
			frameCount = int(dataFile[lineNumer])
			lineNumer = lineNumer + 1
			for i in range(frameCount):
				bodyCount = int(dataFile[lineNumer])
				for j in range(bodyCount):
					lineNumer = lineNumer + 2
					if j == 2:
						lineNumer = lineNumer + 25
						break
					jointCount = int(dataFile[lineNumer])
					for k in range(jointCount):
						lineNumer = lineNumer + 1
						jointInfo = dataFile[lineNumer].split()
						rowData = rowData + jointInfo[0] + ',' + jointInfo[1] + ',' + jointInfo[2] + ','
				if bodyCount == 1:
					for h in range(75):
						rowData = rowData + '0' + ','
				lineNumer = lineNumer + 1
				rowData = rowData[:-1]
				file.write(rowData + '\n')
				rowData = ""
			lineNumer = 0
			rowData = ""

def createSklCsvFile_3_25_3():
	datasetFolderPath = 'E:\\Thesis\\Skeleton dataset\\NTU RGB+D Dataset\\nturgb+d_skeletons'
	file = open("skl_3.csv", "w")
	brokenFileList = open("samples_with_missing_skeletons_fixed.txt", "r").read()
	rowData = ""
	lineNumer = 0
	for f in os.listdir(datasetFolderPath):
		if f not in brokenFileList:
			print("processing file : " + f)
			datasetFilePath = os.path.join(datasetFolderPath, f)
			dataFile = open(datasetFilePath, "r").readlines()
			frameCount = int(dataFile[lineNumer])
			lineNumer = lineNumer + 1
			for i in range(frameCount):
				bodyCount = int(dataFile[lineNumer])
				for j in range(bodyCount):
					lineNumer = lineNumer + 2
					jointCount = int(dataFile[lineNumer])
					for k in range(jointCount):
						lineNumer = lineNumer + 1
						jointInfo = dataFile[lineNumer].split()
						rowData = rowData + jointInfo[0] + ',' + jointInfo[1] + ',' + jointInfo[2] + ','
				if bodyCount < 3:
					zeroLineNumber = (3 - bodyCount)*75
					for h in range(zeroLineNumber):
						rowData = rowData + '0' + ','
				lineNumer = lineNumer + 1
				rowData = rowData[:-1]
				file.write(rowData + '\n')
				rowData = ""
			lineNumer = 0
			rowData = ""
			
def samplesWith3SkeletonPerFrame():
	datasetFolderPath = 'E:\\Thesis\\Skeleton dataset\\NTU RGB+D Dataset\\nturgb+d_skeletons'
	file = open("samples_with_3_skeleton_per_frame.txt", "w")
	brokenFileList = open("samples_with_missing_skeletons_fixed.txt", "r").read()
	lineNumer = 1
	for f in os.listdir(datasetFolderPath):
		if f not in brokenFileList:
			datasetFilePath = os.path.join(datasetFolderPath, f)
			dataFile = open(datasetFilePath, "r").readlines()
			bodyCount = int(dataFile[lineNumer])
			if bodyCount > 2:
				print(f)
				file.write(f + '\n')
			
#createDescCsvFile()
#createSklCsvFile()
#samplesWith3SkeletonPerFrame()
#createSklCsvFile_3_25_3()
createSklCsvFile_3_25_2()