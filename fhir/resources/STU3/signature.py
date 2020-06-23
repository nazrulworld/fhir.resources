# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import element, fhirtypes


class Signature(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..
    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different signature
    approaches have different utilities.
    """

    resource_type = Field("Signature", const=True)

    blob: fhirtypes.Base64Binary = Field(
        None,
        alias="blob",
        title="Type `Base64Binary`",
        description="The actual signature content (XML DigSig. JWT, picture, etc.)",
    )
    blob__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_blob", title="Extension field for ``blob``."
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Type `Code`",
        description="The technical format of the signature",
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    onBehalfOfReference: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOfReference",
        title=(
            "Type `Reference` referencing `Practitioner, RelatedPerson, Patient, "
            "Device, Organization` (represented as `dict` in JSON)"
        ),
        description="The party represented",
        one_of_many="onBehalfOf",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onBehalfOfUri: fhirtypes.Uri = Field(
        None,
        alias="onBehalfOfUri",
        title="Type `Uri`",
        description="The party represented",
        one_of_many="onBehalfOf",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    onBehalfOfUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onBehalfOfUri", title="Extension field for ``onBehalfOfUri``."
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
        title="Type `Instant`",
        description="When the signature was created",
    )
    when__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_when", title="Extension field for ``when``."
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
        title="Type `Uri`",
        description="Who signed",
        one_of_many="who",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    whoUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whoUri", title="Extension field for ``whoUri``."
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
        one_of_many_fields = {
            "onBehalfOf": ["onBehalfOfReference", "onBehalfOfUri"],
            "who": ["whoReference", "whoUri"],
        }
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
