#Νικόλαος Φουρτούνης
#icsd13195

__author__ = "NFourtounis"
__date__ = "$Mar 30, 2018 7:42:24 PM$" 

from random import randint

def isInt(character):#Function που ελέγχει αν ένας χαρακτήρας είναι int
    try:#Αν παίζει το try χωρίς να πετάξει error η int() πάει να πει ότι ο χαρακτήρας είναι int
        int(character)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    t = ((0, 2.5),#Φτιάχνω το tuple μου με τις αποδόσεις
    (0, 1, 5),
    (0, 0, 2.5, 2.5),
    (0,0,1,4,100),
    (0,0,0,2,20,450),
    (0,0,0,1,7,50,1600),
    (0, 0, 0, 1, 3, 20, 100, 5000),
    (0, 0, 0, 0, 2, 10, 50, 1000, 15000),
    (0, 0, 0, 0, 1, 5, 25, 200, 4000, 40000),
    (2, 0, 0, 0, 0, 2, 20, 80, 500, 10000, 100000),
    (2, 0, 0, 0, 0, 1, 10, 50, 250, 1500, 15000, 500000),
    (4, 0, 0, 0, 0, 0, 5,25, 150, 1000, 2500, 25000, 1000000))
    while True:#Ζητάω απο τον χρήστη πόσα νούμερα που θα παίξει
        userInput=input('Πόσα νούμερα θα παίξεις; (Από 1 έως 12)')
        if isInt(userInput):#Ελέγχω αν είναι int
            if (13>int(userInput) and int(userInput)>0):#Ελέγχω αν είναι μέσα στα όρια
                numbers=int(userInput)
                break
            else:
                print("Δώσε νούμερο από 1 έως 12")
        else:
            print("Λάθος χαρακτήρας")

    numbersList=[]

    for i in range(0,numbers,1):#Για τον αριθμό των νουμέρων που θα παίξει
        while True:#Ζητάω απο τον χρήστη τα νούμερα που θα παίξει
            userInput=input('Δώσε %do νούμερο:' % (i+1))
            if isInt(userInput):#Ελέγχω αν είναι int
                if (80>int(userInput) and int(userInput)>0):#Ελέγχω αν είναι μέσα στα όρια
                    numbersList.append(int(userInput))
                    break
                else:
                    print("Δώσε νούμερο από 1 έως 80")
            else:
                print("Λάθος χαρακτήρας")
    while True:#Ζητάω απο τον χρήστη το ποσό που θα παίξει
        userInput=input('Τι ποσό θες να παίξεις (1, 2, 5, 10 ευρώ)')
        if isInt(userInput):#Ελέγχω αν είναι int 
            if (1==int(userInput) or 2==int(userInput) or 5==int(userInput) or 10==int(userInput)):#Ελέγχω αν είναι μέσα στα όρια
                bet=int(userInput)
                break
            else:
                print("Μπορείς να παίξεις μόνο 1, 2, 5 ή 10 ευρώ!")
        else:
            print("Λάθος χαρακτήρας") 
    drawList=[]
    for i in range(1,20,1):#Κρατάω λίστα με 20 τυχαία νούμερα (κλήρωση)
        drawList.append(randint(1,80))
    print("Οι αριθμοί που κληρώθηκαν: ")
    print(drawList)
    numbersPredicted=0
    for i in drawList:#Ελέγχω πόσα πέτυχε ο χρήστης
        for y in numbersList:
            if(i==y):
                numbersPredicted+= 1
    print("Πέτυχες %d νούμερα!" % numbersPredicted)#Του λέω πόσα πέτυχε
    multiplier=t[numbers-1][numbersPredicted]#Υπολογίζω τον πολλαπλασιαστή των αποδόσεων
    valueWon=bet*multiplier#το πολλαπλασιάζω με το ποσό που έπαιξε ο χρήστης
    print ("Κέρδισες %d" % valueWon)#Εκτυπώνω το ποσό που κέρδισε