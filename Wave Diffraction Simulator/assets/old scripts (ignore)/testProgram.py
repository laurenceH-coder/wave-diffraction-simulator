from tkinter import * #imports the required tkinter modules needed for the program's GUIs#
import ctypes
import time
import math
import colorpy as color
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def mainMenuOpen():
    global mainMenu
    mainMenu = Tk() #instantiates a window
    saveFileNumber = StringVar()
    saveFileNumber.set(0) #declares the variable saveFileNumber and sets it to zero
    savedSetupsMenu = [0,0,0]
    #Window Setup
    global windowWidth
    global windowHeight
    windowWidth = str(mainMenu.winfo_screenwidth())
    windowHeight = str(mainMenu.winfo_screenheight()) #gets screen dimensions and stores them as variables
    
    print("Window Width:", windowWidth, "\nWindow Height:", windowHeight) #testing that the system obtains the correct values for windowWidth and
                                                                          #windowHeight
    mainMenu.geometry(windowWidth + "x" + windowHeight) #sets the size of the window to the arbitrary 5size of 500 pixels wide, 600 pixels high
    mainMenu.title("Wave Diffraction Simulator") #sets the title for the main menu window
    waveDiffractionIcon = PhotoImage(file = 'programIcon.png')
    mainMenu.iconphoto(True, waveDiffractionIcon)
    mainMenu.wm_attributes('-transparentcolor', '#ab23ff')
    mainMenu.config(bg = '#f8f4f4')

    #Static GUI Elements Setup (Labels, Images)
    global welcomeLabel
    welcomeLabel = Label(mainMenu,
                         text="Welcome to the Wave \n Diffraction Simulator!",
                         justify="center",
                         font=('Arial',20,'bold'),
                         bg = '#f8f4f4')
    welcomeLabel.place(relx=0.5,y=50, anchor = 'n') #sets text and text settings of the welcome text label and places it

    global savedSetupsLabel
    savedSetupsLabel = Label(mainMenu,
                             text="Saved Setups:",
                             justify="center",
                             font=('Arial', 17, 'underline'),
                             bg = '#f8f4f4')
    
    savedSetupsLabel.place(relx=0.5,rely=0.28, anchor = 'n') #sets text and text settings of the saved setups text label and places it

    try:
        file = open('saveFile1.txt') #checks if save file 1 exists in the save files folder
        global savedSetup1Button
        savedSetup1Button = Radiobutton(mainMenu, text='Save File 1', justify="left", variable=saveFileNumber, value=1)
        savedSetup1Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 padx=125,
                                 pady=45,
                                 indicatoron=0)
        savedSetup1Button.place(relx=0.5,rely=0.35, anchor = 'n') #creates a radio button which allows the user to select to load save file 1
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
        file = open('saveFile2.txt') #checks if save file 2 exists in the save files folder
        global savedSetup2Button
        savedSetup2Button = Radiobutton(mainMenu, text='Save File 2', justify="left", variable=saveFileNumber, value=2)
        savedSetup2Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 padx=125,
                                 pady=45,
                                 indicatoron=0)
        savedSetup2Button.place(relx=0.5,rely=0.53, anchor = 'n') #creates a radio button which allows the user to select to load save file 2
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
        file = open('saveFile3.txt') #checks if save file 3 exists in the save files folder
        global savedSetup3Button
        savedSetup3Button = Radiobutton(mainMenu, text='Save File 3', justify="left", variable=saveFileNumber, value=3)
        savedSetup3Button.config(font=('Arial', 25, 'bold'),
                                 relief='raised',
                                 border=5,
                                 padx=125,
                                 pady=45,
                                 indicatoron=0)
        savedSetup3Button.place(relx=0.5,rely=0.71, anchor = 'n') #creates a radio button which allows the user to select to load save file 3
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

    leftMenuImageUnscaled = PhotoImage(file='testImage1.png')
    leftMenuImage = leftMenuImageUnscaled.zoom(int(windowWidth)//100, int(windowHeight)//100)            #this new image is 3x the original
    leftMenuImage = leftMenuImage.subsample(14, 8)   #halve the size, it is now 1.5x the original
    global leftMenuImageLabel
    leftMenuImageLabel = Label(mainMenu, image=leftMenuImage) #defines and sets the image label which will be shown on the
                                                                #left side of the screen 
    leftMenuImageLabel.place(relx=0.015, rely = 0.5, anchor='w') #places this image on the left side of the screen)

    rightMenuImageUnscaled = PhotoImage(file='testImage1.png')
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
    global chosenDiffractionType
    chosenDiffractionType = StringVar()
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

    

def loadPreviousSystem(saveFileNo, savedSetupsMenuArray):
    print(saveFileNo)
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



def generateSystem(systemValues):
    if len(systemValues) == 1: #this will check if the array of the system values passed in is of the format of a new system being loaded
        if systemValues[0] != "None": 
            print("Generating setup of diffraction type:" , systemValues[0], "!") #A confirmation output message is given for which of the three
                                                                                    #diffraction types has been selected and will be loaded.
        else:
            print("No diffraction type provided!") #A message stating that the user has not selected one of the diffraction type options is provided.
            global newSystemNoTypeLabel
            newSystemNoTypeLabel = Label(mainMenu,
                                         text = "Please select one of the setups above!",
                                         fg="red",
                                         font = ('Arial', 15))
            newSystemNoTypeLabel.place(relx = 0.5, anchor = "center", rely = 0.91) #A label asking the user to select one of the provided diffraction type options is displayed.
            return False
    elif len(systemValues) == 26: #this number is not final, but will check if the array of system values passed in is of the format of a previous system which is being loaded
        print("Loading previous system!")
    else:
        print("Invalid systemValues array provided.")   #If an invalid length of array of system values is passed into the array, the system does not continue further in using it as
                                                        #this would generate errors later in the program. A default diffraction setup will be loaded with an appropriate
                                                        #error message when this subroutine is further developed.
    #Code to remove all menu GUI elements
    confirmDiffractionTypeLabel.place_forget()
    diffractionTypeOptionsLabel.place_forget()
    singleSlitDiffractionSelectionButton.place_forget()
    doubleSlitDiffractionSelectionButton.place_forget()
    diffractionGratingSelectionButton.place_forget()
    confirmDiffractionTypeButton.place_forget()
    backDiffractionTypeButton.place_forget()
    leftMenuImageLabel.place_forget()
    rightMenuImageLabel.place_forget() #removes all of the default widgets except the design images from the confirm diffraction type screen
    
    global gratingState
    gratingState = BooleanVar() #declares global boolean variable gratingState
    gratingState.set(True)
    
    global rayLineCanvas
    rayLineCanvas = Canvas(mainMenu, bg='#f8f4f4', border=0)
    rayLineCanvas.place(relwidth=1, relheight=1, relx = 0, rely = 0, anchor = "nw")#defines and places a full-screen canvas for the ray lines to be plotted on

    global screenPosition
    screenPosition = [0.56,0.4165]
    
    try:
        newSystemNoTypeLabel.place_forget()
    except(NameError):
        print("No error message to remove.") #removes the message informing the user to select a diffraction type if it is present on the screen. If this is not
                                             #present, an output message confirming this exception has run is printed.
        
    #Code to create diffraction environment window
    global grating
    if chosenDiffractionType.get() ==  "Single-Slit":
        diffractionSimulatorTypeText = "Single-Slit Wave Diffraction Simulator"
        mainMenu.title(diffractionSimulatorTypeText) #if the user has selected the single-slit diffraction type, then set title of window to 'Single-Slit
                                                            #Diffraction Simulator'
        diffractionSimulatorTypeText = "Single-Slit Wave \nDiffraction Simulator"
        grating = SimulationApparatus(0.3, 0.0037, "singleSlitGratingIcon.png") #creates an instance of simuationApparatus for the single-slit grating
    elif chosenDiffractionType.get() ==  "Double-Slit":
        diffractionSimulatorTypeText = "Double-Slit Wave Diffraction Simulator"
        mainMenu.title(diffractionSimulatorTypeText) #if the user has selected the single-slit diffraction type, then set title of window to 'Double-Slit
                                                            #Diffraction Simulator'
        diffractionSimulatorTypeText = "Double-Slit Wave \nDiffraction Simulator"
        grating = SimulationApparatus(0.3, 0.0037, "doubleSlitGratingIcon.png") #creates an instance of simuationApparatus for the double-slit grating
    else:
        diffractionSimulatorTypeText = "Diffraction-Grating Wave Diffraction Simulator"
        mainMenu.title(diffractionSimulatorTypeText) #if the user has selected the diffraction-grating diffraction type, then set title of window to 'Diffraction
                                                        #Grating Simulator'
        diffractionSimulatorTypeText = "Diffraction-\nGrating Wave Diffraction \nSimulator"
        grating = SimulationApparatus(0.3, 0.0037, "diffractionGratingIcon.png") #creates an instance of simuationApparatus for the diffraction grating
        
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

    global intensityProfileAxesLabel
    intensityProfileAxesIcon = PhotoImage(file = "intensityProfileIcon.png")
    intensityProfileAxesLabel = Label(mainMenu,
                                      image = intensityProfileAxesIcon)
    intensityProfileAxesLabel.image = intensityProfileAxesIcon #sets the image settings for the label which shows the intensity profile axes

    global intensityProfileIndicatorLabel
    intensityProfileIndicatorLabel = Label(mainMenu, text = "Intensity Profile", font=('Arial', 15)) #sets text and text settings for the label to indicate the intensity
                                                                                                        #profile below it
    
    global viewType
    viewType = StringVar()
    viewType.set("Detailed")
    
    global laserState
    laserState = BooleanVar() #declares global boolean variable laserState
    laserState.set(True)
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
    wavelength.set(500.000) #initialises the wavelength value as 500.000

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
    slitSeparation = DoubleVar() #declares global decimal variable slitSeparation
    slitSeparation.set(2.000) #initialises the slitSeparation value as 2.000

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
                                 to=9.999,
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
                                    text="Slit Separation [s] (mm)",
                                    bg = '#dedede',
                                    font=('Arial', 12))
    slitSeparationSettingsLabel.place(relx = 0.5, rely = 0.272, anchor = 'nw') #defines and places the slitSeparation text label

    global screenGratingDistance
    screenGratingDistance = DoubleVar() #declares global decimal variable screenGratingDistance
    screenGratingDistance.set(1.000) #initialises the screenGratingDistance value as 1.000

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
    rulerState = BooleanVar() #declares global boolean variable rulerState
    rulerState.set(True)
    rulerStateButton = Checkbutton(settingsFrame,
                                   text=" Ruler",
                                   variable=rulerState,
                                   onvalue=True,
                                   offvalue=False) #sets text, variable and on/off values for the button which controls the value of rulerState
    rulerStateButton.config(bg="#dedede",
                            activebackground="#dedede",
                            font=("Arial", 15),
                            border=0,
                            relief="raised",
                            padx=10,
                            pady=5) #sets the visual properties of the check button which controls the value of rulerState
    rulerStateButton.place(relx=0.02, rely = 0.37, anchor = 'nw') #places the check button controlling rulerState's value

    global intensityProfileState
    intensityProfileState = BooleanVar() #declares global boolean variable intensityProfileState
    intensityProfileState.set(True)
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
    protractorState = BooleanVar() #declares global boolean variable protractorState
    protractorState.set(True)
    protractorStateButton = Checkbutton(settingsFrame,
                                   text=" Protractor",
                                   variable=protractorState,
                                   onvalue=True,
                                   offvalue=False) #sets text, variable and on/off values for the button which controls the value of protractorState
    protractorStateButton.config(bg="#dedede",
                            activebackground="#dedede",
                            font=("Arial", 15),
                            border=0,
                            relief="raised",
                            padx=10,
                            pady=5) #sets the visual properties of the check button which controls the value of protractorState
    protractorStateButton.place(relx=0.55, rely = 0.41, anchor = 'nw') #places the check button controlling protractorState's value

    global screenViewState
    screenViewState = BooleanVar() #declares global boolean variable screenViewState
    screenViewState.set(True)
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

    global screenViewFrame
    screenViewFrame = Frame(settingsFrame,
                          bg='#000000',
                          border=0,
                          width=480,
                          height=400) #defines a dark frame for the elements of the screen view environment
    screenViewFrame.place(relx = 1, rely = 0.6808, anchor = 'ne') #places this frame in the bottom-right corner of the user's screen
    
    global disabledScreenViewLabel
    disabledScreenViewLabel = Label(settingsFrame,
                                    bg='#dedede',
                                    text="Click the 'Screen in place'\nbox to enable the screen\nview.",
                                    justify="center",
                                    border=0,
                                    padx=10,
                                    pady=12,
                                    font=('Arial', 21)) #defines a label which displays when the screen view is disabled

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
    laserStateONIconLabel.place(relx=0.0335, rely = 0.435, anchor='nw') #places this image in the correct position
    laserStateONIconLabel.image = laserStateONIcon #adds permanent reference for the laser on icon image to prevent it not being displayed correctly

    laserStateOFFIconUnscaled = PhotoImage(file="OFFSwitchIcon.png")
    laserStateOFFIcon = laserStateOFFIconUnscaled.subsample(4,4)
    global laserStateOFFIconLabel
    laserStateOFFIconLabel = Label(mainMenu, image=laserStateOFFIcon, border=0) #defines and sets the image label which will display when the laser is off
    laserStateOFFIconLabel.image = laserStateOFFIcon #adds permanent reference for the laser off icon image to prevent it not being displayed correctly

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
            intensityProfileAxesLabel.place(relx = 0.578 ,rely = 0.456 ,anchor="w") #displays the intensity profile axes and its indicator label is the intensity profile
                                                                                    #is enabled
        metreScaleArrowLabel.place(relx = 0.02, rely = 0.935, anchor = 'nw') #displays the scale label if detailed view is initially enabled
    else:
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
    screenState.set(True)
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


