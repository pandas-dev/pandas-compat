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
    'is_float', 'is_float_dtype',
    'is_int64_dtype', 'is_integer',
    'is_integer_dtype', 'is_number', 'is_numeric_dtype',
    'is_object_dtype', 'is_sparse',
    'is_timedelta64_dtype', 'is_timedelta64_ns_dtype',
    'is_re', 'is_re_compilable',
    'is_iterator',
    'is_list_like', 'is_hashable'])
def test_introspection_017(func):
    result = getattr(pdc, func)
    assert result is not None


# 018
@pytest.mark.skipif(
    pdc._pd_version_under_019, reason='pandas >= 0.18.0 required')
@pytest.mark.parametrize("func", [
    'is_extension_type', 'is_scalar', 'is_dict_like', 'is_string_dtype',
    'pandas_dtype', 'is_named_tuple', 'is_file_like', 'is_period'])
def test_introspection_018(func):
    result = getattr(pdc, func)
    assert result is not None


# 019
@pytest.mark.skipif(
    pdc._pd_version_under_019, reason='pandas >= 0.19.0 required')
@pytest.mark.parametrize("func", [
    'union_categoricals', 'infer_dtype'])
def test_introspection_019(func):
    result = getattr(pdc, func)
    assert result is not None


# 020
@pytest.mark.skipif(
    pdc._pd_version_under_019, reason='pandas >= 0.20.0 required')
@pytest.mark.parametrize("func", [
    'is_interval', 'is_interval_dtype', 'is_period_dtype',
    'is_signed_integer_dtype', 'is_unsigned_integer_dtype'])
def test_introspection_020(func):
    result = getattr(pdc, func)
    assert result is not None


# 017
@pytest.mark.parametrize("dtype", [
    'CategoricalDtype',
    'DatetimeTZDtype'])
def test_dtypes_017(dtype):
    result = getattr(pdc, dtype)
    assert result is not None


# 020
@pytest.mark.skipif(
    pdc._pd_version_under_019, reason='pandas >= 0.19.0 required')
@pytest.mark.parametrize("dtype", [
    'IntervalDtype',
    'PeriodDtype'])
def test_dtypes(dtype):
    result = getattr(pdc, dtype)
    assert result is not None
