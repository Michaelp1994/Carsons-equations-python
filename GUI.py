from CarsonsEquations import *
import tkinter as tk;
import os

window = tk.Tk()
window.geometry("500x500")

frame = tk.Frame()

distance_label = tk.Label(text="Distance (m)", master=frame)
distance_entry = tk.Entry(width=50, master=frame)

xcoord_label = tk.Label(text="X coord (m)", master=frame)
xcoord_entry = tk.Entry(width=50, master=frame)

ycoord_label = tk.Label(text="Y coord (m)", master=frame)
ycoord_entry = tk.Entry(width=50, master=frame)

diam_label = tk.Label(text="Diameter (mm)", master=frame)
diam_entry = tk.Entry(width=50, master=frame)

rac_label = tk.Label(text="RAC (ohm/km)", master=frame)
rac_entry = tk.Entry(width=50, master=frame)

gmr_label = tk.Label(text="GMR (mm)", master=frame)
gmr_entry = tk.Entry(width=50, master=frame)

conductors = [];

def add_conductor(event):
    xcoord = float(xcoord_entry.get())
    ycoord = float(ycoord_entry.get())
    diam = float(diam_entry.get())/1000
    rac = float(rac_entry.get())/1000
    gmr = float(gmr_entry.get())/1000
    new_conductor = Conductor([xcoord, ycoord], diam, rac, gmr)
    conductors.append(new_conductor)
    xcoord_entry.delete(0, tk.END)
    ycoord_entry.delete(0, tk.END)
    diam_entry.delete(0, tk.END)
    rac_entry.delete(0, tk.END)
    gmr_entry.delete(0, tk.END)



def calculate(event):
    distance = float(distance_entry.get())
    [rMatrix, xMatrix, cMatrix] = CarsonsEquations(conductors)
    print("r Matrix: ohm/m");
    print(rMatrix);
    print("x Matrix: ohm/m");
    print(xMatrix);
    print("c Matrix: nF/m");
    print(cMatrix);
    Cmatrix = numpy.multiply(distance, cMatrix); # nF
    Rmatrix = numpy.multiply(distance, rMatrix); # ohms
    Xmatrix = numpy.multiply(1j*distance, xMatrix); # ohms

    # Calculate Y prim Matrix
    Zmatrix = numpy.add(Rmatrix, Xmatrix) # ohms 
    Ymatrix = numpy.linalg.inv(Zmatrix); # 1/ohms

    YcMatrix = numpy.multiply(1j*(omega/2)*10**-9, Cmatrix)
    firstMatrix = Ymatrix+YcMatrix;
    firstColumn = numpy.vstack((firstMatrix, -Ymatrix))
    secondColumn = numpy.vstack((-Ymatrix, firstMatrix))
    YprimMatrix = numpy.hstack((firstColumn, secondColumn))

    GprimMatrix = numpy.real(YprimMatrix);
    BprimMatrix = numpy.imag(YprimMatrix);
    print("G Prim Matrix:");
    print(GprimMatrix);
    print("B Prim Matrix:");
    print(BprimMatrix);
    f = open("lineCode.dss", "w")
    f.write(f"New linecode.example nphases={len(conductors)} BaseFreq=60\n")
    f.write(f"~rmatrix = " + createOpenDSSMatrix(rMatrix))
    f.write(f"\n~xmatrix = " + createOpenDSSMatrix(xMatrix))
    f.write(f"\n~cmatrix = " + createOpenDSSMatrix(cMatrix))
    f.close()
    os.startfile("lineCode.dss")
    window.destoy();

def createOpenDSSMatrix(m):
    output = "[";
    for row in m:
        for column in row:
            output += f"{column} "
        output += "|"
    output += "]";
    return output
    

addButton = tk.Button(
    text="Add Conductor",
    width=25,
    height=5,
    master=frame
)
addButton.bind("<Button-1>", add_conductor)
calculateButton = tk.Button(
    text="Calculate",
    width=25,
    height=5,
    master=frame
)
calculateButton.bind("<Button-1>", calculate)

distance_label.pack();
distance_entry.pack();
xcoord_label.pack();
xcoord_entry.pack();
ycoord_label.pack();
ycoord_entry.pack();
diam_label.pack();
diam_entry.pack();
rac_label.pack();
rac_entry.pack();
gmr_label.pack();
gmr_entry.pack();
addButton.pack();
calculateButton.pack();
frame.pack();



window.mainloop()