def saveSetupPrompt():
    print("ran saveSetupPrompt successfully") #test output to tell if saveSetupPrompt runs successfully upon clicking the 'Save Setup' button

def loadSetupPrompt():
    print("ran loadSetupPrompt successfully") #test output to tell if loadSetupPrompt runs successfully upon clicking the 'Load Setup' button

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
        slitSeparationSettingsLabel.config(text = "Slit Separation [s] (mm)")
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
        intensityProfileAxesLabel.place_forget() #hides intensity profile axes and its indicator label
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
    print("ran mainMenuReturnFromEnvironment successfully") #test output to tell if mainMenuReturnFromEnvironment runs successfully upon clicking the 'Return to Main Menu'
                                                            #button

def toggleLaserState():
    if (laserState.get()) == True:
        laserStateOFFIconLabel.place_forget()  #hides the off laser image
        laserStateONIconLabel.place(relx=0.0335, rely = 0.435, anchor='nw') #places the on laser image
    else:
        laserStateONIconLabel.place_forget() #hides the on laser image
        laserStateOFFIconLabel.place(relx=0.0335, rely = 0.435, anchor='nw') #places the off laser image
        
def toggleScreenView():
    if screenViewState.get() == True:
        screenViewFrame.place(relx = 1, rely = 0.6808, anchor = 'ne') #places this frame in the bottom-right corner of the user's screen
        disabledScreenViewLabel.place_forget() #removes no longer needed screen view disabled text label
    else:
        screenViewFrame.place_forget() #removes no longer needed screen view frame
        if screenState.get() == True:
            disabledScreenViewLabel.config(text = "Click the 'Screen View'\nbox to enable the screen\nview.")
        disabledScreenViewLabel.place(relx=0.5, rely = 0.725, anchor = 'n') #sets text and text settings of the screen view disabled text label and places it
    
    
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
        grating.setXCord(0.3+0.12*(2-screenGratingDistance.get()))
        
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

