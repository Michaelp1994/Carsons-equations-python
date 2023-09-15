## OPENDSS

Gmatrix_DSS = [0.133333333	-0.133333333; -0.133333333	0.133333333];

Bmatrix_DSS = [0	0; 0	0];

Ymatrix_DSS = complex(Gmatrix_DSS, Bmatrix_DSS)

##Zmatrix_DSS = inv(Ymatrix_DSS)

Vmatrix = [100; 0];

Imatrix = Ymatrix_DSS*Vmatrix



## XGSLAB

Zmatrix_XGS = [-7.5+0i	-7.5+0i
-7.5+0i	-7.5+0i];

Vmatrix_calc = Zmatrix_XGS*Imatrix

##Ymatrix_XGS = inv(Zmatrix_XGS);
