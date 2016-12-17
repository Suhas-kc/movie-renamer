import os
import shutil
import json
import re 
import urllib

path = raw_input('Enter the path for the Movies folder: ')

assert os.path.exists(path)
os.chdir(os.path.abspath(path))
rejected = []
done = []

date = re.compile(r'\d\d\d\d')

for folderName , subfolders , fileNames in os.walk('.'):
	for fileName in fileNames:
		extension = fileName[-4:]
		print fileName
		if extension == '.mp4' or extension == '.mkv' or extension == '.avi':
			try:
				mo = date.search(fileName)
				dateOfMovie = mo.group()
				datePos = fileName.find(str(dateOfMovie))
			 
				searchTerm = fileName[:datePos]
				fh = urllib.urlopen('http://www.omdbapi.com/?t=%s' %(searchTerm))
				data = json.load(fh)
				if data['Response'] == 'True':
					proper_name = data['Title']
					shutil.move('./%s/' %(folderName) + fileName,'./%s/' %(folderName) + proper_name + extension)
					print 'File successfully renamed from %s to %s' %(fileName,proper_name+extension)
					done.append(proper_name+extension)

			except:
				rejected.append(fileName)
				print 'File %s couldn\'t be renamed' %(fileName)



print 'done: ', done , '\n'

print 'rejected: ', rejected