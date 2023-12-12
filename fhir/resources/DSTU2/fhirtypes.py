# _*_ coding: utf-8 _*_
import datetime
import re
from email.utils import formataddr, parseaddr
from typing import TYPE_CHECKING, Any, Dict, Optional, Pattern, Union
from uuid import UUID

from pydantic.v1 import AnyUrl
from pydantic.v1.errors import ConfigError, DateError, DateTimeError, TimeError
from pydantic.v1.main import load_str_bytes
from pydantic.v1.networks import validate_email
from pydantic.v1.types import (
    ConstrainedBytes,
    ConstrainedDecimal,
    ConstrainedInt,
    ConstrainedStr,
)
from pydantic.v1.validators import (
    bool_validator,
    parse_date,
    parse_datetime,
    parse_time,
)

from .fhirabstractmodel import FHIRAbstractModel
from .fhirtypesvalidators import run_validator_for_fhir_type

if TYPE_CHECKING:
    from pydantic.v1.types import CallableGenerator
    from pydantic.v1.fields import ModelField
    from pydantic.v1.fields import BaseConfig

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

    __fhir_release__: str = "DSTU2"
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

    class Boolean(int):
        """true | false"""

        regex: str = "true|false"
        __visit_name__ = "boolean"

        @classmethod
        def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
            field_schema.update(type="boolean")

        @classmethod
        def __get_validators__(cls) -> "CallableGenerator":
            yield bool_validator


class String(ConstrainedStr):
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


class Base64Binary(ConstrainedBytes):
    """A stream of bytes, base64 encoded (RFC 4648 )"""

    regex = re.compile(r"(\s*([0-9a-zA-Z+=]){4}\s*)+")
    __visit_name__ = "base64Binary"


class Code(ConstrainedStr):
    """Indicates that the value is taken from a set of controlled
    strings defined elsewhere (see Using codes for further discussion).
    Technically, a code is restricted to a string which has at least one
    character and no leading or trailing whitespace, and where there is
    no whitespace other than single spaces in the contents"""

    regex = re.compile(r"^[^\s]+(\s[^\s]+)*$")
    __visit_name__ = "code"


class Id(ConstrainedStr, Primitive):
    """Any combination of upper- or lower-case ASCII letters
    ('A'..'Z', and 'a'..'z', numerals ('0'..'9'), '-' and '.',
    with a length limit of 64 characters.
    (This might be an integer, an un-prefixed OID, UUID or any other identifier
    pattern that meets these constraints.)

    But it is possible to change the default behaviour by using configure_constraints()
    method!
    """

    regex = re.compile(r"^[A-Za-z0-9\-.]+$")
    min_length = 1
    max_length = 64
    __visit_name__ = "id"

    @classmethod
    def configure_constraints(
        cls,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[Pattern] = None,
    ):
        """There are a lots of discussion about ``Resource.Id`` length of value.
            1. https://bit.ly/360HksL
            2. https://bit.ly/3o1fZgl
        We see there is some agreement and disagreement, because of that we decide to make
        it more flexible. Now it is possible configure three types of constraints.
        """
        if min_length is not None:
            if min_length < 1:
                raise ConfigError("Minimum length must be more than 0.")
            _max_check = max_length or cls.max_length
            if min_length > _max_check:
                raise ConfigError(
                    "Minimum length value cannot be greater than maximum value."
                )
            cls.min_length = min_length

        if max_length is not None:
            if max_length < 1:
                raise ConfigError("Maximum length must be more than 0.")
            _min_check = min_length or cls.min_length
            if max_length < _min_check:
                raise ConfigError(
                    "Maximum length value cannot be less than minimum value."
                )
            cls.max_length = max_length

        if regex is not None:
            cls.regex = regex


class Uuid(UUID, Primitive):
    """A UUID (aka GUID) represented as a URI (RFC 4122 );
    e.g. urn:uuid:c757873d-ec9a-4326-a141-556f43239520"""

    __visit_name__ = "uuid"
    regex = None


class Decimal(ConstrainedDecimal):
    """Rational numbers that have a decimal representation.
    See below about the precision of the number"""

    regex = re.compile(r"^-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?$")
    __visit_name__ = "decimal"


class Integer(ConstrainedInt):
    """A signed integer in the range −2,147,483,648..2,147,483,647 (32-bit;
    for larger values, use decimal)"""

    regex = re.compile(r"^[0]|[-+]?[1-9][0-9]*$")
    __visit_name__ = "integer"


class UnsignedInt(ConstrainedInt):
    """Any non-negative integer in the range 0..2,147,483,647"""

    regex = re.compile(r"^[0]|([1-9][0-9]*)$")
    __visit_name__ = "unsignedInt"
    ge = 0


class PositiveInt(ConstrainedInt):
    """Any positive integer in the range 1..2,147,483,647"""

    regex = re.compile(r"^\+?[1-9][0-9]*$")
    __visit_name__ = "positiveInt"
    gt = 0


class Uri(ConstrainedStr):
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


class Oid(ConstrainedStr):
    """An OID represented as a URI (RFC 3001 ); e.g. urn:oid:1.2.3.4.5"""

    __visit_name__ = "oid"
    regex = re.compile(r"^urn:oid:[0-2](\.(0|[1-9][0-9]*))+$")


class Markdown(ConstrainedStr):
    """A FHIR string (see above) that may contain markdown syntax for optional processing
    by a markdown presentation engine, in the GFM extension of CommonMark format (see below)
    """

    __visit_name__ = "markdown"
    regex = re.compile(r"\s*(\S|\s)*")


class Xhtml(ConstrainedStr):
    regex = None
    __visit_name__ = "xhtml"


class Date(datetime.date):
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


class DateTime(datetime.datetime):
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


class Instant(datetime.datetime):
    """An instant in time in the format YYYY-MM-DDThh:mm:ss.sss+zz:zz
    (e.g. 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z).
    The time SHALL specified at least to the second and SHALL include a time zone.
    Note: This is intended for when precisely observed times are required
    (typically system logs etc.), and not human-reported times - for those,
    use date or dateTime (which can be as precise as instant,
    but is not required to be). instant is a more constrained dateTime

    Note: This type is for system times, not human times (see date and dateTime below).
    """

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


class Time(datetime.time):
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

    __fhir_release__: str = "DSTU2"
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


