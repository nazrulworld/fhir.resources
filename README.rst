=================================
FHIR® Resources (R4, STU3, DSTU2)
=================================


.. image:: https://img.shields.io/pypi/v/fhir.resources.svg
        :target: https://pypi.python.org/pypi/fhir.resources

.. image:: https://img.shields.io/pypi/pyversions/fhir.resources.svg
        :target: https://pypi.python.org/pypi/fhir.resources
        :alt: Supported Python Versions

.. image:: https://img.shields.io/travis/nazrulworld/fhir.resources.svg
        :target: https://travis-ci.org/nazrulworld/fhir.resources

.. image:: https://codecov.io/gh/nazrulworld/fhir.resources/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/nazrulworld/fhir.resources

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://fire.ly/wp-content/themes/fhir/images/fhir.svg
        :target: https://www.hl7.org/implement/standards/product_brief.cfm?product_id=449
        :alt: HL7® FHIR®



Powered by pydantic_, all `FHIR Resources <https://www.hl7.org/fhir/resourcelist.html>`_ are available as python class with built-in
data validation, faster in performance and by default ``orjson`` is included as performance booster! Written in modern python.

* Easy to construct, easy to extended validation, easy to export.
* By inheriting behaviour from pydantic_, compatible with `ORM <https://en.wikipedia.org/wiki/Object-relational_mapping>`_.
* Full support of FHIR® Extensibility for Primitive Data Types are available.
* Previous release of FHIR® Resources are available.
* Free software: BSD license


FHIR® Version Info
------------------

FHIR® (Release R4, version 4.0.1) is available as default. Also previous versions are available as Python sub-package
(each release name string becomes sub-package name, i.e ``STU3`` ).

**Available Previous Versions**:

* ``STU3`` (3.0.2)
* ``DSTU2`` (1.0.2) [partially see `issue#13 <https://github.com/nazrulworld/fhir.resources/issues/13>`_]


Installation
------------

Just a simple ``pip install fhir.resources`` or ``easy_install fhir.resources`` is enough. But if you want development
version, just clone from https://github.com/nazrulworld/fhir.resources and ``pip install -e .[all]``.


Usages
------

**Example: 1**: Construct Resource Model object::

    >>> from fhir.resources.organization import Organization
    >>> from fhir.resources.address import Address
    >>> data = {
    ...     "id": "f001",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": [{"country": "Swizterland"}]
    ... }
    >>> org = Organization(**data)
    >>> org.resource_type == "Organization"
    True
    >>> isinstance(org.address[0], Address)
    >>> True
    >>> org.address[0].country == "Swizterland"
    True
    >>> org.dict()['active'] is True
    True

**Example: 2**: Resource object created from json string::

    >>> from fhir.resources.organization import Organization
    >>> from fhir.resources.address import Address
    >>> json_str = '''{"resourceType": "Organization",
    ...     "id": "f001",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": [{"country": "Swizterland"}]
    ... }'''
    >>> org = Organization.parse_raw(json_str)
    >>> isinstance(org.address[0], Address)
    >>> True
    >>> org.address[0].country == "Swizterland"
    True
    >>> org.dict()['active'] is True
    True


**Example: 3**: Resource object created from json object(py dict)::

    >>> from fhir.resources.patient import Patient
    >>> from fhir.resources.humanname import HumanName
    >>> from datetime import date
    >>> json_obj = {"resourceType": "Patient",
    ...     "id": "p001",
    ...     "active": True,
    ...     "name": [
    ...         {"text": "Adam Smith"}
    ...      ],
    ...     "birthDate": "1985-06-12"
    ... }
    >>> pat = Patient.parse_obj(json_obj)
    >>> isinstance(pat.name[0], HumanName)
    >>> True
    >>> org.birthDate == date(year=1985, month=6, day=12)
    True
    >>> org.active is True
    True


**Example: 4**: Construct Resource object from json file::

    >>> from fhir.resources.patient import Patient
    >>> import os
    >>> import pathlib
    >>> filename = pathlib.Path("foo/bar.json")
    >>> pat = Patient.parse_file(filename)
    >>> pat.resource_type == "Patient"
    True


**Example: 5**: Construct resource object in python way::

    >>> from fhir.resources.organization import Organization
    >>> from fhir.resources.address import Address
    >>> json_obj = {"resourceType": "Organization",
    ...     "id": "f001",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": [{"country": "Swizterland"}]
    ... }

    >>> org = Organization.construct()
    >>> org.id = "f001"
    >>> org.active = True
    >>> org.name = "Acme Corporation"
    >>> org.address = list()
    >>> address = Address.construct()
    >>> address.country = "Swizterland"
    >>> org.address.append(address)
    >>> org.dict() == json_obj
    True


**Example: 4**: Using Resource Factory Function::

    >>> from fhir.resources import construct_fhir_element
    >>> json_dict = {"resourceType": "Organization",
    ...     "id": "mmanu",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": [{"country": "Swizterland"}]
    ... }
    >>> org = construct_fhir_element('Organization', json_dict)
    >>> org.address[0].country == "Swizterland"
    True
    >>> org.dict()['active'] is True
    True


**Example: 5**: Auto validation while providing wrong datatype::

    >>> try:
    ...     org = Organization({"id": "fmk", "address": ["i am wrong type"]})
    ...     raise AssertionError("Code should not come here")
    ... except ValueError:
    ...     pass



Advanced Usages
---------------

FHIR Comments (JSON)
~~~~~~~~~~~~~~~~~~~~

It is possible to add comments inside json like xml, but need to follow some convention, what is suggested by `Grahame Grieve <http://www.healthintersections.com.au/?p=2569>`_;
That is implemented here.

Also it is possible to generate json string output without comments.

Examples::

    >>> observation_str = b"""{
    ...  "resourceType": "Observation",
    ...  "id": "f001",
    ...    "fhir_comments": [
    ...      "   a specimen identifier - e.g. assigned when the specimen was taken by the orderer/placer  use the accession number for the filling lab   ",
    ...      "  Placer ID  "
    ...    ],
    ...  "text": {
    ...      "fhir_comments": [
    ...      "   a specimen identifier - e.g. assigned when the specimen was taken by the orderer/placer  use the accession number for the filling lab   ",
    ...      "  Placer ID  "
    ...    ],
    ...    "status": "generated",
    ...    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">.........</div>"
    ...  },
    ...  "identifier": [
    ...    {
    ...      "use": "official",
    ...      "system": "http://www.bmc.nl/zorgportal/identifiers/observations",
    ...      "value": "6323"
    ...    }
    ...  ],
    ...  "status": "final",
    ...  "_status": {
    ...      "fhir_comments": [
    ...            "  EH: Note to balloters  - lots of choices for whole blood I chose this.  "
    ...          ]
    ...  },
    ...  "code": {
    ...    "coding": [
    ...      {
    ...        "system": "http://loinc.org",
    ...        "code": "15074-8",
    ...        "display": "Glucose [Moles/volume] in Blood"
    ...      }
    ...    ]
    ...  },
    ...  "subject": {
    ...    "reference": "Patient/f001",
    ...    "display": "P. van de Heuvel"
    ...  },
    ...  "effectivePeriod": {
    ...    "start": "2013-04-02T09:30:10+01:00"
    ...  },
    ...  "issued": "2013-04-03T15:30:10+01:00",
    ...  "performer": [
    ...    {
    ...      "reference": "Practitioner/f005",
    ...      "display": "A. Langeveld"
    ...    }
    ...  ],
    ...  "valueQuantity": {
    ...    "value": 6.3,
    ...    "unit": "mmol/l",
    ...    "system": "http://unitsofmeasure.org",
    ...    "code": "mmol/L"
    ...  },
    ...  "interpretation": [
    ...    {
    ...      "coding": [
    ...        {
    ...          "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
    ...          "code": "H",
    ...          "display": "High"
    ...        }
    ...      ]
    ...    }
    ...  ],
    ...  "referenceRange": [
    ...    {
    ...      "low": {
    ...        "value": 3.1,
    ...        "unit": "mmol/l",
    ...        "system": "http://unitsofmeasure.org",
    ...        "code": "mmol/L"
    ...      },
    ...      "high": {
    ...        "value": 6.2,
    ...        "unit": "mmol/l",
    ...        "system": "http://unitsofmeasure.org",
    ...        "code": "mmol/L"
    ...      }
    ...    }
    ...  ]
    ... }"""
    >>> from fhir.resources.observation import Observation
    >>> obj = Observation.parse_raw(observation_str)
    >>> "fhir_comments" in obj.json()
    >>> # Test comments filtering
    >>> "fhir_comments" not in obj.json(exclude_comments=True)

