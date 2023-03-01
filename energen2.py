 
#Energibalans: In = UT
#Qin + matarvatten + luft = avgaser + ånga + aska
#NOTE: Alla flöden kg/s

#Vi vet att avgaserna än 90kg men vi vet inte Qin och vi måste beräkan det genom
#att beräkna bränslet vi stoppar in gånger entaplin den har.

#F = 0.02 Vatten
#A = 0.04 Aska
#Hvap = 2.5MJ/kg
#Hcal = 34 Approximera för Carbon
#Hi = (1-F)(1-A)*Hcal - Hvap((1-5F)*8.94*H+F) = 31MJ/kg

#För att beräkna mängen bränsle behöver vi beräkna hur mycket luft vi behöver som är en del av
#de avgaser vi får ut. Vi vet att luften är 1.2 gånger så mycket som bränslet och att vi får ut

#Skapa Vatten
#0.02 Syre är kompenserat *0.5 för 1:2 förhållande till Vatten. 
#16/1.008 är för att kompensera för att det är 16g/mol O och 1.008g/mol H
#H2 + 0.5O2 = H2O
#H = 0.04 *bränsle
#O = 0.02 *bränsle * 16/1.008 = 0.317*bränsle 

#Skapande av CO2
#C + O2 = CO2
#O = 0.85*bränsle*2*16/12* = 2.27 * bränsle

#Vi väljer att räkna i kilogram istället för volym% för att det är enklare
#N = 0.77 kg / kg luft
#O = 0.23 kg / kg luft
#För varje kg syre behöver vi 3.35 kg kväve
#Tot syre: 2.27+0.317=2.587*bränsle
#Tot kväve = 2.587*bränsle*3.35
#Tot luft = 1.2*(2.587*bränsle*3.35 + 0.317*bränsle) #Kompenserat för överskott


#Massbalans över bränsle/luft
#(2.587*3.35*bränsle + 2.587*bränsle)*1.2 +bränsle -(90 +0.02*bränsle)
#bränsle = 6.21
#Luft = (2.587*3.35*bränsle + 2.587*bränsle)*1.2 = 83.9

#Qin = 31*6.21
# Qin       +  h16*m + hluft*mluft - (havgas*mavgas + h1*m+   
#192.5*10^6+990*10^3*vatten+262*10^3*83.9-(1112*90*10^3+3390*10^3*ånga+2*10^6)=0

#Vatten/ångflöde = 46.3



h1 =3390 #Vapour 500C 90Bar 
h2 = 2234 #Vapour/Liquid mix 0.05bar 33C
h3 = 1112 #Gas 90kg/s 830C 12bar
h4 = 361 #1bar 314grader
h5 = 138 #hl vatten 33C
h6 = 138 #hl vatten 33C
h7 = 2574 #1 bar 100C
h8 = 417  #1bar hl
h9 = 377 #88.9 grader
h10 = 2863 #8bar Hv
h11 = 721 #8 bar hl
h12 = 
h13 = 419 #100 grader hl
h14 = 675 #160grader
h15 = 675# samma bara högre tryck
h16 = 990 #230C hl
h17 = 
hluft = 262 #262grader tryck=12bar
"""