class AbstractBaseType(dict):
    """ """

    __fhir_release__: str = "DSTU2"
    __resource_type__: str = ...  # type: ignore

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type=cls.__resource_type__)

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        yield cls.validate

    @classmethod
    def is_primitive(cls) -> bool:
        """ """
        return False

    @classmethod
    def fhir_type_name(cls) -> str:
        """ """
        return cls.__resource_type__

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


class FHIRPrimitiveExtensionType(AbstractType):
    """ """

    __resource_type__ = "FHIRPrimitiveExtension"


class ElementType(AbstractBaseType):
    """ """

    __resource_type__ = "Element"


class ResourceType(AbstractBaseType):
    """ """

    __resource_type__ = "Resource"


class DomainResourceType(AbstractType):
    __resource_type__ = "DomainResource"


class ExtensionType(AbstractType):
    __resource_type__ = "Extension"


class BackboneElementType(AbstractType):
    __resource_type__ = "BackboneElement"


class MetaType(AbstractType):
    __resource_type__ = "Meta"


class NarrativeType(AbstractType):
    __resource_type__ = "Narrative"


class AddressType(AbstractType):
    __resource_type__ = "Address"


class PeriodType(AbstractType):
    __resource_type__ = "Period"


class AttachmentType(AbstractType):
    __resource_type__ = "Attachment"


class CodeableConceptType(AbstractType):
    __resource_type__ = "CodeableConcept"


class CodingType(AbstractType):
    __resource_type__ = "Coding"


class ContactPointType(AbstractType):
    __resource_type__ = "ContactPoint"


class HumanNameType(AbstractType):
    __resource_type__ = "HumanName"


class IdentifierType(AbstractType):
    __resource_type__ = "Identifier"


class ReferenceType(AbstractType):
    __resource_type__ = "Reference"


class QuantityType(AbstractType):
    __resource_type__ = "Quantity"


class RangeType(AbstractType):
    __resource_type__ = "Range"


class RatioType(AbstractType):
    __resource_type__ = "Ratio"


class SignatureType(AbstractType):
    __resource_type__ = "Signature"


class TimingType(AbstractType):
    __resource_type__ = "Timing"


class TimingRepeatType(AbstractType):
    __resource_type__ = "TimingRepeat"


class DurationType(AbstractType):
    __resource_type__ = "Duration"


class AgeType(AbstractType):
    __resource_type__ = "Age"


class CountType(AbstractType):
    __resource_type__ = "Count"


class MoneyType(AbstractType):
    __resource_type__ = "Money"


class DistanceType(AbstractType):
    __resource_type__ = "Distance"


class SampledDataType(AbstractType):
    __resource_type__ = "SampledData"


class AnnotationType(AbstractType):
    __resource_type__ = "Annotation"


class MediaType(AbstractType):
    __resource_type__ = "Media"


class BasicType(AbstractType):
    __resource_type__ = "Basic"


class BinaryType(AbstractType):
    __resource_type__ = "Binary"


class BodySiteType(AbstractType):
    __resource_type__ = "BodySite"


class FlagType(AbstractType):
    __resource_type__ = "Flag"


class LocationType(AbstractType):
    __resource_type__ = "Location"


class LocationPositionType(AbstractType):
    __resource_type__ = "LocationPosition"


class SlotType(AbstractType):
    __resource_type__ = "Slot"


class ScheduleType(AbstractType):
    __resource_type__ = "Schedule"


class AccountType(AbstractType):
    __resource_type__ = "Account"


class AllergyIntoleranceType(AbstractType):
    __resource_type__ = "AllergyIntolerance"


class AllergyIntoleranceReactionType(AbstractType):
    __resource_type__ = "AllergyIntoleranceReaction"


class AppointmentType(AbstractType):
    __resource_type__ = "Appointment"


class AppointmentParticipantType(AbstractType):
    __resource_type__ = "AppointmentParticipant"


class AppointmentResponseType(AbstractType):
    __resource_type__ = "AppointmentResponse"


class AuditEventType(AbstractType):
    __resource_type__ = "AuditEvent"


class AuditEventEventType(AbstractType):
    __resource_type__ = "AuditEventEvent"


class AuditEventObjectType(AbstractType):
    __resource_type__ = "AuditEventObject"


class AuditEventObjectDetailType(AbstractType):
    __resource_type__ = "AuditEventObjectDetail"


class AuditEventParticipantType(AbstractType):
    __resource_type__ = "AuditEventParticipant"


class AuditEventParticipantNetworkType(AbstractType):
    __resource_type__ = "AuditEventParticipantNetwork"


class AuditEventSourceType(AbstractType):
    __resource_type__ = "AuditEventSource"


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


class CarePlanType(AbstractType):
    __resource_type__ = "CarePlan"


class CarePlanActivityType(AbstractType):
    __resource_type__ = "CarePlanActivity"


class CarePlanActivityDetailType(AbstractType):
    __resource_type__ = "CarePlanActivityDetail"


class CarePlanParticipantType(AbstractType):
    __resource_type__ = "CarePlanParticipant"


class CarePlanRelatedPlanType(AbstractType):
    __resource_type__ = "CarePlanRelatedPlan"


class ClaimType(AbstractType):
    __resource_type__ = "Claim"


class ClaimCoverageType(AbstractType):
    __resource_type__ = "ClaimCoverage"


class ClaimDiagnosisType(AbstractType):
    __resource_type__ = "ClaimDiagnosis"


class ClaimItemType(AbstractType):
    __resource_type__ = "ClaimItem"


class ClaimItemDetailType(AbstractType):
    __resource_type__ = "ClaimItemDetail"


class ClaimItemDetailSubDetailType(AbstractType):
    __resource_type__ = "ClaimItemDetailSubDetail"


class ClaimItemProsthesisType(AbstractType):
    __resource_type__ = "ClaimItemProsthesis"


class ClaimMissingTeethType(AbstractType):
    __resource_type__ = "ClaimMissingTeeth"


class ClaimPayeeType(AbstractType):
    __resource_type__ = "ClaimPayee"


class ClaimResponseType(AbstractType):
    __resource_type__ = "ClaimResponse"


class ClaimResponseAddItemType(AbstractType):
    __resource_type__ = "ClaimResponseAddItem"


class ClaimResponseAddItemAdjudicationType(AbstractType):
    __resource_type__ = "ClaimResponseAddItemAdjudication"


class ClaimResponseAddItemDetailType(AbstractType):
    __resource_type__ = "ClaimResponseAddItemDetail"


class ClaimResponseAddItemDetailAdjudicationType(AbstractType):
    __resource_type__ = "ClaimResponseAddItemDetailAdjudication"


