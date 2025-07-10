=======
History
=======

8.1.0 (2025-07-10)
------------------

New features

- Issue #181 ``summary`` (https://www.hl7.org/fhir/search.html#_summary) mode feature added.

Fixes

- Issue #184 pyright struggles with default position args.
- Issue #186 missing py.typed marker, causing mypy import errors.
- Issue #183 Pydantic 2.11+ Deprecation Warnings: model_fields Should Be Accessed on Class, Not Instance.

8.0.0 (2024-12-25)
------------------

- The minimum required version for ``fhir-core`` is ``1.0.0``, which obviously comes with new features and bug fixes. For example xml serialization/deserialization. `See changes log here <https://github.com/nazrulworld/fhir-core/blob/1.0.0/HISTORY.rst#100-2024-12-25>`_

- Issue #168 https://github.com/nazrulworld/fhir.resources/issues/166

8.0.0b4 (2024-10-24)
--------------------

-  `PR#160 <https://github.com/nazrulworld/fhir.resources/pull/160>`_ switch the type of Element.id from id to string for R4B [cybernop]


8.0.0b3 (2024-10-10)
--------------------

- Minimum version of ``fhir-core`` package have been updated.
- All of fhir resources are regenerated for to comply with the optionality of fhir model's field. Issue https://github.com/nazrulworld/fhir.resources/issues/164


8.0.0b2 (2024-10-02)
--------------------

- `Issue #164 <https://github.com/nazrulworld/fhir.resources/issues/164>`_ ``get_fhir_model_class`` is now available and can be imported from base package. For example ``from fhir.resources import get_fhir_model_class`` or ``from fhir.resources.STU3 import get_fhir_model_class``


8.0.0b1 (2024-08-05)
--------------------

Breaking

- Drop support for python 3.7

- FHIR DTU2 packages are no longer available.


7.1.0 (2023-12-14)
------------------

New features

See migration guide.

Breaking

- Drop support for python 3.6.
- Drop support for pydantic v1.
- The function ``FHIRAbstractModel::add_root_validator`` is no longer available.

Deprecations

Some of functions from ``FHIRAbstractModel`` are deprecated to comply with Pydantic V2. Some are

- ``FHIRAbstractModel::dict``

- ``FHIRAbstractModel::json``

- ``FHIRAbstractModel::parse_obj``

- ``FHIRAbstractModel::parse_raw``: no longer supports xml and yaml data.

- ``FHIRAbstractModel::parse_file``: no longer supports xml and yaml file.



Improvements

- `Issue 133 <https://github.com/nazrulworld/fhir.resources/issues/133>`_ Pydantic 2.0 migration plan. It's not fully migration though, instead of using of Pydantic V1 API.
- `Issue 144 <https://github.com/nazrulworld/fhir.resources/issues/144>`_ Parsing XML byte string MESH acknowledgment response.


7.0.2 (2023-07-03)
------------------

-  `Issue 124 <https://github.com/nazrulworld/fhir.resources/issues/134>`_ on the wake of 2.x pydantic release, pydantic's max version restriction added.


7.0.1 (2023-05-29)
------------------

Fixes

- Issue #128 `pkg_resources.declare_namespace deprecation <https://github.com/nazrulworld/fhir.resources/issues/128>`_

- Issue #129 `urn not supported in Url <https://github.com/nazrulworld/fhir.resources/issues/129>`_

7.0.0 (2023-04-08)
------------------

New Feature

- Support for `FHIR version R5 <https://www.hl7.org/fhir/R5/resourcelist.html>`_ has been added under root package.


Breaking

- All root resources (FHIR version R4B) are moved under sub-package ``R4B``. Have a look at the migration guide.


6.5.0 (2023-01-01)
------------------

Breaking

- FHIR R4B release has been overlapped on current R4 as default release. See changes (Release R4B: May 28, 2022) http://hl7.org/fhir/R4B/history.html. More detail at http://hl7.org/fhir/R4B/diff.html

Improvements

- Issue #90 logging level downgraded from warning to debug.
- Primitive `URL` type is now accepting the relative path without prefix "/".


6.4.0 (2022-05-11)
------------------

Bugfixes

- Fix, primitive extension was not included if primitive field value is null. [nazrulworld]
- Issue `#101 ElementDefinition.id typing is incorrect <https://github.com/nazrulworld/fhir.resources/issues/101>`_

Improvements

- Issue `#97 <https://github.com/nazrulworld/fhir.resources/issues/97>`_ Now null value accepted as a member of String List.
- Primitive DataType `Ùrl`` is now accepting relative path.

Breaking

- ``Element.id`` & ``Resource.id`` don't have any extension. See https://chat.fhir.org/#narrow/stream/179166-implementers/topic/Resource.2Eid.20and.20primitive.20extension.

6.2.2 (2022-04-02)
------------------

- Issue `#96 <https://github.com/nazrulworld/fhir.resources/issues/96>`_, fixes datetime's ISO format representation for YAML. [nazrulworld]


