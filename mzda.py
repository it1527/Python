print ("***************************************************************************************************************")
print ("********************************   VYPOCET CISTE MZDY SE VSEMI PRIPLATKY  *************************************")
print ("***************************************************************************************************************")
print ("***************************************************************************************************************")
print ("***************************************************************************************************************")
print ("Pozn. Vypocet je pro zjisteni ciste mzdy supportu se vsemi priplatky (nocni, vikendy, svatky) *****************")
print ("***** Jedna smena se pocita jako 11 hodin odpracovane doby (1 hodina se nezapocitava - jde o dve **************")
print ("***** pulhodinove, neplacene pauzy. ***************************************************************************")
print ("***** Priplatky z fixniho platu se pocitaji tak, ze se vezme hruba mesicni mzda napr. 25000,- CZK *************")
print ("***** a vypocitame si jaky je hruby prumer CZK na hodinu. Tzn. 25000 : 176 = 142,-. Takze prumer **************")
print ("***** na hodinu je 142,- CZK a z tohoto prumeru se vypocte dane procento priplatku (napr. priplatek za nocni **")
print ("***** je 20%) tak 142 * 0,20 = 28,4,- CZK. Tzn. ze za jednu nocni smenu bude hruby priplatek ******************")
print ("***** 28,4 * 11 = 312,- CZK. A upravime hruby zaklad o tuto castku 25000 + 312 = 25312,- CZK HRUBEHO **********")
print ("***** Pak se uz jen vypocita cista mzda z tohoto upraveneho, noveho, hrubeho prijmu. **************************")
print ("Pozn. Pokud je vice priplatku za jednu smenu, treba nocni a jeste vikend pak se tyto priplatky SCITAJI! *******")
print ("***************************************************************************************************************")
print ("***************************************************************************************************************")
print ("***************************************************************************************************************")
print ("***************************************************************************************************************")

hrubeho = int(input("Kolik mas hrubeho?  "))
zaloha = hrubeho * 0.15
slev = zaloha - 2320
soc = hrubeho * 0.065
zdrav = hrubeho * 0.045
cisteho = hrubeho - slev - soc - zdrav
print ("Cisteho mas:", cisteho) 
print ()

priplateknoc = float(input("Jaky je priplatek (%) za nocni? (zadej desetinne cislo - napr. 10% zadej jako 0.1)  "))
priplatekvik = float(input("Jaky je priplatek (%) za vikend? (zadej desetinne cislo - napr. 25% zadej jako 0.25)  "))

print ("Za svatek je vzdy 100%")
print ()

pocetdnu = int(input("kolik jsi odpracoval dvanactek?  "))
vikend = int(input("Kolik dnu o vikendu?  "))
pocethod = pocetdnu * 11
vikhod = vikend * 11
nocni = int(input("Kolik jsi mel nocnich?  "))
denni = pocetdnu - nocni
nochod = nocni * 11
svatek = int(input("kolik smen o svatku?  "))
svathod = svatek * 11
prumhod = hrubeho / pocethod
prumsmen = hrubeho / pocetdnu
nocpri = prumhod * priplateknoc * nochod
svatpri = prumhod * 1 * svathod
vikpri = prumhod * priplatekvik * vikhod
hrubeho = hrubeho + nocpri + vikpri + svatpri
zaloha = hrubeho * 0.15
slev = zaloha - 2320
soc = hrubeho * 0.065
zdrav = hrubeho * 0.045
cisteho = hrubeho - slev - soc - zdrav

print ("pocet odpracovanych hodin: ", pocethod)
print () 
print ("Nocni ", nocni, "   Denni ", denni)
print ()
print ("Prumer na HODINU je: ", prumhod)
print ()
print ("Prumer na SMENU je: ", prumsmen)
print ()
print ("Priplatek za nocni mas: ", nocpri)
print ()
print ("Priplatek za vikend mas: ", vikpri)
print ()
print ("Priplatek za svatky mas: ", svatpri)
print ()
print ()
print ("CELKOVA HRUBA MZDA PO VSECH PRIPLATCICH JE: ", hrubeho, "   CELKOVA CISTA MZDA JE: ", cisteho)
print ()