class ClaimResponseCoverageType(AbstractType):
    __resource_type__ = "ClaimResponseCoverage"


class ClaimResponseErrorType(AbstractType):
    __resource_type__ = "ClaimResponseError"


class ClaimResponseItemType(AbstractType):
    __resource_type__ = "ClaimResponseItem"


class ClaimResponseItemAdjudicationType(AbstractType):
    __resource_type__ = "ClaimResponseItemAdjudication"


class ClaimResponseItemDetailType(AbstractType):
    __resource_type__ = "ClaimResponseItemDetail"


class ClaimResponseItemDetailAdjudicationType(AbstractType):
    __resource_type__ = "ClaimResponseItemDetailAdjudication"


class ClaimResponseItemDetailSubDetailType(AbstractType):
    __resource_type__ = "ClaimResponseItemDetailSubDetail"


class ClaimResponseItemDetailSubDetailAdjudicationType(AbstractType):
    __resource_type__ = "ClaimResponseItemDetailSubDetailAdjudication"


class ClaimResponseNoteType(AbstractType):
    __resource_type__ = "ClaimResponseNote"


class ClinicalImpressionType(AbstractType):
    __resource_type__ = "ClinicalImpression"


class ClinicalImpressionFindingType(AbstractType):
    __resource_type__ = "ClinicalImpressionFinding"


class ClinicalImpressionInvestigationsType(AbstractType):
    __resource_type__ = "ClinicalImpressionInvestigations"


class ClinicalImpressionRuledOutType(AbstractType):
    __resource_type__ = "ClinicalImpressionRuledOut"


class CommunicationType(AbstractType):
    __resource_type__ = "Communication"


class CommunicationPayloadType(AbstractType):
    __resource_type__ = "CommunicationPayload"


class CommunicationRequestType(AbstractType):
    __resource_type__ = "CommunicationRequest"


class CommunicationRequestPayloadType(AbstractType):
    __resource_type__ = "CommunicationRequestPayload"


class CompositionType(AbstractType):
    __resource_type__ = "Composition"


class CompositionAttesterType(AbstractType):
    __resource_type__ = "CompositionAttester"


class CompositionEventType(AbstractType):
    __resource_type__ = "CompositionEvent"


class CompositionSectionType(AbstractType):
    __resource_type__ = "CompositionSection"


class ConceptMapType(AbstractType):
    __resource_type__ = "ConceptMap"


class ConceptMapContactType(AbstractType):
    __resource_type__ = "ConceptMapContact"


class ConceptMapElementType(AbstractType):
    __resource_type__ = "ConceptMapElement"


class ConceptMapElementTargetType(AbstractType):
    __resource_type__ = "ConceptMapElementTarget"


class ConceptMapElementTargetDependsOnType(AbstractType):
    __resource_type__ = "ConceptMapElementTargetDependsOn"


class ConditionType(AbstractType):
    __resource_type__ = "Condition"


class ConditionEvidenceType(AbstractType):
    __resource_type__ = "ConditionEvidence"


class ConditionStageType(AbstractType):
    __resource_type__ = "ConditionStage"


class ConformanceType(AbstractType):
    __resource_type__ = "Conformance"


class ConformanceContactType(AbstractType):
    __resource_type__ = "ConformanceContact"


class ConformanceDocumentType(AbstractType):
    __resource_type__ = "ConformanceDocument"


class ConformanceImplementationType(AbstractType):
    __resource_type__ = "ConformanceImplementation"


class ConformanceMessagingType(AbstractType):
    __resource_type__ = "ConformanceMessaging"


class ConformanceMessagingEndpointType(AbstractType):
    __resource_type__ = "ConformanceMessagingEndpoint"


class ConformanceMessagingEventType(AbstractType):
    __resource_type__ = "ConformanceMessagingEvent"


class ConformanceRestType(AbstractType):
    __resource_type__ = "ConformanceRest"


class ConformanceRestInteractionType(AbstractType):
    __resource_type__ = "ConformanceRestInteraction"


class ConformanceRestOperationType(AbstractType):
    __resource_type__ = "ConformanceRestOperation"


class ConformanceRestResourceType(AbstractType):
    __resource_type__ = "ConformanceRestResource"


class ConformanceRestResourceInteractionType(AbstractType):
    __resource_type__ = "ConformanceRestResourceInteraction"


class ConformanceRestSecurityType(AbstractType):
    __resource_type__ = "ConformanceRestSecurity"


class ConformanceRestSecurityCertificateType(AbstractType):
    __resource_type__ = "ConformanceRestSecurityCertificate"


class ConformanceSoftwareType(AbstractType):
    __resource_type__ = "ConformanceSoftware"


class ConformanceRestResourceSearchParamType(AbstractType):
    __resource_type__ = "ConformanceRestResourceSearchParam"


class PatientType(AbstractType):
    __resource_type__ = "Patient"


class PatientAnimalType(AbstractType):
    __resource_type__ = "PatientAnimal"


class PatientCommunicationType(AbstractType):
    __resource_type__ = "PatientCommunication"


class PatientContactType(AbstractType):
    __resource_type__ = "PatientContact"


class PatientLinkType(AbstractType):
    __resource_type__ = "PatientLink"


class OrderType(AbstractType):
    __resource_type__ = "Order"


class OrderWhenType(AbstractType):
    __resource_type__ = "OrderWhen"


class OrderResponseType(AbstractType):
    __resource_type__ = "OrderResponse"


class OrganizationType(AbstractType):
    __resource_type__ = "Organization"


class OrganizationContactType(AbstractType):
    __resource_type__ = "OrganizationContact"


class PersonType(AbstractType):
    __resource_type__ = "Person"


class PersonLinkType(AbstractType):
    __resource_type__ = "PersonLink"


class PractitionerType(AbstractType):
    __resource_type__ = "Practitioner"


class PractitionerPractitionerRoleType(AbstractType):
    __resource_type__ = "PractitionerPractitionerRole"


class PractitionerQualificationType(AbstractType):
    __resource_type__ = "PractitionerQualification"


class ValueSetType(AbstractType):
    __resource_type__ = "ValueSet"


class ValueSetCodeSystemType(AbstractType):
    __resource_type__ = "ValueSetCodeSystem"


class ValueSetCodeSystemConceptType(AbstractType):
    __resource_type__ = "ValueSetCodeSystemConcept"


class ValueSetCodeSystemConceptDesignationType(AbstractType):
    __resource_type__ = "ValueSetCodeSystemConceptDesignation"


