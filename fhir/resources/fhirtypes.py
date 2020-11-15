# _*_ coding: utf-8 _*_
import datetime
import re
from email.utils import formataddr, parseaddr
from typing import TYPE_CHECKING, Any, Dict, Optional, Pattern, Union
from uuid import UUID

from pydantic import AnyUrl
from pydantic.errors import DateError, DateTimeError, TimeError
from pydantic.main import load_str_bytes
from pydantic.networks import validate_email
from pydantic.types import (
    ConstrainedBytes,
    ConstrainedDecimal,
    ConstrainedInt,
    ConstrainedStr,
)
from pydantic.validators import bool_validator, parse_date, parse_datetime, parse_time

from .fhirabstractmodel import FHIRAbstractModel
from .fhirtypesvalidators import run_validator_for_fhir_type

if TYPE_CHECKING:
    from pydantic.types import CallableGenerator
    from pydantic.fields import ModelField
    from pydantic import BaseConfig

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

FHIR_DATE_PARTS = re.compile(r"(?P<year>\d{4})(-(?P<month>\d{2}))?(-(?P<day>\d{2}))?$")
FHIR_PRIMITIVES = [
    "boolean",
    "string",
    "base64Binary",
    "code",
    "id",
    "decimal",
    "integer",
    "unsignedInt",
    "positiveInt",
    "uri",
    "oid",
    "uuid",
    "canonical",
    "url",
    "markdown",
    "xhtml",
    "date",
    "dateTime",
    "instant",
    "time",
]


class Primitive:
    """FHIR Primitive Data Type Base Class"""

    __fhir_release__: str = "R4"
    __visit_name__: Optional[str] = None
    regex: Optional[Pattern[str]] = None

    @classmethod
    def is_primitive(cls) -> bool:
        """ """
        return True

    @classmethod
    def fhir_type_name(cls) -> Optional[str]:
        """ """
        return cls.__visit_name__


if TYPE_CHECKING:
    Boolean = bool
else:

    class Boolean(int, Primitive):
        """true | false"""

        regex = re.compile("true|false")
        __visit_name__ = "boolean"

        @classmethod
        def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
            field_schema.update(type="boolean")

        @classmethod
        def __get_validators__(cls) -> "CallableGenerator":
            yield bool_validator


class String(ConstrainedStr, Primitive):
    """A sequence of Unicode characters
    Note that strings SHALL NOT exceed 1MB (1024*1024 characters) in size.
    Strings SHOULD not contain Unicode character points below 32, except for
    u0009 (horizontal tab), u0010 (carriage return) and u0013 (line feed).
    Leading and Trailing whitespace is allowed, but SHOULD be removed when using
    the XML format. Note: This means that a string that consists only of whitespace
    could be trimmed to nothing, which would be treated as an invalid element value.
    Therefore strings SHOULD always contain non-whitespace conten"""

    regex = re.compile(r"[ \r\n\t\S]+")
    __visit_name__ = "string"


class Base64Binary(ConstrainedBytes, Primitive):
    """A stream of bytes, base64 encoded (RFC 4648 )"""

    regex = re.compile(r"(\s*([0-9a-zA-Z+=]){4}\s*)+")
    __visit_name__ = "base64Binary"


class Code(ConstrainedStr, Primitive):
    """Indicates that the value is taken from a set of controlled
    strings defined elsewhere (see Using codes for further discussion).
    Technically, a code is restricted to a string which has at least one
    character and no leading or trailing whitespace, and where there is
    no whitespace other than single spaces in the contents"""

    regex = re.compile(r"[^\s]+(\s[^\s]+)*")
    __visit_name__ = "code"


class Id(ConstrainedStr, Primitive):
    """Any combination of upper- or lower-case ASCII letters
    ('A'..'Z', and 'a'..'z', numerals ('0'..'9'), '-' and '.',
    with a length limit of 64 characters.
    (This might be an integer, an un-prefixed OID, UUID or any other identifier
    pattern that meets these constraints.)
    """

    regex = re.compile(r"[A-Za-z0-9\-.]{1,64}")
    min_length = 1
    max_length = 64
    __visit_name__ = "id"


class Decimal(ConstrainedDecimal, Primitive):
    """Rational numbers that have a decimal representation.
    See below about the precision of the number"""

    regex = re.compile(r"-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?")
    __visit_name__ = "decimal"


class Integer(ConstrainedInt, Primitive):
    """A signed integer in the range −2,147,483,648..2,147,483,647 (32-bit;
    for larger values, use decimal)"""

    regex = re.compile(r"[0]|[-+]?[1-9][0-9]*")
    __visit_name__ = "integer"


class UnsignedInt(ConstrainedInt, Primitive):
    """Any non-negative integer in the range 0..2,147,483,647"""

    regex = re.compile(r"[0]|([1-9][0-9]*)")
    __visit_name__ = "unsignedInt"
    ge = 0


class PositiveInt(ConstrainedInt, Primitive):
    """Any positive integer in the range 1..2,147,483,647"""

    regex = re.compile(r"\+?[1-9][0-9]*")
    __visit_name__ = "positiveInt"
    gt = 0


class Uri(ConstrainedStr, Primitive):
    """A Uniform Resource Identifier Reference (RFC 3986 ).
    Note: URIs are case sensitive.
    For UUID (urn:uuid:53fefa32-fcbb-4ff8-8a92-55ee120877b7)
    use all lowercase xs:anyURI A JSON string - a URI
    Regex: \\S* (This regex is very permissive, but URIs must be valid.
    Implementers are welcome to use more specific regex statements
    for a URI in specific contexts)
    URIs can be absolute or relative, and may have an optional fragment identifier
    This data type can be bound to a ValueSet"""

    __visit_name__ = "uri"
    regex = re.compile(r"\S*")


class Oid(ConstrainedStr, Primitive):
    """An OID represented as a URI (RFC 3001 ); e.g. urn:oid:1.2.3.4.5"""

    __visit_name__ = "oid"
    regex = re.compile(r"urn:oid:[0-2](\.(0|[1-9][0-9]*))+")


class Uuid(UUID, Primitive):
    """A UUID (aka GUID) represented as a URI (RFC 4122 );
    e.g. urn:uuid:c757873d-ec9a-4326-a141-556f43239520"""

    __visit_name__ = "uuid"
    regex = None


class Canonical(Uri):
    """A URI that refers to a resource by its canonical URL (resources with a url property).
    The canonical type differs from a uri in that it has special meaning in this specification,
    and in that it may have a version appended, separated by a vertical bar (|).
    Note that the type canonical is not used for the actual canonical URLs that are
    the target of these references, but for the URIs that refer to them, and may have
    the version suffix in them. Like other URIs, elements of type canonical may also have
    #fragment references"""

    __visit_name__ = "canonical"


class Url(AnyUrl, Primitive):
    """A Uniform Resource Locator (RFC 1738 ).
    Note URLs are accessed directly using the specified protocol.
    Common URL protocols are http{s}:, ftp:, mailto: and mllp:,
    though many others are defined"""

    __visit_name__ = "url"

    @classmethod
    def validate(  # type: ignore
        cls, value: str, field: "ModelField", config: "BaseConfig"
    ) -> Union["AnyUrl", str]:
        """ """
        if value.startswith("mailto:"):
            schema = value[0:7]
            email = value[7:]
            realname = parseaddr(email)[0]
            name, email = validate_email(email)
            if realname:
                email = formataddr((name, email))
            return schema + email
        elif value.startswith("mllp:") or value.startswith("llp:"):
            # xxx: find validation
            return value
        elif value in FHIR_PRIMITIVES:
            # Extensions may contain a valueUrl for a primitive FHIR type
            return value

        return AnyUrl.validate(value, field, config)


class Markdown(ConstrainedStr, Primitive):
    """A FHIR string (see above) that may contain markdown syntax for optional processing
    by a markdown presentation engine, in the GFM extension of CommonMark format (see below)"""

    __visit_name__ = "markdown"
    regex = re.compile(r"\s*(\S|\s)*")


class Xhtml(ConstrainedStr, Primitive):
    __visit_name__ = "xhtml"


class Date(datetime.date, Primitive):
    """A date, or partial date (e.g. just year or year + month)
    as used in human communication. The format is YYYY, YYYY-MM, or YYYY-MM-DD,
    e.g. 2018, 1973-06, or 1905-08-23.
    There SHALL be no time zone. Dates SHALL be valid dates"""

    regex = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2]"
        r"[0-9]|3[0-1]))?)?"
    )
    __visit_name__ = "date"

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":

        yield cls.validate

    @classmethod
    def validate(
        cls, value: Union[datetime.date, str, bytes, int, float]
    ) -> Union[datetime.date, str]:
        """ """
        if not isinstance(value, str):
            # default handler
            return parse_date(value)

        match = FHIR_DATE_PARTS.match(value)

        if not match:
            if not cls.regex.match(value):
                raise DateError()
        elif not match.groupdict().get("day"):
            if match.groupdict().get("month") and int(match.groupdict()["month"]) > 12:
                raise DateError()
            # we keep original
            return value
        return parse_date(value)


class DateTime(datetime.datetime, Primitive):
    """A date, date-time or partial date (e.g. just year or year + month) as used
    in human communication. The format is YYYY, YYYY-MM, YYYY-MM-DD or
    YYYY-MM-DDThh:mm:ss+zz:zz, e.g. 2018, 1973-06, 1905-08-23,
    2015-02-07T13:28:17-05:00 or 2017-01-01T00:00:00.000Z.
    If hours and minutes are specified, a time zone SHALL be populated.
    Seconds must be provided due to schema type constraints but may be
    zero-filled and may be ignored at receiver discretion.
    Dates SHALL be valid dates. The time "24:00" is not allowed.
    Leap Seconds are allowed - see below"""

    regex = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|"
        r"3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|"
        r"60)(\.[0-9]+)?(Z|([+\-])((0[0-9]|"
        r"1[0-3]):[0-5][0-9]|14:00)))?)?)?"
    )
    __visit_name__ = "dateTime"

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":

        yield cls.validate

    @classmethod
    def validate(
        cls, value: Union[datetime.date, datetime.datetime, str, bytes, int, float]
    ) -> Union[datetime.datetime, datetime.date, str]:
        """ """
        if isinstance(value, datetime.date):
            return value

        if not isinstance(value, str):
            # default handler
            return parse_datetime(value)
        match = FHIR_DATE_PARTS.match(value)
        if match:
            if (
                match.groupdict().get("year")
                and match.groupdict().get("month")
                and match.groupdict().get("day")
            ):
                return parse_date(value)
            elif match.groupdict().get("year") and match.groupdict().get("month"):
                if int(match.groupdict()["month"]) > 12:
                    raise DateError()
            # we don't want to loose actual information, so keep as string
            return value
        if not cls.regex.match(value):
            raise DateTimeError()

        return parse_datetime(value)


class Instant(datetime.datetime, Primitive):
    """An instant in time in the format YYYY-MM-DDThh:mm:ss.sss+zz:zz
    (e.g. 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z).
    The time SHALL specified at least to the second and SHALL include a time zone.
    Note: This is intended for when precisely observed times are required
    (typically system logs etc.), and not human-reported times - for those,
    use date or dateTime (which can be as precise as instant,
    but is not required to be). instant is a more constrained dateTime

    Note: This type is for system times, not human times (see date and dateTime below)."""

    regex = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|"
        r"3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]"
        r"|60)(\.[0-9]+)?(Z|([+\-])((0[0-9]|"
        r"1[0-3]):[0-5][0-9]|14:00))"
    )
    __visit_name__ = "instant"

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":

        yield cls.validate

    @classmethod
    def validate(cls, value):
        """ """
        if isinstance(value, str):
            if not cls.regex.match(value):
                raise DateTimeError()
        return parse_datetime(value)


class Time(datetime.time, Primitive):
    """A time during the day, in the format hh:mm:ss.
    There is no date specified. Seconds must be provided due
    to schema type constraints but may be zero-filled and may
    be ignored at receiver discretion.
    The time "24:00" SHALL NOT be used. A time zone SHALL NOT be present.
    Times can be converted to a Duration since midnight."""

    regex = re.compile(r"([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?")
    __visit_name__ = "time"

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":

        yield cls.validate

    @classmethod
    def validate(cls, value):
        """ """
        if isinstance(value, str):
            if not cls.regex.match(value):
                raise TimeError()

        return parse_time(value)


def get_fhir_type_class(model_name):
    try:
        return globals()[model_name + "Type"]
    except KeyError:
        raise LookupError(f"'{__name__}.{model_name}Type' doesnt found.")


class AbstractType(dict):
    """ """

    __fhir_release__: str = "R4"
    __resource_type__: str = ...  # type: ignore

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type=cls.__resource_type__)

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        from . import fhirtypesvalidators

        yield getattr(fhirtypesvalidators, cls.__resource_type__.lower() + "_validator")

    @classmethod
    def is_primitive(cls) -> bool:
        """ """
        return False

    @classmethod
    def fhir_type_name(cls) -> str:
        """ """
        return cls.__resource_type__


class FHIRPrimitiveExtensionType(AbstractType):
    """ """

    __resource_type__ = "FHIRPrimitiveExtension"


class AbstractBaseType(dict):
    """ """

    __fhir_release__: str = "R4"
    __resource_type__: str = ...  # type: ignore

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type=cls.__resource_type__)

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        yield cls.validate

    @classmethod
    def validate(cls, v, values, config, field):
        """ """
        if isinstance(v, (bytes, str)):
            input_data = load_str_bytes(v)
            resource_type = input_data.get("resourceType", None)
        elif isinstance(v, FHIRAbstractModel):
            resource_type = v.resource_type
        else:
            resource_type = v.get("resourceType", None)

        if resource_type is None or resource_type == cls.__resource_type__:
            from . import fhirtypesvalidators

            v = getattr(
                fhirtypesvalidators, cls.__resource_type__.lower() + "_validator"
            )(v)
            return v

        type_class = get_fhir_type_class(resource_type)
        v = run_validator_for_fhir_type(type_class, v, values, config, field)
        return v

    @classmethod
    def is_primitive(cls) -> bool:
        """ """
        return False

    @classmethod
    def fhir_type_name(cls) -> str:
        """ """
        return cls.__resource_type__


