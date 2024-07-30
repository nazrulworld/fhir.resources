# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Organization
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import organization
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_organization_1(inst):
    assert inst.alias[0] == "HL7 International"
    assert inst.contact[0].address.city == "Ann Arbor"
    assert inst.contact[0].address.country == "USA"
    assert inst.contact[0].address.line[0] == "3300 Washtenaw Avenue, Suite 227"
    assert inst.contact[0].address.postalCode == "48104"
    assert inst.contact[0].address.state == "MI"
    assert (
        inst.contact[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/extended-contact-availability"
            }
        ).valueUri
    )
    assert (
        inst.contact[0].extension[0].valueAvailability.availableTime[0].availableEndTime
        == ExternalValidatorModel.model_validate({"valueTime": "07:00:00"}).valueTime
    )
    assert (
        inst.contact[0]
        .extension[0]
        .valueAvailability.availableTime[0]
        .availableStartTime
        == ExternalValidatorModel.model_validate({"valueTime": "09:00:00"}).valueTime
    )
    assert (
        inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[0]
        == "mon"
    )
    assert (
        inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[1]
        == "tue"
    )
    assert (
        inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[2]
        == "wed"
    )
    assert (
        inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[3]
        == "thu"
    )
    assert (
        inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[4]
        == "fri"
    )
    assert (
        inst.contact[0].extension[0].valueAvailability.notAvailableTime[0].description
        == "Public holidays"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "(+1) 734-677-7777"
    assert inst.contact[0].telecom[1].system == "fax"
    assert inst.contact[0].telecom[1].value == "(+1) 734-677-6622"
    assert inst.contact[0].telecom[2].system == "email"
    assert inst.contact[0].telecom[2].value == "hq@HL7.org"
    assert inst.endpoint[0].reference == "Endpoint/example"
    assert inst.id == "hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Health Level Seven International"
    assert inst.text.status == "generated"


def test_organization_1(base_settings):
    """No. 1 tests collection for Organization.
    Test File: organization-example.json
    """
    filename = base_settings["unittest_data_dir"] / "organization-example.json"
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_1(inst2)


def impl_organization_2(inst):
    assert inst.active is True
    assert inst.contact[0].address.country == "Swizterland"
    assert inst.id == "mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Acme Corporation"
    assert inst.text.status == "generated"


def test_organization_2(base_settings):
    """No. 2 tests collection for Organization.
    Test File: organization-example-mmanu.json
    """
    filename = base_settings["unittest_data_dir"] / "organization-example-mmanu.json"
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_2(inst2)


def impl_organization_3(inst):
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "mobile"
    assert inst.contact[0].telecom[0].value == "+1 555 234 3523"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "gastro@acme.org"
    assert inst.id == "1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.acme.org.au/units"}
        ).valueUri
    )
    assert inst.identifier[0].value == "Gastro"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Gastroenterology"
    assert inst.text.status == "generated"


def test_organization_3(base_settings):
    """No. 3 tests collection for Organization.
    Test File: organization-example-gastro.json
    """
    filename = base_settings["unittest_data_dir"] / "organization-example-gastro.json"
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_3(inst2)


def impl_organization_4(inst):
    assert inst.alias[0] == "Michigan State Department of Health"
    assert inst.id == "3"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://michigan.gov/state-dept-ids"}
        ).valueUri
    )
    assert inst.identifier[0].value == "25"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Michigan Health"
    assert inst.text.status == "generated"


def test_organization_4(base_settings):
    """No. 4 tests collection for Organization.
    Test File: organization-example-mihealth.json
    """
    filename = base_settings["unittest_data_dir"] / "organization-example-mihealth.json"
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_4(inst2)


def impl_organization_5(inst):
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "+1 555 234 1234"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "contact@labs.acme.org"
    assert inst.id == "1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.acme.org.au/units"}
        ).valueUri
    )
    assert inst.identifier[0].value == "ClinLab"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Clinical Lab"
    assert inst.text.status == "generated"


def test_organization_5(base_settings):
    """No. 5 tests collection for Organization.
    Test File: organization-example-lab.json
    """
    filename = base_settings["unittest_data_dir"] / "organization-example-lab.json"
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_5(inst2)


def impl_organization_6(inst):
    assert inst.active is True
    assert inst.contact[0].address.line[0] == "South Wing, floor 2"
    assert inst.contact[0].name[0].text == "mevr. D. de Haan"
    assert inst.contact[0].purpose.coding[0].code == "ADMIN"
    assert (
        inst.contact[0].purpose.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/contactentity-type"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "022-655 2321"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "cardio@burgersumc.nl"
    assert inst.contact[0].telecom[2].system == "fax"
    assert inst.contact[0].telecom[2].value == "022-655 2322"
    assert inst.id == "f002"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Burgers UMC Cardiology unit"
    assert inst.partOf.reference == "Organization/f001"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "dept"
    assert inst.type[0].coding[0].display == "Hospital Department"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/organization-type"}
        ).valueUri
    )