6.2.1 (2022-01-14)
------------------

- Issues `#89 <https://github.com/nazrulworld/fhir.resources/issues/89>`_ & `#90 <https://github.com/nazrulworld/fhir.resources/issues/90>`_ possible breaking for ``FHIRAbstractModel.dict`` (if pydnatic specific extra argument has been provided) is neutralized.[nazrulworld]


6.2.0 (2022-01-01)
------------------

Bugfixes

- Issue #88 fixes typo mistake. Resource name const  was wrong. [nazrulworld]


6.2.0b3 (2021-06-26)
--------------------

New Feature

- String type class is now configurable, it is possible to allow empty str value.

Bugfixes

- Issue #75 Remove "tests" from installed package.
- Issue `#74 When are Falsy values evaluated as None? <https://github.com/nazrulworld/fhir.resources/issues/74>`_

- Fixes some issues for DSTU2 https://github.com/nazrulworld/fhir.resources/pull/71 & https://github.com/nazrulworld/fhir.resources/pull/70 [ItayGoren]


6.2.0b2 (2021-04-05)
--------------------

New Feature

- Parsing YAML file or string/bytes contents, now accept extra parameter ``loader`` class.
- Parsing from XML file or string/bytes contents are now supported. With possible to provide xmlparser for schema validation purpose.

Bugfixes

- Added correct fhir version name into Primitive Type Base class for ``STU3`` and ``DSTU2``.


6.2.0b1 (2021-03-31)
--------------------

New Feature

- `Issue #47 <https://github.com/nazrulworld/fhir.resources/issues/47>`_ add YAML support.
- `Issue #51 <https://github.com/nazrulworld/fhir.resources/issues/51>`_ Help on converting XML to FHIR format.
- `Issue #63 <https://github.com/nazrulworld/fhir.resources/issues/63>`_ Now JSON output key's sequence is matching with original FHIR specification.

Breaking

- ``FHIRAbstractModel.json()`` and ``FHIRAbstractModel.dict()`` parameters signatures are more FHIR specific and additional parameters are removed (pydantic specific).


Bugfixes

- Added missing ``element_property`` field attribute for class ``FHIRPrimitiveExtension``.

6.1.0 (2021-02-13)
------------------

- Breaking/Fixes: `PR#48 <https://github.com/nazrulworld/fhir.resources/pull/48>`_ ``Resource.id`` type has been replaced with ``fhirtypes.Id`` from ``fhirtypes.String`` (only for R4) [ItayGoren]

- Fixes: constraints regex for fhirtypes ``Id``, ``Code``, ``Integer``, ``Decimal``, ``UnsignedInt``, ``PositiveInt`` and so on. [nazrulworld]


6.0.0 (2020-12-17)
------------------

- Issue #21 Remaining resources are added. [iatechicken]


6.0.0b11 (2020-11-25)
---------------------

- Fixes: wrong ``ClaimResponseAddItemAdjudicationType`` resource type name into ``DTSU2``.


6.0.0b10 (2020-11-15)
---------------------

Improvements

- ``FHIRAbstractModel::add_root_validator`` is more improved and practical with proper validation, more now possible provide class method as root validator.


Bugfixes

- `Issue #41 <https://github.com/nazrulworld/fhir.resources/issues/41>`_ pydantic.errors.ConfigError: duplicate validator function.

6.0.0b9 (2020-11-05)
--------------------

Improvements

- Now supports of ``simplejson`` is available automatically (depends on importable) along side with ``orjson`` and default ``json`` library.
  Order of json serializer available (orjson -> simplejson(as fallback) -> json(as default)).

Breaking

- ``orjson`` is not available by default, have to use extra_require ``orjson`` to available that.


6.0.0b8 (2020-11-02)
--------------------

- ``pydantic`` minimum version has been set to ``1.7.2``.


6.0.0b7 (2020-10-31)
--------------------

*If you face import error ``from pydantic.utils import ROOT_KEY``, please upgrade your pydnatic version to <1.7*

Fixes

- `Issue #39 <https://github.com/nazrulworld/fhir.resources/issues/39>`_ added compatibility with ``pydantic`` version between ``1.6.x`` and ``1.7.x`` [nazrulworld]

Improvements

- Issue #40 `Make fhir primitive element field optional if extension value is provided. <https://github.com/nazrulworld/fhir.resources/issues/40>`_

6.0.0b6 (2020-10-24)
--------------------

Improvements

