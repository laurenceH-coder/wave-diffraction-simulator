from tkinter import * #imports the required tkinter modules needed for the program's GUIs#
import ctypes
import time
import math
import colorpy as color
import colorsys as ColorSys
from colormap import rgb2hex
import pyautogui
from PIL import Image
import datetime
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def mainMenuOpen(debounce):
    if debounce == False:
        debounce = True
        global mainMenu
        mainMenu = Tk() #instantiates a window
        #Window Setup
        global windowWidth
        global windowHeight
        windowWidth = "1920"
        windowHeight = "1080"
        #windowWidth = str(mainMenu.winfo_screenwidth())
        #windowHeight = str(mainMenu.winfo_screenheight()) #gets screen dimensions and stores them as variables
        
        print("Window Width:", windowWidth, "\nWindow Height:", windowHeight) #testing that the system obtains the correct values for windowWidth and
                                                                              #windowHeight
        mainMenu.geometry(windowWidth + "x" + windowHeight) #sets the size of the window to the arbitrary 5size of 500 pixels wide, 600 pixels high
        waveDiffractionIcon = PhotoImage(file = 'programIcon.png')
        mainMenu.iconphoto(True, waveDiffractionIcon)
        mainMenu.wm_attributes('-transparentcolor', '#ab23ff')
        mainMenu.config(bg = '#f8f4f4')
    mainMenu.title("Wave Diffraction Simulator") #sets the title for the main menu window
    savedSetupsMenu = [0,0,0]
    saveFileNumber = StringVar()
    saveFileNumber.set(0) #declares the variable saveFileNumber and sets it to zero

    #Static GUI Elements Setup (Labels, Images)
    global welcomeLabel
    welcomeLabel = Label(mainMenu,
                         text="Welcome to the Wave \n Diffraction Simulator!",
                         justify="center",
                         font=('Arial',20,'bold'),
                         bg = '#f8f4f4')
    welcomeLabel.place(relx=0.5,y=35, anchor = 'n') #sets text and text settings of the welcome text label and places it

    global savedSetupsLabel
    savedSetupsLabel = Label(mainMenu,
                             text="Saved Setups:",
                             justify="center",
                             font=('Arial', 17, 'underline'),
                             bg = '#f8f4f4')
    
    savedSetupsLabel.place(relx=0.5,rely=0.28, anchor = 'n') #sets text and text settings of the saved setups text label and places it
    try:
        with open('saveFile1.txt', 'r') as file1mainMenu:
            for line in file1mainMenu:
                fileNamePreviousFile1 = line.rstrip("\n")
                break
            #displays file name of first save file as the text on a button if it is exists 
        global savedSetup1Button
        savedSetup1Button = Radiobutton(mainMenu, text=fileNamePreviousFile1, justify="left", variable=saveFileNumber, value=1)
        savedSetup1Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 pady=45,
                                 indicatoron=0)
        savedSetup1Button.place(relx=0.5,rely=0.35, relwidth = 0.3, anchor = 'n') #creates a radio button which allows the user to select to load save file 1
        savedSetupsMenu[0] = 1 #sets flag in the array to indicate that a save file exists at save file position 1

    except(FileNotFoundError): #if save file 1 does not exist in the save files folder then...
        global savedSetup1EmptyLabel
        savedSetup1EmptyLabel = Label(mainMenu,
                                      text="Empty",
                                      justify="center",
                                      bg='#c2c2c2',
                                      border=5,
                                      relief='groove',
                                      padx=180,
                                      pady=55,
                                      font=('Arial', 22, 'bold')) 

        savedSetup1EmptyLabel.place(relx=0.5,rely=0.35, anchor = 'n') #sets text and text settings of the empty setup 1 file text label
                                                                        #and places it
    try:
        with open('saveFile2.txt', 'r') as file2mainMenu:
            for line in file2mainMenu:
                fileNamePreviousFile2 = line.rstrip("\n")
                break
            #displays file name of second save file as the text on a button if it is exists
        global savedSetup2Button
        savedSetup2Button = Radiobutton(mainMenu, text=fileNamePreviousFile2, justify="left", variable=saveFileNumber, value=2)
        savedSetup2Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 pady=45,
                                 indicatoron=0)
        savedSetup2Button.place(relx=0.5,rely=0.53, relwidth = 0.3, anchor = 'n') #creates a radio button which allows the user to select to load save file 2
        savedSetupsMenu[1] = 1 #sets flag in the array to indicate that a save file exists at save file position 2
        
    except(FileNotFoundError): #if save file 2 does not exist in the save files folder then...
        global savedSetup2EmptyLabel
        savedSetup2EmptyLabel = Label(mainMenu,
                                      text="Empty",
                                      justify="center",
                                      bg='#c2c2c2',
                                      border=5,
                                      relief='groove',
                                      padx=180,
                                      pady=55,
                                      font=('Arial', 22, 'bold'))

        savedSetup2EmptyLabel.place(relx=0.5,rely=0.53, anchor = 'n') #sets text and text settings of the empty setup 2 file text label
                                                                        #and places it

    try:
        with open('saveFile3.txt', 'r') as file3mainMenu:
            for line in file3mainMenu:
                fileNamePreviousFile3 = line.rstrip("\n")
                break
            #displays file name of third save file as the text on a button if it is exists
        global savedSetup3Button
        savedSetup3Button = Radiobutton(mainMenu, text=fileNamePreviousFile3, justify="left", variable=saveFileNumber, value=3)
        savedSetup3Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 pady=45,
                                 indicatoron=0)
        savedSetup3Button.place(relx=0.5,rely=0.71, relwidth = 0.3, anchor = 'n') #creates a radio button which allows the user to select to load save file 3
        savedSetupsMenu[2] = 1 #sets flag in the array to indicate that a save file exists at save file position 3
        
    except(FileNotFoundError): #if save file 3 does not exist in the save files folder then...
        global savedSetup3EmptyLabel
        savedSetup3EmptyLabel = Label(mainMenu,
                                      text="Empty",
                                      justify="center",
                                      bg='#c2c2c2',
                                      border=5,
                                      relief='groove',
                                      padx=180,
                                      pady=55,
                                      font=('Arial', 22, 'bold'))

        savedSetup3EmptyLabel.place(relx=0.5,rely=0.71, anchor = 'n') #sets text and text settings of the empty setup 2 file text label and
                                                                        #places it

    leftMenuImageUnscaled = PhotoImage(file='leftMenuImage.png')
    leftMenuImage = leftMenuImageUnscaled.zoom(int(windowWidth)//100, int(windowHeight)//100)            #this new image is 3x the original
    leftMenuImage = leftMenuImage.subsample(14, 8)   #halve the size, it is now 1.5x the original
    global leftMenuImageLabel
    leftMenuImageLabel = Label(mainMenu, image=leftMenuImage) #defines and sets the image label which will be shown on the
                                                                #left side of the screen 
    leftMenuImageLabel.place(relx=0.015, rely = 0.5, anchor='w') #places this image on the left side of the screen)

    rightMenuImageUnscaled = PhotoImage(file='rightMenuImage.png')
    rightMenuImage = rightMenuImageUnscaled.zoom(int(windowWidth)//100, int(windowHeight)//100)            #this new image is 3x the original
    rightMenuImage = rightMenuImage.subsample(14, 8)   #halve the size, it is now 1.5x the original
    global rightMenuImageLabel
    rightMenuImageLabel = Label(mainMenu, image=rightMenuImage) #defines and sets the image label which will be shown on the right
                                                                #side of the screen
    rightMenuImageLabel.place(relx=0.985, rely = 0.5, anchor='e') #places this image on the right side of the screen

    #Interactive GUI Elements Setup (Buttons)
    global newSetupButton
    newSetupButton = Button(mainMenu, text='New Setup') #defines a button with the text 'New Setup' in the main menu window
    newSetupButton.place(relx=0.495 ,rely=0.2, anchor = 'e') #places the button at the correct position just below and to the left of the
                                                            #welcome text
    newSetupButton.config(font=('Arial', 25, 'bold'),
                          relief='raised',
                          border=5,
                          padx=20,
                          pady=20,
                          command= newSetupWindowOpen) #sets the font settings of the button
                                                      #sets the relief of the button to raised and border size of the button to 5 to
                                                        #make it visible enough.
                                                      #sets the padding of the button to 20 in each direction so that the button is larger
                                                      #causes newSetupWindowOpen() to run when the new setup button is clicked
    global chosenDiffractionType
    chosenDiffractionType = StringVar()
    global loadSetupButton
    loadSetupButton = Button(mainMenu, text='Load Setup') #defines a button with the text 'New Setup' in the main menu window
    loadSetupButton.place(relx=0.505 ,rely=0.2, anchor = 'w') #places the button at the correct position just below and to the
                                                              #right of the welcome text
    loadSetupButton.config(font=('Arial', 25, 'bold'),
                          relief='raised',
                          border=5,
                          padx=13,
                          pady=20,
                          command= lambda: loadPreviousSystem(saveFileNumber.get(), savedSetupsMenu))
                        #sets the font settings of the button
                        #sets the relief of the button to raised and border size of the button to 5 to make it visible enough.
                        #sets the padding of the button to 13 horizontally and 20 vertically so that the button is larger
                        #causes newSetupWindowOpen() to run when the new setup button is clicked, with the correct parameters
    

    #Placing Window
    mainMenu.mainloop() #place window on user's screen

    

def newSetupWindowOpen():
    print("newSetupWindowOpen ran successfully") #outputs a message to confirm that the procedure newSetupWindowOpen() has run upon clicking the
                                                 #new setup button
    welcomeLabel.place_forget()
    savedSetupsLabel.place_forget()
    newSetupButton.place_forget()
    loadSetupButton.place_forget() #hides all of the text and button widgets on main menu which appear upon any execution of the program
    try:
        savedSetup1EmptyLabel.place_forget()
    except(NameError):
        savedSetup1Button.place_forget()
    try:
        savedSetup2EmptyLabel.place_forget()
    except(NameError):
        savedSetup2Button.place_forget()
    try:
        savedSetup3EmptyLabel.place_forget()
    except(NameError):
        savedSetup3Button.place_forget() #The program tries to remove every empty setup label that exists, and any that don't will throw an exception which the program responds to by
                                            #removing the button that must exist in its place instead.
    try:
        loadSystemNoFilesLabel.place_forget()
    except(NameError):
        print("No no-file error label to remove")
    try:
        loadSystemNoSelectionLabel.place_forget()
    except(NameError):
        print("No no-selection error label to remove") #The program removes any existing error messages on the user's screen and gives an appropriate output message if it has not
                                                            #needed to do this if none are present.

    #Diffraction type choosing window setup
    global confirmDiffractionTypeLabel
    confirmDiffractionTypeLabel = Label(mainMenu,
                                        text="Confirm the type of \n Wave Diffraction.",
                                        justify="center",
                                        font=('Arial',20,'bold'))
    confirmDiffractionTypeLabel.place(relx=0.5,y=50, anchor = 'n') #sets text and text settings of the 'confirm the type of wave diffraction' text label and places it

    global diffractionTypeOptionsLabel
    diffractionTypeOptionsLabel = Label(mainMenu,
                                        text="Options",
                                        justify="center",
                                        font=('Arial', 18, 'underline'))
    diffractionTypeOptionsLabel.place(relx=0.5,rely=0.28, anchor = 'n') #sets text and text settings of the diffraction type options text label and places it

    global singleSlitDiffractionSelectionButton
    #chosenDiffractionType = StringVar()
    chosenDiffractionType.set("None") #sets a starting value for the chosen diffraction type for the simulation so that none of the radio buttons are selected by default
    singleSlitDiffractionSelectionButton = Radiobutton(mainMenu, text='Single-Slit Diffraction', justify="left", variable=chosenDiffractionType, value="Single-Slit")
    singleSlitDiffractionSelectionButton.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 padx=59,
                                 pady=45,
                                 indicatoron=0)
    singleSlitDiffractionSelectionButton.place(relx=0.5,rely=0.35, anchor = 'n') #creates a radio button which allows the user to select to a single-slit diffraction setup

    global doubleSlitDiffractionSelectionButton
    doubleSlitDiffractionSelectionButton = Radiobutton(mainMenu, text='Double-Slit Diffraction', justify="left", variable=chosenDiffractionType, value="Double-Slit")
    doubleSlitDiffractionSelectionButton.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 padx=54,
                                 pady=45,
                                 indicatoron=0)
    doubleSlitDiffractionSelectionButton.place(relx=0.5,rely=0.53, anchor = 'n') #creates a radio button which allows the user to select to a double-slit diffraction setup

    global diffractionGratingSelectionButton
    diffractionGratingSelectionButton = Radiobutton(mainMenu, text='Diffraction Grating', justify="left", variable=chosenDiffractionType, value="Diffraction-Grating")
    diffractionGratingSelectionButton.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 padx=83,
                                 pady=45,
                                 indicatoron=0)
    diffractionGratingSelectionButton.place(relx=0.5,rely=0.71, anchor = 'n') #creates a radio button which allows the user to select to a diffraction grating setup
    
    global confirmDiffractionTypeButton
    confirmDiffractionTypeButton = Button(mainMenu, text='Confirm') #defines a button with the text 'Confirm' in the diffraction type choosing menu window
    confirmDiffractionTypeButton.place(relx=0.505 ,rely=0.2, anchor = 'w') #places the button at the correct position just below and to the
                                                                              #right of the choose diffraction type text label
    confirmDiffractionTypeButton.config(font=('Arial', 25, 'bold'),
                          relief='raised',
                          border=5,
                          padx=13,
                          pady=20,
                          command= lambda: generateSystem([chosenDiffractionType.get()]))
                        #sets the font settings of the button
                        #sets the relief of the button to raised and border size of the button to 5 to make it visible enough.
                        #sets the padding of the button to 13 horizontally and 20 vertically so that the button is larger
                        #causes generateSystem to run when the confirm button is clicked, with the correct parameters
    
    global backDiffractionTypeButton
    backDiffractionTypeButton = Button(mainMenu, text='Back') #defines a button with the text 'Back' in the diffraction type choosing menu window
    backDiffractionTypeButton.place(relx=0.495 ,rely=0.2, anchor = 'e') #places the button at the correct position just below and to the left of the
                                                                        #choose diffraction type text label
    
    backDiffractionTypeButton.config(font=('Arial', 25, 'bold'),
                                     relief='raised',
                                     border=5,
                                     padx=45,
                                     pady=20,
                                     command= returnToMainMenuFromDTypeChoice)  #sets the font settings of the button
                                                                                #sets the relief of the button to raised and border size of the
                                                                                #button to 5 to make it visible enough.
                                                                                #sets the padding of the button to 20 in each direction so that the
                                                                                #button is larger causes returnToMainMenu() to run when the back button is clicked.

    

def loadPreviousSystem(saveFileNo, savedSetupsMenuArray): #subroutine to access and validate the values of a save file to be loaded, before calling generateSystem to load
                                                          #the diffraction environment
    if int(saveFileNo) != 0:
        print("Preparing to load save file", str(saveFileNo), ".") #outputs a message to confirm that the procedure
                                                                   #loadPreviousSystem(saveFileNumber)
    else:
        print("Invalid save file number!")
        if savedSetupsMenuArray[0] == 0 and savedSetupsMenuArray[1] == 0 and savedSetupsMenuArray[2] == 0:
            global loadSystemNoFilesLabel
            loadSystemNoFilesLabel = Label(mainMenu,
                                            text = "No previous setups to load. Please create a new setup.",
                                            fg="red",
                                            font = ('Arial', 15))
            loadSystemNoFilesLabel.place(relx = 0.5, anchor = "center", rely = 0.91)
            #Checks if there are no loadable save files and outputs a suitable error message for this case if the load setup button has
            #been clicked by the user.
        else:
            global loadSystemNoSelectionLabel
            loadSystemNoSelectionLabel = Label(mainMenu,
                                                text = "Please select one of the setups to load.",
                                                fg="red",
                                                font = ('Arial', 15))
            loadSystemNoSelectionLabel.place(relx = 0.5, anchor = "center", rely = 0.91)
            #If there is loadable save files and the user has not selected a save file to load before clicking the load setup button,
            #the system displays a suitable error message to the user.
        return "No save file selected."

    #Loading process:
    loadedSystemValues = [] #declares a list to hold the values of the system to be loaded from the file
    with open(("saveFile" + str(saveFileNo) + ".txt"), "r") as saveFileToLoad:
        for line in saveFileToLoad:
            loadedSystemValues.append(line.rstrip("\n"))
    saveFileToLoad.close() #reads each value from the file into the list

    #Ensures that the correct number of values have been obtained. If not, a default single-slit system is loaded with an error message later displayed.
    if len(loadedSystemValues) != 18:
        chosenDiffractionType.set("Single-Slit")
        generateSystem(chosenDiffractionType.get())
        return "DefaultUsed"

    #If the value for the ruler's position is 'default', the initial position for the ruler is used in generateSystem. Otherwise, the ruler position is converted from a
    #string to a list of two items.
    if loadedSystemValues[4] == "Default":
        loadedSystemValues[4] = ["initialRulerXCord", "initialRulerYCord"]
    else:
        loadedSystemValues[4] = list(loadedSystemValues[4])
        loadedSystemValues[4].remove("[")
        loadedSystemValues[4].remove("]")
        seperatorIndexRulerPosition = loadedSystemValues[4].index(",")
        if len(loadedSystemValues[4][0:seperatorIndexRulerPosition]) == 3:
            rulerXCord = str(loadedSystemValues[4][0]) + str(loadedSystemValues[4][1]) + str(loadedSystemValues[4][2])
            if len(loadedSystemValues[4][(seperatorIndexRulerPosition+1):]) == 3:
                rulerYCord = str(loadedSystemValues[4][4]) + str(loadedSystemValues[4][5]) + str(loadedSystemValues[4][6])
            else:
                rulerYCord = str(loadedSystemValues[4][4]) + str(loadedSystemValues[4][5]) + str(loadedSystemValues[4][6]) + str(loadedSystemValues[4][7])
        else:
            rulerXCord = str(loadedSystemValues[4][0]) + str(loadedSystemValues[4][1]) + str(loadedSystemValues[4][2]) + str(loadedSystemValues[4][3])
            if len(loadedSystemValues[4][(seperatorIndexRulerPosition+1):]) == 3:
                rulerYCord = str(loadedSystemValues[4][5]) + str(loadedSystemValues[4][6]) + str(loadedSystemValues[4][7])
            else:
                rulerYCord = str(loadedSystemValues[4][5]) + str(loadedSystemValues[4][6]) + str(loadedSystemValues[4][7]) + str(loadedSystemValues[4][8])
                
        loadedSystemValues[4] = [int(rulerXCord), int(rulerYCord)]
        
        if int(loadedSystemValues[4][0]) < 0 or int(loadedSystemValues[4][0]) > int(windowWidth):
            loadedSystemValues[4][0] = "initialRulerXCord"
        if int(loadedSystemValues[4][1]) < 0 or int(loadedSystemValues[4][1]) > int(windowHeight):
            loadedSystemValues[4][1] = "initialRulerYCord"

    #If the value for the protractor's position is 'default', the initial position for the protractor is used in generateSystem. Otherwise, the protractor position
    #is converted from a string to a list of two items.
    if loadedSystemValues[5] == "Default":
        loadedSystemValues[5] = ["initialProtractorXCord", "initialProtractorYCord"]
    else:  
        loadedSystemValues[5] = list(loadedSystemValues[5])
        loadedSystemValues[5].remove("[")
        loadedSystemValues[5].remove("]")
        seperatorIndexProtractorPosition = loadedSystemValues[5].index(",")
        if len(loadedSystemValues[5][0:seperatorIndexProtractorPosition]) == 3:
            protractorXCord = str(loadedSystemValues[5][0]) + str(loadedSystemValues[5][1]) + str(loadedSystemValues[5][2])
            if len(loadedSystemValues[4][(seperatorIndexProtractorPosition+1):]) == 3:
                protractorYCord = str(loadedSystemValues[5][4]) + str(loadedSystemValues[5][5]) + str(loadedSystemValues[5][6])
            else:
                protractorYCord = str(loadedSystemValues[5][4]) + str(loadedSystemValues[5][5]) + str(loadedSystemValues[5][6]) + str(loadedSystemValues[5][7])
        else:
            protractorXCord = str(loadedSystemValues[5][0]) + str(loadedSystemValues[5][1]) + str(loadedSystemValues[5][2]) + str(loadedSystemValues[5][3])
            if len(loadedSystemValues[5][(seperatorIndexProtractorPosition+1):]) == 3:
                protractorYCord = str(loadedSystemValues[5][5]) + str(loadedSystemValues[5][6]) + str(loadedSystemValues[5][7])
            else:
                protractorYCord = str(loadedSystemValues[5][5]) + str(loadedSystemValues[5][6]) + str(loadedSystemValues[5][7]) + str(loadedSystemValues[5][8])
                
        loadedSystemValues[5] = [int(protractorXCord), int(protractorYCord)]
        
        if int(loadedSystemValues[5][0]) < 0 or int(loadedSystemValues[5][0]) > int(windowWidth):
            loadedSystemValues[5][0] = "initialProtractorXCord"
        if int(loadedSystemValues[5][1]) < 0 or int(loadedSystemValues[5][1]) > int(windowHeight):
            loadedSystemValues[5][1] = "initialProtractorYCord"

    #Sets the title for the window from the file name.
    currentFileName = loadedSystemValues[0]

    #Validates each of the values given in the file, and sets it to a default value if it is not valid.
    if float(loadedSystemValues[2]) < 380 or float(loadedSystemValues[2]) > 700:
        loadedSystemValues[2] = 500.000
    if float(loadedSystemValues[3]) < 0.5 or float(loadedSystemValues[3]) > 2:
        loadedSystemValues[3] = 1.000

    if int(loadedSystemValues[6])%45 != 0 and loadedSystemValues[6] < 0 and loadedSystemValues[6] > 360:
        loadedSystemValues[6] = 0
    if int(loadedSystemValues[7])%45 != 0 and loadedSystemValues[7] < 0 and loadedSystemValues[7] > 360:
        loadedSystemValues[7] = 0

    for x in range (8,15):
        try:
            bool(loadedSystemValues[x])
        except(ValueError, TypeError):
            loadedSystemValues[x] = True

    if loadedSystemValues[15] != "Single-Slit" and loadedSystemValues[15] != "Double-Slit" and loadedSystemValues[15] != "Diffraction-Grating":
        loadedSystemValues[15] = "Single-Slit"
    if loadedSystemValues[16] != "Detailed" and loadedSystemValues[16] != "Simple":
        loadedSystemValues[16] = "Detailed"
    if float(loadedSystemValues[17]) < 1 or float(loadedSystemValues[17]) > 2:
        loadedSystemValues[17] = 1.500

    #Calls generateSystem to create the diffraction environment using the validated set of values from the save file which have been obtained.
    generateSystem(loadedSystemValues)


