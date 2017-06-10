# -*- coding: utf-8 -*-

from ._version import get_versions
from distutils.version import LooseVersion
import pandas as pd

_pdv = LooseVersion(pd.__version__)
_pd_version_under_017 = _pdv < '0.17.0'
_pd_version_under_018 = _pdv < '0.18.0'
_pd_version_under_019 = _pdv < '0.19.0'
_pd_version_under_020 = _pdv < '0.20.0'
_pd_version_under_021 = _pdv < '0.21.0'
_pd_version_under_100 = _pdv < '1.0.0'
_pd_version_is_019 = _pdv.version[1] == 19 and len(_pdv.version) == 3


# api imports

# >= 0.20.0
if not _pd_version_under_020:
    from pandas.api.types import *  # noqa

# >= 0.19.0
elif not _pd_version_under_019:
    from pandas.api.types import *  # noqa
    from pandas.types.dtypes import DatetimeTZDtype, CategoricalDtype  # noqa

# >= 0.18.0
elif not _pd_version_under_018:
    from pandas.core.common import DatetimeTZDtype, CategoricalDtype  # noqa

# >= 0.17.0
elif not _pd_version_under_017:
    from pandas.core.common import DatetimeTZDtype, CategoricalDtype  # noqa

else:
    raise ValueError("pandas < 0.17.0 is not supported for pandas-compat")


versions = get_versions()
__version__ = versions.get('closest-tag', versions['version'])
__git_revision__ = versions['full-revisionid']
del get_versions, versions
