########Gas Laws (Honors Chemistry)########
from Tkinter import *
root = Tk()
canvas = Canvas(root, height=900, width=5000, bg='white')
# canvas.grid(column=1, row=0, rowspan=4, sticky=W)
Label(root, text='If conditions change, fill left and right. Otherwise, fill just left. Put u and c for unknown and constant. Only put unknowns on the right.').grid(column=3)
Label(root, text='Temperature (K):').grid(row=1)
Label(root, text='Volume (L):').grid(row=2)
Label(root, text='Pressure (atm):').grid(row=3)
Label(root, text='Moles:').grid(row=4)

# Label(root, text='If conditions DO NOT change. Put u for unknown.').grid(columnspan=5,column=5,row=0)
Label(root, text='Temperature (K):').grid(row=1,column=5)
Label(root, text='Volume (L):').grid(row=2,column=5)
Label(root, text='Pressure (atm):').grid(row=3,column=5)
Label(root, text='Moles:').grid(row=4,column=5)

eT1 = Entry(root)
eT1.grid(row=1,column=1)
eV1 = Entry(root)
eV1.grid(row=2,column=1)
eP1 = Entry(root)
eP1.grid(row=3,column=1)
eM1 = Entry(root)
eM1.grid(row=4,column=1)
eT2 = Entry(root)
eT2.grid(row=1,column=6)
eV2 = Entry(root)
eV2.grid(row=2,column=6)
eP2 = Entry(root)
eP2.grid(row=3,column=6)
eM2 = Entry(root)
eM2.grid(row=4,column=6)

def which_law(const):
    if const == "t":
        return "b"
    elif const == 'v':
        return "g"
    elif const == 'p':
        return "c"

def convert_c_k(temperature):
    '''Convert Celsius to Kelvin'''
    try: 
        return float(temperature) + 273.15
    except:
        return temperature
def convert_f_k(temperature):
    '''Convert Farenheit to Kelvin'''
    try: 
        return (float(temperature) * (5/9) + 32) + 273.15
    except:
        return temperature

# Gas law is PV = nRT. n is constant.
def boyles(a1,b1,a2,v_p=True):
    # temperature is constant. Find b2.
    # a1 * b1 = a2 * b2
    prod = a1 * b1
    b2 = prod / a2
    # TODO: PROCESS A RET STRING
    if v_p:
        return str(b2) + "Liters"
    else:
        return str(b2) + "atm"
def gay_lussacs(a1,b1,a2,t_p=False):
    # Volume is constant. Find b2.
    # p/t = p/t
    if t_p:
        b2 = b1 * a2 / a1
        return str(b2) + " Kelvin"
    else:
        b2 = a1 * a2 / b1
        return str(b2) + " atm"
def charles(a1,b1,a2,t_v=False):
    # Pressure is constant. Find b2.
    # v/t = v2/t2
    # a1 / b1 = a2 / b2
    if t_v:
        b2 = b1 * a2 / a1
        return str(b2) + " Kelvin"
    else:
        b2 = a1 * a2 / b1
        return str(b2) + " Liters"
def gas_law(p,v,n,t):
    r = .082
    if p == 'u':
        # Solve for pressure. PV = nRT, so P = nRT/V
        return n * r * t / v
    elif v == 'u':
        # Solve for volume. PV = nRT, so V = nRT/P
        return n * r * t / p
    elif n == 'u':
        # Solve for moles. PV = nRT, so n = PV/RT
        return p * v / (r*t)
        # print str(mm * moles) + " grams."
    elif t == 'u':
        # Solve for temperature. PV = nRT, so T = PV/nR
        return p * v / (n*r)

