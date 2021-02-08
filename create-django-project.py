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
        self.modifyProjectURLs()
        self.modifyProjectSettings()
        self.createTemplatesAndStaticFolders()
        self.createIndexHTMLPage()
        self.createMigrationBatchFile()

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

        subprocess.call([self.batchFilePath])
        
    def createMigrationBatchFile(self):
        if os.path.exists(r'C:\_bats'):
            pass
        else:
            os.mkdir(r'C:\_bats')

        self.batchFilePath = ''.join([r'C:\_bats', '\\', 'migration.bat'])

        f = open(self.batchFilePath, 'w')
        f.writelines('@ECHO OFF\n')
        scriptsFolderPath = ''.join([self.rootFolder, '\\', self.environmentName, '\\Scripts'])
        scriptsFolderPath = scriptsFolderPath.replace('\\', '/')

        projectFolder = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.projectName])
        projectFolder = projectFolder.replace('\\', '/')
        
        f.writelines('cd ' + scriptsFolderPath +' && activate && cd.. && cd ' + self.projectName + ' && manage.py makemigrations && manage.py migrate\n')      
        f.writelines('PAUSE')
        f.close()

        #subprocess.call([self.batchFilePath])

    def modifyProjectURLs(self):
        projectUrls = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.projectName, '\\urls.py'])
        lines = []
        f = open(projectUrls, 'r')
        for line in f:
            ln = line.replace('\n', '')
            ln = ln.replace("from django.urls import path", "from django.urls import path, include")
            ln = ln.replace("path('admin/', admin.site.urls),", "path('admin/', admin.site.urls),\n    path('', include('"+ self.appName +".urls')),")
            lines.append(ln)
        f.close()
        os.remove(projectUrls)

        f = open(projectUrls, 'w')
        for line in lines:
            f.writelines(line + '\n')
        f.close()

    def modifyProjectSettings(self):
        projectSettings = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.projectName, '\\settings.py'])
        lines = []
        f = open(projectSettings, 'r')
        for line in f:
            ln = line.replace('\n', '')
            ln = ln.replace("'django.contrib.staticfiles',", "'django.contrib.staticfiles',\n    '" + self.appName + "',")
            ln = ln.replace("ROOT_URLCONF = '" + self.projectName + ".urls'", "ROOT_URLCONF = '" + self.projectName + ".urls'\nAUTH_USER_MODEL = '" + self.appName + ".CustomUser'")
            lines.append(ln)
        f.close()
        os.remove(projectSettings)

        f = open(projectSettings, 'w')
        for line in lines:
            f.writelines(line + '\n')
        f.close()

    def createTemplatesAndStaticFolders(self):
        appFolder = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.appName])
        os.makedirs(''.join([appFolder, '\\templates\\', self.appName]))
        os.makedirs(''.join([appFolder, '\\static\\', self.appName]))

    def createIndexHTMLPage(self):
        destinationHTML = ''.join([self.rootFolder, '\\', self.environmentName, '\\', self.projectName, '\\', self.appName, '\\templates\\', self.appName, '\\index.html'])        
        originHTML = ''.join([os.path.dirname(os.path.realpath(__file__)), '\\templates\\index.html'])

        lines = []
        f = open(originHTML, 'r')
        for line in f:
            ln = line.replace('\n', '')
            ln = ln.replace('title_template', self.projectName.capitalize())
            ln = ln.replace('project_name_template', self.projectName.capitalize())
            lines.append(ln)
        f.close()
        
        f = open(destinationHTML, 'w')
        for line in lines:
            f.writelines(line + '\n')
        f.close()

if __name__ == '__main__':
    environmentName =input('Enter Environment Name with env_ prefix e.g env_school : ')
    projectName = input('Enter Project Name : ')
    appName = input('Enter App Name : ')
    rootFolder = r'C:\_django'
    createDjangoProject(rootFolder,
                        environmentName,
                        projectName,
                        appName)
