#!python3
import os
import shutil


def processfile(suffix, project, author, repo):
    source = open("testproject.kicad_" + suffix, "r")
    destination = open(repo + ".kicad_" + suffix, "w")
    for line in source:
        if '(title "~")' in line:
            destination.write(line.replace("~", project))
        elif '(comment 1 "~")' in line:
            destination.write(line.replace("~", author))
        elif '(comment 2 "~")' in line:
            destination.write(line.replace("~", repo))
        elif "testproject" in line:
            destination.write(line.replace("testproject", repo))
        else:
            destination.write(line)
    source.close()
    destination.close()
    os.remove("testproject.kicad_" + suffix)


project = input("Project Name : ")
author = input("Author Name : ")
repo = input("Github Repo Name (Not URL!) : ")

processfile("pcb", project, author, repo)
processfile("sch", project, author, repo)
processfile("prl", project, author, repo)
processfile("pro", project, author, repo)
source = open("readmetemplate.md", "r")
destination = open("readme.md", "w")
for line in source:
    line = line.replace("projectname", project)
    line = line.replace("authorname", author)
    destination.write(line)
source.close()
destination.close()
os.remove("readmetemplate.md")

shutil.rmtree(".git")
os.system("chmod +x pre-commit")
os.system("git init")
os.rename("pre-commit", ".git/hooks/pre-commit")
os.system("git remote add origin https://github.com/fieldkit/" + repo)
os.system("git add .")
os.system('git commit -a -m "Blank Initialization"')
os.system("git branch -M main")
os.system("git push -u origin main")
os.system("open readme.md")
os.system("open " + repo + ".kicad_pro")