def updateSlitSeparationValueFromEntry(event):
    try:
        if (float(stringSlitSeparation.get()))>9.999 or (float(stringSlitSeparation.get()))<1:
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
        savedSetup1Button.place(relx=0.5,rely=0.35, anchor = 'n')
    try:
        savedSetup2EmptyLabel.place(relx=0.5,rely=0.53, anchor = 'n')
    except(NameError):
        savedSetup2Button.place(relx=0.5,rely=0.53, anchor = 'n')
    try:
        savedSetup3EmptyLabel.place(relx=0.5,rely=0.71, anchor = 'n')
    except(NameError):
        savedSetup3Button.place(relx=0.5,rely=0.71, anchor = 'n') #The program attempts to replace every empty setup label that existed originally in the starting main menu screen,
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

def drawArrowLine(xCord1, yCord1, xCord2, yCord2, canvas, widthLine):
    canvas.delete('all')
    canvas.create_line(xCord1, yCord1, xCord2, yCord2, width=widthLine) #creates the required arrow line of specified width between two specified points on a
                                                                        #specified canvas

def toggleGratingState():
    if (gratingState.get()) == False:
        grating.hide() #hides grating
        leftScreenGratingArrowLabel.place_forget()
        rightScreenGratingArrowLabel.place_forget()
        screenGratingDistanceScaleLabel.place_forget()
        screenGratingArrowCanvas.delete('all') #hides all of the environment's labels/arrows for the grating
        slitSeparationSlider.config(state='disabled')
        screenGratingDistanceSlider.config(state='disabled')
        screenGratingDistanceSliderValueLabel.config(state='disabled')
        slitSeparationSliderValueLabel.config(state='disabled') #disables uneditable variables for when the grating is inactive
        
    else:
        grating.display() #shows grating
        if screenState.get() == True:
            updateScreenGratingDistanceValueFromSlider("enable") #runs updateScreenGratingDistanceValueFromSlider to show appropriate labels and update position of grating
            screenGratingDistanceSlider.config(state='normal')
            screenGratingDistanceSliderValueLabel.config(state='normal')
        slitSeparationSlider.config(state='normal')
        slitSeparationSliderValueLabel.config(state='normal') #re-enables uneditable variables when the grating is inactive when it becomes active again
    updateDiffractionPattern()