class ValueSetComposeType(AbstractType):
    __resource_type__ = "ValueSetCompose"


class ValueSetComposeIncludeType(AbstractType):
    __resource_type__ = "ValueSetComposeInclude"


class ValueSetComposeIncludeConceptType(AbstractType):
    __resource_type__ = "ValueSetComposeIncludeConcept"


class ValueSetComposeIncludeFilterType(AbstractType):
    __resource_type__ = "ValueSetComposeIncludeFilter"


class ValueSetContactType(AbstractType):
    __resource_type__ = "ValueSetContact"


class ValueSetExpansionType(AbstractType):
    __resource_type__ = "ValueSetExpansion"


class ValueSetExpansionContainsType(AbstractType):
    __resource_type__ = "ValueSetExpansionContains"


class ValueSetExpansionParameterType(AbstractType):
    __resource_type__ = "ValueSetExpansionParameter"


class ProcedureType(AbstractType):
    __resource_type__ = "Procedure"


class ProcedureFocalDeviceType(AbstractType):
    __resource_type__ = "ProcedureFocalDevice"


class ProcedurePerformerType(AbstractType):
    __resource_type__ = "ProcedurePerformer"


class ProcedureRequestType(AbstractType):
    __resource_type__ = "ProcedureRequest"


class DiagnosticReportType(AbstractType):
    __resource_type__ = "DiagnosticReport"


class DiagnosticReportImageType(AbstractType):
    __resource_type__ = "DiagnosticReportImage"


class DocumentReferenceType(AbstractType):
    __resource_type__ = "DocumentReference"


class DocumentReferenceContentType(AbstractType):
    __resource_type__ = "DocumentReferenceContent"


class DocumentReferenceContextType(AbstractType):
    __resource_type__ = "DocumentReferenceContext"


class DocumentReferenceContextRelatedType(AbstractType):
    __resource_type__ = "DocumentReferenceContextRelated"


class DocumentReferenceRelatesToType(AbstractType):
    __resource_type__ = "DocumentReferenceRelatesTo"


class DocumentManifestType(AbstractType):
    __resource_type__ = "DocumentManifest"


class DocumentManifestContentType(AbstractType):
    __resource_type__ = "DocumentManifestContent"


class DocumentManifestRelatedType(AbstractType):
    __resource_type__ = "DocumentManifestRelated"


class GoalType(AbstractType):
    __resource_type__ = "Goal"


class GoalOutcomeType(AbstractType):
    __resource_type__ = "GoalOutcome"


class GroupType(AbstractType):
    __resource_type__ = "Group"


class GroupCharacteristicType(AbstractType):
    __resource_type__ = "GroupCharacteristic"


class GroupMemberType(AbstractType):
    __resource_type__ = "GroupMember"


class ElementDefinitionType(AbstractType):
    __resource_type__ = "ElementDefinition"


class ElementDefinitionSlicingType(AbstractType):
    __resource_type__ = "ElementDefinitionSlicing"


class ElementDefinitionSlicingDiscriminatorType(AbstractType):
    __resource_type__ = "ElementDefinitionSlicingDiscriminator"


class ElementDefinitionTypeType(AbstractType):
    __resource_type__ = "ElementDefinitionType"


class ElementDefinitionMappingType(AbstractType):
    __resource_type__ = "ElementDefinitionMapping"


class ElementDefinitionExampleType(AbstractType):
    __resource_type__ = "ElementDefinitionExample"


class ElementDefinitionConstraintType(AbstractType):
    __resource_type__ = "ElementDefinitionConstraint"


class ElementDefinitionBaseType(AbstractType):
    __resource_type__ = "ElementDefinitionBase"


class ElementDefinitionBindingType(AbstractType):
    __resource_type__ = "ElementDefinitionBinding"


class ElementDefinitionBindingValueSetType(AbstractType):
    __resource_type__ = "ElementDefinitionBindingValueSet"


class EligibilityRequestType(AbstractType):
    __resource_type__ = "EligibilityRequest"


class EligibilityResponseType(AbstractType):
    __resource_type__ = "EligibilityResponse"


class EncounterType(AbstractType):
    __resource_type__ = "Encounter"


class EncounterHospitalizationType(AbstractType):
    __resource_type__ = "EncounterHospitalization"


class EncounterLocationType(AbstractType):
    __resource_type__ = "EncounterLocation"


class EncounterParticipantType(AbstractType):
    __resource_type__ = "EncounterParticipant"


class EncounterStatusHistoryType(AbstractType):
    __resource_type__ = "EncounterStatusHistory"


class EnrollmentRequestType(AbstractType):
    __resource_type__ = "EnrollmentRequest"


class EnrollmentResponseType(AbstractType):
    __resource_type__ = "EnrollmentResponse"


class ImmunizationType(AbstractType):
    __resource_type__ = "Immunization"


class ImmunizationExplanationType(AbstractType):
    __resource_type__ = "ImmunizationExplanation"


class ImmunizationReactionType(AbstractType):
    __resource_type__ = "ImmunizationReaction"


class ImmunizationVaccinationProtocolType(AbstractType):
    __resource_type__ = "ImmunizationVaccinationProtocol"


class MedicationAdministrationType(AbstractType):
    __resource_type__ = "MedicationAdministration"


class MedicationAdministrationDosageType(AbstractType):
    __resource_type__ = "MedicationAdministrationDosage"


class MedicationStatementType(AbstractType):
    __resource_type__ = "MedicationStatement"


class MedicationStatementDosageType(AbstractType):
    __resource_type__ = "MedicationStatementDosage"


class ObservationType(AbstractType):
    __resource_type__ = "Observation"


class ObservationComponentType(AbstractType):
    __resource_type__ = "ObservationComponent"


class ObservationReferenceRangeType(AbstractType):
    __resource_type__ = "ObservationReferenceRange"


class ObservationRelatedType(AbstractType):
    __resource_type__ = "ObservationRelated"


class OperationOutcomeType(AbstractType):
    __resource_type__ = "OperationOutcome"


class OperationOutcomeIssueType(AbstractType):
    __resource_type__ = "OperationOutcomeIssue"


class MedicationType(AbstractType):
    __resource_type__ = "Medication"


class MedicationPackageType(AbstractType):
    __resource_type__ = "MedicationPackage"


class MedicationPackageContentType(AbstractType):
    __resource_type__ = "MedicationPackageContent"


class MedicationProductType(AbstractType):
    __resource_type__ = "MedicationProduct"


