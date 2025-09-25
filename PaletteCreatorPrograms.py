# Program to save and create color palettes

# Function Bay

def addToFile(toWrite):
    with open("PaletteStorage.txt","a") as paletteFile:
        paletteFile.write(toWrite + "\n")

#returns list
def readFromFile():
    with open("PaletteStorage.txt","r") as paletteFile:
        return paletteFile.readlines()

def exportTranslater(name, colors):
    toExport = name + "$"
    for color in colors:
        toExport = toExport + color + "%"
    toExport = toExport
    return toExport

def paletteCreator():
    userEngaged = True

    print("Welcome to the paletteCreator!")

    # Ask for the name of the new palette
    paletteName = input("Enter palette name: ")

    # Create a palette list
    selectedColors = []

    while userEngaged:
        # Ask user to input a color
        colorPicker = input("Enter a color: ")
        
        # Add the color to the palette
        selectedColors.append(colorPicker)

        # Ask if the user wants to add another color
        userChoice = input("Would you like to add another color? (Y/N): ")

        if userChoice.lower() == "n":
            userEngaged = False

    # Print all colors in the new palette
    print(selectedColors)

    toSave = input("Would you like to save this palette? (Y/N): ")

    if toSave == 'Y' or 'y':
        paletteToSave = exportTranslater(paletteName, selectedColors)
        addToFile(paletteToSave)
    input("[Enter] to close: ")

def loadPalettesFromStorage():
    loadedPalettes = []

    savedPaletteList = readFromFile()
    for savedPalette in savedPaletteList: # pulls the string off the list

        savedClass = ""
        incrementList = []
        wordBus = ""
        paletteNameList = []
        pos = 0

        for savedChar in savedPalette: # pulls the char off the string
                                
            if savedChar != "$" or "%" or "\n":
            
                incrementList.append(savedChar)
                    

            if savedChar == "$":
                while pos < len(incrementList)-1:
                    wordBus = wordBus + incrementList[pos]
                    pos += 1   
                wordBus = Palette(wordBus)
                loadedPalettes.append(wordBus)
                savedClass = wordBus
                wordBus = ""
                incrementList = []
                pos = 0

            if savedChar == "%":
                while pos < len(incrementList)-1:
                    wordBus = wordBus + incrementList[pos]
                    pos += 1
                        
                savedClass.addColor(wordBus)

                wordBus = ""
                incrementList = []
                pos = 0
                    
                        
            else:
                pass

    for a in loadedPalettes:
        a.printColors()
    input("[Enter] to close: ")    
# Class to represent a Palette
class Palette:
    def __init__(self, newName):
        self.name = newName  # Set the palette name
        self.colors = []  # Initialize an empty list to store colors

    def addColor(self, colorToAdd):
        # Add a new color to the palette
        self.colors.append(colorToAdd)

    def printColors(self):
        # Print the colors in the palette
        print(f"Palette '{self.name}' colors:")
        for color in self.colors:
            print(color)

    def printName(self):
        print(self.newName)

# Class to recreate Palette from the file

# First get the name of the palette, (first x characters until some symbol [used for formating] is detected)

# Then pull out the colors, seperated by a different character and use the addColor function to add then to the list

# LATER, link these colors to their image and paint counterparts

# Main execution #IMPORTANT NOTE: PALETTESTORAGE MUST END IN \N! OTHERWISE THE LAST INDEX WILL NOT BE DISPLAYED