*Unfortunately comments filtering is not available for FHIRAbstractModel::dict*


Special Case: Missing data
~~~~~~~~~~~~~~~~~~~~~~~~~~

`In some cases <https://www.hl7.org/fhir/extensibility.html#Special-Case>`_, implementers might
find that they do not have appropriate dta for an element with minimum cardinality = 1.
In this case, the element must be present, but unless the resource or a profile on it has made the
actual value of the primitive data type mandatory, it is possible to provide an extension that
explains why the primitive value is not present.
Example (required ``intent`` element is missing but still valid because of extension)::

    >>> json_str = b"""{
    ...    "resourceType": "MedicationRequest",
    ...    "id": "1620518",
    ...    "meta": {
    ...        "versionId": "1",
    ...        "lastUpdated": "2020-10-27T11:04:42.215+00:00",
    ...        "source": "#z072VeAlQWM94jpc",
    ...        "tag": [
    ...            {
    ...                "system": "http://www.alpha.alp/use-case",
    ...                "code": "EX20"
    ...            }
    ...        ]
    ...    },
    ...    "status": "completed",
    ...    "_intent": {
    ...        "extension": [
    ...            {
    ...                "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
    ...                "valueCode": "unknown"
    ...            }
    ...        ]
    ...    },
    ...    "medicationReference": {
    ...        "reference": "Medication/1620516",
    ...        "display": "Erythromycin 250 MG Oral Tablet"
    ...    },
    ...    "subject": {
    ...        "reference": "Patient/1620472"
    ...    },
    ...    "encounter": {
    ...        "reference": "Encounter/1620506",
    ...        "display": "Follow up encounter"
    ...    },
    ...    "authoredOn": "2018-06-16",
    ...    "requester": {
    ...        "reference": "Practitioner/1620502",
    ...        "display": "Dr. Harold Hippocrates"
    ...    },
    ...    "reasonReference": [
    ...        {
    ...            "reference": "Condition/1620514",
    ...            "display": "Otitis Media"
    ...        }
    ...    ],
    ...    "dosageInstruction": [
    ...        {
    ...            "text": "250 mg 4 times per day for 10 days",
    ...            "timing": {
    ...                "repeat": {
    ...                    "boundsDuration": {
    ...                        "value": 10,
    ...                        "unit": "day",
    ...                        "system": "http://unitsofmeasure.org",
    ...                        "code": "d"
    ...                    },
    ...                    "frequency": 4,
    ...                    "period": 1,
    ...                    "periodUnit": "d"
    ...                }
    ...            },
    ...            "doseAndRate": [
    ...                {
    ...                    "doseQuantity": {
    ...                        "value": 250,
    ...                        "unit": "mg",
    ...                        "system": "http://unitsofmeasure.org",
    ...                        "code": "mg"
    ...                    }
    ...                }
    ...            ]
    ...        }
    ...    ],
    ...    "priorPrescription": {
    ...        "reference": "MedicationRequest/1620517",
    ...        "display": "Amoxicillin prescription"
    ...    }
    ... }"""
    >>> from fhir.resources.medicationrequest import MedicationRequest
    >>> obj = MedicationRequest.parse_raw(json_str)
    >>> "intent" not in obj.dict()


Custom Validators
~~~~~~~~~~~~~~~~~

``fhir.resources`` is providing extensive API to create and attach custom validator into any model. See more `about root validator <https://pydantic-docs.helpmanual.io/usage/validators/#root-validators>`_
Some convention you have to follow while creating a root validator.

1. Number of arguments are fixed, as well as names are also. i.e ``(cls, values)``.
2. Should return ``values``, unless any exception need to be raised.
3. Validator should be attached only one time for individual Model.

