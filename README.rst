===============================
FHIR® Resources (R5, R4B, STU3)
===============================

.. image:: https://img.shields.io/pypi/v/fhir.resources.svg
        :target: https://pypi.python.org/pypi/fhir.resources

.. image:: https://img.shields.io/pypi/pyversions/fhir.resources.svg
        :target: https://pypi.python.org/pypi/fhir.resources
        :alt: Supported Python Versions

.. image:: https://img.shields.io/travis/com/nazrulworld/fhir.resources.svg
        :target: https://app.travis-ci.com/github/nazrulworld/fhir.resources

.. image:: https://ci.appveyor.com/api/projects/status/0qu5vyue1jwxb4km?svg=true
        :target: https://ci.appveyor.com/project/nazrulworld/fhir-resources
        :alt: Windows Build

.. image:: https://codecov.io/gh/nazrulworld/fhir.resources/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/nazrulworld/fhir.resources

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://static.pepy.tech/personalized-badge/fhir-resources?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads
    :target: https://pepy.tech/project/fhir-resources
    :alt: Downloads

.. image:: https://www.hl7.org/fhir/assets/images/fhir-logo-www.png
        :target: https://www.hl7.org/implement/standards/product_brief.cfm?product_id=449
        :alt: HL7® FHIR®


FHIR_ (Fast Healthcare Interoperability Resources) is a specification for exchanging healthcare information electronically.
It is designed to facilitate the exchange of data between different healthcare systems and applications, and is commonly used to build APIs (Application Programming Interfaces) for healthcare data.
It is based on modern web technologies, and is designed to be easy to use and implement.
It uses a modular approach, with a set of "resources" that represent different types of healthcare data (such as patients, observations, and diagnoses).
These resources can be combined and extended as needed to support a wide range of healthcare use cases.


This "fhir.resources" package is powered by pydantic_ V2, so it become faster in performance.
Obviously it is written in modern python and has data validation built-in.
It provides tools and classes for all of the `FHIR Resources <https://www.hl7.org/fhir/resourcelist.html>`_ defined in the FHIR specification,
and allows you to create and manipulate FHIR resources in Python. You can then use these resources to build FHIR-based APIs or to work with FHIR data in other ways.


* Easy to construct, easy to extended validation, easy to export.
* By inheriting behaviour from pydantic_, compatible with `ORM <https://en.wikipedia.org/wiki/Object-relational_mapping>`_.
* Full support of FHIR® Extensibility for Primitive Data Types are available.
* Previous release of FHIR® Resources are available.
* Free software: BSD license

**Experimental XML and YAML serialization and deserialization supports. See [Advanced Usages] section!**

FHIR® Version Info
------------------

FHIR® (Release R5, version 5.0.0) is available as default. Also previous versions are available as Python sub-package
(each release name string becomes sub-package name, i.e ``R4B`` ).
From ``fhir.resources`` version 7.0.0; there is no FHIR ``R4`` instead of ``R4B`` is available as sub-package.

**Available Previous Versions**:

* ``R4B`` (4.3.0)
* ``STU3`` (3.0.2)

Installation
------------

Just a simple ``pip install fhir.resources`` is enough. But if you want development
version, just clone from https://github.com/nazrulworld/fhir.resources and ``pip install -e .[dev]``.


Usages
------

**Example: 1**: This example creates a new Organization resource with some of its attributes (id, active, name, address)::

    >>> from fhir.resources.organization import Organization
    >>> from fhir.resources.address import Address
    >>> data = {
    ...     "id": "f001",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": [{"country": "Switzerland"}]
    ... }
    >>> org = Organization(**data)
    >>> org.get_resource_type() == "Organization"
    True
    >>> isinstance(org.address[0], Address)
    True
    >>> org.address[0].country == "Switzerland"
    True
    >>> org.model_dump()['active'] is True
    True

