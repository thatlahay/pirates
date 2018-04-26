import os,sys,fnmatch,re
class finding():
    def finds(self,path,param):
        for root,dicts,files in os.walk(path):
            for filel in files:
                    if fnmatch.fnmatch(filel,param):
                        print(filel)