Example 1: Validator for Patient::

    from typing import Dict
    from fhir.resources.patient import Patient

    import datetime

    def validate_birthdate(cls, values: Dict):
        if not values:
            return values
        if "birthDate" not in values:
            raise ValueError("Patient's ``birthDate`` is required.")

        minimum_date = datetime.date(2002, 1, 1)
        if values["birthDate"] > minimum_date:
            raise ValueError("Minimum 18 years patient is allowed to use this system.")
        return values
    # we want this validator to execute after data evaluating by individual field validators.
    Patient.add_root_validator(validate_gender, pre=False)



ENUM Validator
~~~~~~~~~~~~~~

``fhir.resources`` is providing API for enum constraint for each field (where applicable), but it-self doesn't
enforce enum based validation! see `discussion here <https://github.com/nazrulworld/fhir.resources/issues/23>`_.
If you want to enforce enum constraint, you have to create a validator for that.

Example: Gender Enum::

    from typing import Dict
    from fhir.resources.patient import Patient

    def validate_gender(cls, values: Dict):
        if not values:
            return values
        enums = cls.__fields__["gender"].field_info.extra["enum_values"]
        if "gender" in values and values["gender"] not in enums:
            raise ValueError("write your message")
        return values

    Patient.add_root_validator(validate_gender, pre=True)


Reference Validator
~~~~~~~~~~~~~~~~~~~

``fhir.resources`` is also providing enum like list of permitted resource types through field property ``enum_reference_types``.
You can get that list by following above (Enum) approaches  ``resource_types = cls.__fields__["managingOrganization"].field_info.extra["enum_reference_types"]``


Migration (from later than ``6.X.X``)
-------------------------------------

This migration guide states some underlying changes of ``API`` and replacement, those are commonly used from later than ``6.X.X`` version.


``fhir.resources.fhirelementfactory.FHIRElementFactory::instantiate``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Replacement:** ``fhir.resources.construct_fhir_element``

- First parameter value is same as previous, the Resource name.

- Second parameter is more flexible than previous! it is possible to provide not only json ``dict`` but also
  json string or json file path.

- No third parameter, what was in previous version.


``fhir.resources.fhirabstractbase.FHIRAbstractBase::__init__``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Replacement:** ``fhir.resources.fhirabstractmodel.FHIRAbstractModel::parse_obj<classmethod>``

- First parameter value is same as previous, json dict.

- No second parameter, what was in previous version.


``fhir.resources.fhirabstractbase.FHIRAbstractBase::as_json``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Replacement:** ``fhir.resources.fhirabstractmodel.FHIRAbstractModel::dict``

- Output are almost same previous, but there has some difference in case of some date type, for example py date,
  datetime, Decimal are in object representation.

- It is possible to use ``fhir.resources.fhirabstractmodel.FHIRAbstractModel::json`` as replacement, when
  json string is required (so not need further, json dumps from dict)


Note:

All resources/classes are derived from ``fhir.resources.fhirabstractmodel.FHIRAbstractModel`` what was previously
from ``fhir.resources.fhirabstractbase.FHIRAbstractBase``.


Release and Version Policy
--------------------------

Starting from  version ``5.0.0`` we are following our own release policy and we although follow Semantic Versioning scheme like FHIR® version.
Unlike previous statement (bellow), releasing now is not dependent on FHIR®.


**removed statement**

    This package is following `FHIR® release and versioning policy <https://www.hl7.org/fhir/versions.html>`_, for example say, FHIR releases next version 4.0.1,
    we also release same version here.


Credits
-------

All FHIR® Resources (python classes) are generated using fhir-parser_ which is forked from https://github.com/smart-on-fhir/fhir-parser.git.


This package skeleton was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`fhir-parser`: https://github.com/nazrulworld/fhir-parser
.. _`pydantic`: https://pydantic-docs.helpmanual.io/r

© Copyright HL7® logo, FHIR® logo and the flaming fire are registered trademarks
owned by `Health Level Seven International <https://www.hl7.org/legal/trademarks.cfm?ref=https://pypi.org/project/fhir-resources/>`_

.. role:: strike
    :class: strike
