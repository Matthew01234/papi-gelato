print ('Welkom bij Papi Gelato')


prijshoorentje = 1,25
prijsbakje = 0,75
prijsbolletjes = 1,25


def bestellen():
    x = True
    while x == True:
        aantalBolletjes = int(str(input('Hoeveel bolletjes wil je? ')))
        if aantalBolletjes in [1,2,3]:
            y = 0
            while y < aantalBolletjes:
                y += 1
                smaak =  input ('Welke smaak wilt u voor bolletje nummer '+ str(y) + '? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
                if smaak.upper() in "ACMV": print () 
                else: 
                    print ('Sorry, dat snap ik niet...')  
                    y -= 1   
            hoorentjeofbakje = input('Wilt u deze '+str(aantalBolletjes) +' bolletje(s) in A) een hoorntje of B) een bakje?” ').upper()
            if hoorentjeofbakje == ('A'):
                hoorentjeofbakje = 'hoorntje'
                print ('Hier is uw '+ (hoorentjeofbakje)+' met '+ str(aantalBolletjes) +' bolletje(s)')
            elif hoorentjeofbakje == ('B'):
                hoorentjeofbakje = ('bakje')
                print ('Hier is uw '+ (hoorentjeofbakje)+' met '+ str(aantalBolletjes) +' bolletje(s)')
                    
                
                    
            else: print ('Sorry, dat snap ik niet...') 

        elif aantalBolletjes in [4,5,6,7,8]:
            y = 0
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
            if opnieuwbestellen == ('J'):
                bestellen()
                o = False
            elif opnieuwbestellen == ('N'):
                print ('Bedankt en tot ziens!')
                x = False
                o = False
            else: print ('Sorry, dat snap ik niet') 
        return aantalBolletjes, hoorentjeofbakje




def bonnentje(hoorentjeofbakje,aantalBolletjes ):
    print ('--------------["Papi Gelato"]--------------')
    print ('Bedankt voor je bestelling hierbij uw bon!')
    if aantalBolletjes > ('0'):
        print ('bolletjes:' + aantalBolletjes * prijsbolletjes)
    if hoorentjeofbakje == ('A'):
        print ('Hoorentje: '+ prijshoorentje +'')
    if hoorentjeofbakje == ('B'):
        print ('Bakje: '+ prijsbakje +'')





bestellen() 
bonnentje()