def generateSystem(systemValues):
    #Runs this code if a previously saved system is being loaded (indicated by the size of the systemValues list provided as a parameter).
    if len(systemValues) != 1:
        #If there are a correct number of values in the list passed as a parameter, then the previous system (with any validation changes made in loadPreviousSystem) can
        #be generated normally.
        if len(systemValues) == 18:
            print("Loading previous system!")
            chosenDiffractionType.set(systemValues[15])
        #If there are less than 18 values given in the list, then the save file is likely invalid and so cannot be loaded by the system. It instead loads a default
        #single-slit system.
        else:
            if len(systemValues) != 1: #this will check if the array of the system values passed in is of the format of a new system being loaded
                print("Invalid systemValues array provided.")
                global erroneousLoadLabel
                erroneousLoadLabel = Label(mainMenu,
                                        text = ("Erroneous save file. Default single-slit diffraction simulator loaded."),
                                        fg= "red",
                                        bg = "#f8f4f4",
                                        font = ('Arial', 14))
                erroneousLoadLabel.place(relx = 0.175, anchor = "nw", rely = 0.018)
                chosenDiffractionType.set("Single-Slit")
                systemValues = ["None", "N/A", 500.000, 1.000, ["initialRulerXCord","initialRulerYCord"] , ["initialProtractorXCord", "initialProtractorYCord"],
                            0, 0, True, True, True, True, True, True, True, chosenDiffractionType.get(), "Detailed", 1.500]
                
        #Code to remove starting menu GUI elements
        welcomeLabel.place_forget()
        savedSetupsLabel.place_forget()
        newSetupButton.place_forget()
        try:
            loadSetupButton.place_forget()
        except:
            print("No Button to remove")
        try:
            savedSetup1EmptyLabel.place_forget()
        except(NameError):
            savedSetup1Button.place_forget()
        try:
            savedSetup2EmptyLabel.place_forget()
        except(NameError):
            savedSetup2Button.place_forget()
        try:
            savedSetup3EmptyLabel.place_forget()
        except(NameError):
            savedSetup3Button.place_forget() #The program tries to remove every empty setup label that exists, and any that don't will throw an exception which the program responds to by
                                                    #removing the button that must exist in its place instead.
        try:
            loadSystemNoFilesLabel.place_forget()
        except(NameError):
            print("No no-file error label to remove")
        try:
            loadSystemNoSelectionLabel.place_forget()
        except(NameError):
            print("No no-selection error label to remove") #The program removes any existing error messages on the user's screen and gives an appropriate output message if it has not
                                                                    #needed to do this if none are present.
    #If a new system is being loaded, the below code will be run.
    else:
        #If a diffraction type has been selected by the user, a default system of this chosen diffraction type is generated.
        if systemValues[0] != "None": 
            print("Generating setup of diffraction type:" , systemValues[0], "!") #A confirmation output message is given for which of the three
                                                                                        #diffraction types has been selected and will be loaded.
            systemValues = ["None", "N/A", 500.000, 1.000, ["initialRulerXCord","initialRulerYCord"] , ["initialProtractorXCord", "initialProtractorYCord"],
                            0, 0, True, True, True, True, True, True, True, chosenDiffractionType.get(), "Detailed", 1.500]
            #Code to remove menu GUI elements
            confirmDiffractionTypeLabel.place_forget()
            diffractionTypeOptionsLabel.place_forget()
            singleSlitDiffractionSelectionButton.place_forget()
            doubleSlitDiffractionSelectionButton.place_forget()
            diffractionGratingSelectionButton.place_forget()
            confirmDiffractionTypeButton.place_forget()
            backDiffractionTypeButton.place_forget()
        #If the user has not chosen a diffraction type, for the new system to be generated with, the user is prompted to choose one and the subroutine ends.
        else:
            print("No diffraction type provided!") #A message stating that the user has not selected one of the diffraction type options is provided.
            global newSystemNoTypeLabel
            newSystemNoTypeLabel = Label(mainMenu,
                                             text = "Please select one of the setups above!",
                                             fg="red",
                                             font = ('Arial', 15))
            newSystemNoTypeLabel.place(relx = 0.5, anchor = "center", rely = 0.91)
            #A label asking the user to select one of the provided diffraction type options is displayed.
            return False

    #Removes remaining GUI elements no longer needed
    leftMenuImageLabel.place_forget()
    rightMenuImageLabel.place_forget() #removes all of the default widgets except the design images from the confirm diffraction type screen
    
    global gratingState
    gratingState = BooleanVar() #declares global boolean variable gratingState
    gratingState.set(systemValues[13])

    global screenLength
    screenLength= 6.4 #sets the approximate value for the screen length in metres   #3.62
    
    global rayLineCanvas
    rayLineCanvas = Canvas(mainMenu, bg='#f8f4f4', border=0)
    rayLineCanvas.place(relwidth=1, relheight=1, relx = 0, rely = 0, anchor = "nw") #defines and places a full-screen canvas for the ray lines to be plotted on

    global intensityProfileCanvas
    intensityProfileCanvas = Canvas(mainMenu, bg='#f8f4f4', border=0)
    intensityProfileCanvas.place(relwidth=0.153, relheight=0.897, relx = 0.58, rely = 0.005, anchor = "nw") #defines and places a canvas for the intensity profile to be
                                                                                                            #plotted on
    global verticalIntensityProfileAxis
    global horizontalIntensityProfileAxis
    #verticalIntensityProfileAxis = intensityProfileCanvas.create_line(0,0,0,1000, fill = "black", width = 30)
    #horizontalIntensityProfileAxis = intensityProfileCanvas.create_line(0,445,500,445, fill = "black", width = 12) #creates lines for the axes of the intensity profile

    global screenPosition
    screenPosition = [0.56,0.4165] #sets the global constant position for the centre of the screen

    global singleSlitCentrePosition
    singleSlitCentrePosition = [0.425,0.4165] #defines the global list for the position of the centre of the slit of the single-slit grating

    global upperDoubleSlitCentrePosition
    upperDoubleSlitCentrePosition = [0.425,0.3795] #defines the global list for the position of the centre of the upper slit of the double-slit grating

    global lowerDoubleSlitCentrePosition
    lowerDoubleSlitCentrePosition = [0.425,0.4535] #defines the global list for the position of the centre of the lower slit of the double-slit grating

    global diffractionGratingSlitPositions
    diffractionGratingSlitPositions = []
    for x in range(0,10):
        diffractionGratingSlitPositions.append([0.4235, 0.0727 + (x*0.076)]) #defines the global 2D list for the positions of the centres of each slit of the
                                                                             #diffraction grating
    
    try:
        newSystemNoTypeLabel.place_forget()
    except(NameError):
        print("No error message to remove.") #removes the message informing the user to select a diffraction type if it is present on the screen. If this is not
                                             #present, an output message confirming this exception has run is printed.
        
    #Code to create diffraction environment window
    global lowerGrating
    global upperGrating
    global middleGrating
    global gratingObjectsList
    
    if chosenDiffractionType.get() ==  "Single-Slit":
        diffractionSimulatorTypeText = "Single-Slit Wave Diffraction Simulator"
        if systemValues[0] != "None":
            mainMenu.title(systemValues[0]) #If a previously saved system is loaded, its file name is used as the window title.
        else:
            mainMenu.title(diffractionSimulatorTypeText) #if the user has selected the single-slit diffraction type, then set title of window to 'Single-Slit
                                                            #Diffraction Simulator'
        diffractionSimulatorTypeText = "Single-Slit Wave \nDiffraction Simulator"

        upperGrating = SimulationApparatus(0.3, 0.007, "singleSlitGratingObjectIcon.png")
        lowerGrating = SimulationApparatus(0.3, 0.462, "singleSlitGratingObjectIcon.png") #creates two instances of simuationApparatus for each part of the single-slit
                                                                                          #grating
    elif chosenDiffractionType.get() ==  "Double-Slit":
        diffractionSimulatorTypeText = "Double-Slit Wave Diffraction Simulator"
        if systemValues[0] != "None":
            mainMenu.title(systemValues[0]) #If a previously saved system is loaded, its file name is used as the window title.
        else:
            mainMenu.title(diffractionSimulatorTypeText) #if the user has selected the single-slit diffraction type, then set title of window to 'Double-Slit
                                                            #Diffraction Simulator'
        diffractionSimulatorTypeText = "Double-Slit Wave \nDiffraction Simulator"
        
        upperGrating = SimulationApparatus(0.3, 0.007, "lowerUpperDoubleSlitGratingIcon.png")
        middleGrating = SimulationApparatus(0.3, 0.418, "middleDoubleSlitGratingIcon.png")
        lowerGrating = SimulationApparatus(0.35, 0.499, "lowerUpperDoubleSlitGratingIcon.png") #creates three instances of simuationApparatus for each part of the
                                                                                                #single-slit grating
    else:
        diffractionSimulatorTypeText = "Diffraction-Grating Wave Diffraction Simulator"
        if systemValues[0] != "None":
            mainMenu.title(systemValues[0]) #If a previously saved system is loaded, its file name is used as the window title.
        else:
            mainMenu.title(diffractionSimulatorTypeText) #if the user has selected the diffraction-grating diffraction type, then set title of window to 'Diffraction
                                                        #Grating Simulator'
        diffractionSimulatorTypeText = "Diffraction-\nGrating Wave Diffraction \nSimulator"

        gratingObjectsList = []
        for x in range(0,11):
            currentGratingObject = SimulationApparatus(0.3, 0.0037 + (x*0.0825), "diffractionGratingObjectIcon.png")
            gratingObjectsList.append(currentGratingObject) #creates eleven instances of simuationApparatus for each part of the diffraction grating and stores them in
                                                            #a list so that they can be iteratively accessed
        
    global settingsFrame
    settingsFrame = Frame(mainMenu,
                          bg='#dedede',
                          border=5,
                          relief='groove',
                          width=480,
                          height=int(windowHeight)) #defines a frame for the right-side of the screen's UI elements
    settingsFrame.place(relx = 1, rely = 0, anchor = 'ne') #places this frame in the top-right corner of the user's screen
    
    settingsTextLabel = Label(settingsFrame,
                              text="Settings",
                              justify="center",
                              bg='#c2c2c2',
                              border=5,
                              relief='groove',
                              padx=160,
                              pady=20,
                              font=('Arial', 22, 'bold'))
    settingsTextLabel.place(relx=0.5, rely = -0.005, anchor = 'n') #sets text and text settings of the settings text label and places it

    #global intensityProfileAxesLabel
    #intensityProfileAxesIcon = PhotoImage(file = "intensityProfileIcon.png")
    #intensityProfileAxesLabel = Label(mainMenu,
                                      #image = intensityProfileAxesIcon)
    #intensityProfileAxesLabel.image = intensityProfileAxesIcon #sets the image settings for the label which shows the intensity profile axes

    global intensityProfileIndicatorLabel
    intensityProfileIndicatorLabel = Label(mainMenu, text = "Intensity Profile", font=('Arial', 15)) #sets text and text settings for the label to indicate the intensity
                                                                                                        #profile below it
    
    global viewType
    viewType = StringVar()
    viewType.set(systemValues[16]) #declares and initialises the value of the view type
    
    global laserState
    laserState = BooleanVar()
    laserState.set(systemValues[12]) #declares and initialises the value of the laser state
    laserStateButton = Checkbutton(settingsFrame,
                                   text=" Laser Light State (ON/OFF)",
                                   variable=laserState,
                                   onvalue=True,
                                   offvalue=False) #sets text, variable and on/off values for the button which controls the value of laserState
    laserStateButton.config(bg="#dedede",
                            activebackground="#dedede",
                            font=("Arial", 15),
                            border=0,
                            relief="raised",
                            padx=10,
                            pady=5,
                            command=toggleLaserState) #sets the visual properties of the check button which controls the value of laserState
    laserStateButton.place(relx=0.02, rely = 0.09, anchor = 'nw') #places the check button controlling laserState's value
    
    global wavelength
    wavelength = DoubleVar() #declares global decimal variable wavelength
    wavelength.set(systemValues[2]) #initialises the wavelength value as the corresponding value held in systemValues

    global wavelengthInputErrorLabel
    wavelengthInputErrorLabel = Label(settingsFrame,
                                          text="Please enter a suitable value.",
                                          justify="center",
                                          border = 0,
                                          bg='#dedede',
                                          fg='red',
                                          font=('Arial', 10)) #defines the error message label which is displayed if an invalid wavelength value is entered
    global wavelengthSlider
    wavelengthSlider = Scale(settingsFrame,
                             showvalue=1,
                             bg = '#dedede',
                             variable = wavelength,
                             from_=380,
                             border=0,
                             to=700,
                             length = 120,
                             orient=HORIZONTAL,
                             resolution=0.001,
                             command = updateWavelengthValueFromSlider) #creates a slider for the value of wavelength accurate to 3 decimal places
    #runs updateWavelengthValueFromSlider every time the slider is moved to a new value
    #so that the diffraction pattern and value in the entry box for wavelength are updated
    #upon each change to the wavelength
    wavelengthSlider.place(relx=0.04, rely = 0.215, anchor = 'nw') #places the wavelength slider in the settings tab


    global stringWavelength #declares a variable to hold the string value of wavelength for the entry box
    stringWavelength = StringVar()
    stringWavelength.set(str(wavelength.get())) #initialises this variable to have the string version of the intitial wavelength value
    global wavelengthSliderValueLabel #makes the wavelength entry box accessible throughout the program when needed by declaring it as global
    wavelengthSliderValueLabel = Entry(settingsFrame,
                                       textvariable = stringWavelength,
                                       justify = "center",
                                       width=8) 
    wavelengthSliderValueLabel.place(relx=0.33, rely = 0.225, anchor = 'nw') #defines and places the wavelength entry box
    updateWavelengthValueFromSlider("initialSet") #initially runs the function to update the wavelength value to correctly set the value in the entry box
    wavelengthSliderValueLabel.bind('<FocusOut>', updateWavelengthValueFromEntry)
    wavelengthSliderValueLabel.bind('<Return>', updateWavelengthValueFromEntry) #runs updateWavelengthValueFromEntry every time the entry box's value is changed
                                                                                #so that the diffraction pattern and value in the slider for wavelength are updated
                                                                                #upon each change to the wavelength
    global wavelengthSettingsLabel
    wavelengthSettingsLabel = Label(settingsFrame,
                                    text="Wavelength [λ] (nm)",
                                    bg = '#dedede',
                                    font=('Arial', 12))
    wavelengthSettingsLabel.place(relx = 0.5, rely = 0.222, anchor = 'nw') #defines and places the wavelength text label

    global slitSeparation
    slitSeparation = DoubleVar()
    slitSeparation.set(systemValues[17]) #declares and initialises the slitSeparation value as the corresponding value held in systemValues

    global slitSeparationInputErrorLabel
    slitSeparationInputErrorLabel = Label(settingsFrame,
                                          text="Please enter a suitable value.",
                                          justify="center",
                                          border = 0,
                                          bg='#dedede',
                                          fg='red',
                                          font=('Arial', 10)) #defines the error message label which is displayed if an invalid slitSeparation value is entered
    global slitSeparationSlider
    slitSeparationSlider = Scale(settingsFrame,
                                 showvalue=1,
                                 bg = '#dedede',
                                 variable = slitSeparation,
                                 from_=1,
                                 border=0,
                                 to=2,
                                 length = 120,
                                 orient=HORIZONTAL,
                                 resolution=0.001,
                                 command = updateSlitSeparationValueFromSlider) #creates a slider for the value of slitSeparation accurate to 3 decimal places
    #runs updateSlitSeparationValueFromSlider every time the slider is changed to a new value
    #so that the diffraction pattern and value in the entry box for slitSeparation are updated
    #upon each change to the slitSeparation
    slitSeparationSlider.place(relx=0.04, rely = 0.265, anchor = 'nw') #places the slitSeparation slider in the settings tab


    global stringSlitSeparation #declares a variable to hold the string value of slitSeparation for the entry box
    stringSlitSeparation = StringVar()
    stringSlitSeparation.set(str(slitSeparation.get())) #initialises this variable to have the string version of the intitial slitSeparation value
    global slitSeparationSliderValueLabel #makes the slitSeparation entry box accessible throughout the program when needed by declaring it as global
    slitSeparationSliderValueLabel = Entry(settingsFrame,
                                       textvariable = stringSlitSeparation,
                                       justify = "center",
                                       width=8) 
    slitSeparationSliderValueLabel.place(relx=0.33, rely = 0.275, anchor = 'nw') #defines and places the slitSeparation entry box
    updateSlitSeparationValueFromSlider("initialSet") #initially runs the function to update the slitSeparation value to correctly set the value in the entry box
    slitSeparationSliderValueLabel.bind('<FocusOut>', updateSlitSeparationValueFromEntry)
    slitSeparationSliderValueLabel.bind('<Return>', updateSlitSeparationValueFromEntry) #runs updateslitSeparationValueFromEntry every time the entry box's value is
                                                                                #changed so that the diffraction pattern and value in the slider for slitSeparation are
                                                                                #updated upon each change to the slitSeparation
    global slitSeparationSettingsLabel
    slitSeparationSettingsLabel = Label(settingsFrame,
                                    text="Slit Separation [s] (μm)",
                                    bg = '#dedede',
                                    font=('Arial', 12))
    slitSeparationSettingsLabel.place(relx = 0.5, rely = 0.272, anchor = 'nw') #defines and places the slitSeparation text label

    global screenGratingDistance
    screenGratingDistance = DoubleVar()
    screenGratingDistance.set(systemValues[3]) #declares and initialises the screen-grating distance value as the corresponding value held in systemValues

    global screenGratingArrowCanvas
    screenGratingArrowCanvas = Canvas(mainMenu, bg='#f8f4f4', border=0)
    screenGratingArrowCanvas.place(relwidth=0.27, relheight=0.1, relx = 0.565, rely = 0.9, anchor = "ne")#defines and places a canvas for the screen-grating distance arrow

    leftScreenGratingArrowIcon = PhotoImage(file = "screenGratingDistanceArrowIconLeft.png")
    global leftScreenGratingArrowLabel
    leftScreenGratingArrowLabel = Label(screenGratingArrowCanvas, image = leftScreenGratingArrowIcon, padx=0, border=0)
    leftScreenGratingArrowLabel.image = leftScreenGratingArrowIcon #defines the label for the left arrow of the screen-grating distance arrow
    
    rightScreenGratingArrowIcon = PhotoImage(file = "screenGratingDistanceArrowIconRight.png")
    global rightScreenGratingArrowLabel
    rightScreenGratingArrowLabel = Label(screenGratingArrowCanvas, image = rightScreenGratingArrowIcon, padx=0, border=0)
    rightScreenGratingArrowLabel.image = rightScreenGratingArrowIcon #defines the label for the left arrow of the screen-grating distance arrow

    global screenGratingDistanceScaleLabel
    screenGratingDistanceScaleLabel = Label(screenGratingArrowCanvas, text = "D (m)", font=('Arial', 15))

    global screenGratingDistanceInputErrorLabel
    screenGratingDistanceInputErrorLabel = Label(settingsFrame,
                                          text="Please enter a suitable value.",
                                          justify="center",
                                          border = 0,
                                          bg='#dedede',
                                          fg='red',
                                          font=('Arial', 10)) #defines the error message label which is displayed if an invalid screenGratingDistance value is entered
    global screenGratingDistanceSlider
    screenGratingDistanceSlider = Scale(settingsFrame,
                                        showvalue=1,
                                        bg = '#dedede',
                                        variable = screenGratingDistance,
                                        from_=0.5,
                                        border=0,
                                        to=2.0,
                                        length = 120,
                                        orient=HORIZONTAL,
                                        resolution=0.001,
                                        command = updateScreenGratingDistanceValueFromSlider)
    #creates a slider for the value of screenGratingDistance accurate to 3 decimal places
    #runs updateScreenGratingDistanceValueFromSlider every time the
    #slider is changed to a new value so that the diffraction pattern and value in the
    #entry box for slitSeparation are updated upon each change to the slitSeparation
    screenGratingDistanceSlider.place(relx=0.04, rely = 0.325, anchor = 'nw') #places the screenGratingDistance slider in the settings tab



    global stringScreenGratingDistance #declares a variable to hold the string value of screenGratingDistance for the entry box
    stringScreenGratingDistance = StringVar()
    stringScreenGratingDistance.set(str(screenGratingDistance.get())) #initialises this variable to have the string version of the intitial screenGratingDistance value
    global screenGratingDistanceSliderValueLabel #makes the screenGratingDistance entry box accessible throughout the program when needed by declaring it as global
    screenGratingDistanceSliderValueLabel = Entry(settingsFrame,
                                       textvariable = stringScreenGratingDistance,
                                       justify = "center",
                                       width=8) 
    screenGratingDistanceSliderValueLabel.place(relx=0.33, rely = 0.335, anchor = 'nw') #defines and places the screenGratingDistance entry box
    updateScreenGratingDistanceValueFromSlider("initialSet") #initially runs the function to update the screenGratingDistance value to correctly set the value in the
                                                                    #entry box
    screenGratingDistanceSliderValueLabel.bind('<FocusOut>', updateScreenGratingDistanceValueFromEntry)
    screenGratingDistanceSliderValueLabel.bind('<Return>', updateScreenGratingDistanceValueFromEntry) #runs updateScreenGratingDistanceValueFromEntry every
                                                                                #time the entry box's value is changed so that the diffraction pattern and value in the
                                                                                #slider for screenGratingDistance are updated upon each change to the screenGratingDistance
    global screenGratingDistanceSettingsLabel
    screenGratingDistanceSettingsLabel = Label(settingsFrame,
                                               text="Screen-Grating Distance \n[D] (m)",
                                               bg = '#dedede',
                                               justify='left',
                                               font=('Arial', 12))
    screenGratingDistanceSettingsLabel.place(relx = 0.5, rely = 0.322, anchor = 'nw') #defines and places the screenGratingDistance text label

    global rulerState
    rulerState = BooleanVar()
    rulerState.set(systemValues[8]) #declares and initialises the ruler state value as the corresponding value held in systemValues
    rulerStateButton = Checkbutton(settingsFrame,
                                   text=" Ruler",
                                   variable=rulerState,
                                   onvalue=True,
                                   offvalue=False,
                                   command=toggleRulerState) #sets text, variable and on/off values for the button which controls the value of rulerState
    rulerStateButton.config(bg="#dedede",
                            activebackground="#dedede",
                            font=("Arial", 15),
                            border=0,
                            relief="raised",
                            padx=10,
                            pady=5) #sets the visual properties of the check button which controls the value of rulerState
    rulerStateButton.place(relx=0.02, rely = 0.37, anchor = 'nw') #places the check button controlling rulerState's value

    global intensityProfileState
    intensityProfileState = BooleanVar()
    intensityProfileState.set(systemValues[11]) #declares and initialises the intensity profile state value as the corresponding value held in systemValues
    global intensityProfileStateButton
    intensityProfileStateButton = Checkbutton(settingsFrame,
                                   text=" Intensity Profile",
                                   variable=intensityProfileState,
                                   onvalue=True,
                                   offvalue=False) #sets text, variable and on/off values for the button which controls the value of intensityProfileState
    intensityProfileStateButton.config(bg="#dedede",
                                       activebackground="#dedede",
                                       font=("Arial", 15),
                                       border=0,
                                       relief="raised",
                                       padx=10,
                                       pady=5,
                                       command = toggleIntensityProfile) #sets the visual properties of the check button which controls the value of intensityProfileState
    intensityProfileStateButton.place(relx=0.02, rely = 0.41, anchor = 'nw') #places the check button controlling intensityProfileState's value

    global protractorState
    protractorState = BooleanVar()
    protractorState.set(systemValues[9]) #declares and initialises the protractor state value as the corresponding value held in systemValues
    protractorStateButton = Checkbutton(settingsFrame,
                                   text=" Protractor",
                                   variable=protractorState,
                                   onvalue=True,
                                   offvalue=False,
                                        command=toggleProtractorState) #sets text, variable and on/off values for the button which controls the value of protractorState
    protractorStateButton.config(bg="#dedede",
                            activebackground="#dedede",
                            font=("Arial", 15),
                            border=0,
                            relief="raised",
                            padx=10,
                            pady=5) #sets the visual properties of the check button which controls the value of protractorState
    protractorStateButton.place(relx=0.55, rely = 0.41, anchor = 'nw') #places the check button controlling protractorState's value

    global screenViewState
    screenViewState = BooleanVar()
    screenViewState.set(systemValues[10]) #declares and initialises the screen view state value as the corresponding value held in systemValues
    global screenViewStateButton
    screenViewStateButton = Checkbutton(settingsFrame,
                                   text=" Screen View",
                                   variable=screenViewState,
                                   onvalue=True,
                                   offvalue=False) #sets text, variable and on/off values for the button which controls the value of screenViewState
    screenViewStateButton.config(bg="#dedede",
                            activebackground="#dedede",
                            font=("Arial", 15),
                            border=0,
                            relief="raised",
                            padx=10,
                            pady=5,
                            command=toggleScreenView) #sets the visual properties of the check button which controls the value of screenViewState
    screenViewStateButton.place(relx=0.02, rely = 0.45, anchor = 'nw') #places the check button controlling screenViewState's value

    saveSetupButton = Button(settingsFrame, #defines a button with the text 'Save Setup' in the settings tab
                             text = 'Save Setup')
    saveSetupButton.place(relx=0.05, rely = 0.5, anchor = 'nw') #places the button at the correct position
    saveSetupButton.config(font=('Arial', 12, 'bold'),
                          relief='raised',
                          border=2,
                          padx=40,
                          pady=2,
                          command= saveSetupPrompt) #sets the font settings of the button
                                                      #sets the relief of the button to raised and border size of the button to 2 to make it visible enough.
                                                      #sets the padding of the button to 40 in the x direction and 2 in the y direction so that the button is large enough
                                                      #causes saveSetupPrompt() to run when the save setup button is clicked
    loadSetupButton = Button(settingsFrame, #defines a button with the text 'Load Setup' in the settings tab
                             text = 'Load Setup')
    loadSetupButton.place(relx=0.53, rely = 0.5, anchor = 'nw') #places the button at the correct position
    loadSetupButton.config(font=('Arial', 12, 'bold'),
                          relief='raised',
                          border=2,
                          padx=35,
                          pady=2,
                          command= loadSetupPrompt) #sets the font settings of the button
                                                      #sets the relief of the button to raised and border size of the button to 2 to make it visible enough.
                                                      #sets the padding of the button to 35 in the x direction and 2 in the y direction so that the button is large enough
                                                      #causes loadSetupPrompt() to run when the save setup button is clicked
    
    global switchViewButton
    switchViewButton = Button(settingsFrame, #defines a button with the text 'Switch to Simple View' in the settings tab
                             text = 'Switch to Simple View')
    switchViewButton.place(relx=0.05, rely = 0.55, anchor = 'nw') #places the button at the correct position
    switchViewButton.config(font=('Arial', 10, 'bold'),
                          relief='raised',
                          border=2,
                          padx=9,
                          pady=8,
                          command= switchViewPrompt) #sets the font settings of the button
                                                      #sets the relief of the button to raised and border size of the button to 2 to make it visible enough.
                                                      #sets the padding of the button to 9 in the x direction and 8 in the y direction so that the button is large enough
                                                      #causes switchViewPrompt() to run when the save setup button is clicked

    mainMenuButton = Button(settingsFrame, #defines a button with the text 'Return to Main Menu' in the settings tab
                             text = 'Return to Main Menu')
    mainMenuButton.place(relx=0.53, rely = 0.55, anchor = 'nw') #places the button at the correct position
    mainMenuButton.config(font=('Arial', 10, 'bold'),
                          relief='raised',
                          border=2,
                          padx=9,
                          pady=8,
                          command= mainMenuReturnFromEnvironment) #sets the font settings of the button
                                                      #sets the relief of the button to raised and border size of the button to 2 to make it visible enough.
                                                      #sets the padding of the button to 9 in the x direction and 8 in the y direction so that the button is large enough
                                                      #causes mainMenuReturnFromEnvironment() to run when the save setup button is clicked

    screenViewTitleLabel = Label(settingsFrame,
                              text="Screen View",
                              justify="center",
                              bg='#c2c2c2',
                              border=5,
                              relief='groove',
                              padx=125,
                              pady=12,
                              font=('Arial', 22, 'bold'))
    screenViewTitleLabel.place(relx=0.5, rely = 0.61, anchor = 'n') #sets text and text settings of the screen view title text label and places it

    global screenViewCanvas
    screenViewCanvas = Canvas(settingsFrame,
                          bg='#000000',
                          border=0,
                          width=480,
                          height=400) #defines a dark frame for the elements of the screen view environment
    
    global disabledScreenViewLabel
    disabledScreenViewLabel = Label(settingsFrame,
                                    bg='#dedede',
                                    text="Click the 'Screen in place'\nbox to enable the screen\nview.",
                                    justify="center",
                                    border=0,
                                    padx=10,
                                    pady=12,
                                    font=('Arial', 21)) #defines a label which displays when the screen view is disabled
    if screenViewState.get() == False:
        disabledScreenViewLabel.place(relx=0.5, rely = 0.725, anchor = 'n') #places disabled screen view label if it is disabled
    else:
        screenViewCanvas.place(relx = 1, rely = 0.6808, anchor = 'ne') #places this frame in the bottom-right corner of the user's screen if the screen view is enabled

    global viewTypeLabel
    viewTypeLabel = Label(mainMenu,
                          text="Detailed View",
                          justify="center",
                          bg='#c2c2c2',
                          border=5,
                          relief='groove',
                          padx=50,
                          pady=10,
                          font=('Arial', 20, 'bold'))
    viewTypeLabel.place(relx = 0, rely = 0, anchor = 'nw') #defines a label which displays the type of view (simple or detailed) which is enabled
    
    laserImageIconUnscaled = PhotoImage(file="laserIcon.png")
    laserImageIcon = laserImageIconUnscaled.subsample(4,4)
    global laserImageLabel
    laserImageLabel = Label(mainMenu, image=laserImageIcon) #defines and sets the image label which will display the laser
    laserImageLabel.place(relx=0.02, rely = 0.418, anchor='nw') #places this image in the correct position
    laserImageLabel.image = laserImageIcon #adds permanent reference for the laser image to prevent it not being displayed correctly

    laserStateONIconUnscaled = PhotoImage(file="ONSwitchIcon.png")
    laserStateONIcon = laserStateONIconUnscaled.subsample(4,4)
    global laserStateONIconLabel
    laserStateONIconLabel = Label(mainMenu, image=laserStateONIcon, border=0) #defines and sets the image label which will display when the laser is on
    laserStateONIconLabel.image = laserStateONIcon #adds permanent reference for the laser on icon image to prevent it not being displayed correctly

    laserStateOFFIconUnscaled = PhotoImage(file="OFFSwitchIcon.png")
    laserStateOFFIcon = laserStateOFFIconUnscaled.subsample(4,4)
    global laserStateOFFIconLabel
    laserStateOFFIconLabel = Label(mainMenu, image=laserStateOFFIcon, border=0) #defines and sets the image label which will display when the laser is off
    laserStateOFFIconLabel.image = laserStateOFFIcon #adds permanent reference for the laser off icon image to prevent it not being displayed correctly

    if laserState.get() == True:
        laserStateONIconLabel.place(relx=0.0335, rely = 0.435, anchor='nw') #places the image for the switched on laser if it is enabled
    else:
        laserStateOFFIconLabel.place(relx=0.0335, rely = 0.435, anchor='nw') #places the image for the switched off laser if it is disabled

    global screen
    screen = SimulationApparatus(0.56, 0.0037, "screenIcon.png") #creates an instance of simuationApparatus for the screen

    global metreScaleArrowLabel
    metreScaleArrowIcon = PhotoImage(file = "metreScaleArrowIcon.png")
    metreScaleArrowLabel = Label(mainMenu, image=metreScaleArrowIcon)
    metreScaleArrowLabel.image = metreScaleArrowIcon #defines the image label which will display the scale of the simulation

    global informationBoxFrame
    informationBoxFrame = Frame(mainMenu,
                                bg='#dedede',
                                border=5,
                                relief='groove',
                                height=int(windowHeight)) #defines a frame for the information text boxes

    global informationBoxTitleLabel
    informationBoxTitleLabel = Label(informationBoxFrame,
                                     text="Information",
                                     justify="center",
                                     bg='#c2c2c2',
                                     border=5,
                                     relief='groove',
                                     padx=50,
                                     pady=20,
                                     font=('Arial', 22, 'bold')) #sets text and text settings of the information box title

    global informationLabelMain
    informationLabelMain = Label(informationBoxFrame,
                                 bg='#dedede',
                                 border=0,
                                 padx=0,
                                 pady=5,
                                 font=('Arial', 11),
                                 justify = "left",
                                 text=('Welcome to the ' + diffractionSimulatorTypeText + '! Here you can \nlearn how light diffracts as it \napproaches a gap of ' +
                                'similar size to \nits wavelength. \n\nTo make light diffract (spread out) \nmore or less when it passes through \nthe ' +
                                'grating, you can toggle the \nsettings to the right. \n\nSlit separation is the size of the \ngap(s) on the grating. Screen-grating ' +
                                '\ndistance is the distance between the \nscreen and grating, which will move \nthe grating back or forward upon \nbeing changed. \n\n' +
                                'Wavelength is the wavelength of the \nlight on a scale between 380 to 700 \nnanometres (which is the spectrum \nof visible light). ' +
                                'Changing this will \nalso alter what colour the light \nappears as. \n\nTo calculate any of the above \nvariables for yourself using '
                                'the \nothers, you can use the below \nformula:'))
                                #sets text and text settings of the label for the main body of text in the informationbox
    
    global informationLabelFormulaeTitle1
    informationLabelFormulaeTitle1 = Label(informationBoxFrame,
                                           bg='#dedede',
                                           border=0,
                                           padx=0,
                                           pady=0,
                                           font=('Arial', 11, "bold"),
                                           justify = "left",
                                           text = "Double Slit:") #sets the text and text settings of the label for the 'Double-slit:' bold text for the formula section
                                                                    #of the information box
    global informationLabelFormulaeFringeSpacing
    informationLabelFormulaeFringeSpacing = Label(informationBoxFrame,
                                                  bg='#dedede',
                                                  border=0,
                                                  padx=0,
                                                  pady=0,
                                                  font=('Arial', 11),
                                                  justify = "left",
                                                  text = "Fringe Spacing = λD/s") #sets the text and text settings of the label for fringe spacing formula text for the
                                                                                  #formula section of the information box
    global informationLabelFormulaeTitle2
    informationLabelFormulaeTitle2 = Label(informationBoxFrame,
                                           bg='#dedede',
                                           border=0,
                                           padx=0,
                                           pady=0,
                                           font=('Arial', 11, "bold"),
                                           justify = "left",
                                           text = "Diffraction Grating and \nSlit Separation:") #sets the text and text settings of the label for the 'Diffraction
                                                                                                #Grating and Slit Separation:' bold text for the formula section
                                                                                                #of the information box
    global informationLabelFormulaeAndSymbols
    informationLabelFormulaeAndSymbols = Label(informationBoxFrame,
                                               bg='#dedede',
                                               border=0,
                                               padx=0,
                                               pady=0,
                                               font=('Arial', 11),
                                               justify = "left",
                                               text = ("s*sinθ = nλ \n\n(n is the position of the maxima, e.g, \nn=0 for the central maxima, n=1 for \nboth adjacent "+
                                                "maximas to the central \nmaxima, etc.")) #sets the text and text settings of the label for second formula and the
                                                                                        #explanation of its symbols
    global informationLabelThetaExplanation
    informationLabelThetaExplanation = Label(informationBoxFrame,
                                               bg='#dedede',
                                               border=0,
                                               padx=0,
                                               pady=0,
                                               font=('Arial', 11),
                                               justify = "left",
                                               text ="(θ is the angle the rayline to maxima \nn from the slit makes to the central \nmaxima line)") #sets the text and text
                                                #settings for the label which explains what the symbol θ means in the formulae
    if viewType.get() == "Detailed":
        if intensityProfileState.get() == True:
            intensityProfileIndicatorLabel.place(relx=0.65, rely=0.96, anchor = "center")
            intensityProfileCanvas.place(relwidth=0.153, relheight=0.897, relx = 0.58, rely = 0.005, anchor = "nw") #places the canvas for the intensity profile to be
                                                                                                                    #plotted on
            verticalIntensityProfileAxis = intensityProfileCanvas.create_line(0,0,0,1000, fill = "black", width = 30)
            horizontalIntensityProfileAxis = intensityProfileCanvas.create_line(0,445,500,445, fill = "black", width = 12)
            #creates lines for the axes of the intensity profile
        metreScaleArrowLabel.place(relx = 0.02, rely = 0.935, anchor = 'nw') #displays the scale label if detailed view is initially enabled
    else:
        viewTypeLabel.config(text = "Simple View") 
        switchViewButton.config(text="Switch to Detailed View", padx=3)
        informationBoxFrame.place(relx = 0.754, rely = 0, relwidth = 0.165, anchor = 'ne') #places this frame in the top-right corner of the user's screen
        informationBoxTitleLabel.place(relx=0.495, rely = -0.005, anchor = 'n') #places the information box title text label
        informationLabelMain.place(relx=0.02, rely=0.085, anchor = "nw") #places the label for the main body of text in the informationbox
                                                                         #(anchored to north-west so the first line always starts in the same position)
        if chosenDiffractionType.get() ==  "Single-Slit" or chosenDiffractionType.get() ==  "Double-Slit":
            informationLabelThetaExplanation.place(relx=0.02, rely=0.855, anchor = "nw")
            informationLabelFormulaeAndSymbols.place(relx=0.02, rely=0.73, anchor = "nw")
            informationLabelFormulaeTitle2.place(relx=0.02, rely=0.71, anchor = "nw")
            informationLabelFormulaeFringeSpacing.place(relx=0.02, rely=0.69, anchor = "nw")
            informationLabelFormulaeTitle1.place(relx=0.02, rely=0.67, anchor = "nw") #adjusts the text labels below the main one to these positions if single-slit or
                                                                                    #double-slit options have been selected so that they appear with the correct spacing
                                                                                    #below the main text body of the information box
        else:
            informationLabelFormulaeAndSymbols.config(text = ("s*sinθ = nλ \n(n is the position of the maxima, e.g, \nn=0 for the central maxima, n=1 for \nboth adjacent "+
                                                    "maximas to the central \nmaxima, etc.")) #alters the spacing the text of the label for second formula and the
                                                                                            #explanation of its symbols
            informationLabelThetaExplanation.place(relx=0.02, rely=0.855, anchor = "nw")
            informationLabelFormulaeAndSymbols.place(relx=0.02, rely=0.745, anchor = "nw")
            informationLabelFormulaeTitle2.place(relx=0.02, rely=0.725, anchor = "nw")
            informationLabelFormulaeFringeSpacing.place(relx=0.02, rely=0.705, anchor = "nw")
            informationLabelFormulaeTitle1.place(relx=0.02, rely=0.685, anchor = "nw") #adjusts the text labels below the main one to these positions if diffraction-
                                                                                        #grating option has been selected so that they appear with the correct spacing
                                                                                        #below the main text body of the information box
        

    gratingStateButton = Checkbutton(settingsFrame,
                                   text=" Grating in place",
                                   variable=gratingState,
                                   onvalue=True,
                                   offvalue=False) #sets text, variable and on/off values for the button which controls the value of gratingState
    gratingStateButton.config(bg="#dedede",
                              activebackground="#dedede",
                              font=("Arial", 15),
                              border=0,
                              relief="raised",
                              padx=10,
                              pady=5,
                              command = toggleGratingState) #sets the visual properties of the check button which controls the value of gratingState
    gratingStateButton.place(relx=0.02, rely = 0.13, anchor = 'nw') #places the check button controlling gratingState's value
    
    global screenState
    screenState = BooleanVar() #declares global boolean variable screenState
    screenState.set(systemValues[14])
    screenStateButton = Checkbutton(settingsFrame,
                                   text=" Screen in place",
                                   variable=screenState,
                                   onvalue=True,
                                   offvalue=False) #sets text, variable and on/off values for the button which controls the value of screenState
    screenStateButton.config(bg="#dedede",
                             activebackground="#dedede",
                             font=("Arial", 15),
                             border=0,
                             relief="raised",
                             padx=10,
                             pady=5,
                             command = toggleScreenState) #sets the visual properties of the check button which controls the value of screenState
    screenStateButton.place(relx=0.02, rely = 0.17, anchor = 'nw') #places the check button controlling screenState's value
    updateDiffractionPattern() #displays initial diffraction pattern

    global ruler
    global protractor
    if systemValues[4][0] == "initialRulerXCord":
        newRulerXCord = 0.15
    else:
        newRulerXCord = systemValues[4][0]/int(windowWidth)
        
    if systemValues[4][1] == "initialRulerYCord":
        newRulerYCord = 0.81
    else:
        newRulerYCord = systemValues[4][1]/int(windowHeight)
        
    if systemValues[5][0] == "initialProtractorXCord":
        newProtractorXCord = 0.12
    else:
        newProtractorXCord = systemValues[5][0]/int(windowWidth)
        
    if systemValues[5][1] == "initialProtractorYCord":
        newProtractorYCord = 0.67
    else:
        newProtractorYCord = systemValues[5][1]/int(windowHeight)
        
    ruler = MeasuringEquipment(newRulerXCord, newRulerYCord, "rulerIcon.png", int(systemValues[6]), 4, 50) #creates the ruler object
    protractor = MeasuringEquipment(newProtractorXCord, newProtractorYCord, "protractorIcon.png", int(systemValues[7]), 3, 110) #creates the protractor object
    switchViewPrompt()
    switchViewPrompt()

