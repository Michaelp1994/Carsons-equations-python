import numpy;
u0 = 1.2566370621219*10**-6; # N/A^2
e0 = 8.854187812813*10**-12; # F/m


class Conductor:
  def __init__(self, coord, diam, rac, gmr):
    self.coord = coord;
    self.diameter = diam;
    self.rac = rac;
    self.gmr = gmr;


def calcDistance(p1, p2):
  return numpy.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2));

def calcImageDistance(p1, p2):
  return numpy.sqrt(((p2[0]-p1[0])**2)+((-p2[1]-p1[1])**2));

def matrixDifference(m1, m2):
  diff = numpy.subtract(m1, m2);
  ratio = numpy.divide(diff, m2);
  abs = numpy.absolute(ratio);
  percentage = numpy.multiply(100, abs);
  rounded = numpy.matrix.round(percentage, 2);
  return rounded;


def CarsonsEquations_DSS(conductors, resistivity, freq):
  resistance_ground = u0*2*numpy.pi*freq/8; # ohm/m
  reactance_ground = u0*freq*numpy.log(658.5*numpy.sqrt(resistivity / freq )); # ohm/m
  num_conductors = len(conductors);
  rMatrix = numpy.zeros((num_conductors,num_conductors)); # ohm/m
  xMatrix = numpy.zeros((num_conductors,num_conductors)); # ohm/m
  pMatrix = numpy.zeros((num_conductors,num_conductors)); # m/nF

  for i, first_cond in enumerate(conductors):
    for j, second_cond in enumerate(conductors):
      image_distance = calcImageDistance(first_cond.coord, second_cond.coord); # m
      if (i==j):
        self_reactance = u0*freq*numpy.log(1/first_cond.gmr); # ohm/m
        xMatrix[i][i] = (self_reactance + reactance_ground); # ohm/m
        rMatrix[i][i] =  (first_cond.rac+resistance_ground); # ohm/m
        radius = first_cond.diameter/2; # m
        # pMatrix[i][i] =  (17987.41615)*numpy.log(image_distance/radius)*10**-3; # m/nF
        pMatrix[i][i] =  (1/(2*numpy.pi*e0))*numpy.log(image_distance/radius)*10**-9 # m/nF
      else: 
          cond_distance= calcDistance(first_cond.coord, second_cond.coord); # m
          mutual_reactance = u0*freq*numpy.log(1/cond_distance) # ohm/m
          rMatrix[i][j] = resistance_ground; # ohm/m
          xMatrix[i][j] = (mutual_reactance+reactance_ground); # ohm/m
          # pMatrix[i][j] = (17987.41615)*numpy.log(image_distance/cond_distance)*10**-3 # m/nF
          pMatrix[i][j] = (1/(2*numpy.pi*e0))*numpy.log(image_distance/cond_distance)*10**-9 # m/nF
  cMatrix = numpy.linalg.inv(pMatrix) # nF/m
  return [rMatrix, xMatrix, cMatrix]


## do not touch above this line.



def CarsonsEquations_NETS(conductors, resistivity, freq):
  resistance_ground = u0*2*numpy.pi*freq/8; # ohm/m
  reactance_ground = u0*freq*numpy.log(658.5*numpy.sqrt(resistivity / freq )); # ohm/m
  R_earth = resistance_ground+(reactance_ground*1j)
  num_conductors = len(conductors);
  rMatrix = numpy.zeros((num_conductors,num_conductors)); # ohm/m
  xMatrix = numpy.zeros((num_conductors,num_conductors)); # ohm/m
  pMatrix = numpy.zeros((num_conductors,num_conductors)); # m/nF
  zMatrix = numpy.zeros((num_conductors,num_conductors), dtype=numpy.complex_); # ohm/m

  for i, first_cond in enumerate(conductors):
    for j, second_cond in enumerate(conductors):
      image_distance = calcImageDistance(first_cond.coord, second_cond.coord); # m
      if (i==j):
        radius = first_cond.diameter/2; # m
        zMatrix[i][i] =  R_earth + first_cond.rac
        zMatrix[i][i] += (1j*4*numpy.pi*freq*10**-4)*numpy.log(2*image_distance/first_cond.diameter)
        pMatrix[i][i] =  (1/(2*numpy.pi*e0))*numpy.log(image_distance/radius)
      else: 
          cond_distance= calcDistance(first_cond.coord, second_cond.coord); # m
          zMatrix[i][j] = R_earth+(1j*4*numpy.pi*freq*10**-4)*numpy.log(image_distance/cond_distance)
          pMatrix[i][j] = (1/(2*numpy.pi*e0))*numpy.log(image_distance/cond_distance)

  rMatrix = numpy.real(zMatrix)
  xMatrix = numpy.imag(zMatrix)
  cMatrix = numpy.linalg.inv(pMatrix)*10**9 # nF/m
  return [rMatrix, xMatrix, cMatrix]
