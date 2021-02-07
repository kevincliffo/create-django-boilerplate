import os
import shutil
import subprocess

class createDjangoProject:
    def __init__(self, rootFolder, environmentName, projectName, appName):
        self.batchFilePath = ''
        self.rootFolder = rootFolder
        self.environmentName = environmentName
        self.projectName = projectName
        self.appName = appName
        self.createBatchFile()

    def createBatchFile(self):
        if os.path.exists(r'C:\_bats'):
            pass
        else:
            os.mkdir(r'C:\_bats')

        self.batchFilePath = ''.join([r'C:\_bats', '\\', 'project.bat'])

        f = open(self.batchFilePath, 'w')
        f.writelines('@ECHO OFF\n')
        f.writelines('cd C:/_django && python -m venv ' + self.environmentName
                     + ' && cd ' + self.environmentName + ' && cd scripts '
                     + '&& activate && cd.. && python -m pip install --upgrade pip && pip install django '
                     + '&& django-admin startproject ' + self.projectName + ' && cd '
                     + self.projectName + ' && manage.py startapp ' + self.appName + '\n')        
        f.writelines('PAUSE')
        f.close()
        print('batFile : ' + self.batchFilePath)


        subprocess.call([self.batchFilePath])
        print('hello world')


if __name__ == '__main__':
    environmentName =input('Enter Environment Name with env_ prefix e.g env_school : ')
    projectName = input('Enter Project Name : ')
    appName = input('Enter App Name : ')
    rootFolder = r'C:\_django'
    createDjangoProject(rootFolder,
                        environmentName,
                        projectName,
                        appName)
