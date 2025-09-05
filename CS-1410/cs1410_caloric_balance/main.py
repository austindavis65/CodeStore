from caloric_balance import CaloricBalance
import sys

def formatMenu():
    return ['What would you like to do?', "[f] Record Food Consumption", '[a] Record Physical Activity', "[q] Quit"]

def formatMenuPrompt():
    return 'Enter an option: '

def formatActivityMenu():
    return ['Choose an activity to record', '[j] Jump rope', '[r] Running', '[s] Sitting', '[w] Walking']

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

def createCaloricBalance():
    gender = getUserString('What is your gender: ')
    age = getUserFloat('What is your age: ')
    height = getUserFloat('What is your height in inches: ')
    weight = getUserFloat('What is your weight in pounds: ')
    cb = CaloricBalance(gender,age,height,weight)
    return cb

def recordActivityAction(caloricbalance):
    for i in formatActivityMenu():
        print(i)
    string = getUserString(formatMenuPrompt())
    if string == 'j':
        num = getUserFloat('How long did you do this? ')
        CaloricBalance.recordActivity(caloricbalance,0.074,num)
        print('Your new caloric balance is '+str(CaloricBalance.getBalance(caloricbalance)))
    elif string == 'r':
        num = getUserFloat('How long did you do this? ')
        CaloricBalance.recordActivity(caloricbalance,0.115,num)
        print('Your new caloric balance is '+str(CaloricBalance.getBalance(caloricbalance)))
    elif string == 's':
        num = getUserFloat('How long did you do this? ')
        CaloricBalance.recordActivity(caloricbalance,0.009,num)
        print('Your new caloric balance is '+str(CaloricBalance.getBalance(caloricbalance)))
    elif string == 'w':
        num = getUserFloat('How long did you do this? ')
        CaloricBalance.recordActivity(caloricbalance,0.036,num)
        print('Your new caloric balance is '+str(CaloricBalance.getBalance(caloricbalance)))
    else:
        print('Invalid input')

def eatFoodAction(caloricbalance):
    calories = getUserFloat('How many calories did you consume? ')
    CaloricBalance.eatFood(caloricbalance,calories)
    print('Your new caloric balance is '+str(CaloricBalance.getBalance(caloricbalance)))

def quitAction(caloricbalance):
    print('You have left. Goodbye :)')
    sys.exit(0)

def applyAction(caloricbalance,choice):
    if choice == 'f':
        eatFoodAction(caloricbalance)
    elif choice == 'a':
        recordActivityAction(caloricbalance)
    elif choice == 'q':
        quitAction(caloricbalance)
    else:
        print('Invalid input')
        
def main():
    cb = createCaloricBalance()
    while True:
        for i in formatMenu():
            print(i)
        applyAction(cb,getUserString(formatMenuPrompt()))
        
if __name__ == '__main__':
    main()
    