from CarsonsEquations import *

########### Calculate Line Parameters ################
freq = 60; # Hz
resistivity = 100; # ohm*m
omega = 2*numpy.pi*freq; # rad/s

# Hen
diam_phase = 22.43*10**-3; # m
RAC_phase = 0.147; # ohm/m
GMR_phase =  9.27*10**-3; # m

# Waxwing
diam_neutral = 15.47*10**-3; # m
RAC_neutral = 0.2178; # ohm/m
GMR_neutral = 6.00*10**-3; # m

distance = 1000; # m
# num_conductors = 5

conductors_DSS = [
  Conductor([-5, 20], 22.43*10**-3, 0.147*10**-3, 9.27*10**-3),
  Conductor([0, 20], 22.43*10**-3, 0.147*10**-3, 9.27*10**-3),
  Conductor([5, 20], 22.43*10**-3, 0.147*10**-3, 9.27*10**-3),
  Conductor([-7.5, 30], 15.47*10**-3, 0.2178*10**-3, 6.00*10**-3),
  Conductor([7.5, 30], 15.47*10**-3, 0.2178*10**-3, 6.00*10**-3),
]

conductors_Nets = [
  Conductor([-5, 20], 22.43*10**-3, 0.147*10**-3, 9.27*10**-3),
  Conductor([0, 20], 22.43*10**-3, 0.147*10**-3, 9.27*10**-3),
  Conductor([5, 20], 22.43*10**-3, 0.147*10**-3, 9.27*10**-3),
  Conductor([-7.5, 30], 15.47*10**-3, 0.2178*10**-3, 6.00*10**-3),
  Conductor([7.5, 30], 15.47*10**-3, 0.2178*10**-3, 6.00*10**-3),
]

[rMatrix_DSS, xMatrix_DSS, cMatrix_DSS] = CarsonsEquations_DSS(conductors=conductors_DSS, resistivity=resistivity, freq=freq)
[rMatrix_NETS, xMatrix_NETS, cMatrix_NETS] = CarsonsEquations_NETS(conductors=conductors_Nets, resistivity=resistivity, freq=freq)

print("rMatrix (openDSS): ohm/m");
print(rMatrix_DSS);
print("rMatrix (NETS): ohm/m");
print(rMatrix_NETS);

print("xMatrix (openDSS): ohm/m");
print(xMatrix_DSS);
print("xMatrix (NETS): ohm/m");
print(xMatrix_NETS);

print("cMatrix (openDSS): nF/m");
print(cMatrix_DSS);
print("cMatrix (NETS): nF/m");
print(cMatrix_NETS);


Cmatrix = numpy.multiply(distance, cMatrix_DSS); # nF
Rmatrix = numpy.multiply(distance, rMatrix_DSS); # ohms
Xmatrix = numpy.multiply(1j*distance, xMatrix_DSS); # ohms


# # Calculate Y prim Matrix
Zmatrix = numpy.add(Rmatrix, Xmatrix) # ohms 
Ymatrix = numpy.linalg.inv(Zmatrix); # 1/ohms

YcMatrix = numpy.multiply(1j*(omega/2)*10**-9, Cmatrix)
firstMatrix = Ymatrix+YcMatrix;
firstColumn = numpy.vstack((firstMatrix, -Ymatrix))
secondColumn = numpy.vstack((-Ymatrix, firstMatrix))
YprimMatrix = numpy.hstack((firstColumn, secondColumn))

GprimMatrix = numpy.real(YprimMatrix);
BprimMatrix = numpy.imag(YprimMatrix);

# print("Rmatrix: ohm");
# print(Rmatrix);
# print("Xmatrix: ohm");
# print(Xmatrix);
# print("Cmatrix: nF");
# print(Cmatrix);
# print("Zmatrix: (ohm)");
# print(Zmatrix);
# print("Ymatrix: (1/ohm)");
# print(Ymatrix);
# print("G Prim Matrix:");
# print(GprimMatrix);
# print("B Prim Matrix:");
# print(BprimMatrix);

# COMPARISONS ##


rMatrix_opendss = [[0.000206218, 0.000059218, 0.000059218, 0.000059218, 0.000059218],
[0.000059218, 0.000206218, 0.000059218, 0.000059218, 0.000059218],
[0.000059218, 0.000059218, 0.000206218, 0.000059218, 0.000059218],
[0.000059218, 0.000059218, 0.000059218, 0.000277018, 0.000059218],
[0.000059218, 0.000059218, 0.000059218, 0.000059218, 0.000277018]]
xMatrix_opendss= [[0.000861526, 0.000387241, 0.000334979, 0.000332693, 0.000299504],
[0.000387241, 0.000861526, 0.000387241, 0.000318154, 0.000318154],
[0.000334979, 0.000387241, 0.000861526, 0.000299504, 0.000332693],
[0.000332693, 0.000318154, 0.000299504, 0.000894326, 0.000304407],
[0.000299504, 0.000318154, 0.000332693, 0.000304407, 0.000894326]]

