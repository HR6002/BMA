def meters(rod):
   return rod*5.0292

def feet(meters):
    return meters/0.3048

def miles(meters):
    return meters/1609.34

def furlongs(rods):
    return rods/40

def walk(miles):
    mile=((miles)/3.1)*60
    return mile

def userinput(user):
 userr=float(user)
 return userr

def printing():
 print(f""" meters:{meters(userinput(userrinput))} 
 feet: {feet(meters(userinput(userrinput)))}
 miles: {miles(meters(userinput(userrinput)))}
 furlongs: {furlongs(userinput(userrinput))}
 walking time in minutes : {walk(miles(meters(userinput(userrinput))))}
 """)

userrinput=input("enter number of rods: ")
printing()
