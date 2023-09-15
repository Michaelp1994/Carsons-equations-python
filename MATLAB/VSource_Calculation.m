%Calculating VSource components (YPrim)
KVBase=0.1;
Mvasc3=0.3;
Mvasc1=0.3;
PU=1;
NFases=1;
Vmag=KVBase*PU*1000/2/sin((180/NFases)*pi/180);
%Por defecto
X1=6.6;
R1=1.65;
X2=X1;
R2=R1;
R0=1.9;
X0=5.7;
BaseMVA=0.15;
Zbase=(KVBase^2)/BaseMVA;
% internal calculations
X1R1=X1/R1;
X0R0=X0/R0;
X1=((KVBase^2)/Mvasc3)/sqrt(1+1/(X1R1^2));
R1=X1/X1R1;
X2=X1;
Isc3=Mvasc3*1000/(sqrt(3)*KVBase);
Isc1=Mvasc1*1000/(sqrt(3)*KVBase);
a=1+X0R0^2;
b=4*(R1+X1*X0R0);
c=(4*(R1^2+X1^2)-((3*KVBase*1000/sqrt(3))/Isc1)^2);
comando=strcat(num2str(a),'*x^2+',num2str(b),'*x',num2str(c));
R0=max(subs(solve(comando)));
X0=R0*X0R0;

Xs=(2*X1+X0)/3;     %Self inductance
Rs=(2*R1+R0)/3;     %Self resistance
Xm=(X0-X1)/3;       %mutual inductance
Rm=(R0-R1)/3;       %Mutual resistance

Zs=Rs+i*Xs;
Zm=Rm+i*Xm;
ZMat=[Zs Zm Zm;Zm Zs Zm;Zm Zm Zs];
YPrim=inv(ZMat)

%Calculates the injected currents (Contribution) of the VSource

ang_fase=30;
VMag=KVBase*1000;
Vs=[VMag*(cos((ang_fase)*pi/180)+i*sin((ang_fase)*pi/180));VMag*(cos((ang_fase-120)*pi/180)+i*sin((ang_fase-120)*pi/180));VMag*(cos((ang_fase+120)*pi/180)+i*sin((ang_fase+120)*pi/180))];
Vs=Vs/sqrt(3);
Is=YPrim*Vs



Ymatrix = [0.986365048	-0.33982947	-0.070927402	-0.214448072	-0.176796371	-0.986365048;
-0.33982947	1.136504083	-0.33982947	-0.179486387	-0.179486387	0.33982947;
-0.070927402	-0.33982947	0.986365048	-0.176796371	-0.214448072	0.070927402;
-0.214448072	-0.179486387	-0.176796371	0.964821043	-0.042634799	0.214448072;
-0.176796371	-0.179486387	-0.214448072	-0.042634799	0.964821043	0.176796371;
-0.986365048	0.33982947	0.070927402	0.214448072	0.176796371	0.986365048;
0.33982947	-1.136504083	0.33982947	0.179486387	0.179486387	-0.33982947;
0.070927402	0.33982947	-0.986365048	0.176796371	0.214448072	-0.070927402;
0.214448072	0.179486387	0.176796371	-0.964821043	0.042634799	-0.214448072;
0.176796371	0.179486387	0.214448072	0.042634799	-0.964821043	-0.176796371]