def toggleScreenState():
    if (screenState.get()) == False:
        screen.hide() #hides screen
        screenViewFrame.place_forget() #removes no longer needed screen view frame
        disabledScreenViewLabel.config(text = "Click the 'Screen in place'\nbox to enable the screen\nview.")
        disabledScreenViewLabel.place(relx=0.5, rely = 0.725, anchor = 'n') #sets text and text settings of the screen view disabled text label and places it
        screenViewStateButton.config(state = 'disabled') #disables screen view and the button to toggle it
        intensityProfileIndicatorLabel.place_forget()
        intensityProfileAxesLabel.place_forget() #hides intensity profile axes and its indicator label
        intensityProfileStateButton.config(state = 'disabled') #disables intensity profile and the button to toggle it
        leftScreenGratingArrowLabel.place_forget()
        rightScreenGratingArrowLabel.place_forget()
        screenGratingDistanceScaleLabel.place_forget()
        screenGratingArrowCanvas.delete('all') #hides all of the environment's labels/arrows for the screen
        screenGratingDistanceSlider.config(state='disabled')
        screenGratingDistanceSliderValueLabel.config(state='disabled') #disables uneditable variables for when the screen is inactive
        
    else:
        screen.display() #shows screen
        toggleScreenView()
        screenViewStateButton.config(state = 'normal') #re-enables screen view and the button to toggle it
        if intensityProfileState.get() == True and viewType.get() == "Detailed":
            intensityProfileIndicatorLabel.place(relx=0.65, rely=0.96, anchor = "center")
            intensityProfileStateButton.config(state = 'normal') #re-enables intensity profile, its indicator label the button to toggle it
            intensityProfileAxesLabel.place(relx = 0.578 ,rely = 0.456 ,anchor="w") #shows intensity profile axes at correct position if enabled
        if gratingState.get() == True:
            updateScreenGratingDistanceValueFromSlider("enable") #runs updateScreenGratingDistanceValueFromSlider to show appropriate labels and update position of screen
            screenGratingDistanceSlider.config(state='normal')
            screenGratingDistanceSliderValueLabel.config(state='normal') #re-enables uneditable variables when the screen is inactive when it becomes active again

