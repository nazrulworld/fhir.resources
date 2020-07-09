# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Annotation
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict

from pydantic import Field, root_validator

from . import element, fhirtypes


class Annotation(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Text node with attribution.
    A  text note which also  contains information about who made the statement
    and when.
    """

    resource_type = Field("Annotation", const=True)

    authorReference: fhirtypes.ReferenceType = Field(
        None,
        alias="authorReference",
        title="Individual responsible for the annotation",
        description="The individual responsible for making the annotation.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e author[x]
        one_of_many="author",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Patient",
            "RelatedPerson",
            "Organization",
        ],
    )

    authorString: fhirtypes.String = Field(
        None,
        alias="authorString",
        title="Individual responsible for the annotation",
        description="The individual responsible for making the annotation.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e author[x]
        one_of_many="author",
        one_of_many_required=False,
    )
    authorString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authorString", title="Extension field for ``authorString``."
    )

    text: fhirtypes.Markdown = Field(
        ...,
        alias="text",
        title="The annotation  - text content (as markdown)",
        description="The text of the annotation in markdown format.",
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="time",
        title="When the annotation was made",
        description="Indicates when this particular annotation was made.",
        # if property is element of this resource.
        element_property=True,
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_time", title="Extension field for ``time``."
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