def saveSetupPrompt():
    global saveSystemFrame
    saveSystemFrame = Frame(mainMenu, bg = "#dedede", highlightthickness = 5, highlightbackground="#919191")
    saveSystemFrame.place(relheight = 0.55, relwidth = 0.4, relx = 0.5, rely = 0.45, anchor = "center") #creates a frame for the GUI for the saving process

    global saveSystemTitleLabel
    saveSystemTitleLabel = Label(saveSystemFrame,
                              text="Save System",
                              justify="center",
                              bg='#c2c2c2',
                              border=5,
                              relief='groove',
                              font=('Arial', 22, 'bold'))
    saveSystemTitleLabel.place(relx=0.5, rely = -0.005, relwidth = 1.01, relheight = 0.2, anchor = 'n')
    #sets text and text settings for the title text label for the save GUI and places it

    global saveToSetup1Button
    global saveToFileNumber
    saveToFileNumber = IntVar()
    saveToFileNumber.set("0")
    saveToSetup1Button = Radiobutton(saveSystemFrame, text='Save File 1', justify="left", variable=saveToFileNumber, value=1, command = enterFileName)
    saveToSetup1Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 indicatoron=0)
    try:
        with open('saveFile1.txt', 'r') as file1:
            for line in file1:
                fileNameFromPreviousFile = line.rstrip("\n")
                saveToSetup1Button.config(text = fileNameFromPreviousFile)
                break
            #displays file name of first save file as the text on the button if it is present 
    except(FileNotFoundError):
        saveToSetup1Button.config(text="Empty Save File",
                                      justify="center",
                                      bg='#c2c2c2',
                                      border=5,
                                      relief='groove',
                                      font=('Arial', 22, 'bold'))
        #displays empty if no save file 1 present

    saveToSetup1Button.place(relx=0.5, rely = 0.23, relwidth = 0.95, relheight = 0.225, anchor = 'n')
    #sets the settings for the button responsible for allowing the user to save their setup to save file 1. It will display the file name here if a save file is present
    #or say empty if it is not and will allow the user to overwrite it in either case by clicking on it.
    
    global saveToSetup2Button
    saveToSetup2Button = Radiobutton(saveSystemFrame, text='Save File 2', justify="left", variable=saveToFileNumber, value=2, command = enterFileName)
    saveToSetup2Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 indicatoron=0)
    
    try:
        with open('saveFile2.txt', 'r') as file2:
            for line in file2:
                fileNameFromPreviousFile = line.rstrip("\n")
                saveToSetup2Button.config(text = fileNameFromPreviousFile)
                break
            #displays file name of the second save file as the text on the button if it is present 
    except(FileNotFoundError):
        saveToSetup2Button.config(text="Empty Save File",
                                      justify="center",
                                      bg='#c2c2c2',
                                      border=5,
                                      relief='groove',
                                      font=('Arial', 22, 'bold'))
        #displays empty if no save file 2 present

    saveToSetup2Button.place(relx=0.5, rely = 0.48, relwidth = 0.95, relheight = 0.225, anchor = 'n')
    #sets the settings for the button responsible for allowing the user to save their setup to save file 2. It will display the file name here if a save file is present
    #or say empty if it is not and will allow the user to overwrite it in either case by clicking on it.                                                                        #and places it

    global saveToSetup3Button
    saveToSetup3Button = Radiobutton(saveSystemFrame, text='Save File 3', justify="left", variable=saveToFileNumber, value=3, command = enterFileName)
    saveToSetup3Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 indicatoron=0)
    
    try:
        with open('saveFile3.txt', 'r') as file3:
            for line in file3:
                fileNameFromPreviousFile = line.rstrip("\n")
                saveToSetup3Button.config(text = fileNameFromPreviousFile)
                break
            #displays file name of the third save file as the text on the button if it is present 
    except(FileNotFoundError):
        saveToSetup3Button.config(text="Empty Save File",
                                      justify="center",
                                      bg='#c2c2c2',
                                      border=5,
                                      relief='groove',
                                      font=('Arial', 22, 'bold'))
        #displays empty if no save file 3 present

    saveToSetup3Button.place(relx=0.5, rely = 0.73, relwidth = 0.95, relheight = 0.225, anchor = 'n')
    #sets the settings for the button responsible for allowing the user to save their setup to save file 3. It will display the file name here if a save file is present
    #or say empty if it is not and will allow the user to overwrite it in either case by clicking on it.
    
    print("ran saveSetupPrompt successfully") #Confirms that the procedure has finished executing.
    
