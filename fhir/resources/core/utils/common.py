# _*_ coding: utf-8 _*_
from functools import lru_cache

from pydantic.v1.fields import ModelField
from pydantic.v1.typing import get_args, get_origin

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


@lru_cache(maxsize=1024, typed=True)
def is_list_type(field: ModelField) -> bool:
    """ """
    if field.outer_type_:
        origin = get_origin(field.outer_type_)
        return origin is not None and origin is list
    return False


@lru_cache(maxsize=1024, typed=True)
def is_primitive_type(field: ModelField) -> bool:
    """ """
    origin = get_origin(field.type_)
    if origin is None:
        return (
            getattr(field.type_, "is_primitive", lambda: False)() or field.type_ is bool
        )
    types_ = get_args(field.type_)
    out = False
    if len(types_) == 2:
        for type_ in types_:
            if isinstance(None, type_):
                continue
            out = getattr(type_, "is_primitive", lambda: False)() or type_ is bool
            if out is True:
                return True
    return out


@lru_cache(maxsize=512, typed=True)
def get_fhir_type_name(type_):
    """ """
    try:
        return type_.fhir_type_name()
    except AttributeError:
        if type_ is bool:
            return "boolean"
        if get_origin(type_) is not None:
            types_ = get_args(type_)
            if len(types_) == 2:
                for tp_ in types_:
                    if isinstance(None, tp_):
                        continue
                    return get_fhir_type_name(tp_)
        raise


@lru_cache(maxsize=512, typed=True)
def normalize_fhir_type_class(type_):
    """ """
    if get_origin(type_) is not None:
        types_ = get_args(type_)
        if len(types_) == 2:
            for tp_ in types_:
                if isinstance(None, tp_):
                    continue
                return normalize_fhir_type_class(tp_)
    else:
        return type_
