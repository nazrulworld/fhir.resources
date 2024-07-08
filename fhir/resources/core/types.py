import dataclasses
import datetime
import decimal
import re
import typing
from functools import lru_cache
from uuid import UUID

from annotated_types import SLOTS, BaseMetadata, GroupedMetadata, MaxLen, MinLen
from pydantic import GetCoreSchemaHandler, AnyUrl, Base64Bytes
from pydantic._internal._fields import pydantic_general_metadata
from pydantic._internal._validators import import_string
from pydantic_core import PydanticCustomError
from pydantic_core import Url as PydanticUrl
from pydantic_core import ValidationError, core_schema
from pydantic_core.core_schema import ValidationInfo
from pydantic.types import UUID4

from .fhirabstractmodel import FHIRAbstractModel

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

FHIR_DATE_PARTS = re.compile(r"(?P<year>\d{4})(-(?P<month>\d{2}))?(-(?P<day>\d{2}))?$")
FHIR_PRIMITIVES = frozenset(
    [
        "boolean",
        "string",
        "base64Binary",
        "code",
        "id",
        "decimal",
        "integer",
        "integer64",
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
)


@dataclasses.dataclass(**SLOTS)
class FhirBase:
    """The base type aka validator for FHIR resource model.

    ```py
    from fhir.resources.core.fhirabstractmodel import FHIRAbstractModel
    from fhir.resources.core.types import FhirBase
    from pydantic import Field

    class Patient(FHIRAbstractModel):
        __resource_type__ = "Patient"
        name: str = Field(..., title="Patient name")

    PatientType = FhirBase(model_klass='fhir.resources.patient.Patient')

    class CarePlan(FHIRAbstractModel):
        __resource_type__ = "CarePlan"
        subject: PatientType = Field(..., title="Patient")

    care_plan = CarePlan(subject={'name': 'Petter paddle'})
    print(care_plan)
    #>  subject=Patient(name='Petter paddle')
    ```
    """

    model_klass: type[FHIRAbstractModel]

    def __init__(self, model_klass: str):
        """ """
        self.model_klass = import_string(model_klass)

    @classmethod
    @lru_cache(typed=True)
    def produce_inner_schema(
        cls, source_type: type[typing.Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if isinstance(source_type, cls):
            return handler.generate_schema(source_type.model_klass)
        if typing.get_origin(source_type) is not None:
            for tp in typing.get_args(source_type):
                inner_schema = cls.produce_inner_schema(tp, handler)
                if inner_schema:
                    return inner_schema

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type["FhirBase"], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the FHIR resource validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the FHIR resource validation.

        """
        inner_schema = cls.produce_inner_schema(source_type, handler)  # type: ignore
        if inner_schema is None:
            # show warning log
            inner_schema = core_schema.any_schema()

        def serialize(
            value: typing.Any, info: core_schema.SerializationInfo
        ) -> typing.Dict[str, typing.Any]:
            if typing.TYPE_CHECKING:
                value = typing.cast(FHIRAbstractModel, value)
            if info.mode == "json":
                # todo: what would be differences?
                return value.model_dump()
            else:
                return value.model_dump()

        def _validate(
            input_value: typing.Union[str, bytes, dict, FHIRAbstractModel],
            validator: typing.Callable[[FHIRAbstractModel], typing.Any],
            validation_info: ValidationInfo,
        ) -> FHIRAbstractModel:
            """
            Validate a MAC Address from the provided str value.

            Args:
                input_value: The str value to be validated.
                validator: The source type to be converted.
                validation_info: Validation info.

            Returns:
                FHIRAbstractModel: The parsed FHIR resource.

            """
            return validator(
                cls.fhir_model_validator(input_value, source_type.model_klass)
            )

        return core_schema.with_info_wrap_validator_function(
            _validate,
            inner_schema,
            serialization=core_schema.plain_serializer_function_ser_schema(
                serialize,
                info_arg=True,
                when_used="always",
            ),
        )

    @classmethod
    def fhir_model_validator(
        cls,
        value: typing.Union[str, bytes, dict, FHIRAbstractModel],
        model_klass: type[FHIRAbstractModel],
    ):
        """ """
        if isinstance(value, (str, bytes)):
            value = model_klass.model_validate_json(value)

        elif isinstance(value, dict):
            value = model_klass.model_validate(value)

        if not isinstance(value, model_klass):
            raise PydanticCustomError(
                "model_validation_format",
                "Value is expected from the instance of {model_class}, but got type {type}",
                {"model_class": model_klass.__name__, "type": type(value)},
            )

        if model_klass.__resource_type__ != value.__resource_type__:
            raise PydanticCustomError(
                "model_validation_format",
                'Expected resource_type is "{model_name}", but value has resource_type "{resource_type}"',
                {
                    "model_name": model_klass.__resource_type__,
                    "resource_type": value.__resource_type__,
                },
            )
        return value

    def __hash__(self) -> int:
        return hash(self.model_klass)


@dataclasses.dataclass(frozen=True, **SLOTS)
class String(GroupedMetadata):
    allow_empty_str: bool = False
    __visit_name__ = "string"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        regex = r"[ \r\n\t\S]+"
        if self.allow_empty_str:
            regex = r"(" + regex + r")|(^(?![\s\S]))"
        yield pydantic_general_metadata(pattern=regex)


@dataclasses.dataclass(frozen=True, **SLOTS)
class Base64Binary(GroupedMetadata):
    """A stream of bytes, base64 encoded (RFC 4648 )"""

    __visit_name__ = "base64Binary"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        regex = r"^(\s*([0-9a-zA-Z+=]){4}\s*)+$"
        yield pydantic_general_metadata(pattern=regex)

    @staticmethod
    def to_string(value):
        """ """
        assert isinstance(value, bytes)
        return value.decode()


@dataclasses.dataclass(frozen=True, **SLOTS)
class Code(GroupedMetadata):
    """Indicates that the value is taken from a set of controlled
    strings defined elsewhere (see Using codes for further discussion).
    Technically, a code is restricted to a string which has at least one
    character and no leading or trailing whitespace, and where there is
    no whitespace other than single spaces in the contents"""

    __visit_name__ = "code"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        regex = r"^[^\s]+(\s[^\s]+)*$"
        yield pydantic_general_metadata(pattern=regex)

    @staticmethod
    def to_string(value):
        """ """
        if isinstance(value, bytes):
            value = value.decode()
        assert isinstance(value, str)
        return value


@dataclasses.dataclass(frozen=True, **SLOTS)
class Id(GroupedMetadata):
    """Any combination of upper- or lower-case ASCII letters
    ('A'..'Z', and 'a'..'z', numerals ('0'..'9'), '-' and '.',
    with a length limit of 64 characters.
    (This might be an integer, an un-prefixed OID, UUID or any other identifier
    pattern that meets these constraints.)

    But it is possible to change the default behaviour by using configure_constraints()
    method!

    There are a lots of discussion about ``Resource.Id`` length of value.
        1. https://bit.ly/360HksL
        2. https://bit.ly/3o1fZgl
    We see there is some agreement and disagreement, because of that we decide to make
    it more flexible. Now it is possible configure three types of constraints.
    """

    pattern = r"^[A-Za-z0-9\-.]+$"
    min_length = 1
    max_length = 64
    __visit_name__ = "id"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        if self.min_length is not None:
            yield MinLen(self.min_length)
        if self.max_length is not None:
            yield MaxLen(self.max_length)
        if self.pattern:
            yield pydantic_general_metadata(pattern=self.pattern)

    @staticmethod
    def to_string(value):
        """ """
        if isinstance(value, bytes):
            value = value.decode()
        assert isinstance(value, str)
        return value


@dataclasses.dataclass(**SLOTS)
class Decimal:
    """Rational numbers that have a decimal representation.
    See below about the precision of the number"""

    pattern = re.compile(r"^-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?$")
    __visit_name__ = "decimal"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type["Decimal"], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the FHIR resource validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the FHIR resource validation.

        """

        def _validate(
            input_value: decimal.Decimal,
        ) -> decimal.Decimal:
            """
            Validate a MAC Address from the provided str value.

            Args:
                input_value: The Decimal value to be validated.
            Returns:
                FHIRAbstractModel: The parsed FHIR resource.

            """
            if not cls.pattern.match(str(input_value)):
                raise ValueError
            return input_value

        return core_schema.no_info_after_validator_function(
            _validate,
            core_schema.decimal_schema(),
        )

    @classmethod
    def to_string(cls, value):
        """ """
        assert isinstance(value, decimal.Decimal)
        return str(float(value))

    def __hash__(self) -> int:
        return hash(self.__class__)


@dataclasses.dataclass(frozen=True, **SLOTS)
class Integer(GroupedMetadata):
    """A signed integer in the range −2,147,483,648..2,147,483,647 (32-bit;
    for larger values, use decimal)"""

    pattern = re.compile(r"^[0]|[-+]?[1-9][0-9]*$")
    min_length: int = -2147483648
    max_length: int = 2147483647

    __visit_name__ = "integer"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        yield MinLen(self.min_length)

        yield MaxLen(self.max_length)

    @classmethod
    def to_string(cls, value):
        """ """
        assert isinstance(value, int)
        return str(value)


class Integer64(Integer):
    """A signed integer in the range
    -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807 (64-bit).
    This type is defined to allow for record/time counters that can get very large"""

    min_length: int = -9223372036854775808
    max_length: int = 9223372036854775807
    __visit_name__ = "integer64"


class UnsignedInt(Integer):
    """Any non-negative integer in the range 0..2,147,483,647"""

    regex = re.compile(r"^[0]|([1-9][0-9]*)$")
    __visit_name__ = "unsignedInt"
    min_length = 0


class PositiveInt(UnsignedInt):
    """Any positive integer in the range 1..2,147,483,647"""

    regex = re.compile(r"^\+?[1-9][0-9]*$")
    __visit_name__ = "positiveInt"
    min_length = 1


@dataclasses.dataclass(frozen=True, **SLOTS)
class PatternConstraint(GroupedMetadata):
    pattern: re.Pattern = None

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        yield pydantic_general_metadata(pattern=self.pattern)


class Uri(PatternConstraint):
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
    pattern = re.compile(r"\S*")

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, bytes):
            value = value.decode()
        assert isinstance(value, str)
        return value


class Oid(PatternConstraint):
    """An OID represented as a URI (RFC 3001 ); e.g. urn:oid:1.2.3.4.5"""

    __visit_name__ = "oid"
    pattern = re.compile(r"^urn:oid:[0-2](\.(0|[1-9][0-9]*))+$")

    @staticmethod
    def to_string(value):
        """ """
        if isinstance(value, bytes):
            value = value.decode()
        assert isinstance(value, str)
        return value


class Uuid:
    """A UUID (aka GUID) represented as a URI (RFC 4122 );
    e.g. urn:uuid:c757873d-ec9a-4326-a141-556f43239520"""

    __visit_name__ = "uuid"

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, UUID):
            value = f"urn:uuid:{value}"
        assert isinstance(value, str)
        return value


class Canonical(Uri):
    """A URI that refers to a resource by its canonical URL (resources with a url property).
    The canonical type differs from a uri in that it has special meaning in this specification,
    and in that it may have a version appended, separated by a vertical bar (|).
    Note that the type canonical is not used for the actual canonical URLs that are
    the target of these references, but for the URIs that refer to them, and may have
    the version suffix in them. Like other URIs, elements of type canonical may also have
    #fragment references"""

    __visit_name__ = "canonical"

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, bytes):
            value = value.decode()
        assert isinstance(value, str)
        return value


@dataclasses.dataclass(frozen=True, **SLOTS)
class Url:
    """A Uniform Resource Locator (RFC 1738 ).
    Note URLs are accessed directly using the specified protocol.
    Common URL protocols are http{s}:, ftp:, mailto: and mllp:,
    though many others are defined"""

    path_pattern = re.compile(r"^/(?P<resourceType>[^\s?/]+)(/[^\s?/]+)*")
    __visit_name__ = "url"

    @classmethod
    @lru_cache(typed=True)
    def produce_inner_schema(
        cls, source_type: type[typing.Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if source_type is str:
            return core_schema.str_schema()
        if source_type is PydanticUrl:
            return core_schema.url_schema()
        if typing.get_origin(source_type) is not None:
            for tp in typing.get_args(source_type):
                inner_schema = cls.produce_inner_schema(tp, handler)
                if inner_schema:
                    return inner_schema

    @classmethod
    def _validate_url(  # type: ignore
        cls,
        input_value: typing.Union[str, PydanticUrl],
        validator: typing.Callable[[typing.Union[str, PydanticUrl]], typing.Any],
    ) -> typing.Union[str, PydanticUrl]:
        """ """
        # todo: check with 'mailto:', 'mllp:', 'llp:'
        # todo: validate email?
        # if input_value.startswith("mailto:"):
        #    schema = input_value[0:7]
        #    email = input_value[7:]
        #    realname = parseaddr(email)[0]
        #    name, email = validate_email(email)
        #    if realname:
        #        email = formataddr((name, email))
        #    return schema + email

        if input_value in FHIR_PRIMITIVES:
            # Extensions may contain a valueUrl for a primitive FHIR type
            # no further validation
            return input_value

        try:
            return validator(input_value)
        except ValidationError as exc:
            # we are allowing relative path
            if not input_value.startswith("/"):
                matched = cls.path_pattern.match("/" + input_value)
            else:
                matched = cls.path_pattern.match(input_value)
            if matched is not None:
                if re.match(
                    r"^[A-Za-z0-9\-.#]+$", matched.groupdict().get("resourceType", "")
                ):
                    # @ToDo: required resource type validation?
                    return input_value
            raise

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type["Decimal"], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the FHIR resource validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the FHIR resource validation.

        """
        inner_schema = cls.produce_inner_schema(source_type, handler)

        def _validate(
            input_value: typing.Union[str, PydanticUrl],
            validator: typing.Callable[[typing.Union[str, PydanticUrl]], typing.Any],
            validation_info: ValidationInfo,
        ) -> typing.Union[str, PydanticUrl]:
            """
            Validate a MAC Address from the provided str value.

            Args:
                input_value: The Decimal value to be validated.
            Returns:
                FHIRAbstractModel: The parsed FHIR resource.

            """
            if isinstance(input_value, PydanticUrl):
                return validator(input_value)
            return cls._validate_url(input_value, validator)

        return core_schema.with_info_wrap_validator_function(
            _validate,
            inner_schema,
        )

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, PydanticUrl):
            value = str(value)
        if isinstance(value, bytes):
            value = value.decode()
        assert isinstance(value, str)
        return value


class Markdown(PatternConstraint):
    """A FHIR string (see above) that may contain markdown syntax for optional processing
    by a markdown presentation engine, in the GFM extension of CommonMark format (see below)
    """

    __visit_name__ = "markdown"
    pattern = re.compile(r"\s*(\S|\s)*")


class Xhtml:  # type:ignore
    __visit_name__ = "xhtml"

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, bytes):
            value = value.decode()
        assert isinstance(value, str)
        return value


@dataclasses.dataclass(frozen=True, **SLOTS)
class Date:
    """A date, or partial date (e.g. just year or year + month)
    as used in human communication. The format is YYYY, YYYY-MM, or YYYY-MM-DD,
    e.g. 2018, 1973-06, or 1905-08-23.
    There SHALL be no time zone. Dates SHALL be valid dates"""

    pattern = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2]"
        r"[0-9]|3[0-1]))?)?"
    )
    __visit_name__ = "date"

    @classmethod
    def produce_inner_schema(cls):
        """ """
        return core_schema.date_schema()

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type[typing.Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the FHIR resource validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the FHIR resource validation.

        """

        # inner_schema = cls.produce_inner_schema(source_type, handler)

        def _validate(
            input_value: typing.Union[str, PydanticUrl],
            validator: typing.Callable[[typing.Union[str, PydanticUrl]], typing.Any],
            validation_info: ValidationInfo,
        ) -> typing.Union[str, PydanticUrl]:
            """
            Validate a MAC Address from the provided str value.

            Args:
                input_value: The Decimal value to be validated.
            Returns:
                FHIRAbstractModel: The parsed FHIR resource.

            """
            return cls._validate_date(input_value, validator)

        return core_schema.with_info_wrap_validator_function(
            _validate,
            cls.produce_inner_schema(),
        )

    @classmethod
    def _validate_date(
        cls,
        input_value: typing.Union[datetime.date, str],
        validator: typing.Callable[[typing.Union[str, datetime.date]], typing.Any],
    ) -> typing.Union[datetime.date, str]:
        """ """
        if not isinstance(input_value, str):
            # default handler
            return validator(input_value)

        match = FHIR_DATE_PARTS.match(input_value)
        if match and not match.groupdict().get("day"):
            if match.groupdict().get("month") and int(match.groupdict()["month"]) > 12:
                raise ValueError
            # we keep original
            return input_value

        return validator(input_value)

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, (datetime.date, datetime.time, datetime.datetime)):
            value = value.isoformat()
        assert isinstance(value, str)
        return value


class DateTime(Date):
    """A date, date-time or partial date (e.g. just year or year + month) as used
    in human communication. The format is YYYY, YYYY-MM, YYYY-MM-DD or
    YYYY-MM-DDThh:mm:ss+zz:zz, e.g. 2018, 1973-06, 1905-08-23,
    2015-02-07T13:28:17-05:00 or 2017-01-01T00:00:00.000Z.
    If hours and minutes are specified, a time zone SHALL be populated.
    Seconds must be provided due to schema type constraints but may be
    zero-filled and may be ignored at receiver discretion.
    Dates SHALL be valid dates. The time "24:00" is not allowed.
    Leap Seconds are allowed - see below"""

    pattern = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|"
        r"3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|"
        r"60)(\.[0-9]+)?(Z|([+\-])((0[0-9]|"
        r"1[0-3]):[0-5][0-9]|14:00)))?)?)?"
    )
    __visit_name__ = "dateTime"

    @classmethod
    def produce_inner_schema(cls):
        """ """
        return core_schema.datetime_schema()


class Instant(DateTime):
    """An instant in time in the format YYYY-MM-DDThh:mm:ss.sss+zz:zz
    (e.g. 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z).
    The time SHALL specified at least to the second and SHALL include a time zone.
    Note: This is intended for when precisely observed times are required
    (typically system logs etc.), and not human-reported times - for those,
    use date or dateTime (which can be as precise as instant,
    but is not required to be). instant is a more constrained dateTime

    Note: This type is for system times, not human times (see date and dateTime below).
    """

    pattern = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|"
        r"3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]"
        r"|60)(\.[0-9]+)?(Z|([+\-])((0[0-9]|"
        r"1[0-3]):[0-5][0-9]|14:00))"
    )
    __visit_name__ = "instant"


