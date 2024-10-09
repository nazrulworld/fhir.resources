from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Annotation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class Annotation(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Text node with attribution.
    A  text note which also  contains information about who made the statement
    and when.
    """

    __resource_type__ = "Annotation"

    authorReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="authorReference",
        title="Individual responsible for the annotation",
        description="The individual responsible for making the annotation.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e author[x]
            "one_of_many": "author",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "RelatedPerson",
                "Organization",
            ],
        },
    )

    authorString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="authorString",
        title="Individual responsible for the annotation",
        description="The individual responsible for making the annotation.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e author[x]
            "one_of_many": "author",
            "one_of_many_required": False,
        },
    )
    authorString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_authorString", title="Extension field for ``authorString``."
    )

    text: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="text",
        title="The annotation  - text content (as markdown)",
        description="The text of the annotation in markdown format.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    time: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="time",
        title="When the annotation was made",
        description="Indicates when this particular annotation was made.",
        json_schema_extra={
            "element_property": True,
        },
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_time", title="Extension field for ``time``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Annotation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "authorReference", "authorString", "time", "text"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("text", "text__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields
