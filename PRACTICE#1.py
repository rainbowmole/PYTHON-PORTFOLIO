print('ELAPSED TIME', "\n")

#input
ET = int(input('Enter elapsed time in seconds: '))

#process
H = (ET//60)//60
M = (ET//60)%60
S = (ET%60)%60

#Output
print("\t", H, "Hours", M, "Minutes", S, "Seconds", "\n" )

#CHECKING
print("CHECKING", "\n")
print("Enter Elapsed Time in:", "\n")

#INPUT
H2 = int(input("Hours: "))
M2 = int(input("Minutes: "))
S2 = int(input("Seconds: "))

#PROCESS
ET2 = (H2*3600)+(M2*60)+S2

print("Total elapsed time in seconds: ", ET2, "\n")

if ET == ET2:
    print("VALID PROGRAM")
else:
    print("ERROR")