class ElementType(AbstractBaseType):
    """ """

    __resource_type__ = "Element"


class ResourceType(AbstractBaseType):
    """ """

    __resource_type__ = "Resource"


class AccountType(AbstractType):
    __resource_type__ = "Account"


class AccountCoverageType(AbstractType):
    __resource_type__ = "AccountCoverage"


class AccountGuarantorType(AbstractType):
    __resource_type__ = "AccountGuarantor"


class ActivityDefinitionType(AbstractType):
    __resource_type__ = "ActivityDefinition"


class ActivityDefinitionDynamicValueType(AbstractType):
    __resource_type__ = "ActivityDefinitionDynamicValue"


class ActivityDefinitionParticipantType(AbstractType):
    __resource_type__ = "ActivityDefinitionParticipant"


class AddressType(AbstractType):
    __resource_type__ = "Address"


class AdverseEventType(AbstractType):
    __resource_type__ = "AdverseEvent"


class AdverseEventSuspectEntityType(AbstractType):
    __resource_type__ = "AdverseEventSuspectEntity"


class AdverseEventSuspectEntityCausalityType(AbstractType):
    __resource_type__ = "AdverseEventSuspectEntityCausality"


class AgeType(AbstractType):
    __resource_type__ = "Age"


class AllergyIntoleranceType(AbstractType):
    __resource_type__ = "AllergyIntolerance"


class AllergyIntoleranceReactionType(AbstractType):
    __resource_type__ = "AllergyIntoleranceReaction"


class AnnotationType(AbstractType):
    __resource_type__ = "Annotation"


class AppointmentType(AbstractType):
    __resource_type__ = "Appointment"


class AppointmentParticipantType(AbstractType):
    __resource_type__ = "AppointmentParticipant"


class AppointmentResponseType(AbstractType):
    __resource_type__ = "AppointmentResponse"


class AttachmentType(AbstractType):
    __resource_type__ = "Attachment"


class AuditEventType(AbstractType):
    __resource_type__ = "AuditEvent"


class AuditEventAgentType(AbstractType):
    __resource_type__ = "AuditEventAgent"


class AuditEventAgentNetworkType(AbstractType):
    __resource_type__ = "AuditEventAgentNetwork"


class AuditEventEntityType(AbstractType):
    __resource_type__ = "AuditEventEntity"


class AuditEventEntityDetailType(AbstractType):
    __resource_type__ = "AuditEventEntityDetail"


class AuditEventSourceType(AbstractType):
    __resource_type__ = "AuditEventSource"


class BackboneElementType(AbstractType):
    __resource_type__ = "BackboneElement"


class BasicType(AbstractType):
    __resource_type__ = "Basic"


class BinaryType(AbstractType):
    __resource_type__ = "Binary"


class BiologicallyDerivedProductType(AbstractType):
    __resource_type__ = "BiologicallyDerivedProduct"


class BiologicallyDerivedProductCollectionType(AbstractType):
    __resource_type__ = "BiologicallyDerivedProductCollection"


class BiologicallyDerivedProductManipulationType(AbstractType):
    __resource_type__ = "BiologicallyDerivedProductManipulation"


class BiologicallyDerivedProductProcessingType(AbstractType):
    __resource_type__ = "BiologicallyDerivedProductProcessing"


class BiologicallyDerivedProductStorageType(AbstractType):
    __resource_type__ = "BiologicallyDerivedProductStorage"


class BodyStructureType(AbstractType):
    __resource_type__ = "BodyStructure"


class BundleType(AbstractType):
    __resource_type__ = "Bundle"


class BundleEntryType(AbstractType):
    __resource_type__ = "BundleEntry"


class BundleEntryRequestType(AbstractType):
    __resource_type__ = "BundleEntryRequest"


class BundleEntryResponseType(AbstractType):
    __resource_type__ = "BundleEntryResponse"


class BundleEntrySearchType(AbstractType):
    __resource_type__ = "BundleEntrySearch"


class BundleLinkType(AbstractType):
    __resource_type__ = "BundleLink"


class CapabilityStatementType(AbstractType):
    __resource_type__ = "CapabilityStatement"


class CapabilityStatementDocumentType(AbstractType):
    __resource_type__ = "CapabilityStatementDocument"


class CapabilityStatementImplementationType(AbstractType):
    __resource_type__ = "CapabilityStatementImplementation"


class CapabilityStatementMessagingType(AbstractType):
    __resource_type__ = "CapabilityStatementMessaging"


class CapabilityStatementMessagingEndpointType(AbstractType):
    __resource_type__ = "CapabilityStatementMessagingEndpoint"


class CapabilityStatementMessagingSupportedMessageType(AbstractType):
    __resource_type__ = "CapabilityStatementMessagingSupportedMessage"


class CapabilityStatementRestType(AbstractType):
    __resource_type__ = "CapabilityStatementRest"


class CapabilityStatementRestInteractionType(AbstractType):
    __resource_type__ = "CapabilityStatementRestInteraction"


class CapabilityStatementRestResourceType(AbstractType):
    __resource_type__ = "CapabilityStatementRestResource"


class CapabilityStatementRestResourceInteractionType(AbstractType):
    __resource_type__ = "CapabilityStatementRestResourceInteraction"


class CapabilityStatementRestResourceOperationType(AbstractType):
    __resource_type__ = "CapabilityStatementRestResourceOperation"


class CapabilityStatementRestResourceSearchParamType(AbstractType):
    __resource_type__ = "CapabilityStatementRestResourceSearchParam"


class CapabilityStatementRestSecurityType(AbstractType):
    __resource_type__ = "CapabilityStatementRestSecurity"


class CapabilityStatementSoftwareType(AbstractType):
    __resource_type__ = "CapabilityStatementSoftware"


class CarePlanType(AbstractType):
    __resource_type__ = "CarePlan"


class CarePlanActivityType(AbstractType):
    __resource_type__ = "CarePlanActivity"


class CarePlanActivityDetailType(AbstractType):
    __resource_type__ = "CarePlanActivityDetail"


class CareTeamType(AbstractType):
    __resource_type__ = "CareTeam"


class CareTeamParticipantType(AbstractType):
    __resource_type__ = "CareTeamParticipant"


class CatalogEntryType(AbstractType):
    __resource_type__ = "CatalogEntry"


class CatalogEntryRelatedEntryType(AbstractType):
    __resource_type__ = "CatalogEntryRelatedEntry"


class ChargeItemType(AbstractType):
    __resource_type__ = "ChargeItem"


class ChargeItemDefinitionType(AbstractType):
    __resource_type__ = "ChargeItemDefinition"


class ChargeItemDefinitionApplicabilityType(AbstractType):
    __resource_type__ = "ChargeItemDefinitionApplicability"


class ChargeItemDefinitionPropertyGroupType(AbstractType):
    __resource_type__ = "ChargeItemDefinitionPropertyGroup"


class ChargeItemDefinitionPropertyGroupPriceComponentType(AbstractType):
    __resource_type__ = "ChargeItemDefinitionPropertyGroupPriceComponent"


class ChargeItemPerformerType(AbstractType):
    __resource_type__ = "ChargeItemPerformer"


class ClaimType(AbstractType):
    __resource_type__ = "Claim"


class ClaimAccidentType(AbstractType):
    __resource_type__ = "ClaimAccident"


class ClaimCareTeamType(AbstractType):
    __resource_type__ = "ClaimCareTeam"


class ClaimDiagnosisType(AbstractType):
    __resource_type__ = "ClaimDiagnosis"


class ClaimInsuranceType(AbstractType):
    __resource_type__ = "ClaimInsurance"


class ClaimItemType(AbstractType):
    __resource_type__ = "ClaimItem"


class ClaimItemDetailType(AbstractType):
    __resource_type__ = "ClaimItemDetail"


class ClaimItemDetailSubDetailType(AbstractType):
    __resource_type__ = "ClaimItemDetailSubDetail"


class ClaimPayeeType(AbstractType):
    __resource_type__ = "ClaimPayee"


class ClaimProcedureType(AbstractType):
    __resource_type__ = "ClaimProcedure"


class ClaimRelatedType(AbstractType):
    __resource_type__ = "ClaimRelated"


class ClaimResponseType(AbstractType):
    __resource_type__ = "ClaimResponse"


class ClaimResponseAddItemType(AbstractType):
    __resource_type__ = "ClaimResponseAddItem"


class ClaimResponseAddItemDetailType(AbstractType):
    __resource_type__ = "ClaimResponseAddItemDetail"


class ClaimResponseAddItemDetailSubDetailType(AbstractType):
    __resource_type__ = "ClaimResponseAddItemDetailSubDetail"


class ClaimResponseErrorType(AbstractType):
    __resource_type__ = "ClaimResponseError"


class ClaimResponseInsuranceType(AbstractType):
    __resource_type__ = "ClaimResponseInsurance"


class ClaimResponseItemType(AbstractType):
    __resource_type__ = "ClaimResponseItem"


class ClaimResponseItemAdjudicationType(AbstractType):
    __resource_type__ = "ClaimResponseItemAdjudication"


class ClaimResponseItemDetailType(AbstractType):
    __resource_type__ = "ClaimResponseItemDetail"


class ClaimResponseItemDetailSubDetailType(AbstractType):
    __resource_type__ = "ClaimResponseItemDetailSubDetail"


class ClaimResponsePaymentType(AbstractType):
    __resource_type__ = "ClaimResponsePayment"


class ClaimResponseProcessNoteType(AbstractType):
    __resource_type__ = "ClaimResponseProcessNote"


class ClaimResponseTotalType(AbstractType):
    __resource_type__ = "ClaimResponseTotal"


class ClaimSupportingInfoType(AbstractType):
    __resource_type__ = "ClaimSupportingInfo"


class ClinicalImpressionType(AbstractType):
    __resource_type__ = "ClinicalImpression"


class ClinicalImpressionFindingType(AbstractType):
    __resource_type__ = "ClinicalImpressionFinding"


class ClinicalImpressionInvestigationType(AbstractType):
    __resource_type__ = "ClinicalImpressionInvestigation"


class CodeSystemType(AbstractType):
    __resource_type__ = "CodeSystem"


class CodeSystemConceptType(AbstractType):
    __resource_type__ = "CodeSystemConcept"


class CodeSystemConceptDesignationType(AbstractType):
    __resource_type__ = "CodeSystemConceptDesignation"


class CodeSystemConceptPropertyType(AbstractType):
    __resource_type__ = "CodeSystemConceptProperty"


class CodeSystemFilterType(AbstractType):
    __resource_type__ = "CodeSystemFilter"


class CodeSystemPropertyType(AbstractType):
    __resource_type__ = "CodeSystemProperty"


class CodeableConceptType(AbstractType):
    __resource_type__ = "CodeableConcept"


class CodingType(AbstractType):
    __resource_type__ = "Coding"


class CommunicationType(AbstractType):
    __resource_type__ = "Communication"


class CommunicationPayloadType(AbstractType):
    __resource_type__ = "CommunicationPayload"


class CommunicationRequestType(AbstractType):
    __resource_type__ = "CommunicationRequest"


class CommunicationRequestPayloadType(AbstractType):
    __resource_type__ = "CommunicationRequestPayload"


class CompartmentDefinitionType(AbstractType):
    __resource_type__ = "CompartmentDefinition"


class CompartmentDefinitionResourceType(AbstractType):
    __resource_type__ = "CompartmentDefinitionResource"


class CompositionType(AbstractType):
    __resource_type__ = "Composition"


class CompositionAttesterType(AbstractType):
    __resource_type__ = "CompositionAttester"


class CompositionEventType(AbstractType):
    __resource_type__ = "CompositionEvent"


class CompositionRelatesToType(AbstractType):
    __resource_type__ = "CompositionRelatesTo"


class CompositionSectionType(AbstractType):
    __resource_type__ = "CompositionSection"


class ConceptMapType(AbstractType):
    __resource_type__ = "ConceptMap"


class ConceptMapGroupType(AbstractType):
    __resource_type__ = "ConceptMapGroup"


class ConceptMapGroupElementType(AbstractType):
    __resource_type__ = "ConceptMapGroupElement"


class ConceptMapGroupElementTargetType(AbstractType):
    __resource_type__ = "ConceptMapGroupElementTarget"


class ConceptMapGroupElementTargetDependsOnType(AbstractType):
    __resource_type__ = "ConceptMapGroupElementTargetDependsOn"


class ConceptMapGroupUnmappedType(AbstractType):
    __resource_type__ = "ConceptMapGroupUnmapped"


class ConditionType(AbstractType):
    __resource_type__ = "Condition"


class ConditionEvidenceType(AbstractType):
    __resource_type__ = "ConditionEvidence"


class ConditionStageType(AbstractType):
    __resource_type__ = "ConditionStage"


class ConsentType(AbstractType):
    __resource_type__ = "Consent"


class ConsentPolicyType(AbstractType):
    __resource_type__ = "ConsentPolicy"


class ConsentProvisionType(AbstractType):
    __resource_type__ = "ConsentProvision"


class ConsentProvisionActorType(AbstractType):
    __resource_type__ = "ConsentProvisionActor"


class ConsentProvisionDataType(AbstractType):
    __resource_type__ = "ConsentProvisionData"


class ConsentVerificationType(AbstractType):
    __resource_type__ = "ConsentVerification"


class ContactDetailType(AbstractType):
    __resource_type__ = "ContactDetail"


class ContactPointType(AbstractType):
    __resource_type__ = "ContactPoint"


class ContractType(AbstractType):
    __resource_type__ = "Contract"


class ContractContentDefinitionType(AbstractType):
    __resource_type__ = "ContractContentDefinition"


class ContractFriendlyType(AbstractType):
    __resource_type__ = "ContractFriendly"


