=======
History
=======

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