def enterFileName():
    print("enterFileName ran successfully.") #test output to confirm that enterFileName has run after clicking the radio buttons.
    #Removes previous GUI
    saveToSetup1Button.place_forget()
    saveToSetup2Button.place_forget()
    saveToSetup3Button.place_forget()
    saveSystemTitleLabel.place_forget()
    #Modifies frame and title label so that they have a new size which is appropriate for the user to enter a file name for their saved setup.
    saveSystemFrame.place_forget()
    saveSystemFrame.place(relheight = 0.3, relwidth = 0.3, relx = 0.5, rely = 0.45, anchor = "center")
    saveSystemTitleLabel.place(relx=0.5, rely = -0.005, relwidth = 1.01, relheight = 0.3, anchor = 'n')

    #Declares global variables for each of the widgets created in this procedure as they will be needed to be deleted in the following procedures
    global fileName
    global fileNameEntryBox
    global fileNameEntryLabel
    global fileNameSubmitButton
    global cancelSaveButton

    #Declares and initialises as empty a string variable for the user-entered file name
    fileName = StringVar()
    fileName.set("")
 
    #Creates a label which indicates that to the left on the GUI the user will enter the file name.
    fileNameEntryLabel = Label(saveSystemFrame,
                              text="Save file name:",
                              justify="center",
                              bg = "#dedede",
                               border = 0,
                              font=('Arial', 15, 'bold'))
    fileNameEntryLabel.place(relx=0.01, rely = 0.45, relwidth = 0.35, relheight = 0.2, anchor = 'w')
    
    #Creates an entry box which allows the user to enter their file name.                          
    fileNameEntryBox = Entry(saveSystemFrame, textvariable = fileName, justify="center", font=('Arial', 14, 'bold'))
    fileNameEntryBox.place(relx=0.95, rely = 0.45, relwidth = 0.56, relheight = 0.15, anchor = 'e')
    
    #Creates a button which allows the user to submit their file name and save the setup in the selected file slot.
    fileNameSubmitButton = Button(saveSystemFrame, text='Save', justify="left", command = saveSystem)
    fileNameSubmitButton.config(font=('Arial', 17, 'bold'),
                                 relief='raised',
                                 border=5)
    fileNameSubmitButton.place(relx=0.9, rely = 0.9, relwidth = 0.3, relheight = 0.25, anchor = 'se')

    #Creates a button which allows the user to cancel the saving process.
    cancelSaveButton = Button(saveSystemFrame, text='Cancel', justify="left", command = cancelSaveSystem)
    cancelSaveButton.config(font=('Arial', 17, 'bold'),
                                 relief='raised',
                                 border=5)
    cancelSaveButton.place(relx=0.1, rely = 0.9, relwidth = 0.3, relheight = 0.25, anchor = 'sw')

def cancelSaveSystem():
    print("cancelSaveSystem ran successfully!") #test output to confirm module runs at correct time
    fileNameEntryBox.place_forget()
    fileNameSubmitButton.place_forget()
    cancelSaveButton.place_forget()
    saveSystemFrame.place_forget()
    fileNameEntryLabel.place_forget() #cancels the saving operation and removes the save system GUI

def saveSystem(): #procedure to save the current setup in the correct file
    print("saveSystem ran successfully!") #test output to confirm module runs at correct time
    noEndSpacesFileName = str(fileName.get())
    noEndSpacesFileName = noEndSpacesFileName.rstrip(" ")
    noEndSpacesFileName = noEndSpacesFileName.lstrip(" ")
    fileName.set(noEndSpacesFileName) #removes extra spaces from the file name at either the start or end of the name
    global invalidNameErrorSaveLabel
    #Defines a set of accepted characters for the file name to contain.
    acceptedCharacters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8",
                          "9","(",")","_","-", ",",".","*", " "]
    #Removes any error labels leftover.
    try:
        invalidNameErrorSaveLabel.place_forget()
    except:
        acceptedCharacters = acceptedCharacters
    #creates a suitable error label if the user enters a file name which is too long.
    if len(fileName.get()) > 20:
        invalidNameErrorSaveLabel = Label(saveSystemFrame,
                                            text = "Please enter a shorter file name (less than 20 characters).",
                                            fg="red",
                                          bg = "#dedede",
                                            font = ('Arial', 12))
        invalidNameErrorSaveLabel.place(relx = 0.5, anchor = "center", rely = 0.585)
        return "Too Long"
    #creates a suitable error label if the user enters a file name which is 0 characters long.
    elif len(fileName.get()) < 1:
        invalidNameErrorSaveLabel = Label(saveSystemFrame,
                                            text = "Please enter a longer file name (at least 1 character).",
                                            fg="red",
                                          bg = "#dedede",
                                            font = ('Arial', 13))
        invalidNameErrorSaveLabel.place(relx = 0.5, anchor = "center", rely = 0.585)
        return "Too Long"

    fileNameString = str(fileName.get())

    #checks the file name, if of the correct length, for any invalid characters andcreates a suitable error label if any of these are included.
    for x in range(0,len(fileNameString)):
        if fileNameString[x].lower() not in acceptedCharacters:
            invalidNameErrorSaveLabel = Label(saveSystemFrame,
                                            text = ("Please enter a valid file name (contains characters a-z, A-Z, 0-9,\n brackets, comma, underscore, dash, period, space,"
                                              + " asterisk)."),
                                            fg="red",
                                              bg = "#dedede",
                                            font = ('Arial', 11))
            invalidNameErrorSaveLabel.place(relx = 0.5, anchor = "center", rely = 0.6)
            return "Invalid Character"

    #Accesses the current date through the datetime library.
    current_time = datetime.datetime.now()
    currentDate = (str(current_time.day) + "/" + str(current_time.month) + "/" + str(current_time.year))
    
    #Sets the list of values to be saved.
    saveFileValues = [fileName.get(), currentDate, wavelength.get(), screenGratingDistance.get(), ruler.getNewCords(), protractor.getNewCords(), ruler.getOrientation(),
                      protractor.getOrientation(), rulerState.get(), protractorState.get(), screenViewState.get(), intensityProfileState.get(), laserState.get(),
                      gratingState.get(),screenState.get(), chosenDiffractionType.get(), viewType.get(), slitSeparation.get()]
    print(saveFileValues) #test output to check that suitable values are being saved
    
    #Saves the systems current values from the list above on seperate lines so they are later retrievable.
    saveFile = open(("saveFile" + str(saveToFileNumber.get()) + ".txt"), "w")
    for each in saveFileValues:
        saveFile.write(str(each) + "\n")
    saveFile.close()

    #Displays a label which informs the user that the file has been successfully saved. This is removed once a change is made to the diffraction pattern.
    global successfulSaveLabel
    successfulSaveLabel = Label(mainMenu,
                                text = ("File successfully saved as " + fileNameString + "."),
                                fg= "#06c716",
                                bg = "#f8f4f4",
                                font = ('Arial', 14))

    #Removes the save GUI.
    successfulSaveLabel.place(relx = 0.175, anchor = "nw", rely = 0.018)
    fileNameEntryBox.place_forget()
    fileNameSubmitButton.place_forget()
    cancelSaveButton.place_forget()
    saveSystemFrame.place_forget()
    fileNameEntryLabel.place_forget()
        

