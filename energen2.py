 

#Skapa Vatten
#H = 0.04 *bränsle
#O = 0.02 *bränsle * 16/1.008 = 0.317*bränsle

#Lägg till skapande av CO2 till Vatten
#N = 0.77% kg / luft
#O = 0.23% kg / luft
#N = = O*3.35 = 0.317*3.35*bränsle

#Luft: N + O = 0.317*3.35*bränsle + 0.317*bränsle 
#Luftöverskott = 1.2 * luft

#x = bränsle
#(0.317*3.35*x + 0.317*x)*1.2 +x -(90 +0.04*x+0.36*x +0.02*x) = 0
#IN = UT
#IN = 6.39(ALLT BRÄNSLE) + 86.3(ALL LUFT) + Matarvatten
#UT = 90(Avgaser) + Ånga

#x = 6.39
#luftöverskott = 1.2*(0.317*3.35*x + 0.317*x) = 86.3


# Qin       +  h16*m + hluft*mluft - (havgas*mavgas + h1*m+   
#198.5*10^6+990*10^3*x+262*10^3*86.3-(1112*90*10^3+3390*10^3*x+2*10^6)=0
x = 49.6 #vatten


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








