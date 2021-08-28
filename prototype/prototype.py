import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import popup
from PIL import Image
import os
sg.theme('DarkAmber') 

def error():#error message
    layout = [
        [sg.Text("Username Or Password wrong ")],
        [sg.Text("Please check your account infomation",size=(15,15))],
        [sg.Button("Back")]
    ]
    window = sg.Window("error",layout)
    event,values=window.read()
    if event == "Back":
        window.close()
        login()
def upload():#upload function
    layout = [
        [sg.Text("Year")],
        [sg.Input(key="YEAR")],
        [sg.Text("Position")],
        [sg.Input(key="POSITION")],
        [sg.Text("Gender")],
        [sg.Input(key="GENDER")],
        [sg.Text("ID")],
        [sg.Input(key="ID")],
        [sg.Button('Upload')],
        [sg.Button("Back")]

    ]
    window= sg.Window("Upload",layout,size=(500, 300))
    event,values=window.read()
    if event=="Upload":
        year=values["YEAR"]
        positions=values["POSITION"]
        gender=values["GENDER"]
        id=values["ID"]
        if year==""or positions=="" or gender=="" or id=="" :
            popup("wrong data check again")
            window.close()
            upload()
        else:
            popup("successfully uploaded")
            window.close()
            upload()

    if event=="Back":
        window.close()
        main_page()   



def OverView():#overview layout
    layout = [
        [sg.Button("line",size=(10,5))],
        [sg.Button("curly",size=(10,5))],
        [sg.Button("Overview",size=(10,5))],
        [sg.Button("Back",size=(10,5))], 
    ]
    window= sg.Window("data",layout,size=(600,400),element_justification='c')
    event,values=window.read()
    print(event,values)
    if event=="curly":
        window.close()
        curly()
        
    if event=="line":
        window.close()
        line()
    if event=="Overview":
        window.close()
        nzShark()    
    if event =="Back":
        window.close()
        main_page()    
    
def nzShark():
    current_dir = os.path.dirname(os.path.abspath(__file__))#current path 
    img=Image.open(current_dir+"/data1.png")
    plt.figure("New Zealand White Sharks")
    plt.imshow(img)
    print(current_dir)
    plt.show()
    OverView()

def  line():#a line chart
    
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 100])

    plt.plot(xpoints, ypoints)
    plt.show()
    
    OverView()


def curly():# a curly chart
    pl=plt.figure(figsize=(8,6),dpi=80)#create a canvas
    x=np.arange(0,1.01,0.01)
    plt.title('curly line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.xticks([0,0.2,0.4,0.6,0.8,1])
    plt.yticks([0,0.2,0.4,0.6,0.8,1])
    plt.plot(x,x**2)
    plt.plot(x,x**4)
    plt.show()
    OverView()
#this is register window   
def register():
    layout=[
            [sg.Text("YourUserName"),
            sg.Input(key="_USER_")],
            [sg.Text("Input Password"),
            sg.Input(key="_REGPASSWORD_")],
             [sg.Text('Password again'),sg.Input(key="_PASSWORD2_")],
            [sg.Text('Select Occupation')],
            [sg.Checkbox('Student', size=(10,1)), sg.Checkbox('Scientist',size=(10,1)), sg.Checkbox('Tourism',size=(10,1))],
           [sg.Button('Submit')],
            
        ]
    window2=sg.Window('Register',layout,size=(500, 300))
    event,values=window2.read()
    print(event,values)
    if event == "Submit":
        window2.close()
        login()    

def main_page():#main page
    layout =[
        [sg.Button('Overview',size=(10,5))],
        [sg.Button('Search',size=(10,5))],
        [sg.Button('Upload',size=(10,5))]
    ]
    window = sg.Window("Main page",layout,size=(600,300),element_justification='c')
    window.read()
    event,values = window.read()
    if event == "Overview":
        window.close()
        OverView()
    if event == "Search":
        window.close()
        search()
    if event == "Upload":
        window.close()
        upload()        

def search():
    layout=[
        [sg.Text("Input key words here")],
        [sg.Input(key='KEYWORDS')],
        [sg.Text("result shows here",key='RESULT')],
        [sg.Button("Search")],
        [sg.Button("Back")],
    ]
    window = sg.Window("search",layout,size=(600, 400))  
    event,values=window.read()
    if event =="Search":
        
        keywords=values['KEYWORDS']
         
        if keywords =="":
            popup("can not be an empty string")
            window.close()
            search()
        else:
            window['RESULT'].update(keywords)
            popup("Search success",keywords)
            window.close() 
            search()   
        print(values)    
               
    if event=="Back":
        window.close()
        main_page()      

# make layout for login window
def login():

    layout=[ 
            [sg.Text("Username"),sg.Input(key="USER")],
            [sg.Text("Password"),sg.Input(key="PASSWORD")],
            [sg.Button('Login',button_color=(sg.YELLOWS[0], sg.BLUES[0]))],[sg.Button('Register',button_color=(sg.YELLOWS[0], sg.BLUES[0]))]
           
        ]
    window=sg.Window('Home page',layout,size=(500, 300))
    while True:
            
        event,values=window.read()
        print(event)
        if event is None  :
            break
        if event == 'Register':
            window.close()
            register()
        if event=="Login":
            print(event,values)
            user=values["USER"]
            passwords=values["PASSWORD"]
            if user=="" or passwords=="":
                window.close()
                error()
            window.close()
            main_page()
                
   
login()  