def loadSetupPrompt():
    mainMenuReturnFromEnvironment() #brings user back to starting menu screen to load one of their setups

def switchViewPrompt():
    if (viewType.get()) == "Simple":
        viewType.set("Detailed")
        viewTypeLabel.config(text = "Detailed View")
        switchViewButton.config(text = "Switch to Simple View",
                                padx=9)
        metreScaleArrowLabel.place(relx = 0.02, rely = 0.935, anchor = 'nw')
        leftScreenGratingArrowLabel.place(x = 490-(screenGratingDistance.get()*230), rely = 0.5, anchor = 'w')
        rightScreenGratingArrowLabel.place(relx = 0.96, rely = 0.5, anchor = 'e') #if simple view was activated, switches to detailed view and places required labels
        updateScreenGratingDistanceValueFromSlider("switchedView") #adds screen-grating distance label back
        wavelengthSliderValueLabel.place(relx=0.33, rely = 0.225, anchor = 'nw') #places the wavelength entry box
        slitSeparationSliderValueLabel.place(relx=0.33, rely = 0.275, anchor = 'nw') #places the slitSeparation entry box
        screenGratingDistanceSliderValueLabel.place(relx=0.33, rely = 0.335, anchor = 'nw') #places the screenGratingDistance entry box
        if screenState.get() == True:
            toggleIntensityProfile() #shows intensity profile axes and indicator label at correct position if screen and intensity profile are enabled prior to simple
                                     #view being enabled
            intensityProfileStateButton.config(state="normal") #enables intensity profile button if the above occurs
        
        wavelengthSettingsLabel.config(text = "Wavelength [λ] (nm)")
        wavelengthSettingsLabel.place(relx = 0.5, rely = 0.222, anchor = 'nw') #moves the wavelength text label and adds units
        slitSeparationSettingsLabel.config(text = "Slit Separation [s] (μm)")
        slitSeparationSettingsLabel.place(relx = 0.5, rely = 0.272, anchor = 'nw') #moves the slitSeparation text label and adds units
        screenGratingDistanceSettingsLabel.config(text = "Screen-Grating Distance \n[D] (m)")
        screenGratingDistanceSettingsLabel.place(relx = 0.5, rely = 0.322, anchor = 'nw') #moves the screenGratingDistance text label and adds units
        wavelengthSlider.config(showvalue=1)
        slitSeparationSlider.config(showvalue=1)
        screenGratingDistanceSlider.config(showvalue=1) #shows slider values
        wavelengthSlider.place(relx=0.04, rely = 0.215, anchor = 'nw')
        slitSeparationSlider.place(relx=0.04, rely = 0.265, anchor = 'nw')
        screenGratingDistanceSlider.place(relx=0.04, rely = 0.325, anchor = 'nw') #moves sliders

        #Removing information box and its elements:
        informationBoxFrame.place_forget() #hides information box frame from the user's screen
        informationBoxTitleLabel.place_forget()
        informationLabelMain.place_forget()
        informationLabelThetaExplanation.place_forget()
        informationLabelFormulaeAndSymbols.place_forget()
        informationLabelFormulaeTitle2.place_forget()
        informationLabelFormulaeFringeSpacing.place_forget()
        informationLabelFormulaeTitle1.place_forget() #hides all information box labels
    else:
        viewType.set("Simple")
        viewTypeLabel.config(text = "Simple View")
        switchViewButton.config(text = "Switch to Detailed View",
                                padx=3)
        metreScaleArrowLabel.place_forget()
        rightScreenGratingArrowLabel.place_forget()
        leftScreenGratingArrowLabel.place_forget() #if detailed view was activated, switches to simple view and hides required labels
        screenGratingArrowCanvas.delete('all')
        screenGratingDistanceScaleLabel.place_forget() #removes the labels for the screen-grating distance
        wavelengthSliderValueLabel.place_forget()
        slitSeparationSliderValueLabel.place_forget()
        screenGratingDistanceSliderValueLabel.place_forget() #hides entry boxes
        intensityProfileIndicatorLabel.place_forget()
        intensityProfileCanvas.delete("all")
        intensityProfileCanvas.place_forget() #hides intensity profile axes and its indicator label
        intensityProfileStateButton.config(state="disabled") #disables intensity profile button

        wavelengthSettingsLabel.config(text = "Wavelength [λ]")
        wavelengthSettingsLabel.place(relx = 0.32, rely = 0.222, anchor = 'nw') #moves the wavelength text label and removes units
        slitSeparationSettingsLabel.config(text = "Slit Separation [s]")
        slitSeparationSettingsLabel.place(relx = 0.32, rely = 0.272, anchor = 'nw') #moves the slitSeparation text label and removes units
        screenGratingDistanceSettingsLabel.config(text = "Screen-Grating Distance [D]")
        screenGratingDistanceSettingsLabel.place(relx = 0.32, rely = 0.322, anchor = 'nw') #moves the screenGratingDistance text label and removes units
        wavelengthSlider.config(showvalue=0)
        slitSeparationSlider.config(showvalue=0)
        screenGratingDistanceSlider.config(showvalue=0) #hides slider values
        wavelengthSlider.place(relx=0.04, rely = 0.228, anchor = 'nw')
        slitSeparationSlider.place(relx=0.04, rely = 0.278, anchor = 'nw')
        screenGratingDistanceSlider.place(relx=0.04, rely = 0.328, anchor = 'nw') #moves sliders

        #Adding information box:
        informationBoxFrame.place(relx = 0.754, rely = 0, relwidth = 0.165, anchor = 'ne') #places this frame in the top-right corner of the user's screen
        informationBoxTitleLabel.place(relx=0.495, rely = -0.005, anchor = 'n') #places the information box title text label
        informationLabelMain.place(relx=0.02, rely=0.085, anchor = "nw") #places the label for the main body of text in the informationbox
                                                                         #(anchored to north-west so the first line always starts in the same position)
        if chosenDiffractionType.get() ==  "Single-Slit" or chosenDiffractionType.get() ==  "Double-Slit":
            informationLabelThetaExplanation.place(relx=0.02, rely=0.855, anchor = "nw")
            informationLabelFormulaeAndSymbols.place(relx=0.02, rely=0.73, anchor = "nw")
            informationLabelFormulaeTitle2.place(relx=0.02, rely=0.71, anchor = "nw")
            informationLabelFormulaeFringeSpacing.place(relx=0.02, rely=0.69, anchor = "nw")
            informationLabelFormulaeTitle1.place(relx=0.02, rely=0.67, anchor = "nw") #adjusts the text labels below the main one to these positions if single-slit or
                                                                                    #double-slit options have been selected so that they appear with the correct spacing
                                                                                    #below the main text body of the information box
        else:
            informationLabelFormulaeAndSymbols.config(text = ("s*sinθ = nλ \n(n is the position of the maxima, e.g, \nn=0 for the central maxima, n=1 for \nboth adjacent "+
                                                    "maximas to the central \nmaxima, etc.")) #alters the spacing the text of the label for second formula and the
                                                                                            #explanation of its symbols
            informationLabelThetaExplanation.place(relx=0.02, rely=0.855, anchor = "nw")
            informationLabelFormulaeAndSymbols.place(relx=0.02, rely=0.745, anchor = "nw")
            informationLabelFormulaeTitle2.place(relx=0.02, rely=0.725, anchor = "nw")
            informationLabelFormulaeFringeSpacing.place(relx=0.02, rely=0.705, anchor = "nw")
            informationLabelFormulaeTitle1.place(relx=0.02, rely=0.685, anchor = "nw") #adjusts the text labels below the main one to these positions if diffraction-
                                                                                        #grating option has been selected so that they appear with the correct spacing
                                                                                        #below the main text body of the information box
        
    print("ran switchViewPrompt successfully")  #test output to tell if switchViewPrompt runs successfully upon clicking the 'Switch to Simple/Detailed View' button

def mainMenuReturnFromEnvironment():
    #HIDING ALL OBJECTS IN DIFFRACTION ENVIRONMENT SO THAT THE MAIN MENU CAN BE REDISPLAYED:
    
    #Clears all canvases so that they are always blank when re-used in next simulation environment.
    rayLineCanvas.place_forget()
    screenViewCanvas.place_forget()
    screenGratingArrowCanvas.place_forget()
    intensityProfileCanvas.place_forget()
    
    #Hides all canvases from view
    rayLineCanvas.place_forget()
    screenViewCanvas.place_forget()
    screenGratingArrowCanvas.place_forget()
    intensityProfileCanvas.place_forget()
    
    if viewType.get() == "Simple":
        #Removing information box and its labels if displayed.
        informationBoxFrame.place_forget()
        informationBoxTitleLabel.place_forget()
        informationLabelMain.place_forget()
        informationLabelThetaExplanation.place_forget()
        informationLabelFormulaeAndSymbols.place_forget()
        informationLabelFormulaeTitle2.place_forget()
        informationLabelFormulaeFringeSpacing.place_forget()
        informationLabelFormulaeTitle1.place_forget()
    else:
        #Removing scale labels if displayed.
        metreScaleArrowLabel.place_forget()
        leftScreenGratingArrowLabel.place_forget()
        rightScreenGratingArrowLabel.place_forget()

    #Removing remaining objects in diffraction environment
    viewTypeLabel.place_forget()
    screenGratingDistanceSlider.place_forget()
    settingsFrame.place_forget()
    ruler.hide()
    protractor.hide()
    intensityProfileIndicatorLabel.place_forget()
    laserImageLabel.place_forget()
    
    #Removes the switch label on the laser dependent on which one is shown.
    if laserState.get() == True:
        laserStateONIconLabel.place_forget()
    else:
        laserStateOFFIconLabel.place_forget()

    #Accesses dictionary for all global identfiers in the program and converts it to a list for indexing through:
    g = globals()
    globalsList = list(g)

    #Defines a list for all the global variables which need to be deleted from memory to prevent their redeclaration and to initialise their values again.
    varList = ["saveSystemFrame",
                "saveSystemTitleLabel",
                "saveToSetup1Button",
                "saveToFileNumber",
                "saveToSetup2Button",
                "saveToSetup3Button",
                "filename",
                "fileNameEntryBox",
                "fileNameEntryLabel",
                "fileNameSubmitButton",
                "cancelSaveButton",
                "invalidNameErrorSaveLabel",
                "successfulSaveLabel",
        "saveFileNumber",
               "savedSetup1EmptyLabel",
               "savedSetup2EmptyLabel",
               "savedSetup3EmptyLabel",
         "confirmDiffractionTypeLabel",
         "diffractionTypeOptionsLabel",
         "singleSlitDiffractionSelectionButton",
         "chosenDiffractionType",
         "doubleSlitDiffractionSelectionButton",
         "diffractionGratingSelectionButton",
         "confirmDiffractionTypeButton",
         "backDiffractionTypeButton",
         "gratingState",
         "screenLength",
         "rayLineCanvas",
         "intensityProfileCanvas",
         "verticalIntensityProfileAxis",
         "horizontalIntensityProfileAxis",
         "screenPosition",
         "upperDoubleSlitCentrePosition",
         "lowerDoubleSlitCentrePosition",
         "singleSlitCentrePosition",
         "diffractionGratingSlitPositions",
         "lowerGrating",
         "upperGrating",
         "middleGrating",
         "gratingObjectsList",
         "settingsFrame",
               "erroneousLoadLabel",
         "intensityProfileIndicatorLabel",
         "viewType",
         "laserState",
         "wavelength",
         "wavelengthInputErrorLabel",
         "wavelengthSlider",
         "stringWavelength",
         "wavelengthSliderValueLabel",
         "wavelengthSettingsLabel",
         "slitSeparation",
         "slitSeparationInputErrorLabel",
         "slitSeparationSlider",
         "stringSlitSeparation",
         "slitSeparationSliderValueLabel",
         "slitSeparationSettingsLabel",
         "screenGratingDistance",
         "screenGratingArrowCanvas",
         "screenGratingArrowCanvas",
         "leftScreenGratingArrowLabel",
         "rightScreenGratingArrowLabel",
         "screenGratingDistanceScaleLabel",
         "screenGratingDistanceInputErrorLabel",
         "screenGratingDistanceSlider",
         "stringScreenGratingDistance",
         "screenGratingDistanceSliderValueLabel",
         "screenGratingDistanceSettingsLabel",
         "rulerState",
         "intensityProfileState",
         "intensityProfileStateButton",
         "protractorState",
         "screenViewState",
         "screenViewStateButton",
         "switchViewButton",
         "screenViewCanvas",
       "disabledScreenViewLabel",
       "viewTypeLabel",
       "laserImageLabel",
       "laserStateONIconLabel",
       "laserStateOFFIconLabel",
       "screen",
       "metreScaleArrowLabel",
       "informationBoxFrame",
       "informationBoxTitleLabel",
       "informationLabelMain",
       "informationLabelFormulaeTitle1",
       "informationLabelFormulaeFringeSpacing",
       "informationLabelFormulaeTitle2",
       "informationLabelFormulaeAndSymbols",
       "informationLabelThetaExplanation",
       "screenState",
       "protractor",
       "ruler"]

    #Deletes each global variable in varList from the dictionary of global variables.
    for each in varList:
        try:
            del g[each]
        except(KeyError):
            q = 1
    #Reopens the main menu, setting the debounce parameter as True so that the creation of the window is not performed again.
    mainMenuOpen(True)
    
    
    print("ran mainMenuReturnFromEnvironment successfully") #test output to tell if mainMenuReturnFromEnvironment runs successfully upon clicking the 'Return to Main Menu'
                                                            #button
def toggleLaserState():
    if (laserState.get()) == True:
        laserStateOFFIconLabel.place_forget()  #hides the off laser image
        laserStateONIconLabel.place(relx=0.0335, rely = 0.435, anchor='nw') #places the on laser image
    else:
        laserStateONIconLabel.place_forget() #hides the on laser image
        laserStateOFFIconLabel.place(relx=0.0335, rely = 0.435, anchor='nw') #places the off laser image
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it
        
def toggleScreenView():
    if screenViewState.get() == True:
        screenViewCanvas.place(relx = 1, rely = 0.6808, anchor = 'ne') #places this frame in the bottom-right corner of the user's screen
        disabledScreenViewLabel.place_forget() #removes no longer needed screen view disabled text label
    else:
        screenViewCanvas.place_forget() #removes no longer needed screen view frame
        if screenState.get() == True:
            disabledScreenViewLabel.config(text = "Click the 'Screen View'\nbox to enable the screen\nview.")
        disabledScreenViewLabel.place(relx=0.5, rely = 0.725, anchor = 'n') #sets text and text settings of the screen view disabled text label and places it
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it
    
def updateWavelengthValueFromSlider(event):
    wavelengthSliderValueLabel.delete(0, END) #clears the previous value in the wavelength entry box
    stringWavelength.set(str(wavelength.get()))
    if len(stringWavelength.get()) < 6:
        wavelengthSliderValueLabel.delete(0, END)
        stringWavelength.set(str(wavelength.get()) + "00") #sets stringWavelength to the string of wavelength with two extra zeros if its length is less than 6
    elif len(stringWavelength.get()) == 6:
        wavelengthSliderValueLabel.delete(0, END)
        stringWavelength.set(str(wavelength.get()) + "0") #sets stringWavelength to the string of wavelength with one extra zeros if its length is  6
    else:
        wavelengthSliderValueLabel.delete(0, END)
        stringWavelength.set(str(wavelength.get())) #sets stringWavelength to the string of wavelength without modification if its length is 7 (so is of the correct format)
    try:
        wavelengthInputErrorLabel.place_forget() #removes any existing error labels
    except(NameError, ValueError):
        print("No wavelength error label to remove.") #output if no error labels to remove
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it

def updateWavelengthValueFromEntry(event):
    try:
        if float((stringWavelength.get()))>700 or float((stringWavelength.get()))<380:
            int("invalid")
        else:
            wavelength.set(float(stringWavelength.get())) #sets the value for the wavelength (and therefore slider) adjust to the float of the string wavelength value
                                                      #held in the entry box
            print(float(stringWavelength.get()))
            print(wavelength.get()) #test to check that outputs are correct
            wavelengthInputErrorLabel.place_forget()
            try:
                wavelengthInputErrorLabel.place_forget() #removes any existing error labels
            except(NameError, ValueError):
                print("No wavelength error label to remove.") #output if no error labels to remove
                
    except(ValueError, TypeError): #if a non-integer
        wavelengthInputErrorLabel.place(relx=0.49, rely = 0.25, anchor = 'nw') #sets text and text settings of the wavelength input error text label and places it
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it
    