**Example: 2**: This example creates a new Organization resource from json string::

    >>> from fhir.resources.organization import Organization
    >>> from fhir.resources.address import Address
    >>> json_str = '''{"resourceType": "Organization",
    ...     "id": "f001",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": [{"country": "Switzerland"}]
    ... }'''
    >>> org = Organization.model_validate_json(json_str)
    >>> isinstance(org.address[0], Address)
    True
    >>> org.address[0].country == "Switzerland"
    True
    >>> org.dict()['active'] is True
    True


**Example: 3**: This example creates a new Patient resource from json object(py dict)::

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
    >>> pat = Patient.model_validate(json_obj)
    >>> isinstance(pat.name[0], HumanName)
    True
    >>> pat.birthDate == date(year=1985, month=6, day=12)
    True
    >>> pat.active is True
    True


**Example: 4**: This example creates a new Patient resource from json file::

    >>> from fhir.resources.patient import Patient
    >>> import os
    >>> import pathlib
    >>> filename = pathlib.Path("foo/bar.json")
    >>> pat = Patient.model_validate_json(filename.read_bytes())
    >>> pat.get_resource_type() == "Patient"
    True


**Example: 5**: This example creates a new Organization resource in python way::

    >>> from fhir.resources.organization import Organization
    >>> from fhir.resources.address import Address
    >>> json_obj = {"resourceType": "Organization",
    ...     "id": "f001",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": [{"country": "Switzerland"}]
    ... }

    >>> org = Organization.model_construct()
    >>> org.id = "f001"
    >>> org.active = True
    >>> org.name = "Acme Corporation"
    >>> org.address = list()
    >>> address = Address.model_construct()
    >>> address.country = "Switzerland"
    >>> org.address.append(address)
    >>> org.model_dump() == json_obj
    True

.. note::
    Please note that due to the way the validation works, you will run into issues if you are using ``model_construct()`` to create
    resources that have more than one mandatory field. See `this comment in issue#56 <https://github.com/nazrulworld/fhir.resources/issues/56#issuecomment-784520234>`_ for details.


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
is implemented here.

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
    >>> obj = Observation.model_validate_json(observation_str)
    >>> "fhir_comments" in obj.model_dump_json()
    >>> # Test comments filtering
    >>> "fhir_comments" not in obj.model_dump_json(exclude_comments=True)


Special Case: Missing data
~~~~~~~~~~~~~~~~~~~~~~~~~~

`In some cases <https://www.hl7.org/fhir/extensibility.html#Special-Case>`_, implementers might
find that they do not have appropriate data for an element with minimum cardinality = 1.
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
    >>> obj = MedicationRequest.model_validate_json(json_str)
    >>> "intent" not in obj.model_dump()


Custom Validators
~~~~~~~~~~~~~~~~~
**This feature is not available**

``fhir.resources`` is providing the extensive API to create and attach custom validator into any model. See more `about root validator <https://pydantic-docs.helpmanual.io/usage/validators/#root-validators>`_
Some convention you have to follow though, while creating a root validator.

