radius_strand = 1.8*10^-2;
bundle_distance = 45*10^-2;
freq = 60;
a = [-8 10];
a2 = [10 -10];
b = [-12 0];
b2 = [12, 0];
c = [8 10];
c2 = [-10 -10];


function distance = calcDistance(x, y)
  distance = sqrt((x(1)-y(1))^2+(x(2)-y(2))^2);
end

u0 = 1.2566370621219*10^-6;
e0 = 8.854187812813*10^-12;

##u0 = 4*pi*10^-7;


distance_a_a2 = calcDistance(a, a2);
distance_a_b = calcDistance(a, b);
distance_a_b2 = calcDistance(a, b2);
distance_a_c = calcDistance(a, c);
distance_a_c2 = calcDistance(a, c2);
distance_a2_b = calcDistance(a2, b);
distance_a2_b2 = calcDistance(a2, b2);
distance_a2_c = calcDistance(a2, c);
distance_a2_c2 = calcDistance(a2, c2);
distance_b_b2 = calcDistance(b, b2);
distance_b_c = calcDistance(b,c);
distance_b_c2 = calcDistance(b, c2);
distance_b2_c = calcDistance(b2, c);
distance_b2_c2 = calcDistance(b2, c2);
distance_c_c2 = calcDistance(c, c2);

gmr_stranded = radius_strand*2.1767; # for 7 strands, 2 layer

gmr_bundle = nthroot(gmr_stranded*sqrt(2)*bundle_distance^3, 4); # for a bundle of 4.

gmr_phase_a = nthroot(gmr_bundle*distance_a_a2,2); # double circuit
gmr_phase_b = nthroot(gmr_bundle*distance_b_b2,2); # double circuit
gmr_phase_c = nthroot(gmr_bundle*distance_c_c2,2); # double circuit

gmr_circuit = nthroot(gmr_phase_a*gmr_phase_b*gmr_phase_c,3)

gmd_ab = nthroot(distance_a_b*distance_a_b2*distance_a2_b*distance_a2_b2,4);
gmd_bc = nthroot(distance_b_c*distance_b_c2*distance_b2_c*distance_b2_c2, 4);
gmd_ac = nthroot(distance_a_c*distance_a_c2*distance_a2_c*distance_a2_c2, 4);

##gmd_ab = 15.4718;
##gmd_bc = 15.4718;

gmd = nthroot(gmd_ab*gmd_bc*gmd_ac, 3);

L = (u0/(2*pi))*log(gmd/gmr_circuit);

X = u0*freq*(gmd/gmr_circuit)

gmr_stranded_c =radius_strand*2.2558 # for 7 strands, 2 layers

gmr_bundle_c = nthroot(gmr_stranded_c*sqrt(2)*bundle_distance^3, 4)
gmr_c_phase_a = nthroot(gmr_bundle_c*distance_a_a2,2); # double circuit
gmr_c_phase_b = nthroot(gmr_bundle_c*distance_b_b2,2); # double circuit
gmr_c_phase_c = nthroot(gmr_bundle_c*distance_c_c2,2); # double circuit

gmr_c_circuit = nthroot(gmr_c_phase_a*gmr_c_phase_b*gmr_c_phase_c,3);

capacitance = (2*pi*e0)/(log(gmd/gmr_c_circuit))

Ya = (4*(pi^2)*e0*freq)/(log(gmd/gmr_c_circuit))