def updateScreenGratingDistanceValueFromSlider(event):
    screenGratingDistanceSliderValueLabel.delete(0, END) #clears the previous value in the screenGratingDistance entry box
    stringScreenGratingDistance.set(str(screenGratingDistance.get()))
    if len(stringScreenGratingDistance.get()) < 4:
        screenGratingDistanceSliderValueLabel.delete(0, END)
        stringScreenGratingDistance.set(str(screenGratingDistance.get()) + "00") #sets screenGratingDistance to the string of screenGratingDistance with two extra
                                                                                    #zeros if its length is less than 4
    elif len(stringScreenGratingDistance.get()) == 4:
        screenGratingDistanceSliderValueLabel.delete(0, END)
        stringScreenGratingDistance.set(str(screenGratingDistance.get()) + "0") #sets screenGratingDistance to the string of screenGratingDistance with one extra zeros
                                                                                #if its length is  4
    else:
        screenGratingDistanceSliderValueLabel.delete(0, END)
        stringScreenGratingDistance.set(str(screenGratingDistance.get())) #sets screenGratingDistance to the string of screenGratingDistance without modification
                                                                            #if its length is 5 (so is of the correct format)
    try:
        screenGratingDistanceInputErrorLabel.place_forget() #removes any existing error labels
    except(NameError, ValueError):
        print("No Screen-Grating Distance error label to remove.") #output if no error labels to remove
    #Updating screen-grating distance scale
    if (gratingState.get()) == True:
        if viewType.get() == "Detailed":
            leftScreenGratingArrowLabel.place(x = 490-(screenGratingDistance.get()*230), rely = 0.5, anchor = 'w') #places the left arrow at its updated position
            drawArrowLine((490-(screenGratingDistance.get()*230)),50, 490, 50, screenGratingArrowCanvas, 5) #runs the drawArrowLine subroutine to create the scale line
                                                                                                            #for the screen-grating distance
            rightScreenGratingArrowLabel.place(relx = 0.96, rely = 0.5, anchor = 'e') #places the right arrow
            screenGratingDistanceScaleLabel.place(relx = 0.5 + 0.235*(2-screenGratingDistance.get()), rely = 0.76, anchor = 'center') #places the screen-grating distance
                                                                                                                                      #scale label
        if chosenDiffractionType.get() == "Single-Slit":
            upperGrating.setXCord(0.3+0.12*(2-screenGratingDistance.get()))
            lowerGrating.setXCord(0.3+0.12*(2-screenGratingDistance.get())) #places both parts of the grating at the correct x-coordinate based on the screen-grating
                                                                            #distance value which has been selected if a single-slit grating is used
            singleSlitCentrePosition[0] = 0.304+0.12*(2-screenGratingDistance.get()) #updates the global position for the centre of the slit of the
                                                                                            #single-slit grating
        elif  chosenDiffractionType.get() == "Double-Slit":
            upperGrating.setXCord(0.3+0.12*(2-screenGratingDistance.get()))
            middleGrating.setXCord(0.3+0.12*(2-screenGratingDistance.get()))
            lowerGrating.setXCord(0.3+0.12*(2-screenGratingDistance.get())) #places the three parts of the grating at the correct x-coordinate based on the screen-grating
                                                                            #distance value which has been selected if a double-slit grating is used
            upperDoubleSlitCentrePosition[0] = 0.304+0.12*(2-screenGratingDistance.get())
            lowerDoubleSlitCentrePosition[0] = 0.304+0.12*(2-screenGratingDistance.get()) #updates the global positions for the centre of the upper and lower slit
                                                                                          #of the double-slit grating
        else:
            for x in range(0,11):
                gratingObjectsList[x].setXCord(0.3+0.12*(2-screenGratingDistance.get())) #places the eleven parts of the grating at the correct x-coordinate based
                                                                                         #on the screen-grating distance value which has been selected if a diffraction
                                                                                         #grating is used
            for x in range(0,10):
                diffractionGratingSlitPositions[x] =([0.304+0.12*(2-screenGratingDistance.get()), 0.0727 + (x*0.076)]) #updates the global 2D list for the positions of the centres of each slit of the
                                                                                     #diffraction grating
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it
        
def updateScreenGratingDistanceValueFromEntry(event):
    try:
        if (float(stringScreenGratingDistance.get()))>2 or (float(stringScreenGratingDistance.get()))<0.5:
            int("invalid")
        else:
            screenGratingDistance.set(float(stringScreenGratingDistance.get())) #sets the value for the screenGratingDistance (and therefore slider) adjust to the
                                                                                #float of the string screenGratingDistance value held in the entry box

            print(float(stringScreenGratingDistance.get()))
            print(screenGratingDistance.get()) #test to check that outputs are correct
            try:
                screenGratingDistanceInputErrorLabel.place_forget() #removes any existing error labels
            except(NameError):
                print("No slit separation error label to remove.") #output if no error labels to remove
    except(ValueError, TypeError): #if a non-integer
        screenGratingDistanceInputErrorLabel.place(relx=0.49, rely = 0.375, anchor = 'nw') #sets text and text settings of the screenGratingDistance input error
                                                                                          #text label and places it
    updateScreenGratingDistanceValueFromSlider(event)

def updateSlitSeparationValueFromSlider(event):
    slitSeparationSliderValueLabel.delete(0, END) #clears the previous value in the slit separation entry box
    stringSlitSeparation.set(str(slitSeparation.get()))
    if len(stringSlitSeparation.get()) < 4:
        stringSlitSeparation.set("")
        slitSeparationSliderValueLabel.delete(0, END)
        stringSlitSeparation.set(str(slitSeparation.get()) + "00") #sets stringSlitSeparation to the string of slitSeparation with two extra zeros if its length is
                                                                   #less than 4
    elif len(stringSlitSeparation.get()) == 4:
        slitSeparationSliderValueLabel.delete(0, END)
        stringSlitSeparation.set(str(slitSeparation.get()) + "0") #sets stringSlitSeparation to the string of slitSeparation with one extra zeros if its length is  4
    else:
        slitSeparationSliderValueLabel.delete(0, END)
        stringSlitSeparation.set(str(slitSeparation.get())) #sets stringSlitSeparation to the string of slitSeparation without modification if its length is 5
                                                    #(so is of the correct format)
    try:
        slitSeparationInputErrorLabel.place_forget() #removes any existing error labels
    except(NameError, ValueError):
        print("No slit separation error label to remove.") #output if no error labels to remove
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it

def updateSlitSeparationValueFromEntry(event):
    try:
        if (float(stringSlitSeparation.get()))>2 or (float(stringSlitSeparation.get()))<1: #throws an exception which is caught and causes an error label to be
                                                                                            #created if the slit separation value entered is not within the valid range
            int("invalid")
        else:
            slitSeparation.set(float(stringSlitSeparation.get())) #sets the value for the slitSeparation (and therefore slider) adjust to the float of the string
                                                                  #slitSeparation value held in the entry box

            print(float(stringSlitSeparation.get()))
            print(slitSeparation.get()) #test to check that outputs are correct
            try:
                slitSeparationInputErrorLabel.place_forget() #removes any existing error labels
            except(NameError):
                print("No slit separation error label to remove.") #output if no error labels to remove
    except(ValueError, TypeError): #if a non-integer
        slitSeparationInputErrorLabel.place(relx=0.49, rely = 0.30, anchor = 'nw') #sets text and text settings of the slitSeparation input error text label and places it
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it


def returnToMainMenuFromDTypeChoice():
    confirmDiffractionTypeLabel.place_forget()
    diffractionTypeOptionsLabel.place_forget()
    singleSlitDiffractionSelectionButton.place_forget()
    doubleSlitDiffractionSelectionButton.place_forget()
    diffractionGratingSelectionButton.place_forget()
    confirmDiffractionTypeButton.place_forget()
    backDiffractionTypeButton.place_forget() #removes all of the default widgets except the design images from the confirm diffraction type screen
    
    try:
        newSystemNoTypeLabel.place_forget()
    except(NameError):
        print("No error message to remove.") #removes the message informing the user to select a diffraction type if it is present on the screen. If this is not present, an output
                                             #message confirming this exception has run is printed.
        
    welcomeLabel.place(relx=0.5,y=50, anchor = 'n') 
    savedSetupsLabel.place(relx=0.5,rely=0.28, anchor = 'n') 
    newSetupButton.place(relx=0.495 ,rely=0.2, anchor = 'e') 
    loadSetupButton.place(relx=0.505 ,rely=0.2, anchor = 'w') #replaces all of the default widgets except the design images on the default main menu screen which is being reverted to
    
    try:
        savedSetup1EmptyLabel.place(relx=0.5,rely=0.35, anchor = 'n')
    except(NameError):
        savedSetup1Button.place(relx=0.5,rely=0.35, relwidth = 0.3, anchor = 'n')
    try:
        savedSetup2EmptyLabel.place(relx=0.5,rely=0.53, anchor = 'n')
    except(NameError):
        savedSetup2Button.place(relx=0.5,rely=0.53, relwidth = 0.3,  anchor = 'n')
    try:
        savedSetup3EmptyLabel.place(relx=0.5,rely=0.71, anchor = 'n')
    except(NameError):
        savedSetup3Button.place(relx=0.5,rely=0.71, relwidth = 0.3,  anchor = 'n')
        #The program attempts to replace every empty setup label that existed originally in the starting main menu screen,
                                                                    #and any that don't will throw an exception which the program responds to by
                                                                    #replacing the button that must have existed in its place instead.
        
class SimulationObject: #defines a general class for all objects within the simulation environment
    def __init__(self, initialXCord, initialYCord):
        self.xCord = initialXCord
        self.yCord = initialYCord
        self.position = [initialXCord, initialYCord]
        self.objectLabel = Label(rayLineCanvas)
        self.setPosition(initialXCord, initialYCord) #constructor method initialises the positional variables of the object and displays its label 
        
    def display(self):
        self.objectLabel.place(relx = self.xCord, rely = self.yCord, anchor = 'nw') #displays object's label at updated position

    def hide(self):
        self.objectLabel.place_forget() #hides the object's label from the user's view

    def setPosition(self, newXCord, newYCord):
        self.xCord = newXCord
        self.yCord = newYCord
        self.position = [newXCord, newYCord]
        self.hide()
        self.display() #updates the position variable of the object and then redisplays it with the updated position
        
    def getPosition(self):
        return self.position #get method to access the position of the object

    def setXCord(self, newXCord):
        self.xCord = newXCord
        self.position[0] = self.xCord
        self.hide()
        self.display() #updates the x-coordinate variable of the object and then redisplays it with the updated position

    def getXCord(self):
        return self.xCord #get method to access the x-coordinate of the object

    def setYCord(self, newYCord):
        self.yCord = newYCord
        self.position[1] = self.yCord
        self.hide()
        self.display() #updates the y-coordinate variable of the object and then redisplays it with the updated position

    def getYCord(self):
        return self.yCord #get method to access the y-coordinate of the object

class SimulationApparatus(SimulationObject): #defines a class for the screen and grating instances within the simulation environment
    def __init__(self, initialXCord, initialYCord, initialSprite):
        super().__init__(initialXCord, initialYCord)
        self.sprite = initialSprite #constructor method initialises the variables of the simulation apparatus object and displays its label with the parent constructor
        self.setSprite(initialSprite)
    def setSprite(self, newSprite):
        self.sprite = newSprite
        selfImage = PhotoImage(file=self.sprite)
        self.objectLabel.config(image=selfImage)
        self.objectLabel.image = selfImage
        self.objectLabel.place_forget()
        self.objectLabel.place(relx = self.xCord, rely = self.yCord, anchor='n') #updates the sprite of the object
    def getSprite():
        return self.sprite #get method to access the sprite of the object

class MeasuringEquipment(SimulationObject): #defines a class for the ruler and protractor instances within the simulation environment
    def __init__(self, initialXCord, initialYCord, initialSprite, initialOrientation, initialZoom, initialRotateLabelOffset):
        super().__init__(initialXCord, initialYCord)
        self.startX = 0
        self.startY = 0
        self.orientation = initialOrientation
        self.rotateLabelOffset = initialRotateLabelOffset
        self.initialRotateLabelOffset = self.rotateLabelOffset
        self.rotateIcon = PhotoImage(file = "RotateIcon.png")
        self.rotateLabel = Label(mainMenu, image = self.rotateIcon, border = 0)
        self.zoom = initialZoom
        self.sprite = initialSprite
        self.spriteType = self.sprite.rstrip("Icon.png")
        self.setSprite(initialSprite)
        self.objectLabel.bind("<B1-Motion>", self.on_drag)
        self.objectLabel.bind("<ButtonRelease>", self.on_drop)
        self.rotateLabel.bind("<Button-1>", self.rotate)
        #causes the clicking and releasing of the mouse button over the measurement object's label to trigger the methods to cause the drag-drop process to occur 
        self.root = self.objectLabel.winfo_toplevel()
        counter = self.orientation//45
        self.orientation = 0
        print(counter)
        if counter > 0:
            self.newX = self.startX
            self.newY = self.startY
        for x in range(counter):
            self.rotate("setup") #rotates the object to its correct initial orientation
        self.objectLabel.place(x = int(windowWidth)*self.xCord, y = int(windowHeight)*self.yCord, anchor='center') 
        #constructor method initialises the variables of the measurement object and displays its label with the parent constructor
    def setSprite(self, newSprite):
        self.sprite = newSprite
        self.selfImage = PhotoImage(file=self.sprite)
        if self.zoom != 1:
            self.selfImage = self.selfImage.subsample(self.zoom)
        self.objectLabel = Label(mainMenu, image = self.selfImage, border = 0)
        self.objectLabel.config(image=self.selfImage)
        self.objectLabel.image = self.selfImage
        self.objectLabel.place_forget()
        self.objectLabel.place(x = int(windowWidth)*self.xCord, y = int(windowHeight)*self.yCord, anchor='center')
        #updates the sprite of the object and places it as a label on the screen
    def createRotateLabel(self): #method to place the rotate label correctly above the measurement object
        self.orientation = int(self.orientation)
        print(self.orientation)
        if self.orientation % 180 == 0:
            self.rotateLabelOffset = self.initialRotateLabelOffset #uses default height for rotate label if the orientation of the object label is a multiple of 180 degrees
        elif self.orientation % 90 == 0:
            if self.spriteType == "ruler":
                self.rotateLabelOffset = self.initialRotateLabelOffset+210
            else:
                self.rotateLabelOffset = self.initialRotateLabelOffset+80
        else:
            if self.spriteType == "ruler":
                self.rotateLabelOffset = self.initialRotateLabelOffset+160
            else:
                self.rotateLabelOffset = self.initialRotateLabelOffset+60
        #calculates the height for the rotate label dependent on if a ruler or protractor is currently selected
        try:
            self.rotateLabel.place(x=self.newX,
                               y=self.newY-self.rotateLabelOffset,
                               anchor='s')
        except(AttributeError):
            self.rotateLabel.place(x=self.root.winfo_pointerx()-self.root.winfo_rootx(),
                                   y=self.root.winfo_pointery()-self.root.winfo_rooty()-self.rotateLabelOffset,
                                   anchor='s') #places the new rotate label using the above calculation and using newX and newY identifiers if they have been defined
                                                #at this point in the execution of the program (i.e, prevents the exception when the first display of the label is run)
        self.rotateLabel.image = self.rotateIcon #adds a reference for the image of the rotate label
    def destroyRotateLabel(self):
        self.rotateLabel.place_forget()
    def getSprite(self):
        return self.sprite #get method to access the sprite of the object
    def display(self):
        self.objectLabel.place(x = int(windowWidth)*self.xCord, y = int(windowHeight)*self.yCord, anchor='center') #displays object's label at updated position
    def hide(self):
        self.objectLabel.place_forget()
        try:
            self.rotateLabel.place_forget()
        except(AttributeError):
            pass
        #hides the object's label and rotate label from the user's view
    def setOrientation(self, newOrientation):
        self.orientation = newOrientation #updates the orientation of the object
    def getOrientation(self):
        return self.orientation #get method to access the orientation of the object
    def on_drag(self,event):
        self.destroyRotateLabel()
        x,y = pyautogui.position()
        self.objectLabel.place(x=self.root.winfo_pointerx()-self.root.winfo_rootx(), y=self.root.winfo_pointery()-self.root.winfo_rooty())
        #updates the position of the measurement object's label for each moment that it is being dragged by the user's cursor
    def on_drop(self,event):
        x,y = pyautogui.position()
        self.objectLabel.place(x=self.root.winfo_pointerx()-self.root.winfo_rootx(), y=self.root.winfo_pointery()-self.root.winfo_rooty())
        self.newX = self.root.winfo_pointerx()-self.root.winfo_rootx()
        self.newY = self.root.winfo_pointery()-self.root.winfo_rooty()
        self.createRotateLabel()
        #sets the final position of the object for the moment when the user releases the cursor after dragging the measurement object's label
    def rotate(self, event): #method to rotate the measurement object by 45 degrees
        if self.sprite == "rulerIcon.png":
            self.spriteType = "ruler"
        else:
            self.spriteType = "protractor"
        self.objectLabel.unbind("<B1-Motion>")
        self.objectLabel.unbind("<B1-Motion>") #unbinds events to drag the previously orientated icon for the label of the ruler/protractor
        self.objectLabel.place_forget()
        if self.orientation == 315:
            self.orientation = 0
            selfImage = PhotoImage(file = (self.spriteType + "Icon.png"))
            selfImage = selfImage.subsample(self.zoom)
            self.objectLabel = Label(mainMenu, image = selfImage, border = 0) #resets the measurement object to a rotation of zero and its default icon if it is about
                                                                              #to be rotated to an orientation 360 degrees
        else:
            self.orientation += 45
            selfImage = PhotoImage(file = (self.spriteType + "IconRotated" + str(self.orientation) + "Degrees.png"))
            selfImage = selfImage.subsample(self.zoom)
            self.objectLabel = Label(mainMenu, image = selfImage, border = 0) #sets the new icon of the measurement object based on its rotation and whether it is a ruler
                                                                              #or protractor
        self.objectLabel.bind("<B1-Motion>", self.on_drag)
        self.objectLabel.bind("<ButtonRelease>", self.on_drop) #binds events to drag the most recently orientated icon for the label of the ruler/protractor
        self.objectLabel.image = selfImage
        self.objectLabel.place(x=self.newX, y = self.newY, anchor = "center") #places the measurement object label with an  updated orientation
        self.createRotateLabel() #runs method to update orientation label
    def getNewCords(self):
        try:
            return [self.newX, self.newY]
        except(AttributeError):
            return "Default"
    def displayNew(self):
        try:
            self.objectLabel.place(x=self.newX, y = self.newY, anchor = "center") 
        except(AttributeError):
            self.display()
            #places the measurement object label with anupdated orientation

#original display method:
    #def display(self):
        #self.objectLabel.place(x = self.xCord, rely = self.yCord, anchor = 'center') #displays object's label at updated position




    #def dragStart(self, event):
        #self.startX = event.x
        #self.startY = event.y #startDragPosition
        #self.objectLabel.image = self.selfImage
    #def dragMotion(self, event):
        #newX = self.objectLabel.winfo_x() - self.startX + event.x #event.x_root #currentPos - initialPos + clickPositionRelativeToWidget
        #newY = self.objectLabel.winfo_y() - self.startY + event.y  #event.y_root
        #print(self.objectLabel.winfo_x())
        #print(self.objectLabel.winfo_y())
        #print(self.startX)
        #print(self.startY)
        #print(event.x)
        #print(event.y)
        #print([newX,newY])
        #self.hide()
        #'self.objectLabel.place(x=newX, y=newY, anchor = "center")
        #self.display()
        #print(self.getPosition())
        #self.place(x=event.x_root, y=event.y_root,anchor=CENTER)
        #widget = event.widget
    #widget._drag_start_x = event.x
    #widget._drag_start_y = event.y

#card = Canvas(window, width=74, height=97, bg='blue')
#card.place(x=300, y=600,anchor=CENTER)
#card.bind("<B1-Motion>", drag)




    #def display(self):
        #self.objectImage = rayLineCanvas.create_image(self.xCord,self.yCord,image=self.selfImage, anchor='center') #displays object's label at updated position
    #def hide(self):
        #rayLineCanvas.delete(self.tag) #hides the object's label from the user's view
    #def drag(event):
        #self.place(x=event.x_root, y=event.y_root,anchor=CENTER)
    #def setPosition(self, newXCord, newYCord):
        #self.xCord = newXCord
        #self.yCord = newYCord
        #self.position = [newXCord, newYCord]
        #self.hide()
        #self.display() #updates the position variable of the object and then redisplays it with the updated position
        
    #def getPosition(self):
        #return self.position #get method to access the position of the object

