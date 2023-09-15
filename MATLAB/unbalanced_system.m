
radius_strand = 1.8*10^-2;
bundle_distance = 45*10^-2;
freq = 60;
resistivity = 100;

# given ACSR Linnet for Phase and 4/0 ACSR for Neutral

# Hen
diam_phase = 22.43*10^-3; # m
RAC_phase = 0.147*10^-3; # ohm/m
GMR_phase =  9.27*10^-3; # m
radius_phase = diam_phase / 2;
# Waxwing
diam_neutral = 15.47*10^-3; # m
RAC_neutral = 0.2178*10^3; # ohm/m
GMR_neutral = 6.00*10^-3; # m


# all in metres
a = [-5 20];
a_image = [-5 -20];
b = [0 20];
b_image = [0, -20];
c = [5 20];
c_image = [5, -20];
d = [-7.5 30];
d_image = [-7.5 -30];
e = [7.5 30];
e_image = [7.5 -30];

function distance = calcDistance(x, y)
  distance = sqrt((x(1)-y(1))^2+(x(2)-y(2))^2);
end

u0 = 1.2566370621219*10^-6;
e0 = 8.854187812813*10^-12;

sdistance_aa = calcDistance(a, a_image);
distance_ab = calcDistance(a, b);
sdistance_ab = calcDistance(a, b_image);
X_self_a = u0*freq*log(1/GMR_phase);

X_mutual_ab = u0*freq*log(1/distance_ab);

R_ground = u0*2*pi*freq/8;

X_ground = u0*freq*log(658.5*sqrt(resistivity / freq ));

Raa = RAC_phase + R_ground;
Xaa = X_self_a + X_ground;

Rab = R_ground;

Xab = X_mutual_ab + X_ground;

Paa = (17987.41615/10^6)*log(sdistance_aa/radius_phase); # km/nF

Pab = (17987.41615/10^6)*log(sdistance_ab/distance_ab); # km/nF

Cmatrix = [0.008 -0.002 -0.001 -0.001 -0.000; # nF/m
-0.002 0.008 -0.002 -0.001 -0.001;
-0.001 -0.002 0.008 -0.000 -0.001;
-0.001 -0.001 -0.000 0.007 -0.001;
-0.000 -0.001 -0.001 -0.001 0.007];

Cmatrix = [7.556 -1.509 -0.698 -0.931 -0.481 ;-1.509 7.794 -1.509 -0.650 -0.650 ;-0.698 -1.509 7.556 -0.481 -0.931 ;-0.931 -0.650 -0.481 6.658 -0.745 ;-0.481 -0.650 -0.931 -0.745 6.658]; # nF/km

Pmatrix = inverse(Cmatrix);

Rmatrix = [2.06217626e-01 5.92176264e-02 5.92176264e-02 5.92176264e-02 5.92176264e-02;
 5.92176264e-02 2.06217626e-01 5.92176264e-02 5.92176264e-02 5.92176264e-02;
 5.92176264e-02 5.92176264e-02 2.06217626e-01 5.92176264e-02 5.92176264e-02;
 5.92176264e-02 5.92176264e-02 5.92176264e-02 2.17800059e+05 5.92176264e-02;
 5.92176264e-02 5.92176264e-02 5.92176264e-02 5.92176264e-02 2.17800059e+05];

Xmatrix =[0.86152644 0.38724071 0.33497864 0.33269315 0.29950441;
 0.38724071 0.86152644 0.38724071 0.31815402 0.31815402;
 0.33497864 0.38724071 0.86152644 0.29950441 0.33269315;
 0.33269315 0.31815402 0.29950441 0.89432647 0.30440729;
 0.29950441 0.31815402 0.33269315 0.30440729 0.89432647];
Cmatrix =1000*[ 0.00755081 -0.00150792 -0.00069718 -0.00093009 -0.00048036;
 -0.00150792  0.00778841 -0.00150792 -0.00064952 -0.00064952;
 -0.00069718 -0.00150792  0.00755081 -0.00048036 -0.00093009;
 -0.00093009 -0.00064952 -0.00048036  0.00665324 -0.0007448 ;
 -0.00048036 -0.00064952 -0.00093009 -0.0007448   0.00665324]

  Gmatrix = inverse(Rmatrix)
 Zmatrix = Rmatrix+j*(Xmatrix-Cmatrix)
 Ymatrix = inverse(Zmatrix)
abcd = y2abcd(Ymatrix);

