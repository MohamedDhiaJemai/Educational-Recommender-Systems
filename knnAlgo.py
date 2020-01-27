# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:56:48 2020

@author: M.Dhia
"""
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors


def knnAlgo(dataset,nn):
    
    #Length of our Dataframe
    lentghDataSet = len(dataset.index)
    lentghDataSet = lentghDataSet -1
    
    X = dataset.iloc[:,0:20].values
    norm_data = MinMaxScaler() #initialisation
    X = norm_data.fit_transform(X)
    
    nbrs = NearestNeighbors(n_neighbors=nn, algorithm='ball_tree').fit(X)
    
    distances, indices = nbrs.kneighbors(X)
    
    distances = np.sort(distances,axis=0)
    
    distances = distances[:,1]
    
    #plt.plot(distances)
          
    lentghIndices = indices[lentghDataSet]
    similarIndice = lentghIndices[1]
    similarStudent = dataset.loc[similarIndice]
    print('Etudient Similaire : ',similarStudent)
    matierOptions = similarStudent[20:]
    print ('Les options de etudiant similaire : ',matierOptions)
    result_list=[]
    print('Les options recommander : ')
    ## l'affichage des nom des matières optionnelles
    options = matierOptions.to_frame()
    q=0
    for value in matierOptions:
        #print(value)
        if (value != -1):
            print(options.index[q])
            result_list.append(options.index[q])
        q=q+1
    return result_list