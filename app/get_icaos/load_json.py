import json

def  exceljson():
    with open('D:\python\ifaereobrasil\python\exceljson.json' , 'r') as f:
        data = json.loads(f.read())
        return data


#'../app/python/exceljson.json'

#'D:\python\ifaereobrasil\python\exceljson.json'

#../app/python/exceljson.json