#card = Canvas(window, width=74, height=97, bg='blue')
#card.place(x=300, y=600,anchor=CENTER)
#card.bind("<B1-Motion>", drag)
        

def drawArrowLine(xCord1, yCord1, xCord2, yCord2, canvas, widthLine):
    canvas.delete('all')
    canvas.create_line(xCord1, yCord1, xCord2, yCord2, width=widthLine) #creates the required arrow line of specified width between two specified points on a
                                                                        #specified canvas

def toggleGratingState():
    if (gratingState.get()) == False:
        if chosenDiffractionType.get() == "Single-Slit":
            upperGrating.hide()
            lowerGrating.hide() #hides both parts of the single-slit grating if the single-slit grating is chosen
        elif  chosenDiffractionType.get() == "Double-Slit":
            upperGrating.hide()
            middleGrating.hide()
            lowerGrating.hide() #hides the three parts of the double-slit grating if the double-slit grating is chosen
        else:
            for x in range(0,11):
                gratingObjectsList[x].hide() #hides all parts of the diffraction grating if the diffraction grating is chosen
        leftScreenGratingArrowLabel.place_forget()
        rightScreenGratingArrowLabel.place_forget()
        screenGratingDistanceScaleLabel.place_forget()
        screenGratingArrowCanvas.delete('all') #hides all of the environment's labels/arrows for the grating
        slitSeparationSlider.config(state='disabled')
        screenGratingDistanceSlider.config(state='disabled')
        screenGratingDistanceSliderValueLabel.config(state='disabled')
        slitSeparationSliderValueLabel.config(state='disabled') #disables uneditable variables for when the grating is inactive
        
    else:
        if chosenDiffractionType.get() == "Single-Slit":
            upperGrating.display()
            lowerGrating.display() #displays both parts of the single-slit grating if the single-slit grating is chosen
        elif  chosenDiffractionType.get() == "Double-Slit":
            upperGrating.display()
            middleGrating.display()
            lowerGrating.display() #displays the three parts of the double-slit grating if the double-slit grating is chosen
        else:
            for x in range(0,11):
                gratingObjectsList[x].display() #displays all parts of the diffraction grating if the diffraction grating is chosen
        if screenState.get() == True:
            updateScreenGratingDistanceValueFromSlider("enable") #runs updateScreenGratingDistanceValueFromSlider to show appropriate labels and update position of grating
            screenGratingDistanceSlider.config(state='normal')
            screenGratingDistanceSliderValueLabel.config(state='normal')
        slitSeparationSlider.config(state='normal')
        slitSeparationSliderValueLabel.config(state='normal') #re-enables uneditable variables when the grating is inactive when it becomes active again
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it

def toggleScreenState():
    if (screenState.get()) == False:
        screen.hide() #hides screen
        screenViewCanvas.place_forget() #removes no longer needed screen view frame
        disabledScreenViewLabel.config(text = "Click the 'Screen in place'\nbox to enable the screen\nview.")
        disabledScreenViewLabel.place(relx=0.5, rely = 0.725, anchor = 'n') #sets text and text settings of the screen view disabled text label and places it
        screenViewStateButton.config(state = 'disabled') #disables screen view and the button to toggle it
        intensityProfileIndicatorLabel.place_forget()
        intensityProfileCanvas.delete("all")
        intensityProfileCanvas.place_forget() #hides intensity profile axes and its indicator label
        intensityProfileStateButton.config(state = 'disabled') #disables intensity profile and the button to toggle it
        leftScreenGratingArrowLabel.place_forget()
        rightScreenGratingArrowLabel.place_forget()
        screenGratingDistanceScaleLabel.place_forget()
        screenGratingArrowCanvas.delete('all') #hides all of the environment's labels/arrows for the screen
        screenGratingDistanceSlider.config(state='disabled')
        screenGratingDistanceSliderValueLabel.config(state='disabled') #disables uneditable variables for when the screen is inactive
        screenGratingArrowCanvas.place_forget() #hides the canvas for the screen-grating distance arrow
        
    else:
        screen.display() #shows screen
        toggleScreenView()
        screenGratingArrowCanvas.place(relwidth=0.27, relheight=0.1, relx = 0.565, rely = 0.9, anchor = "ne")#re-displays the canvas for the screen-grating distance arrow
        screenViewStateButton.config(state = 'normal') #re-enables screen view and the button to toggle it
        if intensityProfileState.get() == True and viewType.get() == "Detailed":
            intensityProfileIndicatorLabel.place(relx=0.65, rely=0.96, anchor = "center")
            intensityProfileStateButton.config(state = 'normal') #re-enables intensity profile, its indicator label the button to toggle it
            intensityProfileCanvas.place(relwidth=0.153, relheight=0.897, relx = 0.58, rely = 0.005, anchor = "nw") #places the canvas for the intensity profile to be
                                                                                                                    #plotted on
            verticalIntensityProfileAxis = intensityProfileCanvas.create_line(0,0,0,1000, fill = "black", width = 30)
            horizontalIntensityProfileAxis = intensityProfileCanvas.create_line(0,445,500,445, fill = "black", width = 12)
            #creates lines for the axes of the intensity profile
        if gratingState.get() == True:
            updateScreenGratingDistanceValueFromSlider("enable") #runs updateScreenGratingDistanceValueFromSlider to show appropriate labels and update position of screen
            screenGratingDistanceSlider.config(state='normal')
            screenGratingDistanceSliderValueLabel.config(state='normal') #re-enables uneditable variables when the screen is inactive when it becomes active again
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it

def toggleIntensityProfile():
    if intensityProfileState.get() == True:
        intensityProfileIndicatorLabel.place(relx=0.65, rely=0.96, anchor = "center")
        intensityProfileCanvas.place(relwidth=0.153, relheight=0.897, relx = 0.58, rely = 0.005, anchor = "nw") #places the canvas for the intensity profile to be
                                                                                                                    #plotted on
        verticalIntensityProfileAxis = intensityProfileCanvas.create_line(0,0,0,1000, fill = "black", width = 30)
        horizontalIntensityProfileAxis = intensityProfileCanvas.create_line(0,445,500,445, fill = "black", width = 12) #creates lines for the axes of the intensity profile
    else:
        intensityProfileIndicatorLabel.place_forget()
        intensityProfileCanvas.delete("all")
        intensityProfileCanvas.place_forget() #hides intensity profile axes and its indicator label if disabled
    try:
        updateDiffractionPattern() #updates diffraction pattern
    except(NameError):
        pass #if environment not finished setting up, and updateDiffractionPattern causes a NameError, subroutine ends without running it

