#%%
from pathlib import Path
from osgeo import gdal
import os
# os.environ['USE_PYGEOS'] = '0'
from joblib import Parallel, delayed
import tqdm

from mods_vulnerability_caseload_ensemble import *
# from mods_geom_ops import *

#%%
###################################################################
# Load datapath and datasets
DIR = "./data"
datadir = Path(DIR + '/shp')
rasdir = Path(DIR + '/tif/...')
resdir = Path(DIR + '/results/....')

# Gorkha test
rasdir = Path(DIR + '/tif/test_gorkha/...')

list_rasters = [file for file in os.listdir(rasdir) if file.lower().endswith(".tif") and not file.startswith('._')]
print(f'\n number of rasters: {len(list_rasters)} in {rasdir}')
print(list_rasters)


##################################################################
#%%
# run algo in parallel
# using Joblib
# earthquake_impact(datadir, list_rasters[0], rasdir, road_only="no", resdir=resdir, building_occupancy=1.0)
results = Parallel(n_jobs=1)(delayed(earthquake_impact)(datadir, raster, rasdir, road_only="no", resdir=resdir, building_occupancy=1.0) for raster in tqdm(list_rasters))



# %%