1. Number of arguments are fixed, as well as names are also. i.e ``(cls, values)``.
2. Should return ``values``, unless any exception need to be raised.
3. Validator should be attached only one time for individual Model. Update [from now, it's not possible to attach multiple time same name validator on same class]

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


Example 2: Validator for Patient from Validator Class::

    from typing import Dict
    from fhir.resources.patient import Patient

    import datetime

    class MyValidator:
        @classmethod
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
    Patient.add_root_validator(MyValidator.validate_gender, pre=False)


**important notes** It is possible add root validator into any base class like ``DomainResource``.
In this case you have to make sure root validator is attached before any import of derived class, other
than validator will not trigger for successor class (if imported before) by nature.

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
        enums = cls.model_fields["gender"].json_schema_extra["enum_values"]
        if "gender" in values and values["gender"] not in enums:
            raise ValueError("write your message")
        return values

    Patient.add_root_validator(validate_gender, pre=True)


Reference Validator
~~~~~~~~~~~~~~~~~~~

``fhir.resources`` is also providing enum like list of permitted resource types through json_schema_extra ``enum_reference_types``.
You can get that list by following above (Enum) approaches  ``resource_types = cls.model_fields["managingOrganization"].json_schema_extra["enum_reference_types"]``



pydantic_ Field Type Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All available fhir resources (types) can be use as pydantic_'s Field's value types. See issue#46 `Support for FastAPI pydantic response models <https://github.com/nazrulworld/fhir.resources/issues/46>`_.
The module ``fhirtypes.py`` contains all fhir resources related types and should trigger validator automatically.


``Resource.id aka fhirtypes.Id`` constraint extensibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are a lots of discussion here here i.) https://bit.ly/360HksL ii.) https://bit.ly/3o1fZgl about the length of ``Resource.Id``'s value.
Based on those discussions, we recommend that keep your ``Resource.Id`` size within 64 letters (for the seek of intercompatibility with third party system), but we are also providing freedom
about the length of Id, in respect with others opinion that 64 chr length is not sufficient, so default length is now 255.
But it is offering to customize as your own requirement by doing a monkey patch.

Examples::
    # ``patch.py``
    >>> import importlib
    >>> from fhir_core import constraints
    >>> from fhir_core import types as ftypes
    >>> constraints.TYPES_ID_MAX_LENGTH = 64
    >>> importlib.reload(ftypes)

Note: when you will change that behaviour, that would impact into your whole project.


XML Supports
~~~~~~~~~~~~
Along side with JSON string export, it is possible to export as XML string!
Before using this feature, make sure associated dependent library is installed. Use ``fhir.resources[xml]`` or ``fhir.resources[all]`` as
your project requirements.

**XML schema validator!**
It is possible to provide custom xmlparser, during load from file or string, meaning that you can validate
data against FHIR xml schema(and/or your custom schema).

Example-1 Export::
    >>> from fhir.resources.patient import Patient
    >>> data = {"active": True, "gender": "male", "birthDate": "2000-09-18", "name": [{"text": "Primal Kons"}]}
    >>> patient_obj = Patient(**data)
    >>> xml_str = patient_obj.model_dump_xml(pretty_print=True)
    >>> print(xml_str)
    <?xml version='1.0' encoding='utf-8'?>
    <Patient xmlns="http://hl7.org/fhir">
      <active value="true"/>
      <name>
        <text value="Primal Kons"/>
      </name>
      <gender value="male"/>
      <birthDate value="2000-09-18"/>
    </Patient>


