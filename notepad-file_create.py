import argparse
from os import path as ospath
# import os
from re import match

def file_create(path='./',data=None):
    if data:
        data =' '.join(data)
    with open(path,'wt') as file:
        file.write(data)
    return 1

def setPath():
    return r'C:\Users\akshi\Desktop\SAP\UI5\ui5 course'
def setPrefix():
    return 'm-'
def setParameters(path=None,prefix=None):
    # call setpath and set prefix
    try: 
        if not path:
            path =setPath()
        if not prefix:
            # prefix =setPrefix()
            prefix =''
        # print((path,prefix))
        
        return (path,prefix)
    except Exception as e:
        raise Exception(e.args) from e
    
    
    
def path_validate(filename,path,prefix='',extension=".txt"):
    try:
        if ospath.isdir(path):
            path =ospath.realpath(path)
            # relative_path =ospath.realpath(path)
            file_exists =ospath.isfile(path+'\\'+prefix+filename+extension)
            print(file_exists)
            if not file_exists:
               return path+'\\'+prefix+filename+extension 
            else:
                raise Exception("file already present")
        else:
            raise Exception("path is invalid")
    except Exception as e:
        raise Exception(e.args) from e
    
    
def validate(filename,f=None,p=None,d=None):
    try: 
        error_flag =1
        if not f and not p:error_flag=4
        elif not f or not p:error_flag=2
        # print(match(r"^[a-zA-z]\w{1,10}$",filename))
        if filename and match(r"^[a-zA-z][\w-]{1,20}$",filename):
            error_flag =error_flag<<1
        if f and error_flag==2 and len(f)<5:
            error_flag =error_flag<<1
        if p and error_flag==4 and match(r"^[a-zA-Z]:\\[\w\s\\]+$",p):
            error_flag =error_flag<<1
            
        if error_flag==8:
            return True
        else:
            # print(error_flag)
            raise Exception("terminal arguments validation error")
    except Exception as e:
        raise Exception(e.args) from e

def argsParser():
    # formater =argparse.RawTextHelpFormatter()
    # formater.add_text("add only file name without any file extension")
    try: 
        actionS ="store"
        parser =argparse.ArgumentParser(
        description="parser to generate the files",
        # formatter_class=formater
        )
        parser.add_argument("filename",metavar="enter stored file name")
        parser.add_argument("-f","--prefix",required=False,metavar="adds Prefix to each created file",action=actionS)
        parser.add_argument("-p","--path",required=False,action=actionS)
        parser.add_argument("-d",required=False,action=actionS,nargs="*")
        p =parser.parse_args()
        return [data[1] for data in p._get_kwargs()]
        # return 0
    except Exception as e:
        # print(e.__context__)
        print("ERROR")
        raise AttributeError(e.args) from e
    
# argsParser()

def main():
    argv =argsParser()
    try: 
        # argv =['temp','-p', "d:\python 2024\\",data:optional]
        argv[0] =argv[0].strip()
        # print(argv)
        # set .yaml parameters
        argv[2],argv[1] =setParameters(argv[2],argv[1])
        argv_validate =validate(*argv)
        # print(argv)
        valid_path =path_validate(argv[0],argv[2],argv[1])
        if valid_path:
            file_create(valid_path,argv[-1])
            print("---done---")
        # match(r"^[a-zA-Z]:\\\w+$","d:\'python 2024'") 
        else:
            print('error')
            raise Exception("path is not valid")
    except Exception as e:
        print(e)
        print(e.__cause__)
        
        
    
main()
# a =match(r"^[a-zA-Z]:\\[\w\s\\]+$",'d:\python 24')
# print(a)

        