# -*- coding: utf-8 -*-

import pytest

try:
    import pandas_compat as pdc
except ValueError:

    # we will raise on import of pdc
    # so if we are at this point we simply skip
    pytest.importorskip("pandas", minversion="0.17.0")


@pytest.mark.parametrize("func", [
    'is_bool', 'is_bool_dtype',
    'is_categorical', 'is_categorical_dtype', 'is_complex',
    'is_complex_dtype', 'is_datetime64_any_dtype',
    'is_datetime64_dtype', 'is_datetime64_ns_dtype',
    'is_datetime64tz_dtype', 'is_datetimetz', 'is_dtype_equal',
    'is_extension_type', 'is_float', 'is_float_dtype',
    'is_int64_dtype', 'is_integer',
    'is_integer_dtype', 'is_number', 'is_numeric_dtype',
    'is_object_dtype', 'is_scalar', 'is_sparse',
    'is_string_dtype', 'is_signed_integer_dtype',
    'is_timedelta64_dtype', 'is_timedelta64_ns_dtype',
    'is_unsigned_integer_dtype', 'is_period',
    'is_period_dtype', 'is_interval', 'is_interval_dtype',
    'is_re', 'is_re_compilable',
    'is_dict_like', 'is_iterator', 'is_file_like',
    'is_list_like', 'is_hashable',
    'is_named_tuple',
    'pandas_dtype', 'union_categoricals', 'infer_dtype'])
def test_introspection(func):
    result = getattr(pdc, func)
    assert result is not None


@pytest.mark.parametrize("dtype", [
    'CategoricalDtype',
    'DatetimeTZDtype',
    pytest.mark.skipif(
        pdc._pd_version_under_019, reason='too old version')('PeriodDtype'),
    pytest.mark.skipif(
        pdc._pd_version_under_019, reason='too old version')('IntervalDtype')])
def test_dtypes(dtype):
    result = getattr(pdc, dtype)
    assert result is not None
