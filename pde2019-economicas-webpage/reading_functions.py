# test lectura de los archivos de datos

import pandas as pd
import numpy as np

# en el archivo de grp puede haber 3 listas
# 1ra columna son los sectores de la mip. no puede haber repetidos. debe coincidir con la columna del mip.
# 2da columna son los sectores de la vbp. puede haber repetidos. puede estar agrupando los mip.
# 3ra columna agrupacion adicional de los vbp. es opcional.

def lecturaMIP(csvfile_mip, sc_mip):

    try:
        df_mip = pd.read_csv(csvfile_mip)
    except:
        try:
            df_mip = pd.read_excel(csvfile_mip)
        except:
            raise 'IOM file should be CSV or EXCEL type'
            
    df_data = df_mip.iloc[:,1:]
    sc_cols = df_data.columns.tolist()
    sc_rows = df_mip.iloc[:,0].tolist()
    # para que sea cuadrada tienen que tener el mismo largo
    assert(len(sc_cols) == len(sc_rows))
    # no hay repetidos
    assert(len(sc_cols) == len(set(sc_cols)))
    assert(len(sc_rows) == len(set(sc_rows)))
    # tienen que coincidir los mismos. set parece ordenarlos
    assert(set(sc_cols) == set(sc_rows))
    # tienen que coincidir con la lista que viene desde el archivo de sectores
    assert(sc_rows == sc_mip)
    # ahora debo verificar el ordenamiento y ajustarlo si no esta ordenado
    matIn = df_data.values
    matOut = np.zeros(matIn.shape)
    # ordeno a partir de los rows (que estarian copiados en los el archivo de sectores) 
    for i,sc in enumerate(sc_rows):
        try:
            j = sc_cols.index(sc)
        except:
            raise 'ERROR'
        else:
            matOut[:,i] = matIn[:,j]
    # la salida es la matriz y los labels
    return matOut

def lecturaVBP(csvfile_vbp, lookup_vbp):
    try:
        df_vbp = pd.read_csv(csvfile_vbp)
    except:
        try:
            df_vbp = pd.read_excel(csvfile_vbp)
        except:
            raise 'GPV should be CSV or EXCEL type'
    
    df_data = df_vbp.iloc[:,1:]
    sc_rows = df_vbp.iloc[:,0].tolist()
    # no hay repetidos
    assert(len(sc_rows) == len(set(sc_rows)))
    # tienen que coincidir los sectores con los mismos que el archivo de sectores
    assert(set(lookup_vbp) == set(sc_rows))   
    matIn = df_data.values
    vbp_global = matIn[:,0]
    vbp_locales = matIn[:,1:]    
    vbp_reg = df_data.iloc[:,1:].columns # De la columna 1 en adelante son los vbp provinciales
    return sc_rows, vbp_global, vbp_locales, vbp_reg
        
def lecturaGRP(csvfile_grp, flagzip=False):
    sc_mip = []
    sc_vbp = []
    sc_zip = []

    try:
        df_grp = pd.read_csv(csvfile_grp)
    except:
        try:
            df_grp = pd.read_excel(csvfile_grp)
        except:
            raise 'GRP file should be CSV or EXCEL type'

    nlin, ncol = df_grp.shape
    sc_mip = df_grp.iloc[:,0].tolist()
    sc_vbp = df_grp.iloc[:,1].tolist()
    # no hay repetidos en la agregacion sectorial del mip
    assert(len(sc_mip) == len(set(sc_mip)))
    # el numero de agregaciones sectoriales de la vbp es menor o igual a la mip 
    assert(len(set(sc_vbp)) <= len(set(sc_mip)))
    if flagzip and ncol == 3:
        sc_zip = df_grp.iloc[:,2].tolist()
        # el numero de agregaciones sectoriales de la vbp es menor o igual a la vbp 
        assert(len(set(sc_zip)) <= len(set(sc_vbp)))
    return sc_mip, sc_vbp, sc_zip
    