class ContractLegalType(AbstractType):
    __resource_type__ = "ContractLegal"


class ContractRuleType(AbstractType):
    __resource_type__ = "ContractRule"


class ContractSignerType(AbstractType):
    __resource_type__ = "ContractSigner"


class ContractTermType(AbstractType):
    __resource_type__ = "ContractTerm"


class ContractTermActionType(AbstractType):
    __resource_type__ = "ContractTermAction"


class ContractTermActionSubjectType(AbstractType):
    __resource_type__ = "ContractTermActionSubject"


class ContractTermAssetType(AbstractType):
    __resource_type__ = "ContractTermAsset"


class ContractTermAssetContextType(AbstractType):
    __resource_type__ = "ContractTermAssetContext"


class ContractTermAssetValuedItemType(AbstractType):
    __resource_type__ = "ContractTermAssetValuedItem"


class ContractTermOfferType(AbstractType):
    __resource_type__ = "ContractTermOffer"


class ContractTermOfferAnswerType(AbstractType):
    __resource_type__ = "ContractTermOfferAnswer"


class ContractTermOfferPartyType(AbstractType):
    __resource_type__ = "ContractTermOfferParty"


class ContractTermSecurityLabelType(AbstractType):
    __resource_type__ = "ContractTermSecurityLabel"


class ContributorType(AbstractType):
    __resource_type__ = "Contributor"


class CountType(AbstractType):
    __resource_type__ = "Count"


class CoverageType(AbstractType):
    __resource_type__ = "Coverage"


class CoverageClassType(AbstractType):
    __resource_type__ = "CoverageClass"


class CoverageCostToBeneficiaryType(AbstractType):
    __resource_type__ = "CoverageCostToBeneficiary"


class CoverageCostToBeneficiaryExceptionType(AbstractType):
    __resource_type__ = "CoverageCostToBeneficiaryException"


class CoverageEligibilityRequestType(AbstractType):
    __resource_type__ = "CoverageEligibilityRequest"


class CoverageEligibilityRequestInsuranceType(AbstractType):
    __resource_type__ = "CoverageEligibilityRequestInsurance"


class CoverageEligibilityRequestItemType(AbstractType):
    __resource_type__ = "CoverageEligibilityRequestItem"


class CoverageEligibilityRequestItemDiagnosisType(AbstractType):
    __resource_type__ = "CoverageEligibilityRequestItemDiagnosis"


class CoverageEligibilityRequestSupportingInfoType(AbstractType):
    __resource_type__ = "CoverageEligibilityRequestSupportingInfo"


class CoverageEligibilityResponseType(AbstractType):
    __resource_type__ = "CoverageEligibilityResponse"


class CoverageEligibilityResponseErrorType(AbstractType):
    __resource_type__ = "CoverageEligibilityResponseError"


class CoverageEligibilityResponseInsuranceType(AbstractType):
    __resource_type__ = "CoverageEligibilityResponseInsurance"


class CoverageEligibilityResponseInsuranceItemType(AbstractType):
    __resource_type__ = "CoverageEligibilityResponseInsuranceItem"


class CoverageEligibilityResponseInsuranceItemBenefitType(AbstractType):
    __resource_type__ = "CoverageEligibilityResponseInsuranceItemBenefit"


class DataRequirementType(AbstractType):
    __resource_type__ = "DataRequirement"


class DataRequirementCodeFilterType(AbstractType):
    __resource_type__ = "DataRequirementCodeFilter"


class DataRequirementDateFilterType(AbstractType):
    __resource_type__ = "DataRequirementDateFilter"


class DataRequirementSortType(AbstractType):
    __resource_type__ = "DataRequirementSort"


class DetectedIssueType(AbstractType):
    __resource_type__ = "DetectedIssue"


class DetectedIssueEvidenceType(AbstractType):
    __resource_type__ = "DetectedIssueEvidence"


class DetectedIssueMitigationType(AbstractType):
    __resource_type__ = "DetectedIssueMitigation"


class DeviceType(AbstractType):
    __resource_type__ = "Device"


class DeviceDefinitionType(AbstractType):
    __resource_type__ = "DeviceDefinition"


class DeviceDefinitionCapabilityType(AbstractType):
    __resource_type__ = "DeviceDefinitionCapability"


class DeviceDefinitionDeviceNameType(AbstractType):
    __resource_type__ = "DeviceDefinitionDeviceName"


class DeviceDefinitionMaterialType(AbstractType):
    __resource_type__ = "DeviceDefinitionMaterial"


class DeviceDefinitionPropertyType(AbstractType):
    __resource_type__ = "DeviceDefinitionProperty"


class DeviceDefinitionSpecializationType(AbstractType):
    __resource_type__ = "DeviceDefinitionSpecialization"


class DeviceDefinitionUdiDeviceIdentifierType(AbstractType):
    __resource_type__ = "DeviceDefinitionUdiDeviceIdentifier"


class DeviceDeviceNameType(AbstractType):
    __resource_type__ = "DeviceDeviceName"


class DeviceMetricType(AbstractType):
    __resource_type__ = "DeviceMetric"


class DeviceMetricCalibrationType(AbstractType):
    __resource_type__ = "DeviceMetricCalibration"


class DevicePropertyType(AbstractType):
    __resource_type__ = "DeviceProperty"


class DeviceRequestType(AbstractType):
    __resource_type__ = "DeviceRequest"


class DeviceRequestParameterType(AbstractType):
    __resource_type__ = "DeviceRequestParameter"


class DeviceSpecializationType(AbstractType):
    __resource_type__ = "DeviceSpecialization"


class DeviceUdiCarrierType(AbstractType):
    __resource_type__ = "DeviceUdiCarrier"


class DeviceUseStatementType(AbstractType):
    __resource_type__ = "DeviceUseStatement"


class DeviceVersionType(AbstractType):
    __resource_type__ = "DeviceVersion"


class DiagnosticReportType(AbstractType):
    __resource_type__ = "DiagnosticReport"


class DiagnosticReportMediaType(AbstractType):
    __resource_type__ = "DiagnosticReportMedia"


class DistanceType(AbstractType):
    __resource_type__ = "Distance"


class DocumentManifestType(AbstractType):
    __resource_type__ = "DocumentManifest"


class DocumentManifestRelatedType(AbstractType):
    __resource_type__ = "DocumentManifestRelated"


class DocumentReferenceType(AbstractType):
    __resource_type__ = "DocumentReference"


class DocumentReferenceContentType(AbstractType):
    __resource_type__ = "DocumentReferenceContent"


class DocumentReferenceContextType(AbstractType):
    __resource_type__ = "DocumentReferenceContext"


class DocumentReferenceRelatesToType(AbstractType):
    __resource_type__ = "DocumentReferenceRelatesTo"


class DomainResourceType(AbstractType):
    __resource_type__ = "DomainResource"


class DosageType(AbstractType):
    __resource_type__ = "Dosage"


class DosageDoseAndRateType(AbstractType):
    __resource_type__ = "DosageDoseAndRate"


class DurationType(AbstractType):
    __resource_type__ = "Duration"


class EffectEvidenceSynthesisType(AbstractType):
    __resource_type__ = "EffectEvidenceSynthesis"


class EffectEvidenceSynthesisCertaintyType(AbstractType):
    __resource_type__ = "EffectEvidenceSynthesisCertainty"


class EffectEvidenceSynthesisCertaintyCertaintySubcomponentType(AbstractType):
    __resource_type__ = "EffectEvidenceSynthesisCertaintyCertaintySubcomponent"


class EffectEvidenceSynthesisEffectEstimateType(AbstractType):
    __resource_type__ = "EffectEvidenceSynthesisEffectEstimate"


class EffectEvidenceSynthesisEffectEstimatePrecisionEstimateType(AbstractType):
    __resource_type__ = "EffectEvidenceSynthesisEffectEstimatePrecisionEstimate"


class EffectEvidenceSynthesisResultsByExposureType(AbstractType):
    __resource_type__ = "EffectEvidenceSynthesisResultsByExposure"


class EffectEvidenceSynthesisSampleSizeType(AbstractType):
    __resource_type__ = "EffectEvidenceSynthesisSampleSize"


class ElementDefinitionType(AbstractType):
    __resource_type__ = "ElementDefinition"


class ElementDefinitionBaseType(AbstractType):
    __resource_type__ = "ElementDefinitionBase"


class ElementDefinitionBindingType(AbstractType):
    __resource_type__ = "ElementDefinitionBinding"


class ElementDefinitionConstraintType(AbstractType):
    __resource_type__ = "ElementDefinitionConstraint"


class ElementDefinitionExampleType(AbstractType):
    __resource_type__ = "ElementDefinitionExample"


class ElementDefinitionMappingType(AbstractType):
    __resource_type__ = "ElementDefinitionMapping"


class ElementDefinitionSlicingType(AbstractType):
    __resource_type__ = "ElementDefinitionSlicing"


class ElementDefinitionSlicingDiscriminatorType(AbstractType):
    __resource_type__ = "ElementDefinitionSlicingDiscriminator"


class ElementDefinitionTypeType(AbstractType):
    __resource_type__ = "ElementDefinitionType"


class EncounterType(AbstractType):
    __resource_type__ = "Encounter"


class EncounterClassHistoryType(AbstractType):
    __resource_type__ = "EncounterClassHistory"


class EncounterDiagnosisType(AbstractType):
    __resource_type__ = "EncounterDiagnosis"


class EncounterHospitalizationType(AbstractType):
    __resource_type__ = "EncounterHospitalization"


class EncounterLocationType(AbstractType):
    __resource_type__ = "EncounterLocation"


class EncounterParticipantType(AbstractType):
    __resource_type__ = "EncounterParticipant"


class EncounterStatusHistoryType(AbstractType):
    __resource_type__ = "EncounterStatusHistory"


class EndpointType(AbstractType):
    __resource_type__ = "Endpoint"


class EnrollmentRequestType(AbstractType):
    __resource_type__ = "EnrollmentRequest"


class EnrollmentResponseType(AbstractType):
    __resource_type__ = "EnrollmentResponse"


class EpisodeOfCareType(AbstractType):
    __resource_type__ = "EpisodeOfCare"


class EpisodeOfCareDiagnosisType(AbstractType):
    __resource_type__ = "EpisodeOfCareDiagnosis"


class EpisodeOfCareStatusHistoryType(AbstractType):
    __resource_type__ = "EpisodeOfCareStatusHistory"


class EventDefinitionType(AbstractType):
    __resource_type__ = "EventDefinition"


class EvidenceType(AbstractType):
    __resource_type__ = "Evidence"


class EvidenceVariableType(AbstractType):
    __resource_type__ = "EvidenceVariable"


class EvidenceVariableCharacteristicType(AbstractType):
    __resource_type__ = "EvidenceVariableCharacteristic"


class ExampleScenarioType(AbstractType):
    __resource_type__ = "ExampleScenario"


class ExampleScenarioActorType(AbstractType):
    __resource_type__ = "ExampleScenarioActor"


class ExampleScenarioInstanceType(AbstractType):
    __resource_type__ = "ExampleScenarioInstance"


class ExampleScenarioInstanceContainedInstanceType(AbstractType):
    __resource_type__ = "ExampleScenarioInstanceContainedInstance"


class ExampleScenarioInstanceVersionType(AbstractType):
    __resource_type__ = "ExampleScenarioInstanceVersion"


class ExampleScenarioProcessType(AbstractType):
    __resource_type__ = "ExampleScenarioProcess"


class ExampleScenarioProcessStepType(AbstractType):
    __resource_type__ = "ExampleScenarioProcessStep"


class ExampleScenarioProcessStepAlternativeType(AbstractType):
    __resource_type__ = "ExampleScenarioProcessStepAlternative"


class ExampleScenarioProcessStepOperationType(AbstractType):
    __resource_type__ = "ExampleScenarioProcessStepOperation"


class ExplanationOfBenefitType(AbstractType):
    __resource_type__ = "ExplanationOfBenefit"


class ExplanationOfBenefitAccidentType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitAccident"


class ExplanationOfBenefitAddItemType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitAddItem"


class ExplanationOfBenefitAddItemDetailType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitAddItemDetail"


class ExplanationOfBenefitAddItemDetailSubDetailType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitAddItemDetailSubDetail"


class ExplanationOfBenefitBenefitBalanceType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitBenefitBalance"


class ExplanationOfBenefitBenefitBalanceFinancialType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitBenefitBalanceFinancial"


class ExplanationOfBenefitCareTeamType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitCareTeam"


class ExplanationOfBenefitDiagnosisType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitDiagnosis"


class ExplanationOfBenefitInsuranceType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitInsurance"


class ExplanationOfBenefitItemType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitItem"


class ExplanationOfBenefitItemAdjudicationType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitItemAdjudication"


class ExplanationOfBenefitItemDetailType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitItemDetail"


class ExplanationOfBenefitItemDetailSubDetailType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitItemDetailSubDetail"


class ExplanationOfBenefitPayeeType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitPayee"


class ExplanationOfBenefitPaymentType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitPayment"


class ExplanationOfBenefitProcedureType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitProcedure"


class ExplanationOfBenefitProcessNoteType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitProcessNote"


class ExplanationOfBenefitRelatedType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitRelated"


class ExplanationOfBenefitSupportingInfoType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitSupportingInfo"


class ExplanationOfBenefitTotalType(AbstractType):
    __resource_type__ = "ExplanationOfBenefitTotal"


class ExpressionType(AbstractType):
    __resource_type__ = "Expression"


class ExtensionType(AbstractType):
    __resource_type__ = "Extension"


class FamilyMemberHistoryType(AbstractType):
    __resource_type__ = "FamilyMemberHistory"


class FamilyMemberHistoryConditionType(AbstractType):
    __resource_type__ = "FamilyMemberHistoryCondition"


class FlagType(AbstractType):
    __resource_type__ = "Flag"


class GoalType(AbstractType):
    __resource_type__ = "Goal"