class MedicationProductBatchType(AbstractType):
    __resource_type__ = "MedicationProductBatch"


class MedicationProductIngredientType(AbstractType):
    __resource_type__ = "MedicationProductIngredient"


class ContractType(AbstractType):
    __resource_type__ = "Contract"


class ContractActorType(AbstractType):
    __resource_type__ = "ContractActor"


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


class ContractTermActorType(AbstractType):
    __resource_type__ = "ContractTermActor"


class ContractTermValuedItemType(AbstractType):
    __resource_type__ = "ContractTermValuedItem"


class ContractValuedItemType(AbstractType):
    __resource_type__ = "ContractValuedItem"


class DeviceType(AbstractType):
    __resource_type__ = "Device"


class RelatedPersonType(AbstractType):
    __resource_type__ = "RelatedPerson"


class DetectedIssueType(AbstractType):
    __resource_type__ = "DetectedIssue"


class DetectedIssueMitigationType(AbstractType):
    __resource_type__ = "DetectedIssueMitigation"


class DataElementType(AbstractType):
    __resource_type__ = "DataElement"


class DataElementContactType(AbstractType):
    __resource_type__ = "DataElementContact"


class DataElementMappingType(AbstractType):
    __resource_type__ = "DataElementMapping"


class DeviceComponentType(AbstractType):
    __resource_type__ = "DeviceComponent"


class DeviceComponentProductionSpecificationType(AbstractType):
    __resource_type__ = "DeviceComponentProductionSpecification"


class DeviceMetricType(AbstractType):
    __resource_type__ = "DeviceMetric"


class DeviceMetricCalibrationType(AbstractType):
    __resource_type__ = "DeviceMetricCalibration"


class DeviceUseRequestType(AbstractType):
    __resource_type__ = "DeviceUseRequest"


class DeviceUseStatementType(AbstractType):
    __resource_type__ = "DeviceUseStatement"


class DiagnosticOrderType(AbstractType):
    __resource_type__ = "DiagnosticOrder"


class DiagnosticOrderEventType(AbstractType):
    __resource_type__ = "DiagnosticOrderEvent"


class DiagnosticOrderItemType(AbstractType):
    __resource_type__ = "DiagnosticOrderItem"


class EpisodeOfCareType(AbstractType):
    __resource_type__ = "EpisodeOfCare"


class EpisodeOfCareCareTeamType(AbstractType):
    __resource_type__ = "EpisodeOfCareCareTeam"


class EpisodeOfCareStatusHistoryType(AbstractType):
    __resource_type__ = "EpisodeOfCareStatusHistory"


class FamilyMemberHistoryType(AbstractType):
    __resource_type__ = "FamilyMemberHistory"


class FamilyMemberHistoryConditionType(AbstractType):
    __resource_type__ = "FamilyMemberHistoryCondition"


class ExplanationOfBenefitType(AbstractType):
    __resource_type__ = "ExplanationOfBenefit"


class HealthcareServiceType(AbstractType):
    __resource_type__ = "HealthcareService"


class HealthcareServiceAvailableTimeType(AbstractType):
    __resource_type__ = "HealthcareServiceAvailableTime"


class HealthcareServiceNotAvailableType(AbstractType):
    __resource_type__ = "HealthcareServiceNotAvailable"


class HealthcareServiceServiceTypeType(AbstractType):
    __resource_type__ = "HealthcareServiceServiceType"


class ImagingObjectSelectionType(AbstractType):
    __resource_type__ = "ImagingObjectSelection"


class ImagingObjectSelectionStudyType(AbstractType):
    __resource_type__ = "ImagingObjectSelectionStudy"


class ImagingObjectSelectionStudySeriesType(AbstractType):
    __resource_type__ = "ImagingObjectSelectionStudySeries"


class ImagingObjectSelectionStudySeriesInstanceType(AbstractType):
    __resource_type__ = "ImagingObjectSelectionStudySeriesInstance"


class ImagingObjectSelectionStudySeriesInstanceFramesType(AbstractType):
    __resource_type__ = "ImagingObjectSelectionStudySeriesInstanceFrames"


class ImagingStudyType(AbstractType):
    __resource_type__ = "ImagingStudy"


class ImagingStudySeriesType(AbstractType):
    __resource_type__ = "ImagingStudySeries"


class ImagingStudySeriesInstanceType(AbstractType):
    __resource_type__ = "ImagingStudySeriesInstance"


class ImmunizationRecommendationType(AbstractType):
    __resource_type__ = "ImmunizationRecommendation"


class ImmunizationRecommendationRecommendationType(AbstractType):
    __resource_type__ = "ImmunizationRecommendationRecommendation"


class ImmunizationRecommendationRecommendationDateCriterionType(AbstractType):
    __resource_type__ = "ImmunizationRecommendationRecommendationDateCriterion"


class ImmunizationRecommendationRecommendationProtocolType(AbstractType):
    __resource_type__ = "ImmunizationRecommendationRecommendationProtocol"


class ImplementationGuideType(AbstractType):
    __resource_type__ = "ImplementationGuide"


class ImplementationGuideContactType(AbstractType):
    __resource_type__ = "ImplementationGuideContact"


class ImplementationGuideDependencyType(AbstractType):
    __resource_type__ = "ImplementationGuideDependency"


class ImplementationGuideGlobalType(AbstractType):
    __resource_type__ = "ImplementationGuideGlobal"


class ImplementationGuidePackageType(AbstractType):
    __resource_type__ = "ImplementationGuidePackage"


class ImplementationGuidePackageResourceType(AbstractType):
    __resource_type__ = "ImplementationGuidePackageResource"


class ImplementationGuidePageType(AbstractType):
    __resource_type__ = "ImplementationGuidePage"


class MedicationDispenseType(AbstractType):
    __resource_type__ = "MedicationDispense"


class MedicationDispenseDosageInstructionType(AbstractType):
    __resource_type__ = "MedicationDispenseDosageInstruction"


class MedicationDispenseSubstitutionType(AbstractType):
    __resource_type__ = "MedicationDispenseSubstitution"


class MedicationOrderType(AbstractType):
    __resource_type__ = "MedicationOrder"


class MedicationOrderDispenseRequestType(AbstractType):
    __resource_type__ = "MedicationOrderDispenseRequest"


class MedicationOrderDosageInstructionType(AbstractType):
    __resource_type__ = "MedicationOrderDosageInstruction"


class MedicationOrderSubstitutionType(AbstractType):
    __resource_type__ = "MedicationOrderSubstitution"


