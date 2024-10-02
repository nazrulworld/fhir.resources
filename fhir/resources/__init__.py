from __future__ import annotations as _annotations

from functools import lru_cache
from typing import TYPE_CHECKING, cast

from fhir_core.fhirabstractmodel import FHIRAbstractModel

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"
__version__ = "8.0.0"
__fhir_version__ = "5.0.0"


@lru_cache(maxsize=None, typed=True)
def get_fhir_model_class(model_name: str) -> type[FHIRAbstractModel]:
    """ """
    from . import fhirtypes as ft

    try:
        model_type = getattr(ft, model_name + "Type")
        if TYPE_CHECKING:
            from fhir_core.types import FhirBase

            model_type = cast(type[FhirBase], model_type)

        return model_type.get_model_klass()

    except AttributeError:
        raise ValueError(f"{model_name} is not a valid FHIR Model")