class GoalTargetType(AbstractType):
    __resource_type__ = "GoalTarget"


class GraphDefinitionType(AbstractType):
    __resource_type__ = "GraphDefinition"


class GraphDefinitionLinkType(AbstractType):
    __resource_type__ = "GraphDefinitionLink"


class GraphDefinitionLinkTargetType(AbstractType):
    __resource_type__ = "GraphDefinitionLinkTarget"


class GraphDefinitionLinkTargetCompartmentType(AbstractType):
    __resource_type__ = "GraphDefinitionLinkTargetCompartment"


class GroupType(AbstractType):
    __resource_type__ = "Group"


class GroupCharacteristicType(AbstractType):
    __resource_type__ = "GroupCharacteristic"


class GroupMemberType(AbstractType):
    __resource_type__ = "GroupMember"


class GuidanceResponseType(AbstractType):
    __resource_type__ = "GuidanceResponse"


class HealthcareServiceType(AbstractType):
    __resource_type__ = "HealthcareService"


class HealthcareServiceAvailableTimeType(AbstractType):
    __resource_type__ = "HealthcareServiceAvailableTime"


class HealthcareServiceEligibilityType(AbstractType):
    __resource_type__ = "HealthcareServiceEligibility"


class HealthcareServiceNotAvailableType(AbstractType):
    __resource_type__ = "HealthcareServiceNotAvailable"


class HumanNameType(AbstractType):
    __resource_type__ = "HumanName"


class IdentifierType(AbstractType):
    __resource_type__ = "Identifier"


class ImagingStudyType(AbstractType):
    __resource_type__ = "ImagingStudy"


class ImagingStudySeriesType(AbstractType):
    __resource_type__ = "ImagingStudySeries"


class ImagingStudySeriesInstanceType(AbstractType):
    __resource_type__ = "ImagingStudySeriesInstance"


class ImagingStudySeriesPerformerType(AbstractType):
    __resource_type__ = "ImagingStudySeriesPerformer"


class ImmunizationType(AbstractType):
    __resource_type__ = "Immunization"


class ImmunizationEducationType(AbstractType):
    __resource_type__ = "ImmunizationEducation"


class ImmunizationEvaluationType(AbstractType):
    __resource_type__ = "ImmunizationEvaluation"


class ImmunizationPerformerType(AbstractType):
    __resource_type__ = "ImmunizationPerformer"


class ImmunizationProtocolAppliedType(AbstractType):
    __resource_type__ = "ImmunizationProtocolApplied"


class ImmunizationReactionType(AbstractType):
    __resource_type__ = "ImmunizationReaction"


class ImmunizationRecommendationType(AbstractType):
    __resource_type__ = "ImmunizationRecommendation"


class ImmunizationRecommendationRecommendationType(AbstractType):
    __resource_type__ = "ImmunizationRecommendationRecommendation"


class ImmunizationRecommendationRecommendationDateCriterionType(AbstractType):
    __resource_type__ = "ImmunizationRecommendationRecommendationDateCriterion"


class ImplementationGuideType(AbstractType):
    __resource_type__ = "ImplementationGuide"


class ImplementationGuideDefinitionType(AbstractType):
    __resource_type__ = "ImplementationGuideDefinition"


class ImplementationGuideDefinitionGroupingType(AbstractType):
    __resource_type__ = "ImplementationGuideDefinitionGrouping"


class ImplementationGuideDefinitionPageType(AbstractType):
    __resource_type__ = "ImplementationGuideDefinitionPage"


class ImplementationGuideDefinitionParameterType(AbstractType):
    __resource_type__ = "ImplementationGuideDefinitionParameter"


class ImplementationGuideDefinitionResourceType(AbstractType):
    __resource_type__ = "ImplementationGuideDefinitionResource"


class ImplementationGuideDefinitionTemplateType(AbstractType):
    __resource_type__ = "ImplementationGuideDefinitionTemplate"


class ImplementationGuideDependsOnType(AbstractType):
    __resource_type__ = "ImplementationGuideDependsOn"


class ImplementationGuideGlobalType(AbstractType):
    __resource_type__ = "ImplementationGuideGlobal"


class ImplementationGuideManifestType(AbstractType):
    __resource_type__ = "ImplementationGuideManifest"


class ImplementationGuideManifestPageType(AbstractType):
    __resource_type__ = "ImplementationGuideManifestPage"


class ImplementationGuideManifestResourceType(AbstractType):
    __resource_type__ = "ImplementationGuideManifestResource"


class InsurancePlanType(AbstractType):
    __resource_type__ = "InsurancePlan"


class InsurancePlanContactType(AbstractType):
    __resource_type__ = "InsurancePlanContact"


class InsurancePlanCoverageType(AbstractType):
    __resource_type__ = "InsurancePlanCoverage"


class InsurancePlanCoverageBenefitType(AbstractType):
    __resource_type__ = "InsurancePlanCoverageBenefit"


class InsurancePlanCoverageBenefitLimitType(AbstractType):
    __resource_type__ = "InsurancePlanCoverageBenefitLimit"


class InsurancePlanPlanType(AbstractType):
    __resource_type__ = "InsurancePlanPlan"


class InsurancePlanPlanGeneralCostType(AbstractType):
    __resource_type__ = "InsurancePlanPlanGeneralCost"


class InsurancePlanPlanSpecificCostType(AbstractType):
    __resource_type__ = "InsurancePlanPlanSpecificCost"


class InsurancePlanPlanSpecificCostBenefitType(AbstractType):
    __resource_type__ = "InsurancePlanPlanSpecificCostBenefit"


class InsurancePlanPlanSpecificCostBenefitCostType(AbstractType):
    __resource_type__ = "InsurancePlanPlanSpecificCostBenefitCost"


class InvoiceType(AbstractType):
    __resource_type__ = "Invoice"


class InvoiceLineItemType(AbstractType):
    __resource_type__ = "InvoiceLineItem"


class InvoiceLineItemPriceComponentType(AbstractType):
    __resource_type__ = "InvoiceLineItemPriceComponent"


class InvoiceParticipantType(AbstractType):
    __resource_type__ = "InvoiceParticipant"


class LibraryType(AbstractType):
    __resource_type__ = "Library"


class LinkageType(AbstractType):
    __resource_type__ = "Linkage"


class LinkageItemType(AbstractType):
    __resource_type__ = "LinkageItem"


class ListType(AbstractType):
    __resource_type__ = "List"


class ListEntryType(AbstractType):
    __resource_type__ = "ListEntry"


class LocationType(AbstractType):
    __resource_type__ = "Location"


class LocationHoursOfOperationType(AbstractType):
    __resource_type__ = "LocationHoursOfOperation"


class LocationPositionType(AbstractType):
    __resource_type__ = "LocationPosition"


class MarketingStatusType(AbstractType):
    __resource_type__ = "MarketingStatus"


class MeasureType(AbstractType):
    __resource_type__ = "Measure"


class MeasureGroupType(AbstractType):
    __resource_type__ = "MeasureGroup"


class MeasureGroupPopulationType(AbstractType):
    __resource_type__ = "MeasureGroupPopulation"


class MeasureGroupStratifierType(AbstractType):
    __resource_type__ = "MeasureGroupStratifier"


class MeasureGroupStratifierComponentType(AbstractType):
    __resource_type__ = "MeasureGroupStratifierComponent"


class MeasureReportType(AbstractType):
    __resource_type__ = "MeasureReport"


class MeasureReportGroupType(AbstractType):
    __resource_type__ = "MeasureReportGroup"


class MeasureReportGroupPopulationType(AbstractType):
    __resource_type__ = "MeasureReportGroupPopulation"


class MeasureReportGroupStratifierType(AbstractType):
    __resource_type__ = "MeasureReportGroupStratifier"


class MeasureReportGroupStratifierStratumType(AbstractType):
    __resource_type__ = "MeasureReportGroupStratifierStratum"


class MeasureReportGroupStratifierStratumComponentType(AbstractType):
    __resource_type__ = "MeasureReportGroupStratifierStratumComponent"


class MeasureReportGroupStratifierStratumPopulationType(AbstractType):
    __resource_type__ = "MeasureReportGroupStratifierStratumPopulation"


class MeasureSupplementalDataType(AbstractType):
    __resource_type__ = "MeasureSupplementalData"


class MediaType(AbstractType):
    __resource_type__ = "Media"


class MedicationType(AbstractType):
    __resource_type__ = "Medication"


class MedicationAdministrationType(AbstractType):
    __resource_type__ = "MedicationAdministration"


class MedicationAdministrationDosageType(AbstractType):
    __resource_type__ = "MedicationAdministrationDosage"


class MedicationAdministrationPerformerType(AbstractType):
    __resource_type__ = "MedicationAdministrationPerformer"


class MedicationBatchType(AbstractType):
    __resource_type__ = "MedicationBatch"


class MedicationDispenseType(AbstractType):
    __resource_type__ = "MedicationDispense"


class MedicationDispensePerformerType(AbstractType):
    __resource_type__ = "MedicationDispensePerformer"


class MedicationDispenseSubstitutionType(AbstractType):
    __resource_type__ = "MedicationDispenseSubstitution"


class MedicationIngredientType(AbstractType):
    __resource_type__ = "MedicationIngredient"


class MedicationKnowledgeType(AbstractType):
    __resource_type__ = "MedicationKnowledge"


class MedicationKnowledgeAdministrationGuidelinesType(AbstractType):
    __resource_type__ = "MedicationKnowledgeAdministrationGuidelines"


class MedicationKnowledgeAdministrationGuidelinesDosageType(AbstractType):
    __resource_type__ = "MedicationKnowledgeAdministrationGuidelinesDosage"


class MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType(
    AbstractType
):
    __resource_type__ = (
        "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics"
    )


class MedicationKnowledgeCostType(AbstractType):
    __resource_type__ = "MedicationKnowledgeCost"


class MedicationKnowledgeDrugCharacteristicType(AbstractType):
    __resource_type__ = "MedicationKnowledgeDrugCharacteristic"


class MedicationKnowledgeIngredientType(AbstractType):
    __resource_type__ = "MedicationKnowledgeIngredient"


class MedicationKnowledgeKineticsType(AbstractType):
    __resource_type__ = "MedicationKnowledgeKinetics"


class MedicationKnowledgeMedicineClassificationType(AbstractType):
    __resource_type__ = "MedicationKnowledgeMedicineClassification"


class MedicationKnowledgeMonitoringProgramType(AbstractType):
    __resource_type__ = "MedicationKnowledgeMonitoringProgram"


class MedicationKnowledgeMonographType(AbstractType):
    __resource_type__ = "MedicationKnowledgeMonograph"


class MedicationKnowledgePackagingType(AbstractType):
    __resource_type__ = "MedicationKnowledgePackaging"


class MedicationKnowledgeRegulatoryType(AbstractType):
    __resource_type__ = "MedicationKnowledgeRegulatory"


class MedicationKnowledgeRegulatoryMaxDispenseType(AbstractType):
    __resource_type__ = "MedicationKnowledgeRegulatoryMaxDispense"


class MedicationKnowledgeRegulatoryScheduleType(AbstractType):
    __resource_type__ = "MedicationKnowledgeRegulatorySchedule"


class MedicationKnowledgeRegulatorySubstitutionType(AbstractType):
    __resource_type__ = "MedicationKnowledgeRegulatorySubstitution"


class MedicationKnowledgeRelatedMedicationKnowledgeType(AbstractType):
    __resource_type__ = "MedicationKnowledgeRelatedMedicationKnowledge"


class MedicationRequestType(AbstractType):
    __resource_type__ = "MedicationRequest"


class MedicationRequestDispenseRequestType(AbstractType):
    __resource_type__ = "MedicationRequestDispenseRequest"


class MedicationRequestDispenseRequestInitialFillType(AbstractType):
    __resource_type__ = "MedicationRequestDispenseRequestInitialFill"


class MedicationRequestSubstitutionType(AbstractType):
    __resource_type__ = "MedicationRequestSubstitution"


class MedicationStatementType(AbstractType):
    __resource_type__ = "MedicationStatement"


class MedicinalProductType(AbstractType):
    __resource_type__ = "MedicinalProduct"


class MedicinalProductAuthorizationType(AbstractType):
    __resource_type__ = "MedicinalProductAuthorization"


class MedicinalProductAuthorizationJurisdictionalAuthorizationType(AbstractType):
    __resource_type__ = "MedicinalProductAuthorizationJurisdictionalAuthorization"


class MedicinalProductAuthorizationProcedureType(AbstractType):
    __resource_type__ = "MedicinalProductAuthorizationProcedure"


class MedicinalProductContraindicationType(AbstractType):
    __resource_type__ = "MedicinalProductContraindication"


class MedicinalProductContraindicationOtherTherapyType(AbstractType):
    __resource_type__ = "MedicinalProductContraindicationOtherTherapy"


class MedicinalProductIndicationType(AbstractType):
    __resource_type__ = "MedicinalProductIndication"


class MedicinalProductIndicationOtherTherapyType(AbstractType):
    __resource_type__ = "MedicinalProductIndicationOtherTherapy"


class MedicinalProductIngredientType(AbstractType):
    __resource_type__ = "MedicinalProductIngredient"


class MedicinalProductIngredientSpecifiedSubstanceType(AbstractType):
    __resource_type__ = "MedicinalProductIngredientSpecifiedSubstance"


class MedicinalProductIngredientSpecifiedSubstanceStrengthType(AbstractType):
    __resource_type__ = "MedicinalProductIngredientSpecifiedSubstanceStrength"


class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrengthType(
    AbstractType
):
    __resource_type__ = (
        "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"
    )


class MedicinalProductIngredientSubstanceType(AbstractType):
    __resource_type__ = "MedicinalProductIngredientSubstance"


class MedicinalProductInteractionType(AbstractType):
    __resource_type__ = "MedicinalProductInteraction"


class MedicinalProductInteractionInteractantType(AbstractType):
    __resource_type__ = "MedicinalProductInteractionInteractant"