def test_organization_6(base_settings):
    """No. 6 tests collection for Organization.
    Test File: organization-example-f002-burgers-card.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "organization-example-f002-burgers-card.json"
    )
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_6(inst2)


def impl_organization_7(inst):
    assert inst.active is True
    assert inst.contact[0].address.city == "Den Helder"
    assert inst.contact[0].address.country == "NLD"
    assert inst.contact[0].address.line[0] == "Walvisbaai 3"
    assert inst.contact[0].address.postalCode == "2333ZA"
    assert inst.contact[0].address.use == "work"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "+31715269111"
    assert inst.contact[1].address.city == "Den helder"
    assert inst.contact[1].address.country == "NLD"
    assert inst.contact[1].address.line[0] == "Walvisbaai 3"
    assert inst.contact[1].address.line[1] == "Gebouw 2"
    assert inst.contact[1].address.postalCode == "2333ZA"
    assert inst.contact[1].name[0].family == "Brand"
    assert inst.contact[1].name[0].given[0] == "Ronald"
    assert inst.contact[1].name[0].prefix[0] == "Prof.Dr."
    assert inst.contact[1].name[0].text == "Professor Brand"
    assert inst.contact[1].name[0].use == "official"
    assert inst.contact[1].telecom[0].system == "phone"
    assert inst.contact[1].telecom[0].use == "work"
    assert inst.contact[1].telecom[0].value == "+31715269702"
    assert inst.id == "f201"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.zorgkaartnederland.nl/"}
        ).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "Artis University Medical Center"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Artis University Medical Center (AUMC)"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "405608006"
    assert inst.type[0].coding[0].display == "Academic Medical Center"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.type[0].coding[1].code == "V6"
    assert inst.type[0].coding[1].display == "University Medical Hospital"
    assert (
        inst.type[0].coding[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:2.16.840.1.113883.2.4.15.1060"}
        ).valueUri
    )
    assert inst.type[0].coding[2].code == "prov"
    assert inst.type[0].coding[2].display == "Healthcare Provider"
    assert (
        inst.type[0].coding[2].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/organization-type"}
        ).valueUri
    )


def test_organization_7(base_settings):
    """No. 7 tests collection for Organization.
    Test File: organization-example-f201-aumc.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-f201-aumc.json"
    )
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_7(inst2)


def impl_organization_8(inst):
    assert inst.id == "2.16.840.1.113883.19.5"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.19.5"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Good Health Clinic"
    assert inst.text.status == "generated"


def test_organization_8(base_settings):
    """No. 8 tests collection for Organization.
    Test File: organization-example-good-health-care.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "organization-example-good-health-care.json"
    )
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_8(inst2)


def impl_organization_9(inst):
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "022-655 2300"
    assert inst.contact[1].address.city == "Den Burg"
    assert inst.contact[1].address.country == "NLD"
    assert inst.contact[1].address.line[0] == "Galapagosweg 91"
    assert inst.contact[1].address.postalCode == "9105 PZ"
    assert inst.contact[1].address.use == "work"
    assert inst.contact[2].address.city == "Den Burg"
    assert inst.contact[2].address.country == "NLD"
    assert inst.contact[2].address.line[0] == "PO Box 2311"
    assert inst.contact[2].address.postalCode == "9100 AA"
    assert inst.contact[2].address.use == "work"
    assert inst.contact[3].purpose.coding[0].code == "PRESS"
    assert (
        inst.contact[3].purpose.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/contactentity-type"}
        ).valueUri
    )
    assert inst.contact[3].telecom[0].system == "phone"
    assert inst.contact[3].telecom[0].value == "022-655 2334"
    assert inst.contact[4].purpose.coding[0].code == "PATINF"
    assert (
        inst.contact[4].purpose.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/contactentity-type"}
        ).valueUri
    )
    assert inst.contact[4].telecom[0].system == "phone"
    assert inst.contact[4].telecom[0].value == "022-655 2335"
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:2.16.528.1"}
        ).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "91654"
    assert (
        inst.identifier[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:2.16.840.1.113883.2.4.6.1"}
        ).valueUri
    )
    assert inst.identifier[1].use == "usual"
    assert inst.identifier[1].value == "17-0112278"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Burgers University Medical Center"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "V6"
    assert inst.type[0].coding[0].display == "University Medical Hospital"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:2.16.840.1.113883.2.4.15.1060"}
        ).valueUri
    )
    assert inst.type[0].coding[1].code == "prov"
    assert inst.type[0].coding[1].display == "Healthcare Provider"
    assert (
        inst.type[0].coding[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/organization-type"}
        ).valueUri
    )


def test_organization_9(base_settings):
    """No. 9 tests collection for Organization.
    Test File: organization-example-f001-burgers.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-f001-burgers.json"
    )
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_9(inst2)


def impl_organization_10(inst):
    assert inst.alias[0] == "ABC Insurance"
    assert inst.id == "2"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:2.16.840.1.113883.3.19.2.3"}
        ).valueUri
    )
    assert inst.identifier[0].value == "666666"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "XYZ Insurance"
    assert inst.text.status == "generated"


def test_organization_10(base_settings):
    """No. 10 tests collection for Organization.
    Test File: organization-example-insurer.json
    """
    filename = base_settings["unittest_data_dir"] / "organization-example-insurer.json"
    inst = organization.Organization.model_validate_json(filename.read_bytes())
    assert "Organization" == inst.get_resource_type()

    impl_organization_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_10(inst2)
