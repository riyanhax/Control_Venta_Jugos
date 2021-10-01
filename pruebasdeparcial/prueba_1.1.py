opt = input('[1] calcular, [2] salir')
if opt == '1':
    corte = input('digite cual corte : ')
    if corte == '1' or corte == '2':
        q = float(input('quices : '))
        t = float(input('trabajos : '))
        p = float(input('pacial es : '))
        nq = (q * 0.052)
        nt = (t * 0.052)
        np = (p*0.196)
        nfinalcorte=round((nq+nt+np),2)
    else:
        t=float(input('proyecto :'))
        p=float(input('nota parcial : '))
        nt=(t*0.2)
        np=(p*0.2)
        nfinalcorte=round((nt+np),2)
    print(f'la nota de : {corte} corte es de : {nfinalcorte}')
elif opt=='2':
    print('salio')
else:
    print('error')