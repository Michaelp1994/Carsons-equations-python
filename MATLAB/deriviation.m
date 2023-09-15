clear

function distance = calcDistance(p1, p2)
  distance = sqrt((p2(1)-p1(1))^2+(p2(2)-p1(2))^2);
end

freq=60;
length = 401;
## Phase
radius_phase=228.5*10^-3;
RAC_phase=0.0735;
GMRac_phase=65.0875564144*10^-3;



cond1 = [-7.5 18.9];
cond2 = [0 18.9];
cond3 = [7.5 18.9];
cond4 = [-5.2 36.51];
cond5 = [5.2 36.51];

u0 = 1.2566370621219*10^-6;
e0 = 8.854187812813*10^-12;
conds = [0 18.9; 7.5 18.9; 15 18.9; 2.3 36.51; 12.7 36.51];

x = calcDistance(cond1, cond2) * calcDistance(cond1, cond3) *calcDistance(cond1, cond4) *calcDistance(cond1, cond5)*calcDistance(cond2, cond1)*calcDistance(cond2, cond3)*calcDistance(cond2, cond4)*calcDistance(cond2, cond5)*calcDistance(cond3, cond1)*calcDistance(cond3, cond2)*calcDistance(cond3, cond4)*calcDistance(cond3, cond5)*calcDistance(cond4, cond1)*calcDistance(cond4, cond2)*calcDistance(cond4, cond3)*calcDistance(cond4, cond5)*calcDistance(cond5, cond1)*calcDistance(cond5, cond2)*calcDistance(cond5, cond3)*calcDistance(cond5, cond4);

GMD = nthroot(x, 20);
re_bundle = nthroot(0.457^2 * radius_phase, 3);
Xl_phase = j * freq *  u0 * log(GMD / GMRac_phase);

Gc_phase = 0;
Yc_phase = j * 2 * pi * freq * (( 2 * pi * e0) / log(GMD/re_bundle));

Z_phase = RAC_phase + Xl_phase
y_phase = Gc_phase + Yc_phase

Zc = sqrt(Z_phase/y_phase);
y = sqrt(Z_phase*y_phase);
A = cosh(y*length)
B = Zc*sinh(y*length)
C = (1/Zc)*sinh(y*length)
D = cosh(y*length)



##GMD = nthroot(distance(,5);
## Neutral
Diam_neutral=12.7;
Rac_neutral=2.33;
GMRac_neutral=4.6073483;



##New Linegeometry.LineGeometry nconds=5 nphases=3 units=m reduce=no
##~ cond=1 Wire=PHASE x=-7.5 h=18.9  // A
##~ cond=2 Wire=PHASE x=0 h=18.9  // B
##~ cond=3 Wire=PHASE x=7.5 h=18.9 // C
##~ cond=4 Wire=Neutral x=-5.2 h=36.51 // Neutral
##~ cond=5 Wire=Neutral x=5.2 h=36.51 // Neutral