class MessageHeaderType(AbstractType):
    __resource_type__ = "MessageHeader"


class MessageHeaderDestinationType(AbstractType):
    __resource_type__ = "MessageHeaderDestination"


class MessageHeaderResponseType(AbstractType):
    __resource_type__ = "MessageHeaderResponse"


class MessageHeaderSourceType(AbstractType):
    __resource_type__ = "MessageHeaderSource"


class NamingSystemType(AbstractType):
    __resource_type__ = "NamingSystem"


class NamingSystemContactType(AbstractType):
    __resource_type__ = "NamingSystemContact"


class NamingSystemUniqueIdType(AbstractType):
    __resource_type__ = "NamingSystemUniqueId"


class ListType(AbstractType):
    __resource_type__ = "List"


class ListEntryType(AbstractType):
    __resource_type__ = "ListEntry"


class NutritionOrderType(AbstractType):
    __resource_type__ = "NutritionOrder"


class NutritionOrderOralDietType(AbstractType):
    __resource_type__ = "NutritionOrderOralDiet"


class NutritionOrderSupplementType(AbstractType):
    __resource_type__ = "NutritionOrderSupplement"


class NutritionOrderEnteralFormulaType(AbstractType):
    __resource_type__ = "NutritionOrderEnteralFormula"


class NutritionOrderOralDietNutrientType(AbstractType):
    __resource_type__ = "NutritionOrderOralDietNutrient"


class NutritionOrderOralDietTextureType(AbstractType):
    __resource_type__ = "NutritionOrderOralDietTexture"


class NutritionOrderEnteralFormulaAdministrationType(AbstractType):
    __resource_type__ = "NutritionOrderEnteralFormulaAdministration"


class OperationDefinitionType(AbstractType):
    __resource_type__ = "OperationDefinition"


class OperationDefinitionContactType(AbstractType):
    __resource_type__ = "OperationDefinitionContact"


class OperationDefinitionParameterType(AbstractType):
    __resource_type__ = "OperationDefinitionParameter"


class OperationDefinitionParameterBindingType(AbstractType):
    __resource_type__ = "OperationDefinitionParameterBinding"


class ParametersType(AbstractType):
    __resource_type__ = "Parameters"


class ParametersParameterType(AbstractType):
    __resource_type__ = "ParametersParameter"


class ProcessResponseType(AbstractType):
    __resource_type__ = "ProcessResponse"


class ProcessResponseNotesType(AbstractType):
    __resource_type__ = "ProcessResponseNotes"


class ProcessRequestType(AbstractType):
    __resource_type__ = "ProcessRequest"


class ProcessRequestItemType(AbstractType):
    __resource_type__ = "ProcessRequestItem"


class PaymentReconciliationType(AbstractType):
    __resource_type__ = "PaymentReconciliation"


class PaymentReconciliationDetailType(AbstractType):
    __resource_type__ = "PaymentReconciliationDetail"


class PaymentReconciliationNoteType(AbstractType):
    __resource_type__ = "PaymentReconciliationNote"


class PaymentNoticeType(AbstractType):
    __resource_type__ = "PaymentNotice"


class ProvenanceType(AbstractType):
    __resource_type__ = "Provenance"


class ProvenanceAgentType(AbstractType):
    __resource_type__ = "ProvenanceAgent"


class ProvenanceAgentRelatedAgentType(AbstractType):
    __resource_type__ = "ProvenanceAgentRelatedAgent"


class ProvenanceEntityType(AbstractType):
    __resource_type__ = "ProvenanceEntity"


class QuestionnaireResponseType(AbstractType):
    __resource_type__ = "QuestionnaireResponse"


class QuestionnaireResponseGroupType(AbstractType):
    __resource_type__ = "QuestionnaireResponseGroup"


class QuestionnaireResponseGroupQuestionType(AbstractType):
    __resource_type__ = "QuestionnaireResponseGroupQuestion"


class QuestionnaireResponseGroupQuestionAnswerType(AbstractType):
    __resource_type__ = "QuestionnaireResponseGroupQuestionAnswer"


class QuestionnaireType(AbstractType):
    __resource_type__ = "Questionnaire"


class QuestionnaireGroupType(AbstractType):
    __resource_type__ = "QuestionnaireGroup"


class QuestionnaireGroupQuestionType(AbstractType):
    __resource_type__ = "QuestionnaireGroupQuestion"


class ReferralRequestType(AbstractType):
    __resource_type__ = "ReferralRequest"


class RiskAssessmentType(AbstractType):
    __resource_type__ = "RiskAssessment"


class RiskAssessmentPredictionType(AbstractType):
    __resource_type__ = "RiskAssessmentPrediction"


class SearchParameterType(AbstractType):
    __resource_type__ = "SearchParameter"


class SearchParameterContactType(AbstractType):
    __resource_type__ = "SearchParameterContact"


class SubscriptionType(AbstractType):
    __resource_type__ = "Subscription"


class SubscriptionChannelType(AbstractType):
    __resource_type__ = "SubscriptionChannel"


class SubstanceType(AbstractType):
    __resource_type__ = "Substance"


class SubstanceInstanceType(AbstractType):
    __resource_type__ = "SubstanceInstance"


class SubstanceIngredientType(AbstractType):
    __resource_type__ = "SubstanceIngredient"


class SupplyDeliveryType(AbstractType):
    __resource_type__ = "SupplyDelivery"


class SupplyRequestType(AbstractType):
    __resource_type__ = "SupplyRequest"


class SupplyRequestWhenType(AbstractType):
    __resource_type__ = "SupplyRequestWhen"


class TestScriptType(AbstractType):
    __resource_type__ = "TestScript"


class TestScriptContactType(AbstractType):
    __resource_type__ = "TestScriptContact"


class TestScriptMetadataType(AbstractType):
    __resource_type__ = "TestScriptMetadata"


class TestScriptFixtureType(AbstractType):
    __resource_type__ = "TestScriptFixture"


class TestScriptVariableType(AbstractType):
    __resource_type__ = "TestScriptVariable"


class TestScriptSetupType(AbstractType):
    __resource_type__ = "TestScriptSetup"


class TestScriptTestType(AbstractType):
    __resource_type__ = "TestScriptTest"


class TestScriptTeardownType(AbstractType):
    __resource_type__ = "TestScriptTeardown"


class TestScriptMetadataLinkType(AbstractType):
    __resource_type__ = "TestScriptMetadataLink"


class TestScriptMetadataCapabilityType(AbstractType):
    __resource_type__ = "TestScriptMetadataCapability"


