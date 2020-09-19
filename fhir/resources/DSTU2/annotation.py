# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict

from pydantic import Field, root_validator

from . import fhirtypes
from .element import Element


class Annotation(Element):
    """Text node with attribution.

    A  text note which also  contains information about who made the statement
    and when.
    """

    resource_type = Field("Annotation", const=True)

    authorReference: fhirtypes.ReferenceType = Field(
        None,
        alias="authorReference",
        title=(
            "Type `Reference` referencing `Practitioner, Patient, RelatedPerson` "
            "(represented as `dict` in JSON)"
        ),
        description="Individual responsible for the annotation",
        one_of_many="author",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    authorString: fhirtypes.String = Field(
        None,
        alias="authorString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Individual responsible for the annotation",
        one_of_many="author",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    text: fhirtypes.String = Field(
        ...,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="The annotation  - text content",
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="time",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the annotation was made",
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
        one_of_many_fields = {"author": ["authorReference", "authorString"]}
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
