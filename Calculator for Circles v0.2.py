chc=True
def calc_area(con_pi, con_rad):
    print(con_pi*con_rad**2)
    print("")
def calc_enviroment(con_rad,con_pi):
    print(con_pi*con_rad*2)
    print("")
while chc==True:
    print("Calculator for circles \t\n\bDeveloped by AtaJudge")
    print("")
    choice = input("Area or Enviroment? ")
    if choice!="area" and choice!="enviroment":
        print("Undefined calculation request.")
        break
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
    if choice=="area":
        calc_area(con_pi,con_rad)
    elif choice=="enviroment":
        calc_enviroment(con_pi,con_rad)
    print("For calculate more type 'rcalc', for exit type 'ext'. ")
    x=input()
    if x=="rcalc":
        chc=chc
    elif x=="ext":
        chc=False
    