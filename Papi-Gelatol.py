print ('Welkom bij Papi Gelato')


prijshoorentje = 1.25
prijsbakje = 0.75
prijsbolletjes = 1.25
prijsSlagroom = 0,5
prijsSprinkels = 0,3
prijsCaramel = ''
aantalBolletjes = 0
totaalAantalBolletjes = 0
hoorentjeofbakje = ''
totaalAantalHoorentjes = 0
totaalAantalBakjes = 0
totaal = 0



def bonnentje():
    global aantalBolletjes, hoorentjeofbakje, totaalAantalBolletjes, totaalAantalHoorentjes, totaalAantalBakjes
    totaal = (totaalAantalBolletjes * prijsbolletjes) + (totaalAantalHoorentjes * prijshoorentje) + (totaalAantalBakjes * prijsbakje)
    print ('--------------["Papi Gelato"]--------------')
    print ('Bedankt voor je bestelling hierbij uw bon!')
    if aantalBolletjes > 0:
        print (f'bolletjes: {totaalAantalBolletjes} x  {prijsbolletjes} = € ' + str(totaalAantalBolletjes * prijsbolletjes))
    if totaalAantalHoorentjes > 0:
        print (f'Hoorentje: {totaalAantalHoorentjes} x {prijshoorentje} = € '+ str(totaalAantalHoorentjes * prijshoorentje) +'')
    if totaalAantalBakjes > 0:
        print (f'Bakje: {totaalAantalBakjes} x {prijsbakje} = € '+ str(totaalAantalBakjes * prijsbakje) +'')
    print (f'Totaal: € {totaal}')
    print ('--------------["Papi Gelato"]--------------')

def bestellen():
    global aantalBolletjes, hoorentjeofbakje, totaalAantalBolletjes, totaalAantalHoorentjes, totaalAantalBakjes
    x = True
    while x == True:
        aantalBolletjes = int(str(input('Hoeveel bolletjes wil je? ')))
        if aantalBolletjes in [1,2,3]:
            y = 0
            while y < aantalBolletjes:
                y += 1
                topping = input ('Welke topping wil je ')
                smaak =  input ('Welke smaak wilt u voor bolletje nummer '+ str(y) + '? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
                if smaak.upper() in "ACMV": print () 
                else: 
                    print ('Sorry, dat snap ik niet...')  
                    y -= 1   
            hoorentjeofbakje = input('Wilt u deze '+str(aantalBolletjes) +' bolletje(s) in A) een hoorntje of B) een bakje?” ').upper()
            if hoorentjeofbakje == ('A'):
                hoorentjeofbakje = 'A'
                totaalAantalHoorentjes += 1
                print ('Hier is uw hoorentje met '+ str(aantalBolletjes) +' bolletje(s)')
            elif hoorentjeofbakje == ('B'):
                hoorentjeofbakje = ('B')
                totaalAantalBakjes += 1
                print ('Hier is uw bakje met ' + str(aantalBolletjes) +' bolletje(s)')
                    
                
                    
            else: print ('Sorry, dat snap ik niet...') 

        elif aantalBolletjes in [4,5,6,7,8]:
            y = 0
            hoorentjeofbakje = "B"
            while y < aantalBolletjes:
                y += 1
                smaak =  input ('Welke smaak wilt u voor bolletje nummer '+ str(y) + '? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
                if smaak.upper() in "ACMV": print () 
                else: 
                    print ('Sorry, dat snap ik niet...')  
                    y -= 1  
        elif aantalBolletjes > int((8)):
            print('Sorry zulke grote bakken hebben we niet')
            bestellen()
        else: print ('Sorry dat snap ik niet...') 
        o = True
        while o == True:
            opnieuwbestellen = input ('Wil je op nieuw bestellen Ja (J) of Nee (N)').upper()
            totaalAantalBolletjes += aantalBolletjes
            if opnieuwbestellen == ('J'):              
                bestellen()
                o = False
            elif opnieuwbestellen == ('N'):
                print ('Bedankt en tot ziens!')
                x = False
                o = False
                bonnentje()
            else: print ('Sorry, dat snap ik niet') 
        return aantalBolletjes, hoorentjeofbakje










bestellen() 




