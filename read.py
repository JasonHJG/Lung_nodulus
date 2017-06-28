#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:11:24 2017

@author: jingang
"""
import h5py
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
from PIL import Image


# create directories pos/neg
#############################################################
src=os.path.dirname(os.path.abspath(__file__))
if os.path.exists(src+'/data'):
    shutil.rmtree(src+'/data')
if not os.path.exists(src+'/data'):        
    os.mkdir(src+'/data')
    
newpath_train =src+'/data/training'

if os.path.exists(newpath_train):
    shutil.rmtree(newpath_train)
if not os.path.exists(newpath_train):        
    os.mkdir(newpath_train)

os.mkdir(newpath_train+'/positive')
os.mkdir(newpath_train+'/negative')
    
newpath_train1 =src+'/data/validation'
if os.path.exists(newpath_train1):
    shutil.rmtree(newpath_train1)
if not os.path.exists(newpath_train1):        
    os.mkdir(newpath_train1)

os.mkdir(newpath_train1+'/positive')
os.mkdir(newpath_train1+'/negative')
# extract information from the dataset
#############################################################
file=h5py.File('candidates.h5','r')


# prepare the date set 
#############################################################
num_pos=0
num_neg=0
size=len(file.keys())
keys=list(file.keys())
for i in range(size):
    label=file[keys[i]]['metainfo']['label']
    label_value=label.value

    data1=np.array(list(file[keys[i]]['patch']))[:,:,50]
    data2=np.array(list(file[keys[i]]['patch']))[:,50,:]
    data3=np.array(list(file[keys[i]]['patch']))[50,:,:]
    im1 = Image.fromarray(data1).convert('L')
    im2 = Image.fromarray(data2).convert('L')
    im3 = Image.fromarray(data3).convert('L')
    ID1='No.'+str(i)+'_1'
    ID2='No.'+str(i)+'_2'
    ID3='No.'+str(i)+'_3'
 
        
        # positive
    if label_value==1:
            
        if num_pos<1200:
            
            file_train_pos_1=newpath_train+'/positive/'+str(ID1)+'.png'
            file_train_pos_2=newpath_train+'/positive/'+str(ID2)+'.png'
            file_train_pos_3=newpath_train+'/positive/'+str(ID3)+'.png'
            im1.save(file_train_pos_1)
            im2.save(file_train_pos_2)
            im3.save(file_train_pos_3)
            
        elif num_pos>1200 and num_pos<1801:
            file_valid_pos_1=newpath_train1+'/positive/'+str(ID1)+'.png'
            file_valid_pos_2=newpath_train1+'/positive/'+str(ID2)+'.png'
            file_valid_pos_3=newpath_train1+'/positive/'+str(ID3)+'.png'
            im1.save(file_valid_pos_1)
            im2.save(file_valid_pos_2)
            im3.save(file_valid_pos_3)
        num_pos+=3    
    else:
            
        if num_neg<1200:
            file_train_neg_1=newpath_train+'/negative/'+str(ID1)+'.png'
            file_train_neg_2=newpath_train+'/negative/'+str(ID2)+'.png'
            file_train_neg_3=newpath_train+'/negative/'+str(ID3)+'.png'
            im1.save(file_train_neg_1)
            im2.save(file_train_neg_2)
            im3.save(file_train_neg_3)
        elif num_neg>1200 and num_neg<1801:
            file_valid_neg_1=newpath_train1+'/negative/'+str(ID1)+'.png'
            file_valid_neg_2=newpath_train1+'/negative/'+str(ID2)+'.png'
            file_valid_neg_3=newpath_train1+'/negative/'+str(ID3)+'.png'
            im1.save(file_valid_neg_1)
            im2.save(file_valid_neg_2)
            im3.save(file_valid_neg_3)
        num_neg+=3 
    if num_pos >1801 and num_neg>1801:
        break
            
            
      

