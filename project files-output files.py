import os
import shutil
for(dirname,dirs,files) in os.walk('.'):
	for filename in files:
		if filename.endswith('.prproj'):
			if not os.path.exists("project-files"):
				os.makedirs("project-files")
			else:
				shutil.move(filename,"project-files")
		elif filename.endswith('.mp4')|filename.endswith('.mov'):
			if not os.path.exists("output-files"):
				os.makedirs("output-files")
			else:
				shutil.move(filename,"output-files")
		


