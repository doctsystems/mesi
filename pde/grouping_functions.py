import numpy as np

def getIndexFromLookupTables(isc, sc_zip_out, lookup_vbp, lookup_zip):
    k = -1
    # el isc esta en lookup_vbp
    try:
        i = lookup_vbp.index(isc)
    except:
        print('UNEXPECTED ERROR')
    else:
        # con este indice veo en la looku del zip a que nuevo sector (label) la asocio
        zsc = lookup_zip[i]
        # ahora lo busco en la lista zip ordenada de salida y con valores unicos
        try:
            k = sc_zip_out.index(zsc)
        except:
            print('UNEXPECTED ERROR')
    return k
        
def zipMatrices(mip_global, vbp_global, vbp_locales, sc_vbp_in, lookup_vbp, lookup_zip):
    # mip_global, vbp_global y vbp_locales ya estan ordenados de acuerdo a sc_vbp_in
    # sc_vbp_in y lookup_vbp deben tener los mismos elementos, pero la lookup_vbp 
    # es mas larga
    assert(len(sc_vbp_in) == len(set(lookup_vbp)))
    
    insec,nreg = vbp_locales.shape

    st_zip = set(lookup_zip)
    sc_zip_out = sorted(list(st_zip)) # esta es una version de los sectores sin los duplicados
    mxgrp = len(sc_zip_out)

    # reservo memoria para la salida
    out_mip_global = np.zeros((mxgrp,mxgrp), dtype=np.float)
    out_vbp_global = np.zeros((mxgrp,1), dtype=np.float)
    out_vbp_locales = np.zeros((mxgrp,nreg), dtype=np.float)
    
    # generar nueva mip
    for i, isc in enumerate(sc_vbp_in):
        k0 = getIndexFromLookupTables(isc, sc_zip_out, lookup_vbp, lookup_zip)
        for j, jsc in enumerate(sc_vbp_in):
            k1 = getIndexFromLookupTables(jsc, sc_zip_out, lookup_vbp, lookup_zip)
            out_mip_global[k0,k1] += mip_global[i,j]

    # generar nueva tabla de vbp globales
    for i, ivbp in enumerate(sc_vbp_in):
        k0 = getIndexFromLookupTables(ivbp, sc_zip_out, lookup_vbp, lookup_zip)
        out_vbp_global[k0] += vbp_global[i]
    # generar nueva tabla vbp locales
    for j in range(nreg):
        for i, ivbp in enumerate(sc_vbp_in):
            k0 = getIndexFromLookupTables(ivbp, sc_zip_out, lookup_vbp, lookup_zip)
            out_vbp_locales[k0,j] += vbp_locales[i,j]
           
    return sc_zip_out, out_mip_global, out_vbp_global, out_vbp_locales

def agruparMatrices(mip_global, vbp_global, vbp_locales, sc_vbp_in, lookup_mip, lookup_vbp):
    nsec,_nsec = mip_global.shape
    # debe haber el mismo numero de sectores en la mip que en la lookup
    assert(nsec == len(lookup_mip))
    # verificar la vbp
    insec,nreg = vbp_locales.shape
    st_vbp = set(lookup_vbp)
    sc_vbp_out = sorted(list(st_vbp)) # esta es una version de los sectores sin los duplicados
    mxgrp = len(sc_vbp_out)
    # debe tener el mismo numero de sectores
    assert(mxgrp == insec)
    # los sectores de salida deben ser iguales
    assert(set(sc_vbp_out) == set(sc_vbp_in))
    
    # reservo memoria para la salida
    out_mip_global = np.zeros((mxgrp,mxgrp), dtype=np.float)
    out_vbp_global = np.zeros((mxgrp,1), dtype=np.float)
    out_vbp_locales = np.zeros((mxgrp,nreg), dtype=np.float)
       
    # generar nueva mip
    for i in range(len(lookup_mip)):
        ivbp = lookup_vbp[i]
        try:
            k0 = sc_vbp_out.index(ivbp)
        except:
            print('UNEXPECTED ERROR')
        else:            
            for j in range(len(lookup_mip)):
                jvbp = lookup_vbp[j]
                try:
                    k1 = sc_vbp_out.index(jvbp)
                except:
                    print('UNEXPECTED ERROR')
                else:                            
                    out_mip_global[k0,k1] += mip_global[i,j]
    # generar nueva tabla de vbp globales
    for i, ivbp in enumerate(sc_vbp_in):
        try:
            k0 = sc_vbp_out.index(ivbp)
        except:
            print('UNEXPECTED ERROR')
        else:                            
            out_vbp_global[k0] += vbp_global[i]
    # generar nueva tabla vbp locales
    for j in range(nreg):
        for i, ivbp in enumerate(sc_vbp_in):
            try:
                k0 = sc_vbp_out.index(ivbp)
            except:
                print('UNEXPECTED ERROR')
            else:                            
                out_vbp_locales[k0,j] += vbp_locales[i,j]
           
    return sc_vbp_out, out_mip_global, out_vbp_global, out_vbp_locales
