"""Top-level package for PyNHD."""
from importlib.metadata import PackageNotFoundError, version

if int(version("shapely").split(".")[0]) > 1:
    import os

    os.environ["USE_PYGEOS"] = "0"

from pynhd.core import AGRBase, GeoConnex, ScienceBase
from pynhd.exceptions import (
    DependencyError,
    InputRangeError,
    InputTypeError,
    InputValueError,
    MissingColumnError,
    MissingCRSError,
    MissingItemError,
    ZeroMatchedError,
)
from pynhd.network_tools import (
    enhd_flowlines_nx,
    flowline_resample,
    flowline_xsection,
    mainstem_huc12_nx,
    network_resample,
    network_xsection,
    nhdflw2nx,
    nhdplus_l48,
    prepare_nhdplus,
    topoogical_sort,
    vector_accumulation,
)
from pynhd.nhdplus_derived import (
    StreamCat,
    enhd_attrs,
    epa_nhd_catchments,
    nhd_fcode,
    nhdplus_attrs,
    nhdplus_attrs_s3,
    nhdplus_vaa,
    streamcat,
)
from pynhd.print_versions import show_versions
from pynhd.pynhd import NHD, NLDI, NHDPlusHR, PyGeoAPI, WaterData, geoconnex, pygeoapi

try:
    __version__ = version("pynhd")
except PackageNotFoundError:
    __version__ = "999"

__all__ = [
    "DependencyError",
    "InputRangeError",
    "InputValueError",
    "InputTypeError",
    "MissingItemError",
    "MissingColumnError",
    "MissingCRSError",
    "ZeroMatchedError",
    "prepare_nhdplus",
    "geoconnex",
    "topoogical_sort",
    "vector_accumulation",
    "flowline_resample",
    "network_resample",
    "flowline_xsection",
    "network_xsection",
    "nhdflw2nx",
    "enhd_flowlines_nx",
    "mainstem_huc12_nx",
    "nhdplus_l48",
    "StreamCat",
    "streamcat",
    "show_versions",
    "NLDI",
    "AGRBase",
    "GeoConnex",
    "ScienceBase",
    "NHDPlusHR",
    "NHD",
    "PyGeoAPI",
    "pygeoapi",
    "WaterData",
    "nhd_fcode",
    "nhdplus_attrs",
    "nhdplus_attrs_s3",
    "epa_nhd_catchments",
    "enhd_attrs",
    "nhdplus_vaa",
]