'''
if not cond_change:
    constant = raw_input("Is your constant T, V, or P>").lower()
    temperature_unit = "k"
    if not constant == 't':
        temperature_unit = raw_input("Are your temperatures given in C, F or K>")
    if not temperature_unit.lower() in "cfk":
        temperature_unit = raw_input("You typed something wrongly. What unit>")

    print "Input 'u' for unknown.\nSince we have two data sets, put your one unknown in the second data set."
    print "Input 'c' for constant."
    args1 = input("Temperature,Volume,Pressure where volume is in L and pressure is in atm>").split(',')
    args2 = input("Second set of data. Just like before>").split(',')

# Process temperature into Kelvin
if not constant == 't':    
    if not temperature_unit.lower() == "k":
        if temperature_unit.lower() == "f":
            args1[0] = convert_f_k(args1[0])
            args2[0] = convert_f_k(args2[0])
        elif temperature_unit.lower() == "c":
            args1[0] = convert_c_k(args1[0])
            args2[0] = convert_c_k(args2[0])

else:
    # Gas law constant!!!!
    r = .082
    unknown = raw_input("Is your unknown P, V, Mass (M), or T>").lower()
    while unknown not in 'pvmt':
        unknown = raw_input("I don't understand.\nIs your unknown P, V, Mass (M), or T>").lower()
    if not unknown == 'p':
        pressure = input("Pressure in atm>")
    if not unknown == 'v':
        volume = input("Volume in liters>")
    if not unknown == 'm':
        mass_unit = raw_input("If you have moles, input y. If you have grams, input n>").lower()
        if mass_unit == 'y':
            mass_unit = True
        elif mass_unit == 'n':
            mass_unit = False
            mass = 'How many grams do you have then>'
        else:
            while not mass_unit in 'ynu':
                mass_unit = raw_input("I don't understand.\nIf you have moles, input y. If you have grams, input n>").lower()
        if not mass_unit:
            mm = input("What is the molar mass of this gas>")
            moles = mass / mm
    if not unknown == 't':
        temperature_unit = raw_input("Temperature unit: C, F or K>").lower()
        if not temperature_unit in 'cfk':
            while temperature_unit not in 'cfk':
                temperature_unit = raw_input("I don't understand.\nTemperature unit: C, F, or K>").lower()
        temperature = input("Now actual number for temperature>")
        if not temperature_unit == 'k':
            if temperature_unit == 'f':
                temperature = convert_f_k(temperature)
            else:
                temperature = convert_c_k(temperature)
    if unknown == 'p':
        # Solve for pressure. PV = nRT, so P = nRT/V
        print str(mass * r * temperature / volume) + " atm."
    elif unknown == 'v':
        # Solve for volume. PV = nRT, so V = nRT/P
        print str(mass * r * temperature / pressure) + " Liters."
    elif unknown == 'm':
        # Solve for moles. PV = nRT, so n = PV/RT
        print str(pressure * volume / (r*temperature)) + " moles, or alternatively"
        print str(mm * moles) + " grams."
    elif unknown == 't':
        # Solve for temperature. PV = nRT, so T = PV/nR
        print str(pressure * volume / (mass*r)) + " Celsius."

        
# Given T,V,P,T2,V2,P2
law = which_law(constant)
if law == 'b':
    if args2[1] == 'u':
        boyles(float(args1[1]), float(args1[2]),float(args2[2]))
    elif args2[2] == 'u':
        boyles(float(args1[1]), float(args1[2]),float(args2[1]))
if law == 'g':
    if args2[0] =='u':
        # Unknown is T2, pass P2
        gay_lussacs(float(args1[2]), float(args1[0]), float(args2[2]), True)
    elif args2[2] == 'u':
        # Unknown is P2, pass T2
        gay_lussacs(float(args1[2]), float(args1[0]), float(args2[0]))
if law == 'c':
    if args2[0] == 'u':
        # Unknown is T2, pass V2
        charles(float(args1[1]), float(args1[0]), float(args2[1]), True)
    elif args2[1] == 'u':
        # Unknown is V2, pass T2
        charles(float(args1[1]), float(args1[0]), float(args2[0]))'''
def solve2():
    temp = eT1.get()
    vol = eV1.get()
    pres = eP1.get()
    mass = eM1.get()
    try:
        temp = float(temp)
    except:
        pass
    try:
        vol = float(vol)
    except:
        pass
    try:
        pres = float(pres)
    except:
        pass
    try:
        mass = float(mass)
    except:
        pass

    if temp == 'u':
        unknown = 't'
    elif vol == 'u':
        unknown = 'v'
    elif pres == 'u':
        unknown = 'p'
    elif mass == 'u':
        unknown = 'm'
    solution = gas_law(pres,vol,mass,temp)
    solutionVar.set(solution)
def solve():
    t1 = eT1.get()
    v1 = eV1.get()
    p1 = eP1.get()
    t2 = eT2.get()
    v2 = eV2.get()
    p2 = eP2.get()
    try:
        t1 = float(t1)
    except:
        if t1 == 'c':
            law = 'b'
    try:
        v1 = float(v1)
    except:
        if v1 == 'c':
            law = 'g'
    try:
        p1 = float(p1)
    except:
        if p1 == 'c':
            law = 'c'
    try:
        t2 = float(t2)
    except:
        if t2 == 'c':
            law = 'b'
    try:
        v2 = float(v2)
    except:
        if v2 == 'c':
            law == 'g'
    try:
        p2 = float(p2)
    except:
        if p2 == 'c':
            law = 'c'
    args1 = [t1,v1,p1]
    args2 = [t2,v2,p2]

    if law == 'b':
        if args2[1] == 'u':
            solutionVar.set(boyles(float(args1[1]), float(args1[2]),float(args2[2])))
        elif args2[2] == 'u':
            solutionVar.set(boyles(float(args1[1]), float(args1[2]),float(args2[1]),False))
    if law == 'g':
        if args2[0] =='u':
            # Unknown is T2, pass P2
            solutionVar.set(gay_lussacs(float(args1[2]), float(args1[0]), float(args2[2]), True))
        elif args2[2] == 'u':
            # Unknown is P2, pass T2
            solutionVar.set(gay_lussacs(float(args1[2]), float(args1[0]), float(args2[0])))
    if law == 'c':
        if args2[0] == 'u':
            # Unknown is T2, pass V2
            solutionVar.set(charles(float(args1[1]), float(args1[0]), float(args2[1]), True))
        elif args2[1] == 'u':
            # Unknown is V2, pass T2
            solutionVar.set(charles(float(args1[1]), float(args1[0]), float(args2[0])))
def callSolver():
    if eT2.get() == '':
        solve2()
    else:
        solve()
def clear():
    
    eT1.delete(0,END)
    eT2.delete(0,END)
    eP1.delete(0,END)
    eP2.delete(0,END)
    eV1.delete(0,END)
    eV2.delete(0,END)
    eM1.delete(0,END)
    eM2.delete(0,END)
    solutionVar.set('Cleared!')
b2 = Button(root, text = 'Solve', command=callSolver)
b2.grid(row=5, column=3)
solutionVar = StringVar()
solution = Label(root,textvariable=solutionVar).grid(row=6,column=3)
bClear = Button(root, text='Clear', command = clear).grid(row=4,column=3)
root.mainloop()