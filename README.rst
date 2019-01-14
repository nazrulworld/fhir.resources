====================
FHIR® Resources (R4)
====================


.. image:: https://img.shields.io/pypi/v/fhir.resources.svg
        :target: https://pypi.python.org/pypi/fhir.resources

.. image:: https://img.shields.io/pypi/pyversions/fhir.resources.svg
        :target: https://pypi.python.org/pypi/fhir.resources
        :alt: Supported Python Versions

.. image:: https://img.shields.io/travis/nazrulworld/fhir.resources.svg
        :target: https://travis-ci.org/nazrulworld/fhir.resources

.. image:: https://codecov.io/gh/nazrulworld/fhir.resources/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/nazrulworld/fhir.resources


.. image:: https://fire.ly/wp-content/themes/fhir/images/fhir.svg
        :target: https://www.hl7.org/implement/standards/product_brief.cfm?product_id=449
        :alt: HL7® FHIR®



All `FHIR Resources <https://www.hl7.org/fhir/R4/resourcelist.html>`_ are available as python class with built-in
initial validation, exporter as json value.


* Free software: BSD license
* FHIR ResourceList: https://www.hl7.org/fhir/R4/resourcelist.html

Installation
------------

Just a simple ``pip install fhir.resources`` or ``easy_install fhir.resources`` is enough. But if you want development
version, just clone from https://github.com/nazrulworld/fhir.resources and ``python setup.py install``.


**Example: 1**: Resource object created from json string::


    >>> from fhir.resources.organization import Organization
    >>> from fhir.resources.address import Address
    >>> json_dict = {"resourceType": "Organization",
    ...     "id": "mmanu",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": [{"country": "Swizterland"}]
    ... }
    >>> org = Organization(json_dict)
    >>> isinstance(org.address[0], Address)
    >>> True
    >>> org.address[0].country == "Swizterland"
    True
    >>> org.as_json()['active'] is True
    True


**Example: 2**: Construct resource object in python way::


    >>> org = Organization()
    >>> org.id = "mmanu"
    >>> org.active = True
    >>> org.name = "Acme Corporation"
    >>> org.address = list()
    >>> address = Address()
    >>> address.country = "Swizterland"
    >>> org.address.append(address)
    >>> org.as_json() == json_dict
    True


**Example: 3**: Auto validation while providing wrong datatype::

    >>> from fhir.resources.fhirabstractbase import FHIRValidationError
    >>> try:
    ...     org = Organization({"id": "fmk", "address": ["i am wrong type"]})
    ...     raise AssertionError("Code should not come here")
    ... except FHIRValidationError:
    ...     pass



Release and Version Policy
--------------------------

This package is following `FHIR® release and versioning policy <https://www.hl7.org/fhir/versions.html>`_, for example say, FHIR releases next version 4.0.1,
we also release same version here.


Credits
-------

All FHIR® Resources (python classes) are generated using fhir-parser_.


This package skeleton was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`fhir-parser`: https://github.com/smart-on-fhir/fhir-parser.git

© Copyright HL7® logo, FHIR® logo and the flaming fire are registered trademarks
owned by `Health Level Seven International <https://www.hl7.org/legal/trademarks.cfm?ref=https://pypi.org/project/fhir-resources/>`_
