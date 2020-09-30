import os
import sys
import pandas as pd
import numpy as np
import datetime
from functions import _calc_SLQ, _calc_FLQ, _calc_AFLQ, _coef_tecnicos
from reading_functions import lecturaMIP, lecturaVBP, lecturaGRP
from grouping_functions import agruparMatrices, zipMatrices

def calc_SLQ(vbp_global, vbp_local):
    slq = _calc_SLQ(vbp_global,vbp_local)
    return slq

def calc_FLQ(slq, vbp_global, vbp_local):
    flq = _calc_FLQ(slq, vbp_global, vbp_local)
    return flq

def calc_AFLQ(slq, vbp_global, vbp_local):
    aflq = _calc_AFLQ(slq, vbp_global, vbp_local)
    return aflq

def coef_tecnicos(mip_global, vbp_global):
    coef = _coef_tecnicos(mip_global, vbp_global)
    return coef

def calc_MIP_local(mip_global, vbp_global, vbp_local, metodo):
    coef = coef_tecnicos(mip_global, vbp_global)
    slq = calc_SLQ(vbp_global, vbp_local)
    
    if metodo == 'FLQ':
        matParams = calc_FLQ(slq, vbp_global, vbp_local)
    else:
        matParams = calc_AFLQ(slq, vbp_global, vbp_local)
        
    n = len(slq) # Cantidad de sectores
    mip = np.zeros((n,n),dtype=np.float32)
    for i in range(n):
        for j in range(n):
            mip[i][j] = matParams[i][j] * coef[i][j]
    return mip, coef, slq, matParams

def main():
    metodo = 'FLQ'
    if len(sys.argv) > 1:
        file_mip = sys.argv[1]
        file_vbps = sys.argv[2]
        file_grp = sys.argv[3]
        if len(sys.argv) > 4:
            metodo = sys.argv[4]
    else:
        file_mip = os.path.join('in','sg_MIP_Arg.csv')
        file_vbps = os.path.join('in','sg_VBPs.csv')
        file_grp = os.path.join('in','sg_GRP.csv')
        # descomentar para probar con agregacion de sectores
        #file_vbps = os.path.join('in','sg_VBPs_wAgr.csv') 
        #file_grp = os.path.join('in','sg_GRP_wAgr.csv')        
        
    lookup_mip, lookup_vbp, lookup_zip = lecturaGRP(file_grp, flagzip=True)
    mip_global = lecturaMIP(file_mip, lookup_mip)
    sc_vbp, vbp_global, vbp_locales, vbp_reg = lecturaVBP(file_vbps, lookup_vbp)

    sc_vbp_out, out_mip_global, out_vbp_global, out_vbp_locales = agruparMatrices(mip_global, vbp_global, vbp_locales, sc_vbp, lookup_mip, lookup_vbp)
    # hacer el zip si hay una nueva agrupacion de sectores
    sc_vbp_out, out_mip_global, out_vbp_global, out_vbp_locales = zipMatrices(
            out_mip_global, out_vbp_global, out_vbp_locales, sc_vbp_out, lookup_vbp, lookup_zip)

        	
    t = datetime.datetime.now()
    # folderout = 'out-%d-%d-%d.%d' % (t.hour,t.minute,t.second,t.microsecond)
    folderout = 'out'
    if os.path.exists(folderout) == False:
        os.mkdir(folderout)

    for i,region in enumerate(vbp_reg):
        vbp_local = out_vbp_locales[:,i]
        res, coef, slq, matParams = calc_MIP_local(out_mip_global, out_vbp_global, vbp_local, metodo)
        # save mip
        df_mip = pd.DataFrame(columns=sc_vbp_out, data=res, index=range(len(sc_vbp_out)))
        df_mip.insert(0,'SECTOR',sc_vbp_out)
        df_mip.to_csv(os.path.join(folderout,'MIP_%s_%s.csv' % (format(region),metodo)), index=False)
        # save matParams
        df_par = pd.DataFrame(columns=sc_vbp_out, data=matParams, index=range(len(sc_vbp_out)))
        df_par.insert(0,'SECTOR',sc_vbp_out)
        df_par.to_csv(os.path.join(folderout,'%s_%s.csv' % (format(region),metodo)), index=False)
        # save Coefficients
        df_coef = pd.DataFrame(columns=sc_vbp_out, data=coef, index=range(len(sc_vbp_out)))
        df_coef.insert(0,'SECTOR',sc_vbp_out)
        df_coef.to_csv(os.path.join(folderout,'COEF_%s_%s.csv' % (format(region),metodo)), index=False)
        # save 
        reglist = []
        reglist.append(region)
        df_slq = pd.DataFrame(columns=reglist, data=np.asarray(slq).squeeze())
        df_slq.insert(0,'SECTOR',sc_vbp_out)
        df_slq.to_csv(os.path.join(folderout,'SLQ_%s_%s.csv' % (format(region),metodo)), index=False)

        output_filename = os.path.join(folderout,'MIP_%s_%s.xlsx' % (region,metodo))
        with pd.ExcelWriter(output_filename) as writer:
            df_mip.to_excel(writer, index=False, sheet_name='MIP')
            df_par.to_excel(writer, index=False, sheet_name=metodo)
            df_coef.to_excel(writer, index=False, sheet_name='Coefficients')
            df_slq.to_excel(writer, index=False, sheet_name='SLQ')
            writer.save()
            

if __name__ == "__main__":
    main()

# python main.py in\sg_MIP_Arg.csv in\sg_VBPs.csv in\sg_GRP.csv
# python main.py in\sg_MIP_Arg.csv in\sg_VBPs_wAgr.csv in\sg_GRP_wAgr.csv    