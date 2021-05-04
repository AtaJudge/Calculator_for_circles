chc=True
while chc==True:
    print("Calculator for circles \t\n\bDeveloped by AtaJudge")
    print("")
    pi=input("Pi: ")
    if "," in pi:
        pi=pi.replace(",",".")
        con_pi=float(pi)
    elif "." in pi:
        con_pi=float(pi)
    else:
        con_pi=int(pi)
    print("")
    rad=input("Radius: ")
    if "," in rad:
        rad=rad.replace(",",".")
        con_rad=float(rad)
    elif "." in rad:
        con_rad=float(rad)
    else:
        con_rad=int(rad)
    print("")
    print("circumference: " , con_pi*con_rad*2)
    print("area: " , con_pi*con_rad**2)
    print("")
    print("For calculate more; type 'rcalc', for exit type 'ext'. ")
    x=input()
    if x=="rcalc":
        chc=chc
    elif x=="ext":
        chc=False
    else:
        print("WTF???")
        chc=False
    