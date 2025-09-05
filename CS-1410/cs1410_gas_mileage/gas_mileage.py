#Austin Davis class meets at 1 ish


import sys

def milesPerGallon(miles,gallons):
    if gallons == 0:
        return 0.0
    else:
        return miles/gallons

def createNotebook():
    return []

def recordTrip(notebook,date,miles,gallons):
    notebook.append({
        "date": date,
        'miles': miles,
        "gallons": gallons
        })

def listTrips(notebook):
    newlist = []
    if notebook == []:
        return []
    else:
        for trip in notebook:
            message = "On "+str(trip["date"])+': '+str(trip["miles"])+' miles traveled using '+str(trip["gallons"])+' gallons. Gas mileage: '+str(milesPerGallon(trip["miles"],trip["gallons"]))+' MPG'
            newlist.append(message)
        return newlist

def calculateMPG(notebook):
    if notebook:
        miles = 0
        gallons = 0
        for trip in notebook:
            miles += trip['miles']
            gallons += trip['gallons']
        if gallons > 0:
            return miles/gallons
    return 0.0

def formatMenu():
    return ["What Would You like to do?", '[r] Record Gas Consumption', "[l] List Mileage History", '[c] Calculate Gas Mileage', "[q] Quit"]

def formatMenuPrompt():
    return 'Enter an option: '

def getUserString(prompt):
    string = ''
    while string == "":
        string = input(prompt).strip()
    return string


def getUserFloat(prompt):
    keepLooping = True
    while keepLooping:
        ans = input(prompt)
        try:
            num = float(ans)
            if num > 0:
                keepLooping = False;
        except:
            print("you can't convert that string to a float")
    return num

def getDate():
    string = getUserString("What's the date today?")
    return string

def getMiles():
    floats = getUserFloat("How many miles did you drive?")
    return floats

def getGallons():
    floats = getUserFloat("How many gallons did you use?")
    return floats

def recordTripAction(notebook):
    recordTrip(notebook,getDate(),getMiles(),getGallons())
    print("Your Trip was saved")

def listTripsAction(notebook):
    trip = listTrips(notebook)
    if notebook == []:
        print('No trips have been recorded.')
    else:
        for t in trip:
            print(t)

def calculateMPGAction(notebook):
    trip = calculateMPG(notebook)
    if notebook == []:
        print('No trips have been recorded.')
    else:
        print('Average MPG: ' + str(trip))

def quitAction(notebook):
    print("You have quit the program. Have a nice day.")
    sys.exit(0)

def applyAction(notebook,string):
    if string == "r":
        recordTripAction(notebook)
    elif string == "l":
        listTripsAction(notebook)
    elif string == "c":
        calculateMPGAction(notebook)
    elif string == "q":
        quitAction(notebook)
    else:
        print('That option is invalid')

def main():
    notebook = createNotebook()
    while True:
        menu = formatMenu()
        for thing in menu:
            print(thing)
        applyAction(notebook,getUserString(formatMenuPrompt()))



if __name__ == '__main__':
    main()
