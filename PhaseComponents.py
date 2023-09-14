import numpy;

########### Calculate Phase/Sequence Components ################

baseKv = 138
phases = 3

x1r1 = 6.05;
Isc1 = 4700;

Isc3 = 3850;
x0r0 = 5.26;

Z1_radius = ((baseKv*10**3)/(Isc3*numpy.sqrt(3)));
Z1_theta = numpy.arctan(x1r1);

R1 = Z1_radius*numpy.cos(Z1_theta);
X1 = Z1_radius*numpy.sin(Z1_theta);

a = (1+(x0r0**2));
b = 4*(R1+(X1*x0r0));
c = 4*((R1**2)+(X1**2))-((3*230000)/(numpy.sqrt(3)*Isc1))**2;

R0 = (-b + numpy.sqrt((b**2)-(4*a*c)))/(2*a);
X0 = x0r0 * R0;

Z0 = complex(R0, X0);
Z1 = complex(R1, X1);
Z2 = Z1;

Zmatrix = numpy.diag([Z0, Z1, Z2])
print("Z Sequence Matrix: ")
print(Zmatrix);
alpha = numpy.exp(1j*2*numpy.pi/3)

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