@dataclasses.dataclass(frozen=True, **SLOTS)
class Time:
    """A time during the day, in the format hh:mm:ss.
    There is no date specified. Seconds must be provided due
    to schema type constraints but may be zero-filled and may
    be ignored at receiver discretion.
    The time "24:00" SHALL NOT be used. A time zone SHALL NOT be present.
    Times can be converted to a Duration since midnight."""

    pattern = re.compile(r"([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?")
    __visit_name__ = "time"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type[typing.Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the FHIR resource validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the FHIR resource validation.

        """

        # inner_schema = cls.produce_inner_schema(source_type, handler)

        def _validate(
            input_value: typing.Union[str, PydanticUrl],
            validator: typing.Callable[[typing.Union[str, PydanticUrl]], typing.Any],
            validation_info: ValidationInfo,
        ) -> typing.Union[str, PydanticUrl]:
            """
            Validate a MAC Address from the provided str value.

            Args:
                input_value: The Decimal value to be validated.
            Returns:
                FHIRAbstractModel: The parsed FHIR resource.

            """
            return cls._validate_time(input_value, validator)

        return core_schema.with_info_wrap_validator_function(
            _validate,
            core_schema.date_schema(),
        )

    @classmethod
    def _validate_time(cls, input_value, validator):
        """ """
        if isinstance(input_value, str):
            if not cls.pattern.match(input_value):
                raise ValueError

        return validator(input_value)

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, (datetime.date, datetime.time, datetime.datetime)):
            value = value.isoformat()
        assert isinstance(value, str)
        return value


# **************************************
# ****  FHIR Primitive Types ***********
# **************************************
FHIR_PRIMITIVES_MAPS = {}

# boolean
BooleanType = bool
FHIR_PRIMITIVES_MAPS[BooleanType] = "boolean"

# string
StringType = typing.Annotated[str, String(allow_empty_str=False)]
FHIR_PRIMITIVES_MAPS[StringType] = "string"

# base64Binary
Base64BinaryType = typing.Annotated[Base64Bytes, Base64Binary()]
FHIR_PRIMITIVES_MAPS[Base64BinaryType] = "base64Binary"

# code
CodeType = typing.Annotated[str, Code()]
FHIR_PRIMITIVES_MAPS[CodeType] = "code"

# id
IdType = typing.Annotated[str, Id()]
FHIR_PRIMITIVES_MAPS[IdType] = "id"

# decimal
DecimalType = typing.Annotated[decimal.Decimal, Decimal()]
FHIR_PRIMITIVES_MAPS[DecimalType] = "decimal"

# integer
IntegerType = typing.Annotated[int, Integer()]
FHIR_PRIMITIVES_MAPS[IntegerType] = "integer"

# integer64
Integer64Type = typing.Annotated[int, Integer64()]
FHIR_PRIMITIVES_MAPS[Integer64Type] = "integer64"

# unsignedInt
UnsignedIntType = typing.Annotated[int, UnsignedInt()]
FHIR_PRIMITIVES_MAPS[UnsignedIntType] = "unsignedInt"

# positiveInt
PositiveIntType = typing.Annotated[int, PositiveInt()]
FHIR_PRIMITIVES_MAPS[PositiveIntType] = "positiveInt"

# uri
UriType = typing.Annotated[str, Uri()]
FHIR_PRIMITIVES_MAPS[UriType] = "uri"

# canonical
CanonicalType = typing.Annotated[str, Canonical()]
FHIR_PRIMITIVES_MAPS[CanonicalType] = "canonical"

# oid
OidType = typing.Annotated[str, Oid()]
FHIR_PRIMITIVES_MAPS[OidType] = "oid"

# uuid
UuidType = UUID4
FHIR_PRIMITIVES_MAPS[UuidType] = "uuid"

# url
UrlType = typing.Annotated[typing.Union[AnyUrl, str], Url()]
FHIR_PRIMITIVES_MAPS[UrlType] = "url"

# markdown
MarkdownType = typing.Annotated[str, Markdown()]
FHIR_PRIMITIVES_MAPS[MarkdownType] = "markdown"

# xhtml
XhtmlType = typing.Annotated[str, Xhtml()]
FHIR_PRIMITIVES_MAPS[XhtmlType] = "xhtml"

# date
DateType = typing.Annotated[datetime.date, Date()]
FHIR_PRIMITIVES_MAPS[DateType] = "date"

# dateTime
DateTimeType = typing.Annotated[datetime.datetime, DateTime()]
FHIR_PRIMITIVES_MAPS[DateTimeType] = "dateTime"

# instant
InstantType = typing.Annotated[datetime.datetime, Instant()]
FHIR_PRIMITIVES_MAPS[InstantType] = "instant"

# time
TimeType = typing.Annotated[datetime.time, Time()]
FHIR_PRIMITIVES_MAPS[TimeType] = "time"

__all__ = [
    "FhirBase",
    "BooleanType",
    "StringType",
    "Base64BinaryType",
    "CodeType",
    "IdType",
    "IntegerType",
    "Integer64Type",
    "DecimalType",
    "UnsignedIntType",
    "PositiveIntType",
    "CanonicalType",
    "UriType",
    "OidType",
    "UuidType",
    "UrlType",
    "MarkdownType",
    "XhtmlType",
    "DateType",
    "DateTimeType",
    "InstantType",
    "TimeType",
]
