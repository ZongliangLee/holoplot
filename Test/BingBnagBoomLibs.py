
import subprocess
import os
class BingBnagBoomLibs():
    def __init__(self,path):
        os.chdir(path)
        self.number = 0
        self.filename = ''

    def _calculate(self):
        return  str(subprocess.Popen(['BingBangBoom.exe',"calculate", str(self.number)], \
            shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())

    def _save(self):
        return  str(subprocess.Popen(['BingBangBoom.exe',"save", str(self.number),str(self.filename)], \
            shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())

    def _load(self):
        return  str(subprocess.Popen(['BingBangBoom.exe',"load", str(self.filename)], \
            shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())

    def calculate(self, number):
        self.number = number
        return self._calculate()

    def save(self, number, filename):
        self.number = number
        self.filename = filename
        return self._save()
    
    def load(self, filename):
        self.filename = filename
        return self._load()