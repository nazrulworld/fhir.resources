from typing import Optional, Union

from fhir_core.fhirabstractmodel import FHIRAbstractModel

from .fhirtypes import IdType, StringType


class FHIRResourceModel(FHIRAbstractModel):
    """Abstract base model class for all FHIR elements."""

    __resource_type__ = "FHIRAbstractResource"

    id: Optional[Union[IdType, StringType]] = None

    def relative_base(self):
        """ """
        return self.__resource_type__

    def relative_path(self):
        if self.id is None:
            return self.relative_base()
        return "{0}/{1}".format(self.relative_base(), self.id)