class MedicinalProductManufacturedType(AbstractType):
    __resource_type__ = "MedicinalProductManufactured"


class MedicinalProductManufacturingBusinessOperationType(AbstractType):
    __resource_type__ = "MedicinalProductManufacturingBusinessOperation"


class MedicinalProductNameType(AbstractType):
    __resource_type__ = "MedicinalProductName"


class MedicinalProductNameCountryLanguageType(AbstractType):
    __resource_type__ = "MedicinalProductNameCountryLanguage"


class MedicinalProductNameNamePartType(AbstractType):
    __resource_type__ = "MedicinalProductNameNamePart"


class MedicinalProductPackagedType(AbstractType):
    __resource_type__ = "MedicinalProductPackaged"


class MedicinalProductPackagedBatchIdentifierType(AbstractType):
    __resource_type__ = "MedicinalProductPackagedBatchIdentifier"


class MedicinalProductPackagedPackageItemType(AbstractType):
    __resource_type__ = "MedicinalProductPackagedPackageItem"


class MedicinalProductPharmaceuticalType(AbstractType):
    __resource_type__ = "MedicinalProductPharmaceutical"


class MedicinalProductPharmaceuticalCharacteristicsType(AbstractType):
    __resource_type__ = "MedicinalProductPharmaceuticalCharacteristics"


class MedicinalProductPharmaceuticalRouteOfAdministrationType(AbstractType):
    __resource_type__ = "MedicinalProductPharmaceuticalRouteOfAdministration"


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesType(
    AbstractType
):
    __resource_type__ = (
        "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies"
    )


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriodType(
    AbstractType
):
    __resource_type__ = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod"  # noqa:B950


class MedicinalProductSpecialDesignationType(AbstractType):
    __resource_type__ = "MedicinalProductSpecialDesignation"


class MedicinalProductUndesirableEffectType(AbstractType):
    __resource_type__ = "MedicinalProductUndesirableEffect"


class MessageDefinitionType(AbstractType):
    __resource_type__ = "MessageDefinition"


class MessageDefinitionAllowedResponseType(AbstractType):
    __resource_type__ = "MessageDefinitionAllowedResponse"


class MessageDefinitionFocusType(AbstractType):
    __resource_type__ = "MessageDefinitionFocus"


class MessageHeaderType(AbstractType):
    __resource_type__ = "MessageHeader"


class MessageHeaderDestinationType(AbstractType):
    __resource_type__ = "MessageHeaderDestination"


class MessageHeaderResponseType(AbstractType):
    __resource_type__ = "MessageHeaderResponse"


class MessageHeaderSourceType(AbstractType):
    __resource_type__ = "MessageHeaderSource"


class MetaType(AbstractType):
    __resource_type__ = "Meta"


class MetadataResourceType(AbstractType):
    __resource_type__ = "MetadataResource"


class MolecularSequenceType(AbstractType):
    __resource_type__ = "MolecularSequence"


class MolecularSequenceQualityType(AbstractType):
    __resource_type__ = "MolecularSequenceQuality"


class MolecularSequenceQualityRocType(AbstractType):
    __resource_type__ = "MolecularSequenceQualityRoc"


class MolecularSequenceReferenceSeqType(AbstractType):
    __resource_type__ = "MolecularSequenceReferenceSeq"


class MolecularSequenceRepositoryType(AbstractType):
    __resource_type__ = "MolecularSequenceRepository"


class MolecularSequenceStructureVariantType(AbstractType):
    __resource_type__ = "MolecularSequenceStructureVariant"


class MolecularSequenceStructureVariantInnerType(AbstractType):
    __resource_type__ = "MolecularSequenceStructureVariantInner"


class MolecularSequenceStructureVariantOuterType(AbstractType):
    __resource_type__ = "MolecularSequenceStructureVariantOuter"


class MolecularSequenceVariantType(AbstractType):
    __resource_type__ = "MolecularSequenceVariant"


class MoneyType(AbstractType):
    __resource_type__ = "Money"


class NamingSystemType(AbstractType):
    __resource_type__ = "NamingSystem"


class NamingSystemUniqueIdType(AbstractType):
    __resource_type__ = "NamingSystemUniqueId"


class NarrativeType(AbstractType):
    __resource_type__ = "Narrative"


class NutritionOrderType(AbstractType):
    __resource_type__ = "NutritionOrder"


class NutritionOrderEnteralFormulaType(AbstractType):
    __resource_type__ = "NutritionOrderEnteralFormula"


class NutritionOrderEnteralFormulaAdministrationType(AbstractType):
    __resource_type__ = "NutritionOrderEnteralFormulaAdministration"


class NutritionOrderOralDietType(AbstractType):
    __resource_type__ = "NutritionOrderOralDiet"


class NutritionOrderOralDietNutrientType(AbstractType):
    __resource_type__ = "NutritionOrderOralDietNutrient"


class NutritionOrderOralDietTextureType(AbstractType):
    __resource_type__ = "NutritionOrderOralDietTexture"


class NutritionOrderSupplementType(AbstractType):
    __resource_type__ = "NutritionOrderSupplement"


class ObservationType(AbstractType):
    __resource_type__ = "Observation"


class ObservationComponentType(AbstractType):
    __resource_type__ = "ObservationComponent"


class ObservationDefinitionType(AbstractType):
    __resource_type__ = "ObservationDefinition"


class ObservationDefinitionQualifiedIntervalType(AbstractType):
    __resource_type__ = "ObservationDefinitionQualifiedInterval"


class ObservationDefinitionQuantitativeDetailsType(AbstractType):
    __resource_type__ = "ObservationDefinitionQuantitativeDetails"


class ObservationReferenceRangeType(AbstractType):
    __resource_type__ = "ObservationReferenceRange"


class OperationDefinitionType(AbstractType):
    __resource_type__ = "OperationDefinition"


class OperationDefinitionOverloadType(AbstractType):
    __resource_type__ = "OperationDefinitionOverload"


class OperationDefinitionParameterType(AbstractType):
    __resource_type__ = "OperationDefinitionParameter"


class OperationDefinitionParameterBindingType(AbstractType):
    __resource_type__ = "OperationDefinitionParameterBinding"


class OperationDefinitionParameterReferencedFromType(AbstractType):
    __resource_type__ = "OperationDefinitionParameterReferencedFrom"


class OperationOutcomeType(AbstractType):
    __resource_type__ = "OperationOutcome"


class OperationOutcomeIssueType(AbstractType):
    __resource_type__ = "OperationOutcomeIssue"


class OrganizationType(AbstractType):
    __resource_type__ = "Organization"


class OrganizationAffiliationType(AbstractType):
    __resource_type__ = "OrganizationAffiliation"


class OrganizationContactType(AbstractType):
    __resource_type__ = "OrganizationContact"


class ParameterDefinitionType(AbstractType):
    __resource_type__ = "ParameterDefinition"


class ParametersType(AbstractType):
    __resource_type__ = "Parameters"


class ParametersParameterType(AbstractType):
    __resource_type__ = "ParametersParameter"


class PatientType(AbstractType):
    __resource_type__ = "Patient"


class PatientCommunicationType(AbstractType):
    __resource_type__ = "PatientCommunication"


class PatientContactType(AbstractType):
    __resource_type__ = "PatientContact"


class PatientLinkType(AbstractType):
    __resource_type__ = "PatientLink"


class PaymentNoticeType(AbstractType):
    __resource_type__ = "PaymentNotice"


class PaymentReconciliationType(AbstractType):
    __resource_type__ = "PaymentReconciliation"


class PaymentReconciliationDetailType(AbstractType):
    __resource_type__ = "PaymentReconciliationDetail"


class PaymentReconciliationProcessNoteType(AbstractType):
    __resource_type__ = "PaymentReconciliationProcessNote"


class PeriodType(AbstractType):
    __resource_type__ = "Period"


class PersonType(AbstractType):
    __resource_type__ = "Person"


class PersonLinkType(AbstractType):
    __resource_type__ = "PersonLink"


class PlanDefinitionType(AbstractType):
    __resource_type__ = "PlanDefinition"


class PlanDefinitionActionType(AbstractType):
    __resource_type__ = "PlanDefinitionAction"


class PlanDefinitionActionConditionType(AbstractType):
    __resource_type__ = "PlanDefinitionActionCondition"


class PlanDefinitionActionDynamicValueType(AbstractType):
    __resource_type__ = "PlanDefinitionActionDynamicValue"


class PlanDefinitionActionParticipantType(AbstractType):
    __resource_type__ = "PlanDefinitionActionParticipant"


class PlanDefinitionActionRelatedActionType(AbstractType):
    __resource_type__ = "PlanDefinitionActionRelatedAction"


class PlanDefinitionGoalType(AbstractType):
    __resource_type__ = "PlanDefinitionGoal"


class PlanDefinitionGoalTargetType(AbstractType):
    __resource_type__ = "PlanDefinitionGoalTarget"


class PopulationType(AbstractType):
    __resource_type__ = "Population"


class PractitionerType(AbstractType):
    __resource_type__ = "Practitioner"


class PractitionerQualificationType(AbstractType):
    __resource_type__ = "PractitionerQualification"


class PractitionerRoleType(AbstractType):
    __resource_type__ = "PractitionerRole"


class PractitionerRoleAvailableTimeType(AbstractType):
    __resource_type__ = "PractitionerRoleAvailableTime"


class PractitionerRoleNotAvailableType(AbstractType):
    __resource_type__ = "PractitionerRoleNotAvailable"


class ProcedureType(AbstractType):
    __resource_type__ = "Procedure"


class ProcedureFocalDeviceType(AbstractType):
    __resource_type__ = "ProcedureFocalDevice"


class ProcedurePerformerType(AbstractType):
    __resource_type__ = "ProcedurePerformer"


class ProdCharacteristicType(AbstractType):
    __resource_type__ = "ProdCharacteristic"


class ProductShelfLifeType(AbstractType):
    __resource_type__ = "ProductShelfLife"


class ProvenanceType(AbstractType):
    __resource_type__ = "Provenance"


class ProvenanceAgentType(AbstractType):
    __resource_type__ = "ProvenanceAgent"


class ProvenanceEntityType(AbstractType):
    __resource_type__ = "ProvenanceEntity"


class QuantityType(AbstractType):
    __resource_type__ = "Quantity"


class QuestionnaireType(AbstractType):
    __resource_type__ = "Questionnaire"


class QuestionnaireItemType(AbstractType):
    __resource_type__ = "QuestionnaireItem"


class QuestionnaireItemAnswerOptionType(AbstractType):
    __resource_type__ = "QuestionnaireItemAnswerOption"


class QuestionnaireItemEnableWhenType(AbstractType):
    __resource_type__ = "QuestionnaireItemEnableWhen"


class QuestionnaireItemInitialType(AbstractType):
    __resource_type__ = "QuestionnaireItemInitial"


class QuestionnaireResponseType(AbstractType):
    __resource_type__ = "QuestionnaireResponse"


class QuestionnaireResponseItemType(AbstractType):
    __resource_type__ = "QuestionnaireResponseItem"


class QuestionnaireResponseItemAnswerType(AbstractType):
    __resource_type__ = "QuestionnaireResponseItemAnswer"


class RangeType(AbstractType):
    __resource_type__ = "Range"


class RatioType(AbstractType):
    __resource_type__ = "Ratio"


class ReferenceType(AbstractType):
    __resource_type__ = "Reference"


class RelatedArtifactType(AbstractType):
    __resource_type__ = "RelatedArtifact"


class RelatedPersonType(AbstractType):
    __resource_type__ = "RelatedPerson"


class RelatedPersonCommunicationType(AbstractType):
    __resource_type__ = "RelatedPersonCommunication"


class RequestGroupType(AbstractType):
    __resource_type__ = "RequestGroup"


class RequestGroupActionType(AbstractType):
    __resource_type__ = "RequestGroupAction"


class RequestGroupActionConditionType(AbstractType):
    __resource_type__ = "RequestGroupActionCondition"


class RequestGroupActionRelatedActionType(AbstractType):
    __resource_type__ = "RequestGroupActionRelatedAction"


class ResearchDefinitionType(AbstractType):
    __resource_type__ = "ResearchDefinition"


class ResearchElementDefinitionType(AbstractType):
    __resource_type__ = "ResearchElementDefinition"


class ResearchElementDefinitionCharacteristicType(AbstractType):
    __resource_type__ = "ResearchElementDefinitionCharacteristic"


class ResearchStudyType(AbstractType):
    __resource_type__ = "ResearchStudy"


class ResearchStudyArmType(AbstractType):
    __resource_type__ = "ResearchStudyArm"


class ResearchStudyObjectiveType(AbstractType):
    __resource_type__ = "ResearchStudyObjective"


class ResearchSubjectType(AbstractType):
    __resource_type__ = "ResearchSubject"


class RiskAssessmentType(AbstractType):
    __resource_type__ = "RiskAssessment"


class RiskAssessmentPredictionType(AbstractType):
    __resource_type__ = "RiskAssessmentPrediction"


class RiskEvidenceSynthesisType(AbstractType):
    __resource_type__ = "RiskEvidenceSynthesis"


class RiskEvidenceSynthesisCertaintyType(AbstractType):
    __resource_type__ = "RiskEvidenceSynthesisCertainty"


class RiskEvidenceSynthesisCertaintyCertaintySubcomponentType(AbstractType):
    __resource_type__ = "RiskEvidenceSynthesisCertaintyCertaintySubcomponent"


class RiskEvidenceSynthesisRiskEstimateType(AbstractType):
    __resource_type__ = "RiskEvidenceSynthesisRiskEstimate"


class RiskEvidenceSynthesisRiskEstimatePrecisionEstimateType(AbstractType):
    __resource_type__ = "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate"


class RiskEvidenceSynthesisSampleSizeType(AbstractType):
    __resource_type__ = "RiskEvidenceSynthesisSampleSize"


class SampledDataType(AbstractType):
    __resource_type__ = "SampledData"


