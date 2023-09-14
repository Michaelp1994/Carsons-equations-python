

distance =  66967
number_of_towers = 40
number_of_spans = number_of_towers+1
span_length = distance/(number_of_spans)
first_bus = "SE_TOY"
last_bus = "SE_ESO"
phases = 5;
geometry = "LineGeometry"
rho = "100"
tower_resistance = "15"
ohew = True;

default_line_config = f" phases={phases} length={span_length} units=m geometry={geometry} Xg=0 Rg=0 rho={rho} \n"
default_reactor_config = f" phases=1 R={tower_resistance} X=0\n"

f = open("TransmissionLine.dss", "w");

f.write(f"New line.{first_bus}_T1 bus1={first_bus} bus2=T1" + default_line_config + "\n")

for i in range(1, number_of_towers):
        f.write(f"New line.T{i}_T{i+1} bus1=T{i} bus2=T{i+1}" + default_line_config)
        f.write(f"New Reactor.T{i}_RT bus1=T{i}.4 bus2=T{i}.0" + default_reactor_config)
        f.write(f"New Reactor.T{i}_OHEW bus1=T{i}.4 phases=1 bus2=T{i}.4 r=0.01 X=0 \n\n")

f.write(f"New line.T{number_of_towers}_{last_bus} bus1=T{number_of_towers} bus2={last_bus}" + default_line_config)
f.write(f"New Reactor.T{number_of_towers}_RT bus1=T{number_of_towers}.4 bus2=T{number_of_towers}.0" + default_reactor_config)
f.write(f"New Reactor.T{number_of_towers}_OHEW bus1=T{number_of_towers}.4 phases=1 bus2=T{number_of_towers}.4 r=0.01 X=0 \n\n")