class TestScriptSetupActionType(AbstractType):
    __resource_type__ = "TestScriptSetupAction"


class TestScriptTestActionType(AbstractType):
    __resource_type__ = "TestScriptTestAction"


class TestScriptTeardownActionType(AbstractType):
    __resource_type__ = "TestScriptTeardownAction"


class TestScriptSetupActionOperationType(AbstractType):
    __resource_type__ = "TestScriptSetupActionOperation"


class TestScriptSetupActionAssertType(AbstractType):
    __resource_type__ = "TestScriptSetupActionAssert"


class TestScriptSetupActionOperationRequestHeaderType(AbstractType):
    __resource_type__ = "TestScriptSetupActionOperationRequestHeader"


class VisionPrescriptionType(AbstractType):
    __resource_type__ = "VisionPrescription"


class VisionPrescriptionDispenseType(AbstractType):
    __resource_type__ = "VisionPrescriptionDispense"


class SpecimenType(AbstractType):
    __resource_type__ = "Specimen"


class SpecimenCollectionType(AbstractType):
    __resource_type__ = "SpecimenCollection"


class SpecimenTreatmentType(AbstractType):
    __resource_type__ = "SpecimenTreatment"


class SpecimenContainerType(AbstractType):
    __resource_type__ = "SpecimenContainer"


