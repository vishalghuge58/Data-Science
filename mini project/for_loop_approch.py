
import pytesseract
import os
import re
import time

import pandas as pd

class id_pattern():

    def __init__(self,id):

        path=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = path

        self.list_images=os.listdir(f'{id}')

        if id=='adhar_id':
            self.pattern=re.compile(r'[0-9]{4}[ ][0-9]{4}[ ][0-9]{4}')
        elif id == 'pan_id':
            self.pattern=re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')
        elif id == 'driving_id':
            self.pattern=re.compile(r'[A-Z]{2}[0-9]{2}[ ][0-9]{7}')    
        elif id == 'passport_id':
            self.pattern=re.compile(r'[A-Z][0-9]{7}')   
        elif id=='votting_id':
            self.pattern=re.compile(r'[A-Z]{3}[0-9]{7}')    

    def searching(self,txt):

        var=self.pattern.search(txt)
        print(var)

        if var==None:
            return None
        else:
            start=var.start()
            end=var.end()
            string=txt[start:end]

            print(string)
            return string

        

class extract_ids(id_pattern):

    def __init__(self,id):
        self.id=id
        self.list=[]
        self.data={}
        super().__init__(id)
        # with open(f"{self.id}.txt",'w') as f:
        for img in self.list_images:
            image=id+"\\"+img
            txt=pytesseract.image_to_string(image)
            # f.write(txt)
            match=self.searching(txt)
            # if match!=None and match not in self.list:
            self.list.append(match)
            # else:
                # pass
                    
        self.data[self.id]=self.list





class id_info(extract_ids):

    def __init__(self,id):
        super().__init__(id)

  


if __name__=='__main__':

    start_time=time.time()

    dict_data={}
    cwd_list=os.listdir()

    for folder in cwd_list:
        if '.' not in folder:
            ids=id_info(folder)
            dict_data.update(ids.data)
    print(dict_data)

    end_time=time.time()

    print("Time is ==",end_time-start_time)

    df=pd.DataFrame(dict_data)
    print(df)



