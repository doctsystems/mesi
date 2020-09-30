# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:58:08 2020

@author: Pablo
"""

import numpy as np

def _calc_SLQ(vbp_global, vbp_local):
	ratio_global = list(map(lambda x: x/vbp_global.sum(), vbp_global))
	ratio_local = list(map(lambda x: x/vbp_local.sum(), vbp_local))
	slq = []
	for i, s in enumerate(ratio_global):
		if s == 0:
			slq.append(0)
		else:
			slq.append(ratio_local[i] / s)
	return slq

def _calc_FLQ(slq, vbp_global, vbp_local):
    region_data = np.log2( 1 + vbp_local.sum() / vbp_global.sum()) # $'SLQ-BAS'.I7
    delta = np.log((vbp_local.sum() / vbp_global.sum()) / region_data) / np.log(region_data) # $'SLQ-BAS'.K7
    lambda_star = region_data ** delta # FLQ-BAS'.$C$2
    n = len(slq) ## Cantidad de sectores
    flq = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i == j:
                flq[i][j] = slq[i] * lambda_star
#				flq[i][j] = lambda_star tenia esta version en prod
            elif slq[i] > 0:
                flq[i][j] = slq[i] / slq[j] * lambda_star
            else:
                flq[i][j] = 0

    # aplicar el tope de 1
    x = np.where(flq > 1.0)
    flq[x] = 1.0
    
    return flq

def _calc_AFLQ(slq, vbp_global, vbp_local):
    region_data = np.log2( 1 + vbp_local.sum() / vbp_global.sum()) # $'SLQ-BAS'.I7
    delta = np.log((vbp_local.sum() / vbp_global.sum()) / region_data) / np.log(region_data) # $'SLQ-BAS'.K7
    lambda_star = region_data ** delta # FLQ-BAS'.$C$2
    vec_especializacion = np.log2(1 + np.array(slq))
    
    for i in range(len(slq)):
        if slq[i] < 1:
            vec_especializacion[i] = 1
    
    n = len(slq) ## Cantidad de sectores
    aflq = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i == j:
                aflq[i][j] = slq[i] * lambda_star * vec_especializacion[j]
            elif slq[j] > 0:
                aflq[i][j] = slq[i] / slq[j] * lambda_star * vec_especializacion[j]
            else:
                aflq[i][j] = 0
    # aplicar el tope de 1
    x = np.where(aflq > 1.0)
    aflq[x] = 1.0
    return aflq

def _coef_tecnicos(mip_global, vbp_global):
    n = len(vbp_global)
    coef = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            coef[i][j] = mip_global[i][j] / vbp_global[j]
    return coef