def toggleIntensityProfile():
    if intensityProfileState.get() == True:
        intensityProfileIndicatorLabel.place(relx=0.65, rely=0.96, anchor = "center")
        intensityProfileAxesLabel.place(relx = 0.578 ,rely = 0.456 ,anchor="w") #shows intensity profile axes and its indicator label at correct position if enabled
    else:
        intensityProfileIndicatorLabel.place_forget()
        intensityProfileAxesLabel.place_forget() #hides intensity profile axes and its indicator label if disabled

def wavelengthToHex(wavelengthValue):
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
                            700: '#cd0000'}
    try:
        return (wavelengthDictionary[(wavelengthValue//5)*5])
    except(KeyError):
        return -1
    
def updateDiffractionPattern():
    rayLineColour = wavelengthToHex(wavelength.get())
    rayLineCanvas.delete("all")
    if screenState.get() == True:
        currentRayLine = rayLineCanvas.create_line(0.0865*(int(windowWidth)),
                                  screenPosition[1]*(int(windowHeight)),
                                  screenPosition[0]*(int(windowWidth)),
                                  screenPosition[1]*(int(windowHeight)),
                                  width=5,
                                  fill=rayLineColour,
                                  tags = 'lineTag') #draws the central rayline on the canvas as far as the screen if the screen is enabled
    for x in range(100):
        rayLineCanvas.tag_raise('lineTag') #attempts to raises the rayline above the grating
    print(rayLineColour)

mainMenuOpen()

#screenGratingDistanceSlider.bind("<ButtonRelease-1>", updateScreenGratingDistanceValueFromSlider) #runs updateScreenGratingDistanceValueFromSlider every time the
                                                                                #slider is changed to a new value so that the diffraction pattern and value in the
                                                                                #entry box for slitSeparation are updated upon each change to the slitSeparation