- ``FHIRAbstractModel::json`` now takes additional parameter ``return_bytes``, indicates json string would be bytes. [nazrulworld]

- Issue#38 Add support for FHIR comments. As per suggestion of comments in json from `Grahame Grieve <http://www.healthintersections.com.au/?p=2569>`_, now ``fhir_comments`` is accepted. [nazrulworld]

- FHIR comments filter option is added in ``FHIRAbstractModel::json``, means it is possible to exclude any comments while generating json string by providing parameter ``exclude_comments`` value. [nazrulworld]

- More FHIR DSTU2 resources have been added. [Itay Goren]

6.0.0b5 (2020-10-04)
--------------------

Improvements

- ``visionprescription`` and ``supplyrequest`` resources added for DSTU2 [iatechicken]

Fixes

- Issue #28 `'construct_fhir_element' change the given dict <https://github.com/nazrulworld/fhir.resources/issues/28>`_


6.0.0b4 (2020-09-24)
--------------------

Improvements

- orjson_ supports have been available as default json ``dumps`` and ``loads`` for Model.

- ``FHIRAbstractModel::get_json_encoder`` class method now available, which return pydantic compatible json encoder callable, can be used with any json serializer.

- More DSTU2 FHIR Resources have added, https://github.com/nazrulworld/fhir.resources/issues/21. Thanks to [mmabey].

Fixes

- Fixes URL validation in the case where a primitive type is used as URL (which is allowed in StructureDefinition). [simonvadee]

- Fixes `Issue#19 <https://github.com/nazrulworld/fhir.resources/issues/19>`_ Getting validation errors that don't make sense.


6.0.0b3 (2020-08-07)
--------------------

- ``FHIRAbstractModel::get_resource_type`` class method now available, which returning name of the resource.


6.0.0b2 (2020-07-09)
--------------------

- ``FHIRAbstractModel::element_properties`` class method now available, which returning generator of ``ModelField``,
  those are elements of the resource.

- Minor fixes on ``enum_values``.

6.0.0b1 (2020-07-05)
--------------------

Revolutionary evolution has been made, now fully rewritten with modern python, underlying APIs (almost all) have been changed.
Please have look at readme section, for howto.

Improvements

- Full support of FHIR `Extensibility <https://www.hl7.org/fhir/extensibility.html>`_ for `Primitive Data Types <https://www.hl7.org/fhir/datatypes.html#primitive>`_

Breaking

- Drop support for python 2.7.



5.1.0 (2020-04-11)
------------------

Improvements

- FHIR ``STU3`` release version upgraded from ``3.0.1`` to ``3.0.2``, Please find changes history here https://www.hl7.org/fhir/history.html.

- FHIR ``R4`` release version upgraded from ``4.0.0`` to ``4.0.1``, find changes history here https://www.hl7.org/fhir/history.html.


5.0.1 (2019-07-18)
------------------

Bugfixes:

- `Issue#5 <https://github.com/nazrulworld/fhir.resources/issues/5>`_ confusing error message "name 'self' is not defined" [nazrulworld]


5.0.0 (2019-06-08)
------------------

- Nothing but release stable version.


5.0.0b3 (2019-05-14)
--------------------

New features

- Isuue#1 `Add DSTU2 Support <https://github.com/nazrulworld/fhir.resources/issues/1>`_


5.0.0b2 (2019-05-13)
--------------------

Breaking or Improvments

- ``elementProperties``: element now has extra property ``type_name``. Now format like ``(name, json_name, type, type_name, is_list, "of_many", not_optional)``
  The ``type_name`` refers original type name (code) from FHIR Structure Definition and it would be very helpful while
  making fhir search, fhirpath navigator.



5.0.0b1 (2019-01-19)
--------------------

New features

- Implemented own build policy, now previous version of FHIR® resources are available as python sub-package.

Build info

- Default version is ``R4`` (see version info at `4.0.0b1 (2019-01-13)` section)

- ``STU3`` (see version info at `3.0.1 (2019-01-13)` section)


4.0.0 (2019-01-14)
------------------

- see version info at ``4.0.0b1`` section.


4.0.0b1 (2019-01-13)
--------------------

`Version Info (R4)`_ ::

    [FHIR]
    FhirVersion=4.0.0-a53ec6ee1b
    version=4.0.0
    buildId=a53ec6ee1b
    date=20181227223754



3.0.1 (2019-01-13)
------------------

`Version Info (STU3)`_ ::

    [FHIR]
    FhirVersion=3.0.1.11917
    version=3.0.1
    revision=11917
    date=20170419074443


.. _`Version Info (STU3)`: http://hl7.org/fhir/stu3/
.. _`Version Info (R4)`: http://hl7.org/fhir/R4/