class ScheduleType(AbstractType):
    __resource_type__ = "Schedule"


class SearchParameterType(AbstractType):
    __resource_type__ = "SearchParameter"


class SearchParameterComponentType(AbstractType):
    __resource_type__ = "SearchParameterComponent"


class ServiceRequestType(AbstractType):
    __resource_type__ = "ServiceRequest"


class SignatureType(AbstractType):
    __resource_type__ = "Signature"


class SlotType(AbstractType):
    __resource_type__ = "Slot"


class SpecimenType(AbstractType):
    __resource_type__ = "Specimen"


class SpecimenCollectionType(AbstractType):
    __resource_type__ = "SpecimenCollection"


class SpecimenContainerType(AbstractType):
    __resource_type__ = "SpecimenContainer"


class SpecimenDefinitionType(AbstractType):
    __resource_type__ = "SpecimenDefinition"


class SpecimenDefinitionTypeTestedType(AbstractType):
    __resource_type__ = "SpecimenDefinitionTypeTested"


class SpecimenDefinitionTypeTestedContainerType(AbstractType):
    __resource_type__ = "SpecimenDefinitionTypeTestedContainer"


class SpecimenDefinitionTypeTestedContainerAdditiveType(AbstractType):
    __resource_type__ = "SpecimenDefinitionTypeTestedContainerAdditive"


class SpecimenDefinitionTypeTestedHandlingType(AbstractType):
    __resource_type__ = "SpecimenDefinitionTypeTestedHandling"


class SpecimenProcessingType(AbstractType):
    __resource_type__ = "SpecimenProcessing"


class StructureDefinitionType(AbstractType):
    __resource_type__ = "StructureDefinition"


class StructureDefinitionContextType(AbstractType):
    __resource_type__ = "StructureDefinitionContext"


class StructureDefinitionDifferentialType(AbstractType):
    __resource_type__ = "StructureDefinitionDifferential"


class StructureDefinitionMappingType(AbstractType):
    __resource_type__ = "StructureDefinitionMapping"


class StructureDefinitionSnapshotType(AbstractType):
    __resource_type__ = "StructureDefinitionSnapshot"


class StructureMapType(AbstractType):
    __resource_type__ = "StructureMap"


class StructureMapGroupType(AbstractType):
    __resource_type__ = "StructureMapGroup"


class StructureMapGroupInputType(AbstractType):
    __resource_type__ = "StructureMapGroupInput"


class StructureMapGroupRuleType(AbstractType):
    __resource_type__ = "StructureMapGroupRule"


class StructureMapGroupRuleDependentType(AbstractType):
    __resource_type__ = "StructureMapGroupRuleDependent"


class StructureMapGroupRuleSourceType(AbstractType):
    __resource_type__ = "StructureMapGroupRuleSource"


class StructureMapGroupRuleTargetType(AbstractType):
    __resource_type__ = "StructureMapGroupRuleTarget"


class StructureMapGroupRuleTargetParameterType(AbstractType):
    __resource_type__ = "StructureMapGroupRuleTargetParameter"


class StructureMapStructureType(AbstractType):
    __resource_type__ = "StructureMapStructure"


class SubscriptionType(AbstractType):
    __resource_type__ = "Subscription"


class SubscriptionChannelType(AbstractType):
    __resource_type__ = "SubscriptionChannel"


class SubstanceType(AbstractType):
    __resource_type__ = "Substance"


class SubstanceAmountType(AbstractType):
    __resource_type__ = "SubstanceAmount"


class SubstanceAmountReferenceRangeType(AbstractType):
    __resource_type__ = "SubstanceAmountReferenceRange"


class SubstanceIngredientType(AbstractType):
    __resource_type__ = "SubstanceIngredient"


class SubstanceInstanceType(AbstractType):
    __resource_type__ = "SubstanceInstance"


class SubstanceNucleicAcidType(AbstractType):
    __resource_type__ = "SubstanceNucleicAcid"


class SubstanceNucleicAcidSubunitType(AbstractType):
    __resource_type__ = "SubstanceNucleicAcidSubunit"


class SubstanceNucleicAcidSubunitLinkageType(AbstractType):
    __resource_type__ = "SubstanceNucleicAcidSubunitLinkage"


class SubstanceNucleicAcidSubunitSugarType(AbstractType):
    __resource_type__ = "SubstanceNucleicAcidSubunitSugar"


class SubstancePolymerType(AbstractType):
    __resource_type__ = "SubstancePolymer"


class SubstancePolymerMonomerSetType(AbstractType):
    __resource_type__ = "SubstancePolymerMonomerSet"


class SubstancePolymerMonomerSetStartingMaterialType(AbstractType):
    __resource_type__ = "SubstancePolymerMonomerSetStartingMaterial"


class SubstancePolymerRepeatType(AbstractType):
    __resource_type__ = "SubstancePolymerRepeat"


class SubstancePolymerRepeatRepeatUnitType(AbstractType):
    __resource_type__ = "SubstancePolymerRepeatRepeatUnit"


class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType(AbstractType):
    __resource_type__ = "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation"


class SubstancePolymerRepeatRepeatUnitStructuralRepresentationType(AbstractType):
    __resource_type__ = "SubstancePolymerRepeatRepeatUnitStructuralRepresentation"


class SubstanceProteinType(AbstractType):
    __resource_type__ = "SubstanceProtein"


class SubstanceProteinSubunitType(AbstractType):
    __resource_type__ = "SubstanceProteinSubunit"


class SubstanceReferenceInformationType(AbstractType):
    __resource_type__ = "SubstanceReferenceInformation"


class SubstanceReferenceInformationClassificationType(AbstractType):
    __resource_type__ = "SubstanceReferenceInformationClassification"


class SubstanceReferenceInformationGeneType(AbstractType):
    __resource_type__ = "SubstanceReferenceInformationGene"


class SubstanceReferenceInformationGeneElementType(AbstractType):
    __resource_type__ = "SubstanceReferenceInformationGeneElement"


class SubstanceReferenceInformationTargetType(AbstractType):
    __resource_type__ = "SubstanceReferenceInformationTarget"


class SubstanceSourceMaterialType(AbstractType):
    __resource_type__ = "SubstanceSourceMaterial"


class SubstanceSourceMaterialFractionDescriptionType(AbstractType):
    __resource_type__ = "SubstanceSourceMaterialFractionDescription"


class SubstanceSourceMaterialOrganismType(AbstractType):
    __resource_type__ = "SubstanceSourceMaterialOrganism"


class SubstanceSourceMaterialOrganismAuthorType(AbstractType):
    __resource_type__ = "SubstanceSourceMaterialOrganismAuthor"


class SubstanceSourceMaterialOrganismHybridType(AbstractType):
    __resource_type__ = "SubstanceSourceMaterialOrganismHybrid"


class SubstanceSourceMaterialOrganismOrganismGeneralType(AbstractType):
    __resource_type__ = "SubstanceSourceMaterialOrganismOrganismGeneral"


class SubstanceSourceMaterialPartDescriptionType(AbstractType):
    __resource_type__ = "SubstanceSourceMaterialPartDescription"


class SubstanceSpecificationType(AbstractType):
    __resource_type__ = "SubstanceSpecification"


class SubstanceSpecificationCodeType(AbstractType):
    __resource_type__ = "SubstanceSpecificationCode"


class SubstanceSpecificationMoietyType(AbstractType):
    __resource_type__ = "SubstanceSpecificationMoiety"


class SubstanceSpecificationNameType(AbstractType):
    __resource_type__ = "SubstanceSpecificationName"


class SubstanceSpecificationNameOfficialType(AbstractType):
    __resource_type__ = "SubstanceSpecificationNameOfficial"


class SubstanceSpecificationPropertyType(AbstractType):
    __resource_type__ = "SubstanceSpecificationProperty"


class SubstanceSpecificationRelationshipType(AbstractType):
    __resource_type__ = "SubstanceSpecificationRelationship"


class SubstanceSpecificationStructureType(AbstractType):
    __resource_type__ = "SubstanceSpecificationStructure"


class SubstanceSpecificationStructureIsotopeType(AbstractType):
    __resource_type__ = "SubstanceSpecificationStructureIsotope"


class SubstanceSpecificationStructureIsotopeMolecularWeightType(AbstractType):
    __resource_type__ = "SubstanceSpecificationStructureIsotopeMolecularWeight"


class SubstanceSpecificationStructureRepresentationType(AbstractType):
    __resource_type__ = "SubstanceSpecificationStructureRepresentation"


class SupplyDeliveryType(AbstractType):
    __resource_type__ = "SupplyDelivery"


class SupplyDeliverySuppliedItemType(AbstractType):
    __resource_type__ = "SupplyDeliverySuppliedItem"


class SupplyRequestType(AbstractType):
    __resource_type__ = "SupplyRequest"


class SupplyRequestParameterType(AbstractType):
    __resource_type__ = "SupplyRequestParameter"


class TaskType(AbstractType):
    __resource_type__ = "Task"


class TaskInputType(AbstractType):
    __resource_type__ = "TaskInput"


class TaskOutputType(AbstractType):
    __resource_type__ = "TaskOutput"


class TaskRestrictionType(AbstractType):
    __resource_type__ = "TaskRestriction"


class TerminologyCapabilitiesType(AbstractType):
    __resource_type__ = "TerminologyCapabilities"


class TerminologyCapabilitiesClosureType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesClosure"


class TerminologyCapabilitiesCodeSystemType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesCodeSystem"


class TerminologyCapabilitiesCodeSystemVersionType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesCodeSystemVersion"


class TerminologyCapabilitiesCodeSystemVersionFilterType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesCodeSystemVersionFilter"


class TerminologyCapabilitiesExpansionType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesExpansion"


class TerminologyCapabilitiesExpansionParameterType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesExpansionParameter"


class TerminologyCapabilitiesImplementationType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesImplementation"


class TerminologyCapabilitiesSoftwareType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesSoftware"


class TerminologyCapabilitiesTranslationType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesTranslation"


class TerminologyCapabilitiesValidateCodeType(AbstractType):
    __resource_type__ = "TerminologyCapabilitiesValidateCode"


class TestReportType(AbstractType):
    __resource_type__ = "TestReport"


class TestReportParticipantType(AbstractType):
    __resource_type__ = "TestReportParticipant"


class TestReportSetupType(AbstractType):
    __resource_type__ = "TestReportSetup"


class TestReportSetupActionType(AbstractType):
    __resource_type__ = "TestReportSetupAction"


class TestReportSetupActionAssertType(AbstractType):
    __resource_type__ = "TestReportSetupActionAssert"


class TestReportSetupActionOperationType(AbstractType):
    __resource_type__ = "TestReportSetupActionOperation"


class TestReportTeardownType(AbstractType):
    __resource_type__ = "TestReportTeardown"


class TestReportTeardownActionType(AbstractType):
    __resource_type__ = "TestReportTeardownAction"


class TestReportTestType(AbstractType):
    __resource_type__ = "TestReportTest"


class TestReportTestActionType(AbstractType):
    __resource_type__ = "TestReportTestAction"


class TestScriptType(AbstractType):
    __resource_type__ = "TestScript"


class TestScriptDestinationType(AbstractType):
    __resource_type__ = "TestScriptDestination"


class TestScriptFixtureType(AbstractType):
    __resource_type__ = "TestScriptFixture"


class TestScriptMetadataType(AbstractType):
    __resource_type__ = "TestScriptMetadata"


class TestScriptMetadataCapabilityType(AbstractType):
    __resource_type__ = "TestScriptMetadataCapability"


class TestScriptMetadataLinkType(AbstractType):
    __resource_type__ = "TestScriptMetadataLink"


class TestScriptOriginType(AbstractType):
    __resource_type__ = "TestScriptOrigin"


class TestScriptSetupType(AbstractType):
    __resource_type__ = "TestScriptSetup"


class TestScriptSetupActionType(AbstractType):
    __resource_type__ = "TestScriptSetupAction"


class TestScriptSetupActionAssertType(AbstractType):
    __resource_type__ = "TestScriptSetupActionAssert"


class TestScriptSetupActionOperationType(AbstractType):
    __resource_type__ = "TestScriptSetupActionOperation"


class TestScriptSetupActionOperationRequestHeaderType(AbstractType):
    __resource_type__ = "TestScriptSetupActionOperationRequestHeader"


class TestScriptTeardownType(AbstractType):
    __resource_type__ = "TestScriptTeardown"


class TestScriptTeardownActionType(AbstractType):
    __resource_type__ = "TestScriptTeardownAction"


class TestScriptTestType(AbstractType):
    __resource_type__ = "TestScriptTest"


class TestScriptTestActionType(AbstractType):
    __resource_type__ = "TestScriptTestAction"


class TestScriptVariableType(AbstractType):
    __resource_type__ = "TestScriptVariable"


class TimingType(AbstractType):
    __resource_type__ = "Timing"


class TimingRepeatType(AbstractType):
    __resource_type__ = "TimingRepeat"


class TriggerDefinitionType(AbstractType):
    __resource_type__ = "TriggerDefinition"


class UsageContextType(AbstractType):
    __resource_type__ = "UsageContext"


class ValueSetType(AbstractType):
    __resource_type__ = "ValueSet"


class ValueSetComposeType(AbstractType):
    __resource_type__ = "ValueSetCompose"


class ValueSetComposeIncludeType(AbstractType):
    __resource_type__ = "ValueSetComposeInclude"


class ValueSetComposeIncludeConceptType(AbstractType):
    __resource_type__ = "ValueSetComposeIncludeConcept"


class ValueSetComposeIncludeConceptDesignationType(AbstractType):
    __resource_type__ = "ValueSetComposeIncludeConceptDesignation"


class ValueSetComposeIncludeFilterType(AbstractType):
    __resource_type__ = "ValueSetComposeIncludeFilter"


class ValueSetExpansionType(AbstractType):
    __resource_type__ = "ValueSetExpansion"


class ValueSetExpansionContainsType(AbstractType):
    __resource_type__ = "ValueSetExpansionContains"