__all__ = [
    "ElementType",
    "ResourceType",
    "DomainResourceType",
    "ExtensionType",
    "BackboneElementType",
    "MetaType",
    "NarrativeType",
    "AddressType",
    "PeriodType",
    "AttachmentType",
    "CodeableConceptType",
    "CodingType",
    "ContactPointType",
    "HumanNameType",
    "IdentifierType",
    "ReferenceType",
    "QuantityType",
    "RangeType",
    "RatioType",
    "SignatureType",
    "TimingType",
    "TimingRepeatType",
    "DurationType",
    "AgeType",
    "CountType",
    "MoneyType",
    "DistanceType",
    "SampledDataType",
    "AnnotationType",
    "MediaType",
    "BasicType",
    "BinaryType",
    "BodySiteType",
    "FlagType",
    "LocationType",
    "LocationPositionType",
    "SlotType",
    "ScheduleType",
    "AccountType",
    "AllergyIntoleranceType",
    "AllergyIntoleranceReactionType",
    "AppointmentType",
    "AppointmentParticipantType",
    "AppointmentResponseType",
    "AuditEventType",
    "AuditEventEventType",
    "AuditEventObjectType",
    "AuditEventObjectDetailType",
    "AuditEventParticipantType",
    "AuditEventParticipantNetworkType",
    "AuditEventSourceType",
    "BundleType",
    "BundleEntryType",
    "BundleEntryRequestType",
    "BundleEntryResponseType",
    "BundleEntrySearchType",
    "BundleLinkType",
    "CarePlanType",
    "CarePlanActivityType",
    "CarePlanActivityDetailType",
    "CarePlanParticipantType",
    "CarePlanRelatedPlanType",
    "ClaimType",
    "ClaimCoverageType",
    "ClaimDiagnosisType",
    "ClaimItemType",
    "ClaimItemDetailType",
    "ClaimItemDetailSubDetailType",
    "ClaimItemProsthesisType",
    "ClaimMissingTeethType",
    "ClaimPayeeType",
    "ClaimResponseType",
    "ClaimResponseAddItemType",
    "ClaimResponseAddItemAdjudicationType",
    "ClaimResponseAddItemDetailType",
    "ClaimResponseAddItemDetailAdjudicationType",
    "ClaimResponseCoverageType",
    "ClaimResponseErrorType",
    "ClaimResponseItemType",
    "ClaimResponseItemAdjudicationType",
    "ClaimResponseItemDetailType",
    "ClaimResponseItemDetailAdjudicationType",
    "ClaimResponseItemDetailSubDetailType",
    "ClaimResponseItemDetailSubDetailAdjudicationType",
    "ClaimResponseNoteType",
    "ClinicalImpressionType",
    "ClinicalImpressionFindingType",
    "ClinicalImpressionInvestigationsType",
    "ClinicalImpressionRuledOutType",
    "CommunicationType",
    "CommunicationPayloadType",
    "CommunicationRequestType",
    "CommunicationRequestPayloadType",
    "CompositionType",
    "CompositionAttesterType",
    "CompositionEventType",
    "CompositionSectionType",
    "ConceptMapType",
    "ConceptMapContactType",
    "ConceptMapElementType",
    "ConceptMapElementTargetType",
    "ConceptMapElementTargetDependsOnType",
    "ConditionType",
    "ConditionEvidenceType",
    "ConditionStageType",
    "ConformanceType",
    "ConformanceContactType",
    "ConformanceDocumentType",
    "ConformanceImplementationType",
    "ConformanceMessagingType",
    "ConformanceMessagingEndpointType",
    "ConformanceMessagingEventType",
    "ConformanceRestType",
    "ConformanceRestInteractionType",
    "ConformanceRestOperationType",
    "ConformanceRestResourceType",
    "ConformanceRestResourceInteractionType",
    "ConformanceRestSecurityType",
    "ConformanceRestSecurityCertificateType",
    "ConformanceSoftwareType",
    "ConformanceRestResourceSearchParamType",
    "EligibilityRequestType",
    "EligibilityResponseType",
    "PatientType",
    "PatientAnimalType",
    "PatientCommunicationType",
    "PatientContactType",
    "PatientLinkType",
    "OrganizationType",
    "OrganizationContactType",
    "PersonType",
    "PersonLinkType",
    "PractitionerType",
    "PractitionerPractitionerRoleType",
    "PractitionerQualificationType",
    "ValueSetType",
    "ValueSetCodeSystemType",
    "ValueSetCodeSystemConceptType",
    "ValueSetCodeSystemConceptDesignationType",
    "ValueSetComposeType",
    "ValueSetComposeIncludeType",
    "ValueSetComposeIncludeConceptType",
    "ValueSetComposeIncludeFilterType",
    "ValueSetContactType",
    "ValueSetExpansionType",
    "ValueSetExpansionContainsType",
    "ValueSetExpansionParameterType",
    "ProcedureType",
    "ProcedureFocalDeviceType",
    "ProcedurePerformerType",
    "ProcedureRequestType",
    "DiagnosticReportType",
    "DiagnosticReportImageType",
    "GoalType",
    "GoalOutcomeType",
    "GroupType",
    "GroupCharacteristicType",
    "GroupMemberType",
    "EncounterType",
    "EncounterHospitalizationType",
    "EncounterLocationType",
    "EncounterParticipantType",
    "EncounterStatusHistoryType",
    "EnrollmentRequestType",
    "EnrollmentResponseType",
    "ImmunizationType",
    "ImmunizationExplanationType",
    "ImmunizationReactionType",
    "ImmunizationVaccinationProtocolType",
    "MedicationAdministrationType",
    "MedicationAdministrationDosageType",
    "MedicationStatementType",
    "MedicationStatementDosageType",
    "ObservationType",
    "ObservationComponentType",
    "ObservationReferenceRangeType",
    "ObservationRelatedType",
    "OperationOutcomeType",
    "OperationOutcomeIssueType",
    "MedicationType",
    "MedicationPackageType",
    "MedicationPackageContentType",
    "MedicationProductType",
    "MedicationProductBatchType",
    "MedicationProductIngredientType",
    "ContractType",
    "ContractActorType",
    "ContractFriendlyType",
    "ContractLegalType",
    "ContractRuleType",
    "ContractSignerType",
    "ContractTermType",
    "ContractTermActorType",
    "ContractTermValuedItemType",
    "ContractValuedItemType",
    "DateTime",
    "Date",
    "DeviceType",
    "RelatedPersonType",
    "DetectedIssueType",
    "DetectedIssueMitigationType",
    "DataElementType",
    "DataElementContactType",
    "DataElementMappingType",
    "DeviceComponentType",
    "DeviceComponentProductionSpecificationType",
    "DeviceMetricType",
    "DeviceMetricCalibrationType",
    "DeviceUseRequestType",
    "DeviceUseStatementType",
    "DiagnosticOrderType",
    "DiagnosticOrderEventType",
    "DiagnosticOrderItemType",
    "Url",
    "Primitive",
    "Uuid",
    "Canonical",
    "ElementDefinitionType",
    "ElementDefinitionBaseType",
    "ElementDefinitionBindingType",
    "ElementDefinitionBindingValueSetType",
    "ElementDefinitionConstraintType",
    "EpisodeOfCareType",
    "EpisodeOfCareCareTeamType",
    "EpisodeOfCareStatusHistoryType",
    "FamilyMemberHistoryType",
    "FamilyMemberHistoryConditionType",
    "ExplanationOfBenefitType",
    "HealthcareServiceType",
    "HealthcareServiceAvailableTimeType",
    "HealthcareServiceNotAvailableType",
    "HealthcareServiceServiceTypeType",
    "ImagingObjectSelectionType",
    "ImagingObjectSelectionStudyType",
    "ImagingObjectSelectionStudySeriesType",
    "ImagingObjectSelectionStudySeriesInstanceType",
    "ImagingObjectSelectionStudySeriesInstanceFramesType",
    "ImagingStudyType",
    "ImagingStudySeriesType",
    "ImagingStudySeriesInstanceType",
    "ImmunizationRecommendationType",
    "ImmunizationRecommendationRecommendationType",
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "ImmunizationRecommendationRecommendationProtocolType",
    "ImplementationGuideType",
    "ImplementationGuideContactType",
    "ImplementationGuideDependencyType",
    "ImplementationGuideGlobalType",
    "ImplementationGuidePackageType",
    "ImplementationGuidePackageResourceType",
    "ImplementationGuidePageType",
    "ListType",
    "ListEntryType",
    "MedicationDispenseType",
    "MedicationDispenseDosageInstructionType",
    "MedicationDispenseSubstitutionType",
    "MedicationOrderType",
    "MedicationOrderDispenseRequestType",
    "MedicationOrderDosageInstructionType",
    "MedicationOrderSubstitutionType",
    "MessageHeaderType",
    "MessageHeaderDestinationType",
    "MessageHeaderResponseType",
    "MessageHeaderSourceType",
    "NamingSystemType",
    "NamingSystemContactType",
    "NamingSystemUniqueIdType",
    "NutritionOrderType",
    "NutritionOrderOralDietType",
    "NutritionOrderSupplementType",
    "NutritionOrderEnteralFormulaType",
    "NutritionOrderOralDietNutrientType",
    "NutritionOrderOralDietTextureType",
    "NutritionOrderEnteralFormulaAdministrationType",
    "OperationDefinitionType",
    "OperationDefinitionContactType",
    "OperationDefinitionParameterType",
    "OperationDefinitionParameterBindingType",
    "ParametersType",
    "ParametersParameterType",
    "ProcessResponseType",
    "ProcessResponseNotesType",
    "ProcessRequestType",
    "ProcessRequestItemType",
    "PaymentReconciliationType",
    "PaymentReconciliationDetailType",
    "PaymentReconciliationNoteType",
    "PaymentNoticeType",
    "ProvenanceType",
    "ProvenanceAgentType",
    "ProvenanceEntityType",
    "ProvenanceAgentRelatedAgentType",
    "QuestionnaireResponseType",
    "QuestionnaireResponseGroupType",
    "QuestionnaireResponseGroupQuestionType",
    "QuestionnaireResponseGroupQuestionAnswerType",
    "QuestionnaireType",
    "QuestionnaireGroupType",
    "QuestionnaireGroupQuestionType",
    "ReferralRequestType",
    "RiskAssessmentType",
    "RiskAssessmentPredictionType",
    "SearchParameterType",
    "SearchParameterContactType",
    "SubscriptionType",
    "SubscriptionChannelType",
    "SubstanceType",
    "SubstanceInstanceType",
    "SubstanceIngredientType",
    "SupplyDeliveryType",
    "SupplyRequestType",
    "SupplyRequestWhenType",
    "VisionPrescriptionType",
    "VisionPrescriptionDispenseType",
    "SpecimenType",
    "SpecimenCollectionType",
    "SpecimenTreatmentType",
    "SpecimenContainerType",
    "TestScriptType",
    "TestScriptContactType",
    "TestScriptMetadataType",
    "TestScriptFixtureType",
    "TestScriptVariableType",
    "TestScriptSetupType",
    "TestScriptTestType",
    "TestScriptTeardownType",
    "TestScriptMetadataLinkType",
    "TestScriptMetadataCapabilityType",
    "TestScriptSetupActionType",
    "TestScriptTestActionType",
    "TestScriptTeardownActionType",
    "TestScriptSetupActionOperationType",
    "TestScriptSetupActionAssertType",
    "TestScriptSetupActionOperationRequestHeaderType",
]
