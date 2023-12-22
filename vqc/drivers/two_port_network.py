"""General driver of two-port network"""

from typing import (
    Any,
    Optional,
)
from softlab.tu.station import (
    Parameter,
    Device,
    DeviceBuilder,
    register_device_builder,
)
from softlab.jin.sp import Wavement
from vqc.drivers.validators import ValDataFrame
import numpy as np
import pandas as pd

# TODO
class TwoPortNetwork(Device):

    def __init__(self, name: str) -> None:
        super.__init__(name)
