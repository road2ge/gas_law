########Gas Laws (Honors Chemistry)########
constant = raw_input("Is your constant T, V, or P? ").lower()
temp_unit = "k"
if not constant == 't':
    temp_unit = raw_input("Are your temps given in C, F or K? ")
if not temp_unit.lower() in "cfk":
    temp_unit = raw_input("You typed something wrongly. What unit? ")

print "Input 'u' for unknown.\nSince we have two data sets, put your one unknown in the second data set."
print "Input 'c' for constant."
args1 = raw_input("Temperature,Volume,Pressure where volume is in L and pressure is in atm> ").split(',')
args2 = raw_input("Second set of data. Just like before> ").split(',')

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

# Process temperature into Kelvin
if not constant == 't':    
    if not temp_unit.lower() == "k":
        if temp_unit.lower() == "f":
            args1[0] = convert_f_k(args1[0])
            args2[0] = convert_f_k(args2[0])
        elif temp_unit.lower() == "c":
            args1[0] = convert_c_k(args1[0])
            args2[0] = convert_c_k(args2[0])




# Gas law is PV = nRT. n is constant.
def boyles(a1,b1,a2):
    # Temp is constant. Find b2.
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