def wavelengthToHex(wavelengthValue): #declares a function to convert wavelength values to hexadecimal colour values
    wavelengthDictionary = {380: '#610061',
                            385: '#6f0077',
                            390: '#79008d',
                            395: '#8000a1',
                            400: '#8300b5',
                            405: '#8200c8',
                            410: '#7e00db',
                            415: '#7600ed',
                            420: '#6a00ff',
                            425: '#5400ff',
                            430: '#3d00ff',
                            435: '#2300ff',
                            440: '#0000ff',
                            445: '#0028ff',
                            450: '#0046ff',
                            455: '#0061ff',
                            460: '#007bff',
                            465: '#0092ff',
                            470: '#00a9ff',
                            475: '#00c0ff',
                            480: '#00d5ff',
                            485: '#00eaff',
                            490: '#00ffff',
                            495: '#00ffcb',
                            500: '#00ff92',
                            505: '#00ff54',
                            510: '#00ff00',
                            515: '#1fff00',
                            520: '#36ff00',
                            525: '#4aff00',
                            530: '#5eff00',
                            535: '#70ff00',
                            540: '#81ff00',
                            545: '#92ff00',
                            550: '#a3ff00',
                            555: '#b3ff00',
                            560: '#c3ff00',
                            565: '#d2ff00',
                            570: '#e1ff00',
                            575: '#f0ff00',
                            580: '#ffff00',
                            585: '#ffef00',
                            590: '#ffdf00',
                            595: '#ffcf00',
                            600: '#ffbe00',
                            605: '#ffad00',
                            610: '#ff9b00',
                            615: '#ff8900',
                            620: '#ff7700',
                            625: '#ff6300',
                            630: '#ff4f00',
                            635: '#ff3900',
                            640: '#ff2100',
                            645: '#fe0000',
                            650: '#fa0000',
                            655: '#f50000',
                            660: '#f10000',
                            665: '#ed0000',
                            670: '#e80000',
                            675: '#e40000',
                            680: '#df0000',
                            685: '#db0000',
                            690: '#d60000',
                            695: '#d20000',
                            700: '#cd0000'} #defines a dictionary for the hex colour value for every 5 nanometres of wavelength on the scale between 380 and 700nm
    try:
        return (wavelengthDictionary[(wavelengthValue//5)*5]) #returns the corresponding hex colour value to the wavelength given
    except(KeyError):
        return -1 #returns -1 if the given wavelength is not valid
    
def updateDiffractionPattern():
    try:
        ruler.destroyRotateLabel()
        protractor.destroyRotateLabel()
    except(NameError):
        print("No ruler and protractor to destroy rotate label of.")
    try:
        successfulSaveLabel.place_forget()
    except(NameError):
        screenViewState.get()
    try:
        erroneousLoadLabel.place_forget()
    except(NameError):
        screenViewState.get()
    screenViewCanvas.delete("all") #clears all previous spots on the screen view
    rayLineColour = wavelengthToHex(wavelength.get()) #gets the hex colour for the updated wavelength value
    rayLineCanvas.delete("all") #clears the rayline canvas to add new raylines if needed
    if laserState.get() == False:
        intensityProfileCanvas.delete("all") #deletes all of the objects on the intensity profile
        verticalIntensityProfileAxis = intensityProfileCanvas.create_line(0,0,0,1000, fill = "black", width = 30)
        horizontalIntensityProfileAxis = intensityProfileCanvas.create_line(0,445,500,445, fill = "black", width = 12) #adds back the axes of the intensity profile
        screenViewCanvas.delete("all")
        return "laserOff" #displays no more raylines and ends the subroutine if the laser is turned off
    #Laser-to-grating/screen raylines setup
    if gratingState.get() == False or chosenDiffractionType.get() == "Single-Slit":
        if screenState.get() == True:
            currentRayLineEndXCord = screenPosition[0]*(int(windowWidth))
        else:
            currentRayLineEndXCord = int(windowWidth)
        currentRayLine = rayLineCanvas.create_line(0.0865*(int(windowWidth)),
                                      screenPosition[1]*(int(windowHeight)),
                                      currentRayLineEndXCord,
                                      screenPosition[1]*(int(windowHeight)),
                                      width=3,
                                      fill=rayLineColour) #draws a rayline through the centre to the screen if the screen is enabled and either a single-slit grating
                                                          #is used or the grating is not enabled (so no diffraction would occur)
        numberOfSlits = 1 #sets a variable for the number of slits on the grating
        slitPositions = [singleSlitCentrePosition] #sets a list for the positions of each slit on the grating
    elif chosenDiffractionType.get() == "Double-Slit":
        currentRayLine = rayLineCanvas.create_line(0.0865*(int(windowWidth)),
                                      screenPosition[1]*(int(windowHeight)),
                                      lowerDoubleSlitCentrePosition[0]*(int(windowWidth)),
                                      lowerDoubleSlitCentrePosition[1]*(int(windowHeight)),
                                      width=3,
                                      fill=rayLineColour) #draws a rayline from the laser to the lower slit of the double-slit grating if the double-slit setup is used
        currentRayLine = rayLineCanvas.create_line(0.0865*(int(windowWidth)),
                                      screenPosition[1]*(int(windowHeight)),
                                      upperDoubleSlitCentrePosition[0]*(int(windowWidth)),
                                      upperDoubleSlitCentrePosition[1]*(int(windowHeight)),
                                      width=3,
                                      fill=rayLineColour) #draws a rayline from the laser to the upper slit of the double-slit grating if the double-slit setup is used
        numberOfSlits = 2 #sets a variable for the number of slits on the grating
        slitPositions = [lowerDoubleSlitCentrePosition, upperDoubleSlitCentrePosition] #sets a list for the positions of each slit on the grating 
    else:
        for x in range(0,10):
            currentRayLine = rayLineCanvas.create_line(0.0865*(int(windowWidth)),
                                      screenPosition[1]*(int(windowHeight)),
                                      diffractionGratingSlitPositions[x][0]*(int(windowWidth)),
                                      diffractionGratingSlitPositions[x][1]*(int(windowHeight)),
                                      width=3,
                                      fill=rayLineColour) #draws a rayline from the laser to the each slit of the diffraction grating if a multi-slit diffraction grating
                                                          #setup is used.
        numberOfSlits = 10 #sets a variable for the number of slits on the grating
        slitPositions = diffractionGratingSlitPositions #sets a list for the positions of each slit on the grating
        
    #Plotting grating-screen diffraction pattern
    heightBetweenMaximas = (wavelength.get()*(10**-9)*screenGratingDistance.get())/(slitSeparation.get()*(10**-6)) #calculates the distance between each maxima
                                                                                                                        #on the screen
    screenLengthInPixels = screenLength*0.13*int(windowHeight)
    numberOfMaximas = int((2*((screenLength/2)//heightBetweenMaximas))+1) #calculates the number of maximas which need plotting
    countMaximas = int(numberOfMaximas//2) #calculates how many times the inner for loop must iterate for this number of maximas
    heightBetweenMaximas = heightBetweenMaximas*0.13*int(windowHeight) #calculates distance in pixels between each maxima on the screen
    if gratingState.get() == True: #checks that the grating is enabled before plotting the diffraction pattern
        for x in range(0, numberOfSlits):
            bridgingRayline = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth)),
                                                    slitPositions[x][1]*(int(windowHeight)),
                                                    slitPositions[x][0]*(int(windowWidth))+7,
                                                    slitPositions[x][1]*(int(windowHeight)),
                                                    width=3,
                                                    fill=rayLineColour) #adds a rayline between each slit and its slit offset to fix any gaps in the rayline pattern
            for y in range(0, countMaximas+1):
                #Plotting diffraction pattern when the screen is in place.
                if screenState.get() == True:
                    verticalDistanceToLower = (screenPosition[1]*(int(windowHeight))+(y*heightBetweenMaximas)) - (slitPositions[x][1]*(int(windowHeight)))
                    verticalDistanceToUpper = (screenPosition[1]*(int(windowHeight))-(y*heightBetweenMaximas)) - (slitPositions[x][1]*(int(windowHeight)))
                    if chosenDiffractionType.get() == "Single-Slit" or chosenDiffractionType.get() == "Double-Slit": #draws all raylines for the single and double-slit
                                                                                                                     #setups
                        currentRayLine = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth))+7,
                                                      slitPositions[x][1]*(int(windowHeight)),
                                                      screenPosition[0]*(int(windowWidth)),
                                                      screenPosition[1]*(int(windowHeight))+(y*heightBetweenMaximas),
                                                      width=3,
                                                      fill=rayLineColour) #draws a rayline from the current slit to the maxima at distance y * heightBetweenMaximas
                                                                          #vertically below the centre of the screen where y is the counter variable for the number of
                                                                          #times this inner for loop must iterate to plot raylines to all the maximas
                        currentRayLine = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth))+7,
                                                      slitPositions[x][1]*(int(windowHeight)),
                                                      screenPosition[0]*(int(windowWidth)),
                                                      screenPosition[1]*(int(windowHeight))-(y*heightBetweenMaximas),
                                                      width=3,
                                                      fill=rayLineColour) #draws a rayline from the current slit to the maxima at distance y * heightBetweenMaximas
                                                                          #vertically above the centre of the screen
                    elif verticalDistanceToLower < 150 and verticalDistanceToLower > -150: #limits raylines to only having a downwards vertical range of 150 from their
                                                                                            #origin slit to prevent the diffraction pattern becoming messy
                        currentRayLine = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth))+7,
                                                      slitPositions[x][1]*(int(windowHeight)),
                                                      screenPosition[0]*(int(windowWidth)),
                                                      screenPosition[1]*(int(windowHeight))+(y*heightBetweenMaximas),
                                                      width=3,
                                                      fill=rayLineColour) #draws a rayline from the current slit to the maxima at distance y * heightBetweenMaximas
                                                                          #vertically below the centre of the screen where y is the counter variable for the number of
                                                                          #times this inner for loop must iterate to plot raylines to all the maximas
                    elif verticalDistanceToUpper < 150 and verticalDistanceToUpper > -150: #limits raylines to only having a upwards vertical range of 150 from their
                                                                                            #origin slit to prevent the diffraction pattern becoming messy
                        currentRayLine = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth))+7,
                                                      slitPositions[x][1]*(int(windowHeight)),
                                                      screenPosition[0]*(int(windowWidth)),
                                                      screenPosition[1]*(int(windowHeight))-(y*heightBetweenMaximas),
                                                      width=3,
                                                      fill=rayLineColour) #draws a rayline from the current slit to the maxima at distance y * heightBetweenMaximas
                                                                          #vertically above the centre of the screen
                        
                #Plotting diffraction pattern when the screen is not in place.
                else:
                    verticalDistanceToLower = (screenPosition[1]*(int(windowHeight))+(y*heightBetweenMaximas)) - (slitPositions[x][1]*(int(windowHeight)))
                    verticalDistanceToUpper = (screenPosition[1]*(int(windowHeight))-(y*heightBetweenMaximas)) - (slitPositions[x][1]*(int(windowHeight)))
                    if chosenDiffractionType.get() == "Single-Slit" or chosenDiffractionType.get() == "Double-Slit": #draws all raylines for the single and double-slit
                                                                                                                     #setups
                        gradient = ((screenPosition[1]*(int(windowHeight))+(y*heightBetweenMaximas)-(slitPositions[x][1]*(int(windowHeight))))/
                        (screenPosition[0]*(int(windowWidth)) - slitPositions[x][0]*(int(windowWidth))+7))
                        newXDestination = screenPosition[0]*(int(windowWidth))*2
                        if gradient !=0:
                            newYDestination = (screenPosition[1]*(int(windowHeight))) + (newXDestination - slitPositions[x][1])*gradient
                        else:
                            newYDestination = (screenPosition[1]*(int(windowHeight)))
                        currentRayLine = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth))+7,
                                                      slitPositions[x][1]*(int(windowHeight)),
                                                      newXDestination,
                                                      newYDestination,
                                                      width=3,
                                                      fill=rayLineColour) #draws a rayline from the current slit to the maxima at distance y * heightBetweenMaximas
                                                                          #vertically below the centre of the screen where y is the counter variable for the number of
                                                                          #times this inner for loop must iterate to plot raylines to all the maximas

                        if gradient !=0:
                            newYDestination = screenPosition[1]*(int(windowHeight)) - (newXDestination - slitPositions[x][1])*gradient
                        else:
                            newYDestination = (screenPosition[1]*(int(windowHeight)))

                        currentRayLine = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth))+7,
                                                      slitPositions[x][1]*(int(windowHeight)),
                                                      newXDestination,
                                                      newYDestination,
                                                      width=3,
                                                      fill=rayLineColour) #draws a rayline from the current slit to the maxima at distance y * heightBetweenMaximas
                                                                          #vertically above the centre of the screen
                    elif verticalDistanceToLower < 150 and verticalDistanceToLower > -150: #limits raylines to only having a downwards vertical range of 150 from their
                                                                                            #origin slit to prevent the diffraction pattern becoming messy
                        
                        gradient = ((screenPosition[1]*(int(windowHeight))+(y*heightBetweenMaximas)-(slitPositions[x][1]*(int(windowHeight))))/
                        (screenPosition[0]*(int(windowWidth)) - slitPositions[x][0]*(int(windowWidth))+7))
                        newXDestination = screenPosition[0]*(int(windowWidth))*20

                        if gradient !=0:
                            newYDestination = (screenPosition[1]*(int(windowHeight))) + (newXDestination - slitPositions[x][1])*gradient
                        else:
                            newYDestination = (screenPosition[1]*(int(windowHeight)))
                            
                        currentRayLine = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth))+7,
                                                      slitPositions[x][1]*(int(windowHeight)),
                                                      newXDestination,
                                                      newYDestination,
                                                      width=3,
                                                      fill=rayLineColour) #draws a rayline from the current slit to the maxima at distance y * heightBetweenMaximas
                                                                          #vertically below the centre of the screen where y is the counter variable for the number of
                                                                          #times this inner for loop must iterate to plot raylines to all the maximas
                    elif verticalDistanceToUpper < 155 and verticalDistanceToUpper > -155: #limits raylines to only having a upwards vertical range of 150 from their
                                                                                            #origin slit to prevent the diffraction pattern becoming messy
                        gradient = ((screenPosition[1]*(int(windowHeight))-(y*heightBetweenMaximas)-(slitPositions[x][1]*(int(windowHeight))))/
                        (screenPosition[0]*(int(windowWidth)) - slitPositions[x][0]*(int(windowWidth))+7))
                        newXDestination = screenPosition[0]*(int(windowWidth))*20
                        if gradient !=0:
                            newYDestination = screenPosition[1]*(int(windowHeight)) - (newXDestination - slitPositions[x][1])*gradient
                        else:
                            newYDestination = (screenPosition[1]*(int(windowHeight)))
                        currentRayLine = rayLineCanvas.create_line(slitPositions[x][0]*(int(windowWidth))+7,
                                                      slitPositions[x][1]*(int(windowHeight)),
                                                      newXDestination,
                                                      newYDestination,
                                                      width=3,
                                                      fill=rayLineColour) #draws a rayline from the current slit to the maxima at distance y * heightBetweenMaximas
                                                                          #vertically above the centre of the screen


    #Plotting intensity profile graph
    if intensityProfileState.get() == True and screenState.get() == True and viewType.get() == "Detailed": #only creates an intensity profile if it is enabled
        intensityProfileCanvas.delete("all") #clears the previous intensity profile pattern
        verticalIntensityProfileAxis = intensityProfileCanvas.create_line(0,0,0,1000, fill = "black", width = 30)
        horizontalIntensityProfileAxis = intensityProfileCanvas.create_line(0,445,500,445, fill = "black", width = 12)#displays lines for the axes of the intensity profile
        if gratingState.get() == False:
            #Creating Central maxima intensity peak
            intensityProfileCanvas.place(relwidth=0.153, relheight=0.897, relx = 0.58, rely = 0.005, anchor = "nw") #displays canvas for the intensity profile to be
                                                                                                                    #plotted on
            intensityProfileCanvas.create_line(55,
                                               (445-0.4*heightBetweenMaximas),
                                               450,
                                               445,
                                               55,
                                               (445+0.4*heightBetweenMaximas),
                                               fill=rayLineColour,
                                               width=3,
                                               smooth = 1,
                                               capstyle=ROUND,
                                               joinstyle=BEVEL) #draws the central maxima intensity peak
            
            intensityProfileCanvas.create_line(55,
                                               (445-0.4*heightBetweenMaximas),
                                               19,
                                               (445-0.6*heightBetweenMaximas),
                                               15,
                                               0,
                                               fill=rayLineColour,
                                               width=3,
                                               smooth = 1,
                                               capstyle=ROUND,
                                               joinstyle=BEVEL) #draws the top base of the central maxima intensity peak
            intensityProfileCanvas.create_line(55,
                                               (445+0.4*heightBetweenMaximas),
                                               19,
                                               (445+0.6*heightBetweenMaximas),
                                               15,
                                               900,
                                               fill=rayLineColour,
                                               width=3,
                                               smooth = 1,
                                               capstyle=ROUND,
                                               joinstyle=BEVEL) #draws the bottom base of the central maxima intensity peak
            
        else:
            intensity = 1.0 #the intensity for the current peak
            intensityIncrement = 0.9/countMaximas #the reduction in intensity of each peak is calculated
            #Creating Central maxima intensity peak
            line2 = intensityProfileCanvas.create_line(70,
                                               (445-0.4*heightBetweenMaximas),
                                               450,
                                               445,
                                               70,
                                               (445+0.4*heightBetweenMaximas),
                                               fill=rayLineColour,
                                               width=3,
                                               smooth = 1,
                                               capstyle=ROUND,
                                               joinstyle=BEVEL) #draws the central maxima intensity peak
            baseCordMultiplier = 0.4
            minIntensityHeight = 35 #initialises the scaling variables for the bases between each peak prior to the for loop starting
            
            for x in range(0, countMaximas):
                #Creating the curves between the bases of each peak
                intensityProfileCanvas.create_line(2*minIntensityHeight,
                                               (445-baseCordMultiplier*heightBetweenMaximas),
                                               minIntensityHeight,
                                               (445-(baseCordMultiplier+0.1)*heightBetweenMaximas),
                                               2*minIntensityHeight,
                                               (445-(baseCordMultiplier+0.2)*heightBetweenMaximas),
                                               fill=rayLineColour,
                                               width=3,
                                               smooth = 1,
                                               capstyle=ROUND,
                                               joinstyle=BEVEL) #draws the the curves between the base of one of the peaks above the central peak and the next
                intensityProfileCanvas.create_line(2*minIntensityHeight,
                                               (445+baseCordMultiplier*heightBetweenMaximas),
                                               minIntensityHeight,
                                               (445+(baseCordMultiplier+0.1)*heightBetweenMaximas),
                                               2*minIntensityHeight,
                                               (445+(baseCordMultiplier+0.2)*heightBetweenMaximas),
                                               fill=rayLineColour,
                                               width=3,
                                               smooth = 1,
                                               capstyle=ROUND,
                                               joinstyle=BEVEL) #draws the the curves between the base of one of the peaks below the central peak and the next

                #Creating each peak of the intensity profile
                intensity -= intensityIncrement #decreases the intensity for each new peak by the constant amount of intensityIncrement
                intensityProfileCanvas.create_line(2*minIntensityHeight,
                                               (445-(baseCordMultiplier+0.2)*heightBetweenMaximas),
                                               450*(intensity),
                                               (445-(baseCordMultiplier+0.5)*heightBetweenMaximas),
                                               2*(minIntensityHeight-(25/countMaximas)),
                                               (445-(baseCordMultiplier+1)*heightBetweenMaximas),
                                               fill=rayLineColour,
                                               width=3,
                                               smooth = 1,
                                               capstyle=ROUND,
                                               joinstyle=BEVEL) #draws the current intensity peak above the central maxima
                intensityProfileCanvas.create_line(2*minIntensityHeight,
                                               (445+(baseCordMultiplier+0.2)*heightBetweenMaximas),
                                               450*(intensity),
                                               (445+(baseCordMultiplier+0.5)*heightBetweenMaximas),
                                               2*(minIntensityHeight-(25/countMaximas)),
                                               (445+(baseCordMultiplier+1)*heightBetweenMaximas),
                                               fill=rayLineColour,
                                               width=3,
                                               smooth = 1,
                                               capstyle=ROUND,
                                               joinstyle=BEVEL) #draws the current intensity peak below the central maxima
                
                baseCordMultiplier += 1 #increments the positional variable for the base of each peak
                minIntensityHeight -= (25/countMaximas) #decreases the intensity (height) for the base of each peak

        #Plotting screen view:
        rayLineColourAsRGB = rayLineColour.lstrip('#') #removes the # from the hex colour value
        rayLineColourAsRGB = (tuple(int(rayLineColourAsRGB[i:i+2], 16) for i in (0, 2, 4))) #converts rayLineColour to RGB
        rayLineColourH, rayLineColourS, rayLineColourV  = ColorSys.rgb_to_hsv(rayLineColourAsRGB[0], rayLineColourAsRGB[1], rayLineColourAsRGB[2])
        #converts the ray line colour from RGB to HSV for brightness alteration
        rayLineColourListVValues = [] #declares a list to store the V values for each HSV colour for each varying brightness of the ray line colour
        incrementV = rayLineColourV/20 #sets an increment for how quickly the brightness (V value) should fall
        
        for x in range(0,19):
            rayLineColourListVValues.append(rayLineColourV-(incrementV*x)) #iteratively reduces the brightness of the colour and stores each value into the declared list
        rayLineColourListVValues.reverse() #reverses the list so that the circles are plotted with colours in the correct order

        rayLineColoursAsHexList = [] #declares a list to store the hexadecimal values for each HSV colour
        for each in rayLineColourListVValues:
            currentR, currentG, currentR = ColorSys.hsv_to_rgb(rayLineColourH, rayLineColourS ,each)
            rayLineColoursAsHexList.append(rgb2hex(math.trunc(currentR), math.trunc(currentG), math.trunc(currentR))) #iterates through the list and converts each HSV
                                                                                                                        #colour to hexadecimal using the list of V values
                                                                                                                        #and constant H and S values
        sizeMaxima = 1 #sets the size of the current maxima (the central one)
        innerCircleSizeIncrement = (sizeMaxima*40)/len(rayLineColoursAsHexList) #calculates the size difference between each circle 
        innerCircleCornerSizeIncrement = innerCircleSizeIncrement/2 #divides this size difference by two to use for the difference in the coordinates at both the top-left
                                                                    #and bottom right 'corners' of the circle
        countSizeIncrement = 0 #counter variable to decrease the size of the circle by innerCircleSizeIncrement each time the below for loop iterates
        for eachColour in rayLineColoursAsHexList:
            screenViewCanvas.create_oval(225+countSizeIncrement*innerCircleCornerSizeIncrement,
                                         105+countSizeIncrement*innerCircleCornerSizeIncrement,
                                         275-countSizeIncrement*innerCircleCornerSizeIncrement,
                                         155-countSizeIncrement*innerCircleCornerSizeIncrement,
                                         fill = eachColour,
                                         outline="") #plots a circle of the correct 'brightness' (from the calculated colour value) of size
                                                            #50- (innerCircleSizeIncrement multiplied by the counter variable)
            countSizeIncrement +=1 #increments create_oval
        screenViewCanvas.create_oval(243, 123, 257, 137, fill = rayLineColour, outline="") #plots the middle bright spot

        if gratingState.get() == True: #plots the remaining bright spots from the diffraction pattern if the grating is enabled
            print(countMaximas)
            sizeIncrement = sizeMaxima/countMaximas #calculates the amount which the size of each next bright spot from the centre of the screen view should decrease by
            for x in range(0, countMaximas):
                sizeMaxima -= sizeIncrement #decrements the maxima size each time the loop iterates one bright spot further from the central bright spot
                innerCircleSizeIncrement = (sizeMaxima*40)/len(rayLineColoursAsHexList) #calculates the size difference between each circle 
                innerCircleCornerSizeIncrement = innerCircleSizeIncrement/2 #divides this size difference by two to use for the difference in the coordinates at both
                                                                            #the top-left and bottom right 'corners' of the circle
                countSizeIncrement = 0 #counter variable to decrease the size of the circle by innerCircleSizeIncrement each time the below for loop iterates
                offsetX = -heightBetweenMaximas*x*2 #calculates the distance between the central maxima bright spot and the current one being plotted
                
                for countSpotsPerCountMaxima in range(0,2): #loops the creating of the bright spot twice for each side of the central bright spot
                    countSizeIncrement = 0 #counter variable to decrease the size of the circle by innerCircleSizeIncrement each time the below for loop iterates
                    for eachColour in rayLineColoursAsHexList:
                        screenViewCanvas.create_oval(225+countSizeIncrement*innerCircleCornerSizeIncrement + offsetX + 50*sizeIncrement*x,
                                                     105+countSizeIncrement*innerCircleCornerSizeIncrement + 50*sizeIncrement*x,
                                                     275-countSizeIncrement*innerCircleCornerSizeIncrement + offsetX - 50*sizeIncrement*x,
                                                     155-countSizeIncrement*innerCircleCornerSizeIncrement - 50*sizeIncrement*x,
                                                     fill = eachColour,
                                                     outline="") #plots a circle of the correct 'brightness' (from the calculated colour value) of size
                                                                        #50- (innerCircleSizeIncrement multiplied by the counter variable)
                        countSizeIncrement +=1 #increments create_oval
                    screenViewCanvas.create_oval(243 + offsetX + 10*sizeIncrement*x,
                                                 123 + 10*sizeIncrement*x,
                                                 257 + offsetX - 10*sizeIncrement*x,
                                                 137 - 10*sizeIncrement*x,
                                                 fill = rayLineColour,
                                                 outline="") #plots the middle bright spot of the current bright spot
                    offsetX = -offsetX #reverses the offset from the centre to plot the same bright spot on the opposite side of the central maxima's bright spot
                    
def toggleRulerState(): #procedure to toggle the display of the ruler
    if rulerState.get() == False:
        ruler.hide()  #hides the ruler if the ruler is disabled
    else:
        ruler.displayNew() #shows the ruler if the ruler is enabled

def toggleProtractorState(): #procedure to toggle the display of the protractor 
    if protractorState.get() == False:
        protractor.hide() #hides the protractor if the protractor is disabled
    else:
        protractor.displayNew() #shows the protractor if the protractor is enabled



















#Misc documentation code:

#Plotting screen view
#screenViewCanvas.create_oval(225, 105, 275, 155, fill = rayLineColour) #plots middle circle for the central maxima bright spot

#rayLineColour = ColorSys.rgb_to_hsv(rayLineColourAsRGB[0], rayLineColourAsRGB[1], rayLineColourAsRGB[2]) #converts the ray line colour from RGB to HSV for brightness
                                                                                                              #alteration
#print(rayLineColourAsHSV) #output to test whether the RGB value has been successfully converted


































        #print("x0=", (225+countSizeIncrement*innerCircleCornerSizeIncrement), "colour = ", eachColour)
            
#def rgb2hex(r,g,b):
    #return "#{:02x}{:02x}{:02x}".format(r,g,b)
















                
        #Creating darker shades of colour used:
        #for y in range(0,5):
            #screenViewCanvas.create_oval(225-y*10, 105-y*10, 275+y*10, 155+y*10, fill = rayLineColour)
            #for x in range(1,7):
                #try:
                    #rayLineColour[x] = str(int(rayLineColour[x]) - math.trunc(0.25*int(rayLineColour[x])))
                #except(ValueError):
                    #if rayLineColour[x] == "a":
                        #rayLineColour[x] = "8"
                   # elif rayLineColour[x] == "b":
                        #rayLineColour[x] = "9"
                    #elif rayLineColour[x] == "c":
                        #rayLineColour[x] = "9"
                    #elif rayLineColour[x] == "d":
                        #rayLineColour[x] = "9"
                    #elif rayLineColour[x] == "e":
                       # rayLineColour[x] = "a"
                   # elif rayLineColour[x] == "f":
                       # rayLineColour[x] = "a"
        
                    
        #screenViewCanvas.create_oval(150, 150, 350, 350, fill = "green")
        #screenViewCanvas.create_oval(200, 200, 300, 300, fill = "red")
    
mainMenuOpen(False)

#screenGratingDistanceSlider.bind("<ButtonRelease-1>", updateScreenGratingDistanceValueFromSlider) #runs updateScreenGratingDistanceValueFromSlider every time the
                                                                                #slider is changed to a new value so that the diffraction pattern and value in the
                                                                                #entry box for slitSeparation are updated upon each change to the slitSeparation

#heightBetweenMaximas = ((10**-9)*wavelength.get())*screenGratingDistance.get()/(((10**-6)*slitSeparation.get()**2)-((10**-9)*wavelength.get()**2))**0.5
    #rayLineCanvas.create_line(0.5*int(windowWidth),
                              #screenPosition[1]*(int(windowWidth))*20,
                              #0.3*int(windowWidth),
                              #screenPosition[1]*(int(windowWidth))*20 + 0.5*heightBetweenMaximas,
                              #0.3*int(windowWidth),
                              #screenPosition[1]*(int(windowWidth))*20 - 0.5*heightBetweenMaximas,
                              #smooth=1,
                              #width=3,
                              #fill = rayLineColour)

    #centralPeakImage = rayLineCanvas.create_image(100,100,anchor=NW,image=intensityProfileHighPeakIcon)
    #centralPeakImage.image = intensityProfileLowestPeakIcon
    #intensityProfileHighPeakIcon = PhotoImage(file = "IntensityProfilePeakHigh.png")
    #intensityProfileMedPeakIcon = PhotoImage(file = "IntensityProfilePeakMed.png")
    #intensityProfileLowPeakIcon = PhotoImage(file = "IntensityProfilePeakLow.png")
    #intensityProfileLowestPeakIcon = PhotoImage(file = "IntensityProfilePeakLowest.png")

        #intensityProfileCanvas.create_line(50,
                                          # 50,
                                           #70,
                                           #(445-0.4*heightBetweenMaximas),
                                          # 450,
                                          # 445,
                                          ## 70,
                                          # (445+0.4*heightBetweenMaximas),
                                          # 50,
                                          # 800,
                                         #  fill=rayLineColour,
                                         #  width=3,
                                         #  smooth = 1,
                                         #  capstyle=ROUND,
                                         #  joinstyle=BEVEL) #draws the central maxima intensity peak

#def drag_start(event):
    #widget = event.widget
    #widget._drag_start_x = event.x
    #widget._drag_start_y = event.y

#def drag_motion(event):
    #widget = event.widget
    #x = widget.winfo_x() - widget._drag_start_x + event.x
    #y = widget.winfo_y() - widget._drag_start_y + event.y
    #widget.place(x=x, y=y)

#root = tk.Tk()
#canvas = tk.Canvas(root, width=400, height=400)
#canvas.pack()

#rect = canvas.create_rectangle(10, 10, 50, 50, fill="blue")

#rayLineCanvas.tag_bind(ruler.getObjectLabel(), "<Button-1>", drag_start)
#rayLineCanvas.tag_bind(ruler.getObjectLabel(), "<B1-Motion>", drag_motion)
