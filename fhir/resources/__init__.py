# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Any, Dict, Union

from .fhirabstractmodel import FHIRAbstractModel
from .fhirtypesvalidators import get_fhir_model_class

__fhir_version__ = "4.0.1"
__version__ = "6.0.0b7"


def construct_fhir_element(
    element_type: str, data: Union[Dict[str, Any], str, bytes, Path]
) -> FHIRAbstractModel:

    try:
        klass = get_fhir_model_class(element_type)
    except KeyError:
        raise LookupError(
            f"{element_type} doesnt to be valid FHIRModel (element type) name!"
        )
    if isinstance(data, (str, bytes)):
        return klass.parse_raw(data, content_type="application/json")
    elif isinstance(data, Path):
        return klass.parse_file(data)
    return klass.parse_obj(data)


__all__ = ["get_fhir_model_class", "construct_fhir_element"]
