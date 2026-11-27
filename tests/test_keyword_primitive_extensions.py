from fhir.resources.R4B.structuremap import StructureMap as R4BStructureMap
from fhir.resources.structuremap import StructureMap as R5StructureMap
from fhir.resources.STU3.coverage import Coverage as STU3Coverage
from fhir.resources.STU3.coverage import CoverageGrouping as STU3CoverageGrouping
from fhir.resources.STU3.structuremap import StructureMap as STU3StructureMap


def _structuremap_payload():
    return {
        "resourceType": "StructureMap",
        "url": "http://example.org/StructureMap/test",
        "name": "TestMap",
        "status": "draft",
        "import": ["http://example.org/StructureMap/other"],
        "_import": [
            {
                "extension": [
                    {
                        "url": "http://example.org/ext",
                        "valueString": "import-ext",
                    }
                ]
            }
        ],
        "group": [
            {
                "name": "g1",
                "typeMode": "none",
                "input": [{"name": "src", "mode": "source"}],
                "rule": [{"name": "r1", "source": [{"context": "src"}]}],
            }
        ],
    }


def test_r5_structuremap_import_primitive_extension_roundtrip():
    sm = R5StructureMap.model_validate(_structuremap_payload())
    assert sm.import_fhir__ext is not None
    dumped = sm.model_dump()
    assert dumped["_import"][0]["extension"][0]["valueString"] == "import-ext"
    assert '"_import"' in sm.model_dump_json()

    xml_bytes = sm.model_dump_xml()
    assert b"import-ext" in xml_bytes
    sm_from_xml = R5StructureMap.model_validate_xml(xml_bytes)
    assert (
        sm_from_xml.model_dump()["_import"][0]["extension"][0]["valueString"]
        == "import-ext"
    )


def test_r4b_structuremap_import_primitive_extension_roundtrip():
    sm = R4BStructureMap.model_validate(_structuremap_payload())
    assert sm.import_fhir__ext is not None
    dumped = sm.model_dump()
    assert dumped["_import"][0]["extension"][0]["valueString"] == "import-ext"
    assert '"_import"' in sm.model_dump_json()

    xml_bytes = sm.model_dump_xml()
    assert b"import-ext" in xml_bytes
    sm_from_xml = R4BStructureMap.model_validate_xml(xml_bytes)
    assert (
        sm_from_xml.model_dump()["_import"][0]["extension"][0]["valueString"]
        == "import-ext"
    )


def test_stu3_structuremap_import_primitive_extension_roundtrip():
    sm = STU3StructureMap.model_validate(_structuremap_payload())
    assert sm.import_fhir__ext is not None
    dumped = sm.model_dump()
    assert dumped["_import"][0]["extension"][0]["valueString"] == "import-ext"
    assert '"_import"' in sm.model_dump_json()

    xml_bytes = sm.model_dump_xml()
    assert b"import-ext" in xml_bytes
    sm_from_xml = STU3StructureMap.model_validate_xml(xml_bytes)
    assert (
        sm_from_xml.model_dump()["_import"][0]["extension"][0]["valueString"]
        == "import-ext"
    )


def test_stu3_coverage_grouping_class_primitive_extension_roundtrip():
    grouping_data = {
        "class": "A1",
        "_class": {
            "extension": [
                {
                    "url": "http://example.org/ext",
                    "valueString": "class-ext",
                }
            ]
        },
    }
    grouping = STU3CoverageGrouping.model_validate(grouping_data)
    assert grouping.class_fhir__ext is not None
    assert grouping.model_dump()["_class"]["extension"][0]["valueString"] == "class-ext"
    assert '"_class"' in grouping.model_dump_json()

    cov = STU3Coverage.model_validate(
        {"resourceType": "Coverage", "grouping": grouping_data}
    )
    xml_bytes = cov.model_dump_xml()
    assert b"class-ext" in xml_bytes
    cov_from_xml = STU3Coverage.model_validate_xml(xml_bytes)
    assert (
        cov_from_xml.model_dump()["grouping"]["_class"]["extension"][0]["valueString"]
        == "class-ext"
    )
