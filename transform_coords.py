# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:07:37 2018

Function to transform coordinates in pandas dataframe from one CRS to another.

args:
    df
    xname
    yname
    in_epsg
    out_epsg
kwargs:
    outxname
    outyname    
    

@author: jlogan
"""

import pandas as pd
import pyproj

def transform_coords(df, xname, yname, in_epsg, out_epsg, **kwargs):
    
    # set up output col names
    outxname = 'out_x_coord'
    outyname = 'out_y_coord'
    if kwargs is not None:
        if 'outxname' in kwargs:
            if kwargs['outxname'] != xname:
                outxname = kwargs.outxname
            if kwargs['outxname'] == xname:
                raise NameError('Specified output columns name for x coordinate is the same as input column name')
        if 'outyname' in kwargs:
            if kwargs['outyname'] != yname:
                outyname = kwargs.outyname
            if kwargs['outyname'] == yname:
                raise NameError('Specified output columns name for y coordinate is the same as input y column name')
    
    # set up projections
    inProj = pyproj.Proj(init=f'epsg:{in_epsg}')
    outProj = pyproj.Proj(init=f'epsg:{out_epsg}')
    
    # transform coords
    x, y = pyproj.transform(inProj,outProj,df[xname].values,df[yname].values)
    
    outdf = df.copy(deep=True)
    
    # assign to new df col
    outdf[outxname] = x
    outdf[outyname] = y
    
    return outdf

            