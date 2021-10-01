sl=877803
auxt=(102854/30)
pos=(877803*0.04)
pe=(877803*0.04)
fss=(877803*4)
sal=input(f'mes es :')
dia=input(f'dias es :')
try:
    salarios=int(sal)
    dias=int(dia)
    sldia=(sl*salarios/30)
    sb=sldia*dias
    sdev=sb-pos-pe
    if sb>fss:
        lfss=(877803*0.01)
    else:
        lfss=0
    if salarios<=1:
        auxtransp=auxt*dias
        sn=sdev+auxtransp-lfss
        sn=round(sn,2)
    else:
        auxtransp=0
        sn=sdev+auxtransp-lfss
        sn=round(sn,2)
    print(f'\n el sueldo es : {sn}, \n la saludes es: {pos}, \n la pension es : {pe},'
          f'\n la bonificacion es : {lfss}, \n el subsidio es {auxtransp}')
except:
    print('incorrecto')