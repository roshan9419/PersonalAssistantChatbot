import subprocess
import wmi
import os
import sys
import webbrowser

if os.path.exists('Files and Document') == False:
	os.mkdir('Files and Document')
path = 'Files and Document/'

def isContain(text, list):
	for word in list:
		if word in text:
			return True
	return False

def createFile(text):
	# change the applocation as per your system path
	appLocation = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
	
	if isContain(text, ["ppt","power point","powerpoint"]):
		file_name = "sample_file.ppt"
		appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\POWERPNT.exe"

	elif isContain(text, ['excel','spreadsheet']):
		file_name = "sample_file.xsl"
		appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\EXCEL.EXE"

	elif isContain(text, ['word','document']):
		file_name = "sample_file.docx"
		appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.EXE"

	elif isContain(text, ["text","simple","normal"]): file_name = "sample_file.txt"
	elif "python" in text: file_name = "sample_file.py"
	elif "css" in text:	file_name = "sample_file.css"
	elif "javascript" in text: file_name = "sample_file.js"
	elif "html" in text: file_name = "sample_file.html"
	elif "c plus plus" in text or "c + +" in text: file_name = "sample_file.cpp"
	elif "java" in text: file_name = "sample_file.java"
	elif "json" in text: file_name = "sample_file.json"
	else: return "Unable to create this type of file"

	file = open(path + file_name, 'w')
	file.close()
	subprocess.Popen([appLocation, path + file_name])
	return "File is created.\nNow you can edit this file"

def CreateHTMLProject(project_name='Sample'):

	if os.path.isdir(path + project_name):
		webbrowser.open(os.getcwd() + '/' + path + project_name + "\\index.html")
		return 'There is a same project which is already created, look at this...'
	else:
	    os.mkdir(path + project_name)

	os.mkdir(path+project_name+ '/images')
	os.mkdir(path+project_name+ '/videos')

	htmlContent = '<html>\n\t<head>\n\t\t<title> ' + project_name + ' </title>\n\t\t<link rel="stylesheet" type="text/css" href="style.css">\n\t</head>\n<body>\n\t<p id="label"></p>\n\t<button id="btn" onclick="showText()"> Click Me </button>\n\t<script src="script.js"></script>\n</body>\n</html>'

	htmlFile = open(path+project_name+ '/index.html', 'w')
	htmlFile.write(htmlContent)
	htmlFile.close()

	cssContent = '* {\n\tmargin:0;\n\tpadding:0;\n}\nbody {\n\theight:100vh;\n\tdisplay:flex;\n\tjustify-content:center;\n\talign-items:center;\n}\n#btn {\n\twidth:200px;\n\tpadding: 20px 10px;\n\tborder-radius:5px;\n\tbackground-color:red;\n\tcolor:#fff;\n\toutline:none;border:none;\n}\np {\n\tfont-size:30px;\n}'

	cssFile = open(path+project_name+ '/style.css', 'w')
	cssFile.write(cssContent)
	cssFile.close

	jsContent = 'function showText() {\n\tdocument.getElementById("label").innerHTML="Successfully Created '+ project_name +' Project";\n\tdocument.getElementById("btn").style="background-color:green;"\n}'

	jsFile = open(path+project_name+ '/script.js', 'w')
	jsFile.write(jsContent)
	jsFile.close()

	# change the applocation as per your system path
	appLocation = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
	# subprocess.Popen([appLocation, path + project_name])
	subprocess.Popen([appLocation, path + project_name + "/index.html"])
	subprocess.Popen([appLocation, path + project_name + "/style.css"])
	subprocess.Popen([appLocation, path + project_name + "/script.js"])

	webbrowser.open(os.getcwd() + '/' + path + project_name + "\\index.html")


	return f'Successfully Created {project_name} Project'

