########Gas Laws (Honors Chemistry)########
constant = raw_input("Is your constant T, V, or P? ").lower()
temp_unit = raw_input("Are your temps given in C, F or K? ")
if not temp_unit.lower() in "cfk":
    temp_unit = raw_input("You typed something wrongly. What unit? ")

print "Input 'u' for unknown.\nSince we have two data sets, put your one unknown in the second data set."
print "Input 'c' for constant."
args1 = raw_input("Temperature,Volume,Pressure where volume is in L and pressure is in atm ").split(',')
args2 = raw_input("Second set of data. Just like before. ").split(',')

def which_law(arglist):
    index = 0
    for i in arglist:
        if i == 'c':
            break
        index += 1
    string = "bgc"
    return string[index]

def convert_c_k(temperature):
    '''Convert Celsius to Kelvin'''
    return temperature + 273.15
def convert_f_k(temperature):
    '''Convert Farenheit to Kelvin'''
    return (temperature * (5/9) + 32) + 273.15

# Process temperature into Kelvin
if not constant == 't':    
    if not temp_unit.lower() == "k":
        if temp_unit.lower() == "f":
            temp = convert_f_k(temp)
            args1[0] = convert_f_k(args1[0])
            args2[0] = convert_f_k(args2[0])
        elif temp_unit.lower() == "c":
            temp = convert_c_k(temp)
            args1[0] = convert_c_k(args1[0])
            args2[0] = convert_c_k(args2[0])




# Gas law is PV = nRT. n is constant.
def boyles(a1,b1,a2):
    # Temp is constant. Find b2.
    # v,p
    prod = a1 * b1
    b2 = prod / a2
    print b2

def gay_lussacs(a1,b1,a2):
    # Volume is constant. Find b2.
    # t,p
    pass

def charles(a1,b1,a2):
    # Pressure is constant. Find b2.
    # t,v
    pass
if which_law(args1) == 'b':
    if args2[1] == 'u':
        boyles(float(args1[1]), float(args1[2]),float(args2[2]))
    elif args2[2] == 'u':
        boyles(float(args1[1]), float(args1[2]),float(args2[1]))
# elif which_law(args1) == 'c':