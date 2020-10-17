# -*- coding: utf-8 -*-
from .. import fhirtypes  # noqa: F401
from .. import account


def test_Account_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "account-example.canonical.json"
    inst = account.Account.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Account" == inst.resource_type
    impl_Account_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Account" == data["resourceType"]

    inst2 = account.Account(**data)
    impl_Account_1(inst2)


def impl_Account_1(inst):
    assert inst.id == "example"
    assert inst.text.div == "<div>[Put rendering here]</div>"
    assert inst.text.status == "generated"
