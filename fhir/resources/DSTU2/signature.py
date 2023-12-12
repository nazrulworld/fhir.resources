# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .element import Element


class Signature(Element):
    """A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..

    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different Signature
    approaches have different utilities.
    """

    resource_type = Field("Signature", const=True)

    blob: fhirtypes.Base64Binary = Field(
        ...,
        alias="blob",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="The actual signature content (XML DigSig. JWT, picture, etc.)",
    )

    contentType: fhirtypes.Code = Field(
        ...,
        alias="contentType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="The technical format of the signature",
    )

    type: ListType[fhirtypes.CodingType] = Field(
        ...,
        alias="type",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Indication of the reason the entity signed the object(s)",
    )

    when: fhirtypes.Instant = Field(
        ...,
        alias="when",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When the signature was created",
    )

    whoReference: fhirtypes.ReferenceType = Field(
        None,
        alias="whoReference",
        title=(
            "Type `Reference` referencing `Practitioner, RelatedPerson, Patient, "
            "Device, Organization` (represented as `dict` in JSON)"
        ),
        description="Who signed",
        one_of_many="who",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    whoUri: fhirtypes.Uri = Field(
        None,
        alias="whoUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Who signed",
        one_of_many="who",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"who": ["whoReference", "whoUri"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
