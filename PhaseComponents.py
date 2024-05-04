import numpy;

########### Calculate Phase/Sequence Components ################

baseKv = 138

baseVolts = baseKv*10**3;

phases = 3

x1r1 = 16;
Isc1 = 23260;

Isc3 = 27430;
x0r0 = 13.49;

Z1_radius = ((baseVolts)/(Isc3*numpy.sqrt(3)));
print("Z1_radius: ")
print(Z1_radius)
Z1_theta = numpy.arctan(x1r1);
print("Z1 theta: ")
print(Z1_theta)
R1 = Z1_radius*numpy.cos(Z1_theta);
print("R1: ")
print(R1)
X1 = Z1_radius*numpy.sin(Z1_theta);
print("X1: ")
print(X1)


a = (1+(x0r0**2));
print("a: ")
print(a)
b = 4*(R1+(X1*x0r0));
print("b: ")
print(b)
c = 4*((R1**2)+(X1**2))-((3*baseVolts)/(numpy.sqrt(3)*Isc1))**2;
print("c: ")
print(c)


R0 = (-b + numpy.sqrt((b**2)-(4*a*c)))/(2*a);
print("R0: ")
print(R0)
X0 = x0r0 * R0;
print("X0: ") 
print(X0)


Z0 = complex(R0, X0);
Z1 = complex(R1, X1);
Z2 = Z1;

Zmatrix = numpy.diag([Z0, Z1, Z2])
print("Z Sequence Matrix: ")
print(Zmatrix);
alpha = numpy.exp(1j*2*numpy.pi/3)
print(alpha)
alphaMatrix = numpy.array([[1, 1, 1], 
                           [1, alpha**2, alpha], 
                           [1, alpha, alpha**2]])

alphaMatrix2 = numpy.array([
  [1, 1, 1],
  [1, alpha, alpha**2],
  [1, alpha**2, alpha]
]);

matrix1 = numpy.matmul(alphaMatrix, Zmatrix)
matrix2 = numpy.matmul(matrix1, alphaMatrix2)

ZphaseMatrix = (1/3)*matrix2
print("Z Phase Matrix:")
print(ZphaseMatrix)
