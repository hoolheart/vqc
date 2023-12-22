"""Virtual Quantum Computer"""

import pkgutil
from vqc._version import get_version

from vqc import (
    drivers,
    tasks,
    solvers,
    ensemble,
)

__path__ = pkgutil.extend_path(__path__, __name__)
__version__ = get_version()
