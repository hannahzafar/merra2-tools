""" Insert description """
from obstore.store import LocalStore
from virtualizarr import open_virtual_mfdataset
from virtualizarr.parsers import HDFParser
from virtualizarr.registry import ObjectStoreRegistry
from pathlib import Path

# Ignore warnings that do not apply to our use case
import warnings
warnings.filterwarnings(
  "ignore",
  message="Numcodecs codecs are not in the Zarr version 3 specification*",
  category=UserWarning
)

#TODO: Update description
#TODO: Implement more checks it is a Path obj

def create_vzarr_store(filepaths):
    # Build registry dict over all unique parent dirs in filepaths
    registry_map = {}
    for file in filepaths:
        dir_path = file.parent
        prefix = dir_path.as_uri() + "/"
        if prefix not in registry_map:
            registry_map[prefix] = LocalStore(prefix=dir_path)

    # This differs from VZarr2 documentation in that the filepath and the store are in separate directories: registers source dir as a file:// prefix and creates a LocalStore for that source directory 
    registry = ObjectStoreRegistry(registry_map)

    file_urls = [file.as_uri() for file in filepaths]

    vds = open_virtual_mfdataset(
        urls=file_urls,
        parser=HDFParser(),
        registry=registry,
        # loadable_variables=['time'],
        # decode_times=True,
    )

    vstore = Path.cwd() / "virtual_store"
    vstore.mkdir(exist_ok=True)

    vds.vz.to_kerchunk(f"{vstore.name}/vstore.parquet", format="parquet")

    #FIX: What should this function return?
    return
    #NOTE: So I have it able to open multiple files into a vds. How can I write that to a store? Do I want to try icechunk? (I was using json and parquet previously
    # Is this process fast enough that I don't really need to "slice the data" (i.e., select only N+S America and vars I want) or is that still significant?



'''
ds_MERRA2 = xr.open_mfdataset(flist)[var]

# Sel only N+S America
americas_MERRA2 = ds_MERRA2.sel(
    lon=slice(-170, -30),
    lat=slice(-60,80)
)

print(americas_MERRA2)
#FIX: doing the sel takes so long, I think I'm just gonna virtualize
#FIX: Make this script the generation of the virtualizarr
'''