cMatrix_opendss=[[7.556, -1.509, -0.698, -0.931, -0.481],
[-1.509, 7.794, -1.509, -0.650, -0.650],
[-0.698, -1.509, 7.556, -0.481, -0.931],
[-0.931, -0.650, -0.481, 6.658, -0.745],
[-0.481, -0.650, -0.931, -0.745, 6.658]];
cMatrix_opendss = numpy.divide(cMatrix_opendss, 1000)

GprimMatrix_opendss = [
[ 0.4365469929, -0.1472609851, -0.05995437487, -0.1083482761, -0.05153326429, -0.4365469929,  0.1472609851, 0.05995437487,  0.1083482761, 0.05153326429],
[ -0.1472609851,  0.4768205051, -0.1472609851, -0.06777849761, -0.06777849761,  0.1472609851, -0.4768205051,  0.1472609851, 0.06777849761, 0.06777849761 ],
[ -0.05995437487, -0.1472609851,  0.4365469929, -0.05153326429, -0.1083482761, 0.05995437487,  0.1472609851, -0.4365469929, 0.05153326429,  0.1083482761 ],
[ -0.1083482761, -0.06777849761, -0.05153326429,  0.4567770132, -0.09829324725,  0.1083482761, 0.06777849761, 0.05153326429, -0.4567770132, 0.09829324725 ],
[ -0.05153326429, -0.06777849761, -0.1083482761, -0.09829324725,  0.4567770132, 0.05153326429, 0.06777849761,  0.1083482761, 0.09829324725, -0.4567770132 ],
[ -0.4365469929,  0.1472609851, 0.05995437487,  0.1083482761, 0.05153326429,  0.4365469929, -0.1472609851, -0.05995437487, -0.1083482761, -0.05153326429 ],
[ 0.1472609851, -0.4768205051,  0.1472609851, 0.06777849761, 0.06777849761, -0.1472609851,  0.4768205051, -0.1472609851, -0.06777849761, -0.06777849761 ],
[ 0.05995437487,  0.1472609851, -0.4365469929, 0.05153326429,  0.1083482761, -0.05995437487, -0.1472609851,  0.4365469929, -0.05153326429, -0.1083482761 ],
[ 0.1083482761, 0.06777849761, 0.05153326429, -0.4567770132, 0.09829324725, -0.1083482761, -0.06777849761, -0.05153326429,  0.4567770132, -0.09829324725 ],
[ 0.05153326429, 0.06777849761,  0.1083482761, 0.09829324725, -0.4567770132, -0.05153326429, -0.06777849761, -0.1083482761, -0.09829324725,  0.4567770132 ]]

BprimMatrix_opendss = [
[ -1.514862704,  0.3858347934,  0.2506269622,  0.2600523577,  0.1817056428,   1.514864128, -0.3858350779, -0.2506270937, -0.2600525331, -0.1817057334],
[ 0.3858347934,  -1.573462642,  0.3858347934,  0.2050540553,  0.2050540553, -0.3858350779,   1.573464112, -0.3858350779, -0.2050541778, -0.2050541778],
[ 0.2506269622,  0.3858347934,  -1.514862704,  0.1817056428,  0.2600523577, -0.2506270937, -0.3858350779,   1.514864128, -0.1817057334, -0.2600525331],
[ 0.2600523577,  0.2050540553,  0.1817056428,  -1.294759994,  0.1998600362, -0.2600525331, -0.2050541778, -0.1817057334,   1.294761249, -0.1998601767],
[ 0.1817056428,  0.2050540553,  0.2600523577,  0.1998600362,  -1.294759994, -0.1817057334, -0.2050541778, -0.2600525331, -0.1998601767,   1.294761249],
[  1.514864128, -0.3858350779, -0.2506270937, -0.2600525331, -0.1817057334,  -1.514862704,  0.3858347934,  0.2506269622,  0.2600523577,  0.1817056428],
[-0.3858350779,   1.573464112, -0.3858350779, -0.2050541778, -0.2050541778,  0.3858347934,  -1.573462642,  0.3858347934,  0.2050540553,  0.2050540553],
[-0.2506270937, -0.3858350779,   1.514864128, -0.1817057334, -0.2600525331,  0.2506269622,  0.3858347934,  -1.514862704,  0.1817056428,  0.2600523577],
[-0.2600525331, -0.2050541778, -0.1817057334,   1.294761249, -0.1998601767,  0.2600523577,  0.2050540553,  0.1817056428,  -1.294759994,  0.1998600362],
[-0.1817057334, -0.2050541778, -0.2600525331, -0.1998601767,   1.294761249,  0.1817056428,  0.2050540553,  0.2600523577,  0.1998600362,  -1.294759994]
]


print("Difference between rMatrix: ")
print(matrixDifference(rMatrix_DSS, rMatrix_opendss))

print("Difference between xMatrix: ")
print(matrixDifference(xMatrix_DSS, xMatrix_opendss))

print("Difference between cMatrix: ")
print(matrixDifference(cMatrix_DSS, cMatrix_opendss))

print("Difference between G: ")
print(matrixDifference(GprimMatrix, GprimMatrix_opendss))
print("Difference between B: ")
print(matrixDifference(BprimMatrix, BprimMatrix_opendss))
