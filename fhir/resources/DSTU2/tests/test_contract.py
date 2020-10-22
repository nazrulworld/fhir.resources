# -*- coding: utf-8 -*-
from .. import fhirtypes  # noqa: F401
from .. import contract


def test_Contract_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "contract-example.canonical.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type
    impl_Contract_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_Contract_1(inst2)


def impl_Contract_1(inst):
    assert inst.id == "C-123"
    assert inst.text.div == "<div>A human-readable rendering of the contract</div>"
    assert inst.text.status == "generated"
