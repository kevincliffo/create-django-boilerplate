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

        self.createAdmin()
        self.createForms()
        self.createManagers()
        self.createCustomUserModel()
        self.createURLs()
        self.createViews()

    def createManagers(self):
        destinationManagers = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.appName, '\\managers.py'])
        originManagers = ''.join([os.path.dirname(os.path.realpath(__file__)), '\\templates\\managers.py'])

        shutil.copy2(originManagers, destinationManagers)

    def createCustomUserModel(self):
        destinationModels = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.appName, '\\models.py'])
        originModels = ''.join([os.path.dirname(os.path.realpath(__file__)), '\\templates\\models.py'])

        shutil.copy2(originModels, destinationModels)

    def createForms(self):
        destinationForms = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.appName, '\\forms.py'])
        originForms = ''.join([os.path.dirname(os.path.realpath(__file__)), '\\templates\\forms.py'])

        shutil.copy2(originForms, destinationForms)

    def createURLs(self):
        destinationURLs = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.appName, '\\urls.py'])
        originURLs = ''.join([os.path.dirname(os.path.realpath(__file__)), '\\templates\\urls.py'])

        lines = []
        f = open(originURLs, 'r')
        for line in f:
            ln = line.replace('\n', '')
            ln = ln.replace('app_name_placeholder', self.appName)
            lines.append(ln)
        f.close()
        
        f = open(destinationURLs, 'w')
        for line in lines:
            f.writelines(line + '\n')
        f.close()

    def createAdmin(self):
        destinationAdmin = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.appName, '\\admin.py'])
        originAdmin = ''.join([os.path.dirname(os.path.realpath(__file__)), '\\templates\\admin.py'])

        lines = []
        f = open(originAdmin, 'r')
        for line in f:
            ln = line.replace('\n', '')
            ln = ln.replace('template_site_header', self.projectName.capitalize())
            lines.append(ln)
        f.close()
        
        f = open(destinationAdmin, 'w')
        for line in lines:
            f.writelines(line + '\n')
        f.close()

    def createViews(self):
        destinationviews = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.appName, '\\views.py'])
        originViews = ''.join([os.path.dirname(os.path.realpath(__file__)), '\\templates\\views.py'])

        lines = []
        f = open(originViews, 'r')
        for line in f:
            ln = line.replace('\n', '')
            ln = ln.replace('template/', self.appName + f'/')
            lines.append(ln)
        f.close()
        
        f = open(destinationviews, 'w')
        for line in lines:
            f.writelines(line + '\n')
        f.close()
        
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