Example-2 Import from string::
    >>> from fhir.resources.patient import Patient
    >>> data = {"active": True, "gender": "male", "birthDate": "2000-09-18", "name": [{"text": "Primal Kons"}]}
    >>> patient_obj = Patient(**data)
    >>> xml_str = patient_obj.model_dump_xml(pretty_print=True)
    >>> print(xml_str)
    >>> data = b"""<?xml version='1.0' encoding='utf-8'?>
    ... <Patient xmlns="http://hl7.org/fhir">
    ...   <active value="true"/>
    ...   <name>
    ...     <text value="Primal Kons"/>
    ...   </name>
    ...   <gender value="male"/>
    ...   <birthDate value="2000-09-18"/>
    ... </Patient>"""
    >>> patient = Patient.model_validate_xml(data)
    >>> print(patient.model_dump_json(indent=2))
    {
      "resourceType": "Patient",
      "active": true,
      "name": [
        {
          "text": "Primal Kons",
          "family": "Kons",
          "given": [
            "Primal"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "2000-09-18"
    }

    >>> with xml parser
    >>> import lxml
    >>> from fhir_core.xml_utils import xml_loads
    >>> schema = lxml.etree.XMLSchema(file=str(FHIR_XSD_DIR / "patient.xsd"))
    >>> xmlparser = lxml.etree.XMLParser(schema=schema)
    >>> patient2 = xml_loads(Patient, data, xmlparser=xmlparser)
    >>> patient2 == patient
    True

Example-3 Import from file::
    >>> import pathlib
    >>> patient3 = Patient.model_validate_xml(pathlib.Path("Patient.xml").read_bytes())
    >>> patient3 == patient and patient3 == patient2
    True


**XML FAQ**

    - Although generated XML is validated against ``FHIR/patient.xsd`` and ``FHIR/observation.xsd`` in tests, but we suggest you check output of your production data.
    - Comment feature is included, but we recommend you check in your complex usages.


YAML Supports
~~~~~~~~~~~~~

Although there is no official support for YAML documented in FHIR specification, but as an experimental feature, we add this support.
Now it is possible export/import YAML strings.
Before using this feature, make sure associated dependent library is installed. Use ``fhir.resources[yaml]`` or ``fhir.resources[all]`` as
your project requirements.

Example-1 Export::
    >>> from fhir.resources.patient import Patient
    >>> data = {"active": True, "gender": "male", "birthDate": "2000-09-18", "name": [{"text": "Primal Kons", "family": "Kons", "given": ["Primal"]}]}
    >>> patient_obj = Patient(**data)
    >>> yml_str = patient_obj.model_dump_yaml(indent=2)
    >>> print(yml_str)
    resourceType: Patient
    active: true
    name:
    - text: Primal Kons
      family: Kons
      given:
      - Primal
    gender: male
    birthDate: 2000-09-18


Example-2 Import from YAML string::
    >>> from fhir.resources.patient import Patient
    >>> data = b"""
    ... resourceType: Patient
    ... active: true
    ... name:
    ... - text: Primal Kons
    ...   family: Kons
    ...   given:
    ...   - Primal
    ...  gender: male
    ...  birthDate: 2000-09-18
    ... """
    >>> patient_obj = Patient.model_validate_yaml(data)
    >>> json_str = patient_obj.model_dump_json(indent=2)
    >>> print(json_str)
    {
      "resourceType": "Patient",
      "active": true,
      "name": [
        {
          "text": "Primal Kons",
          "family": "Kons",
          "given": [
            "Primal"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "2000-09-18"
    }

Example-3 Import from YAML file::
    >>> import pathlib
    >>> from fhir.resources.patient import Patient
    >>> patient_obj = Patient.model_validate_yaml(pathlib.Path("Patient.yml").read_bytes())
    >>> json_str = patient_obj.model_dump_json(indent=2)
    >>> print(json_str)
    {
      "resourceType": "Patient",
      "active": true,
      "name": [
        {
          "text": "Primal Kons",
          "family": "Kons",
          "given": [
            "Primal"
          ]
        }
      ],
      "gender": "male",
      "birthDate": "2000-09-18"
    }


**YAML FAQ**

- We are using https://pyyaml.org/ PyYAML library, for serialization/deserialization but if we find more faster library, we could use that. you are welcome to provide us your suggestion.
- YAML based comments is not supported yet, instead json comments syntax is used! Of course this comment feature is in our todo list.


Allow Empty String
~~~~~~~~~~~~~~~~~~

Although this is not good practice to allow empty string value against FHIR primitive data type ``String``. But
we in real life scenario, is it unavoidable sometimes.

Examples::
    Place this code inside your __init__.py module or any place, just to make sure that this fragment of codes is runtime executed.

    >>> # ``__init__.py``
    >>> import importlib
    >>> from fhir_core import constraints
    >>> from fhir_core import types as ftypes
    >>> constraints.TYPES_STRING_ALLOW_EMPTY_STR = True
    >>> importlib.reload(ftypes)


FHIR ``summary`` search support
-------------------------------
This package is providing supporting ´´summary mode´´ activated serialization, meaning that you will not need to do extra, if you are planning to support `summary search <https://www.hl7.org/fhir/search.html#_summary>`_

Example::

    >>> from fhir.resources.organization import Organization
    >>> json_str = '''{"resourceType": "Organization",
    ...     "text": {"status": "generated", "div": "<p>summary example</p>"}
    ...     "id": "f001",
    ...     "active": True,
    ...     "name": "Acme Corporation"
    ... }'''
    >>> org = Organization.model_validate_json(json_str)
    >>> summary_dict = org.model_dump(summary_only=True)
    >>> "text" not in summary_dict
    True
    >>> "active" in summary_dict
    True
    >>> "name" in summary_dict

FHIR release R4B over R4
------------------------

FHIR release R4B is coming with not that much changes over the release of R4. So we decided not to create separate sub-package for R4 like STU3, instead there just overlaps on existing R4. This also means that in future, when we will work on R5; there will be sub-package for R4B and no R4.
We suggest you to try make a plan to be upgraded to R4B. Here you could find related information dealing-strategy-R4-R4B_.

You could find full discussion here https://github.com/nazrulworld/fhir.resources/discussions/116

Migration (from ``7.X.X`` to ``8.X.X``)
---------------------------------------

There is no breaking changes in terms of api/functions. But it is recommended that you should use new functions from Pydantic V2
instead of using deprecated functions.

Replacements and/or new functions.

- From ``FHIRAbstractModel::dict`` to ``FHIRAbstractModel::model_dump``
- From ``FHIRAbstractModel::json`` to ``FHIRAbstractModel::model_dump_json``
- From ``FHIRAbstractModel::yaml`` to ``FHIRAbstractModel::model_dump_yaml``
- From ``FHIRAbstractModel::xml`` to ``FHIRAbstractModel::model_dump_xml``
- From ``FHIRAbstractModel::parse_obj`` to ``FHIRAbstractModel::model_validate``
- From ``FHIRAbstractModel::parse_raw`` to ``FHIRAbstractModel::model_validate_json``
- From ``FHIRAbstractModel::parse_file`` to no replacement, we suggest you use pathlib (see examples)
- ``FHIRAbstractModel::model_validate_yaml`` parse YAML string to FHIRAbstractModel.
- ``FHIRAbstractModel::model_validate_xml`` parse XML string to FHIRAbstractModel.


Breaking: removed attributes and/or functions/methods.

- The attribute ``resource_type`` has been removed from base FHIR class. For example no more ``Resource.resource_type`` attribute. Now you have to use Resource.get_resource_type() instead. Although "resource_type" key is available when you will serialize as json or python dict.

Migration (from ``6.X.X`` to ``7.0.X``)
---------------------------------------

First of all, you have to correct all imports path, if you wish to keep continue using FHIR release R4B or R4, as those resources
are moved under sub-package named ``R4B``. Then if you wish to use current ``R5`` release,
read carefully the following documents.

1. See the full changes history -> https://build.fhir.org/history.html
2. See complete lists of differences between R5 and R4B -> https://hl7.org/fhir/R5/diff.html
3. If you are planning to migrate direct from the release ``R4``,
   then it is important to look at the differences between R4B and R4 here -> https://hl7.org/fhir/R4B/diff.html


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
.. _`pydantic`: https://pydantic-docs.helpmanual.io/
.. _`orjson`: https://pypi.org/project/orjson/
.. _`dealing-strategy-R4-R4B`: https://confluence.hl7.org/display/FHIR/Strategies+for+dealing+with+R4+and+R4B
.. _`FHIR`: https://www.hl7.org/implement/standards/product_brief.cfm

© Copyright HL7® logo, FHIR® logo and the flaming fire are registered trademarks
owned by `Health Level Seven International <https://www.hl7.org/legal/trademarks.cfm?ref=https://pypi.org/project/fhir-resources/>`_

.. role:: strike
    :class: strike
.. role:: raw-html(raw)
    :format: html