class ValueSetExpansionParameterType(AbstractType):
    __resource_type__ = "ValueSetExpansionParameter"


class VerificationResultType(AbstractType):
    __resource_type__ = "VerificationResult"


class VerificationResultAttestationType(AbstractType):
    __resource_type__ = "VerificationResultAttestation"


class VerificationResultPrimarySourceType(AbstractType):
    __resource_type__ = "VerificationResultPrimarySource"


class VerificationResultValidatorType(AbstractType):
    __resource_type__ = "VerificationResultValidator"


class VisionPrescriptionType(AbstractType):
    __resource_type__ = "VisionPrescription"


class VisionPrescriptionLensSpecificationType(AbstractType):
    __resource_type__ = "VisionPrescriptionLensSpecification"


class VisionPrescriptionLensSpecificationPrismType(AbstractType):
    __resource_type__ = "VisionPrescriptionLensSpecificationPrism"


__all__ = [
    "Boolean",
    "String",
    "Base64Binary",
    "Code",
    "Id",
    "Decimal",
    "Integer",
    "UnsignedInt",
    "PositiveInt",
    "Uri",
    "Oid",
    "Uuid",
    "Canonical",
    "Url",
    "Markdown",
    "Xhtml",
    "Date",
    "DateTime",
    "Instant",
    "Time",
    "FHIRPrimitiveExtensionType",
    "ElementType",
    "ResourceType",
    "AccountType",
    "AccountCoverageType",
    "AccountGuarantorType",
    "ActivityDefinitionType",
    "ActivityDefinitionDynamicValueType",
    "ActivityDefinitionParticipantType",
    "AddressType",
    "AdverseEventType",
    "AdverseEventSuspectEntityType",
    "AdverseEventSuspectEntityCausalityType",
    "AgeType",
    "AllergyIntoleranceType",
    "AllergyIntoleranceReactionType",
    "AnnotationType",
    "AppointmentType",
    "AppointmentParticipantType",
    "AppointmentResponseType",
    "AttachmentType",
    "AuditEventType",
    "AuditEventAgentType",
    "AuditEventAgentNetworkType",
    "AuditEventEntityType",
    "AuditEventEntityDetailType",
    "AuditEventSourceType",
    "BackboneElementType",
    "BasicType",
    "BinaryType",
    "BiologicallyDerivedProductType",
    "BiologicallyDerivedProductCollectionType",
    "BiologicallyDerivedProductManipulationType",
    "BiologicallyDerivedProductProcessingType",
    "BiologicallyDerivedProductStorageType",
    "BodyStructureType",
    "BundleType",
    "BundleEntryType",
    "BundleEntryRequestType",
    "BundleEntryResponseType",
    "BundleEntrySearchType",
    "BundleLinkType",
    "CapabilityStatementType",
    "CapabilityStatementDocumentType",
    "CapabilityStatementImplementationType",
    "CapabilityStatementMessagingType",
    "CapabilityStatementMessagingEndpointType",
    "CapabilityStatementMessagingSupportedMessageType",
    "CapabilityStatementRestType",
    "CapabilityStatementRestInteractionType",
    "CapabilityStatementRestResourceType",
    "CapabilityStatementRestResourceInteractionType",
    "CapabilityStatementRestResourceOperationType",
    "CapabilityStatementRestResourceSearchParamType",
    "CapabilityStatementRestSecurityType",
    "CapabilityStatementSoftwareType",
    "CarePlanType",
    "CarePlanActivityType",
    "CarePlanActivityDetailType",
    "CareTeamType",
    "CareTeamParticipantType",
    "CatalogEntryType",
    "CatalogEntryRelatedEntryType",
    "ChargeItemType",
    "ChargeItemDefinitionType",
    "ChargeItemDefinitionApplicabilityType",
    "ChargeItemDefinitionPropertyGroupType",
    "ChargeItemDefinitionPropertyGroupPriceComponentType",
    "ChargeItemPerformerType",
    "ClaimType",
    "ClaimAccidentType",
    "ClaimCareTeamType",
    "ClaimDiagnosisType",
    "ClaimInsuranceType",
    "ClaimItemType",
    "ClaimItemDetailType",
    "ClaimItemDetailSubDetailType",
    "ClaimPayeeType",
    "ClaimProcedureType",
    "ClaimRelatedType",
    "ClaimResponseType",
    "ClaimResponseAddItemType",
    "ClaimResponseAddItemDetailType",
    "ClaimResponseAddItemDetailSubDetailType",
    "ClaimResponseErrorType",
    "ClaimResponseInsuranceType",
    "ClaimResponseItemType",
    "ClaimResponseItemAdjudicationType",
    "ClaimResponseItemDetailType",
    "ClaimResponseItemDetailSubDetailType",
    "ClaimResponsePaymentType",
    "ClaimResponseProcessNoteType",
    "ClaimResponseTotalType",
    "ClaimSupportingInfoType",
    "ClinicalImpressionType",
    "ClinicalImpressionFindingType",
    "ClinicalImpressionInvestigationType",
    "CodeSystemType",
    "CodeSystemConceptType",
    "CodeSystemConceptDesignationType",
    "CodeSystemConceptPropertyType",
    "CodeSystemFilterType",
    "CodeSystemPropertyType",
    "CodeableConceptType",
    "CodingType",
    "CommunicationType",
    "CommunicationPayloadType",
    "CommunicationRequestType",
    "CommunicationRequestPayloadType",
    "CompartmentDefinitionType",
    "CompartmentDefinitionResourceType",
    "CompositionType",
    "CompositionAttesterType",
    "CompositionEventType",
    "CompositionRelatesToType",
    "CompositionSectionType",
    "ConceptMapType",
    "ConceptMapGroupType",
    "ConceptMapGroupElementType",
    "ConceptMapGroupElementTargetType",
    "ConceptMapGroupElementTargetDependsOnType",
    "ConceptMapGroupUnmappedType",
    "ConditionType",
    "ConditionEvidenceType",
    "ConditionStageType",
    "ConsentType",
    "ConsentPolicyType",
    "ConsentProvisionType",
    "ConsentProvisionActorType",
    "ConsentProvisionDataType",
    "ConsentVerificationType",
    "ContactDetailType",
    "ContactPointType",
    "ContractType",
    "ContractContentDefinitionType",
    "ContractFriendlyType",
    "ContractLegalType",
    "ContractRuleType",
    "ContractSignerType",
    "ContractTermType",
    "ContractTermActionType",
    "ContractTermActionSubjectType",
    "ContractTermAssetType",
    "ContractTermAssetContextType",
    "ContractTermAssetValuedItemType",
    "ContractTermOfferType",
    "ContractTermOfferAnswerType",
    "ContractTermOfferPartyType",
    "ContractTermSecurityLabelType",
    "ContributorType",
    "CountType",
    "CoverageType",
    "CoverageClassType",
    "CoverageCostToBeneficiaryType",
    "CoverageCostToBeneficiaryExceptionType",
    "CoverageEligibilityRequestType",
    "CoverageEligibilityRequestInsuranceType",
    "CoverageEligibilityRequestItemType",
    "CoverageEligibilityRequestItemDiagnosisType",
    "CoverageEligibilityRequestSupportingInfoType",
    "CoverageEligibilityResponseType",
    "CoverageEligibilityResponseErrorType",
    "CoverageEligibilityResponseInsuranceType",
    "CoverageEligibilityResponseInsuranceItemType",
    "CoverageEligibilityResponseInsuranceItemBenefitType",
    "DataRequirementType",
    "DataRequirementCodeFilterType",
    "DataRequirementDateFilterType",
    "DataRequirementSortType",
    "DetectedIssueType",
    "DetectedIssueEvidenceType",
    "DetectedIssueMitigationType",
    "DeviceType",
    "DeviceDefinitionType",
    "DeviceDefinitionCapabilityType",
    "DeviceDefinitionDeviceNameType",
    "DeviceDefinitionMaterialType",
    "DeviceDefinitionPropertyType",
    "DeviceDefinitionSpecializationType",
    "DeviceDefinitionUdiDeviceIdentifierType",
    "DeviceDeviceNameType",
    "DeviceMetricType",
    "DeviceMetricCalibrationType",
    "DevicePropertyType",
    "DeviceRequestType",
    "DeviceRequestParameterType",
    "DeviceSpecializationType",
    "DeviceUdiCarrierType",
    "DeviceUseStatementType",
    "DeviceVersionType",
    "DiagnosticReportType",
    "DiagnosticReportMediaType",
    "DistanceType",
    "DocumentManifestType",
    "DocumentManifestRelatedType",
    "DocumentReferenceType",
    "DocumentReferenceContentType",
    "DocumentReferenceContextType",
    "DocumentReferenceRelatesToType",
    "DomainResourceType",
    "DosageType",
    "DosageDoseAndRateType",
    "DurationType",
    "EffectEvidenceSynthesisType",
    "EffectEvidenceSynthesisCertaintyType",
    "EffectEvidenceSynthesisCertaintyCertaintySubcomponentType",
    "EffectEvidenceSynthesisEffectEstimateType",
    "EffectEvidenceSynthesisEffectEstimatePrecisionEstimateType",
    "EffectEvidenceSynthesisResultsByExposureType",
    "EffectEvidenceSynthesisSampleSizeType",
    "ElementDefinitionType",
    "ElementDefinitionBaseType",
    "ElementDefinitionBindingType",
    "ElementDefinitionConstraintType",
    "ElementDefinitionExampleType",
    "ElementDefinitionMappingType",
    "ElementDefinitionSlicingType",
    "ElementDefinitionSlicingDiscriminatorType",
    "ElementDefinitionTypeType",
    "EncounterType",
    "EncounterClassHistoryType",
    "EncounterDiagnosisType",
    "EncounterHospitalizationType",
    "EncounterLocationType",
    "EncounterParticipantType",
    "EncounterStatusHistoryType",
    "EndpointType",
    "EnrollmentRequestType",
    "EnrollmentResponseType",
    "EpisodeOfCareType",
    "EpisodeOfCareDiagnosisType",
    "EpisodeOfCareStatusHistoryType",
    "EventDefinitionType",
    "EvidenceType",
    "EvidenceVariableType",
    "EvidenceVariableCharacteristicType",
    "ExampleScenarioType",
    "ExampleScenarioActorType",
    "ExampleScenarioInstanceType",
    "ExampleScenarioInstanceContainedInstanceType",
    "ExampleScenarioInstanceVersionType",
    "ExampleScenarioProcessType",
    "ExampleScenarioProcessStepType",
    "ExampleScenarioProcessStepAlternativeType",
    "ExampleScenarioProcessStepOperationType",
    "ExplanationOfBenefitType",
    "ExplanationOfBenefitAccidentType",
    "ExplanationOfBenefitAddItemType",
    "ExplanationOfBenefitAddItemDetailType",
    "ExplanationOfBenefitAddItemDetailSubDetailType",
    "ExplanationOfBenefitBenefitBalanceType",
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "ExplanationOfBenefitCareTeamType",
    "ExplanationOfBenefitDiagnosisType",
    "ExplanationOfBenefitInsuranceType",
    "ExplanationOfBenefitItemType",
    "ExplanationOfBenefitItemAdjudicationType",
    "ExplanationOfBenefitItemDetailType",
    "ExplanationOfBenefitItemDetailSubDetailType",
    "ExplanationOfBenefitPayeeType",
    "ExplanationOfBenefitPaymentType",
    "ExplanationOfBenefitProcedureType",
    "ExplanationOfBenefitProcessNoteType",
    "ExplanationOfBenefitRelatedType",
    "ExplanationOfBenefitSupportingInfoType",
    "ExplanationOfBenefitTotalType",
    "ExpressionType",
    "ExtensionType",
    "FamilyMemberHistoryType",
    "FamilyMemberHistoryConditionType",
    "FlagType",
    "GoalType",
    "GoalTargetType",
    "GraphDefinitionType",
    "GraphDefinitionLinkType",
    "GraphDefinitionLinkTargetType",
    "GraphDefinitionLinkTargetCompartmentType",
    "GroupType",
    "GroupCharacteristicType",
    "GroupMemberType",
    "GuidanceResponseType",
    "HealthcareServiceType",
    "HealthcareServiceAvailableTimeType",
    "HealthcareServiceEligibilityType",
    "HealthcareServiceNotAvailableType",
    "HumanNameType",
    "IdentifierType",
    "ImagingStudyType",
    "ImagingStudySeriesType",
    "ImagingStudySeriesInstanceType",
    "ImagingStudySeriesPerformerType",
    "ImmunizationType",
    "ImmunizationEducationType",
    "ImmunizationEvaluationType",
    "ImmunizationPerformerType",
    "ImmunizationProtocolAppliedType",
    "ImmunizationReactionType",
    "ImmunizationRecommendationType",
    "ImmunizationRecommendationRecommendationType",
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "ImplementationGuideType",
    "ImplementationGuideDefinitionType",
    "ImplementationGuideDefinitionGroupingType",
    "ImplementationGuideDefinitionPageType",
    "ImplementationGuideDefinitionParameterType",
    "ImplementationGuideDefinitionResourceType",
    "ImplementationGuideDefinitionTemplateType",
    "ImplementationGuideDependsOnType",
    "ImplementationGuideGlobalType",
    "ImplementationGuideManifestType",
    "ImplementationGuideManifestPageType",
    "ImplementationGuideManifestResourceType",
    "InsurancePlanType",
    "InsurancePlanContactType",
    "InsurancePlanCoverageType",
    "InsurancePlanCoverageBenefitType",
    "InsurancePlanCoverageBenefitLimitType",
    "InsurancePlanPlanType",
    "InsurancePlanPlanGeneralCostType",
    "InsurancePlanPlanSpecificCostType",
    "InsurancePlanPlanSpecificCostBenefitType",
    "InsurancePlanPlanSpecificCostBenefitCostType",
    "InvoiceType",
    "InvoiceLineItemType",
    "InvoiceLineItemPriceComponentType",
    "InvoiceParticipantType",
    "LibraryType",
    "LinkageType",
    "LinkageItemType",
    "ListType",
    "ListEntryType",
    "LocationType",
    "LocationHoursOfOperationType",
    "LocationPositionType",
    "MarketingStatusType",
    "MeasureType",
    "MeasureGroupType",
    "MeasureGroupPopulationType",
    "MeasureGroupStratifierType",
    "MeasureGroupStratifierComponentType",
    "MeasureReportType",
    "MeasureReportGroupType",
    "MeasureReportGroupPopulationType",
    "MeasureReportGroupStratifierType",
    "MeasureReportGroupStratifierStratumType",
    "MeasureReportGroupStratifierStratumComponentType",
    "MeasureReportGroupStratifierStratumPopulationType",
    "MeasureSupplementalDataType",
    "MediaType",
    "MedicationType",
    "MedicationAdministrationType",
    "MedicationAdministrationDosageType",
    "MedicationAdministrationPerformerType",
    "MedicationBatchType",
    "MedicationDispenseType",
    "MedicationDispensePerformerType",
    "MedicationDispenseSubstitutionType",
    "MedicationIngredientType",
    "MedicationKnowledgeType",
    "MedicationKnowledgeAdministrationGuidelinesType",
    "MedicationKnowledgeAdministrationGuidelinesDosageType",
    "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType",
    "MedicationKnowledgeCostType",
    "MedicationKnowledgeDrugCharacteristicType",
    "MedicationKnowledgeIngredientType",
    "MedicationKnowledgeKineticsType",
    "MedicationKnowledgeMedicineClassificationType",
    "MedicationKnowledgeMonitoringProgramType",
    "MedicationKnowledgeMonographType",
    "MedicationKnowledgePackagingType",
    "MedicationKnowledgeRegulatoryType",
    "MedicationKnowledgeRegulatoryMaxDispenseType",
    "MedicationKnowledgeRegulatoryScheduleType",
    "MedicationKnowledgeRegulatorySubstitutionType",
    "MedicationKnowledgeRelatedMedicationKnowledgeType",
    "MedicationRequestType",
    "MedicationRequestDispenseRequestType",
    "MedicationRequestDispenseRequestInitialFillType",
    "MedicationRequestSubstitutionType",
    "MedicationStatementType",
    "MedicinalProductType",
    "MedicinalProductAuthorizationType",
    "MedicinalProductAuthorizationJurisdictionalAuthorizationType",
    "MedicinalProductAuthorizationProcedureType",
    "MedicinalProductContraindicationType",
    "MedicinalProductContraindicationOtherTherapyType",
    "MedicinalProductIndicationType",
    "MedicinalProductIndicationOtherTherapyType",
    "MedicinalProductIngredientType",
    "MedicinalProductIngredientSpecifiedSubstanceType",
    "MedicinalProductIngredientSpecifiedSubstanceStrengthType",
    "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrengthType",
    "MedicinalProductIngredientSubstanceType",
    "MedicinalProductInteractionType",
    "MedicinalProductInteractionInteractantType",
    "MedicinalProductManufacturedType",
    "MedicinalProductManufacturingBusinessOperationType",
    "MedicinalProductNameType",
    "MedicinalProductNameCountryLanguageType",
    "MedicinalProductNameNamePartType",
    "MedicinalProductPackagedType",
    "MedicinalProductPackagedBatchIdentifierType",
    "MedicinalProductPackagedPackageItemType",
    "MedicinalProductPharmaceuticalType",
    "MedicinalProductPharmaceuticalCharacteristicsType",
    "MedicinalProductPharmaceuticalRouteOfAdministrationType",
    "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesType",
    "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriodType",
    "MedicinalProductSpecialDesignationType",
    "MedicinalProductUndesirableEffectType",
    "MessageDefinitionType",
    "MessageDefinitionAllowedResponseType",
    "MessageDefinitionFocusType",
    "MessageHeaderType",
    "MessageHeaderDestinationType",
    "MessageHeaderResponseType",
    "MessageHeaderSourceType",
    "MetaType",
    "MetadataResourceType",
    "MolecularSequenceType",
    "MolecularSequenceQualityType",
    "MolecularSequenceQualityRocType",
    "MolecularSequenceReferenceSeqType",
    "MolecularSequenceRepositoryType",
    "MolecularSequenceStructureVariantType",
    "MolecularSequenceStructureVariantInnerType",
    "MolecularSequenceStructureVariantOuterType",
    "MolecularSequenceVariantType",
    "MoneyType",
    "NamingSystemType",
    "NamingSystemUniqueIdType",
    "NarrativeType",
    "NutritionOrderType",
    "NutritionOrderEnteralFormulaType",
    "NutritionOrderEnteralFormulaAdministrationType",
    "NutritionOrderOralDietType",
    "NutritionOrderOralDietNutrientType",
    "NutritionOrderOralDietTextureType",
    "NutritionOrderSupplementType",
    "ObservationType",
    "ObservationComponentType",
    "ObservationDefinitionType",
    "ObservationDefinitionQualifiedIntervalType",
    "ObservationDefinitionQuantitativeDetailsType",
    "ObservationReferenceRangeType",
    "OperationDefinitionType",
    "OperationDefinitionOverloadType",
    "OperationDefinitionParameterType",
    "OperationDefinitionParameterBindingType",
    "OperationDefinitionParameterReferencedFromType",
    "OperationOutcomeType",
    "OperationOutcomeIssueType",
    "OrganizationType",
    "OrganizationAffiliationType",
    "OrganizationContactType",
    "ParameterDefinitionType",
    "ParametersType",
    "ParametersParameterType",
    "PatientType",
    "PatientCommunicationType",
    "PatientContactType",
    "PatientLinkType",
    "PaymentNoticeType",
    "PaymentReconciliationType",
    "PaymentReconciliationDetailType",
    "PaymentReconciliationProcessNoteType",
    "PeriodType",
    "PersonType",
    "PersonLinkType",
    "PlanDefinitionType",
    "PlanDefinitionActionType",
    "PlanDefinitionActionConditionType",
    "PlanDefinitionActionDynamicValueType",
    "PlanDefinitionActionParticipantType",
    "PlanDefinitionActionRelatedActionType",
    "PlanDefinitionGoalType",
    "PlanDefinitionGoalTargetType",
    "PopulationType",
    "PractitionerType",
    "PractitionerQualificationType",
    "PractitionerRoleType",
    "PractitionerRoleAvailableTimeType",
    "PractitionerRoleNotAvailableType",
    "ProcedureType",
    "ProcedureFocalDeviceType",
    "ProcedurePerformerType",
    "ProdCharacteristicType",
    "ProductShelfLifeType",
    "ProvenanceType",
    "ProvenanceAgentType",
    "ProvenanceEntityType",
    "QuantityType",
    "QuestionnaireType",
    "QuestionnaireItemType",
    "QuestionnaireItemAnswerOptionType",
    "QuestionnaireItemEnableWhenType",
    "QuestionnaireItemInitialType",
    "QuestionnaireResponseType",
    "QuestionnaireResponseItemType",
    "QuestionnaireResponseItemAnswerType",
    "RangeType",
    "RatioType",
    "ReferenceType",
    "RelatedArtifactType",
    "RelatedPersonType",
    "RelatedPersonCommunicationType",
    "RequestGroupType",
    "RequestGroupActionType",
    "RequestGroupActionConditionType",
    "RequestGroupActionRelatedActionType",
    "ResearchDefinitionType",
    "ResearchElementDefinitionType",
    "ResearchElementDefinitionCharacteristicType",
    "ResearchStudyType",
    "ResearchStudyArmType",
    "ResearchStudyObjectiveType",
    "ResearchSubjectType",
    "RiskAssessmentType",
    "RiskAssessmentPredictionType",
    "RiskEvidenceSynthesisType",
    "RiskEvidenceSynthesisCertaintyType",
    "RiskEvidenceSynthesisCertaintyCertaintySubcomponentType",
    "RiskEvidenceSynthesisRiskEstimateType",
    "RiskEvidenceSynthesisRiskEstimatePrecisionEstimateType",
    "RiskEvidenceSynthesisSampleSizeType",
    "SampledDataType",
    "ScheduleType",
    "SearchParameterType",
    "SearchParameterComponentType",
    "ServiceRequestType",
    "SignatureType",
    "SlotType",
    "SpecimenType",
    "SpecimenCollectionType",
    "SpecimenContainerType",
    "SpecimenDefinitionType",
    "SpecimenDefinitionTypeTestedType",
    "SpecimenDefinitionTypeTestedContainerType",
    "SpecimenDefinitionTypeTestedContainerAdditiveType",
    "SpecimenDefinitionTypeTestedHandlingType",
    "SpecimenProcessingType",
    "StructureDefinitionType",
    "StructureDefinitionContextType",
    "StructureDefinitionDifferentialType",
    "StructureDefinitionMappingType",
    "StructureDefinitionSnapshotType",
    "StructureMapType",
    "StructureMapGroupType",
    "StructureMapGroupInputType",
    "StructureMapGroupRuleType",
    "StructureMapGroupRuleDependentType",
    "StructureMapGroupRuleSourceType",
    "StructureMapGroupRuleTargetType",
    "StructureMapGroupRuleTargetParameterType",
    "StructureMapStructureType",
    "SubscriptionType",
    "SubscriptionChannelType",
    "SubstanceType",
    "SubstanceAmountType",
    "SubstanceAmountReferenceRangeType",
    "SubstanceIngredientType",
    "SubstanceInstanceType",
    "SubstanceNucleicAcidType",
    "SubstanceNucleicAcidSubunitType",
    "SubstanceNucleicAcidSubunitLinkageType",
    "SubstanceNucleicAcidSubunitSugarType",
    "SubstancePolymerType",
    "SubstancePolymerMonomerSetType",
    "SubstancePolymerMonomerSetStartingMaterialType",
    "SubstancePolymerRepeatType",
    "SubstancePolymerRepeatRepeatUnitType",
    "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType",
    "SubstancePolymerRepeatRepeatUnitStructuralRepresentationType",
    "SubstanceProteinType",
    "SubstanceProteinSubunitType",
    "SubstanceReferenceInformationType",
    "SubstanceReferenceInformationClassificationType",
    "SubstanceReferenceInformationGeneType",
    "SubstanceReferenceInformationGeneElementType",
    "SubstanceReferenceInformationTargetType",
    "SubstanceSourceMaterialType",
    "SubstanceSourceMaterialFractionDescriptionType",
    "SubstanceSourceMaterialOrganismType",
    "SubstanceSourceMaterialOrganismAuthorType",
    "SubstanceSourceMaterialOrganismHybridType",
    "SubstanceSourceMaterialOrganismOrganismGeneralType",
    "SubstanceSourceMaterialPartDescriptionType",
    "SubstanceSpecificationType",
    "SubstanceSpecificationCodeType",
    "SubstanceSpecificationMoietyType",
    "SubstanceSpecificationNameType",
    "SubstanceSpecificationNameOfficialType",
    "SubstanceSpecificationPropertyType",
    "SubstanceSpecificationRelationshipType",
    "SubstanceSpecificationStructureType",
    "SubstanceSpecificationStructureIsotopeType",
    "SubstanceSpecificationStructureIsotopeMolecularWeightType",
    "SubstanceSpecificationStructureRepresentationType",
    "SupplyDeliveryType",
    "SupplyDeliverySuppliedItemType",
    "SupplyRequestType",
    "SupplyRequestParameterType",
    "TaskType",
    "TaskInputType",
    "TaskOutputType",
    "TaskRestrictionType",
    "TerminologyCapabilitiesType",
    "TerminologyCapabilitiesClosureType",
    "TerminologyCapabilitiesCodeSystemType",
    "TerminologyCapabilitiesCodeSystemVersionType",
    "TerminologyCapabilitiesCodeSystemVersionFilterType",
    "TerminologyCapabilitiesExpansionType",
    "TerminologyCapabilitiesExpansionParameterType",
    "TerminologyCapabilitiesImplementationType",
    "TerminologyCapabilitiesSoftwareType",
    "TerminologyCapabilitiesTranslationType",
    "TerminologyCapabilitiesValidateCodeType",
    "TestReportType",
    "TestReportParticipantType",
    "TestReportSetupType",
    "TestReportSetupActionType",
    "TestReportSetupActionAssertType",
    "TestReportSetupActionOperationType",
    "TestReportTeardownType",
    "TestReportTeardownActionType",
    "TestReportTestType",
    "TestReportTestActionType",
    "TestScriptType",
    "TestScriptDestinationType",
    "TestScriptFixtureType",
    "TestScriptMetadataType",
    "TestScriptMetadataCapabilityType",
    "TestScriptMetadataLinkType",
    "TestScriptOriginType",
    "TestScriptSetupType",
    "TestScriptSetupActionType",
    "TestScriptSetupActionAssertType",
    "TestScriptSetupActionOperationType",
    "TestScriptSetupActionOperationRequestHeaderType",
    "TestScriptTeardownType",
    "TestScriptTeardownActionType",
    "TestScriptTestType",
    "TestScriptTestActionType",
    "TestScriptVariableType",
    "TimingType",
    "TimingRepeatType",
    "TriggerDefinitionType",
    "UsageContextType",
    "ValueSetType",
    "ValueSetComposeType",
    "ValueSetComposeIncludeType",
    "ValueSetComposeIncludeConceptType",
    "ValueSetComposeIncludeConceptDesignationType",
    "ValueSetComposeIncludeFilterType",
    "ValueSetExpansionType",
    "ValueSetExpansionContainsType",
    "ValueSetExpansionParameterType",
    "VerificationResultType",
    "VerificationResultAttestationType",
    "VerificationResultPrimarySourceType",
    "VerificationResultValidatorType",
    "VisionPrescriptionType",
    "VisionPrescriptionLensSpecificationType",
    "VisionPrescriptionLensSpecificationPrismType",
]
