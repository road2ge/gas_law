########Gas Laws (Honors Chemistry)########

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
def boyles(a1,b1,a2):
    # temperature is constant. Find b2.
    # a1 * b1 = a2 * b2
    prod = a1 * b1
    b2 = prod / a2
    # TODO: PROCESS A RET STRING
    print b2
def gay_lussacs(a1,b1,a2,t_p=False):
    # Volume is constant. Find b2.
    # p/t = p/t
    if t_p:
        b2 = b1 * a2 / a1
        print str(b2) + " Kelvin is your new temperature"
    else:
        b2 = a1 * a2 / b1
        print str(b2) + " atm is your new pressure"
def charles(a1,b1,a2,t_v=False):
    # Pressure is constant. Find b2.
    # v/t = v2/t2
    # a1 / b1 = a2 / b2
    if t_v:
        b2 = b1 * a2 / a1
        print str(b2) + " Kelvin is your new temperature"
    else:
        b2 = a1 * a2 / b1
        print str(b2) + " liters is your new volume"

cond_change = raw_input("Do conditions change? y/n>")
if cond_change == 'y':
    cond_change = True
elif cond_change == 'n':
    cond_change = False
else:
    while not cond_change in 'yn':
        cond_change = raw_input("I don't understand.\nDo conditions change? y/n>")
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
    if not unknown == 'm'
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
        charles(float(args1[1]), float(args1[0]), float(args2[0]))