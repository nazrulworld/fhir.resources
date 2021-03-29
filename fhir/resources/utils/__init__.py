# _*_ coding: utf-8 _*_
import json
import pathlib
from typing import Any, Callable, Union, no_type_check

from pydantic.parse import Protocol
from pydantic.parse import load_file as default_load_file
from pydantic.parse import load_str_bytes as default_load_str_bytes
from pydantic.types import StrBytes

try:
    from .yaml import yaml_dumps, yaml_loads
except ImportError:

    def raise_yaml_import_error():
        raise ImportError(
            "YAML library not found! Make sure ``fhir.resources`` is "
            "added into your project dependency with extra ´´yaml´´. "
            "for example ``fhir.resources[yaml]``."
        )

    def yaml_dumps(
        data,
        *,
        stream=None,
        indent=None,
        width=None,
        line_break=None,
        sort_keys=False,
        encoding="utf-8",
        return_bytes=True,
    ):
        raise_yaml_import_error()

    def yaml_loads(stream):
        raise_yaml_import_error()


try:
    from .xml import xml_dumps
except ImportError:

    def raise_lxml_import_error():
        raise ImportError(
            "LXML library not found! Make sure ``fhir.resources`` is "
            "added into your project dependency with extra ´´xml´´. "
            "for example ``fhir.resources[xml]``."
        )

    @no_type_check
    def xml_dumps(
        model: "FHIRAbstractModel",  # noqa: F821
        *,
        pretty_print=False,
        xml_declaration=True,
        with_comments=True,
        strip_text=False,
    ):
        raise_lxml_import_error()


__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def load_str_bytes(
    b: StrBytes,
    *,
    content_type: str = None,
    encoding: str = "utf8",
    proto: Protocol = None,
    allow_pickle: bool = False,
    json_loads: Callable[[str], Any] = json.loads,
) -> Any:
    if content_type and content_type.endswith(("yml", "yaml")):
        obj = yaml_loads(stream=b)
    else:
        obj = default_load_str_bytes(
            b,
            proto=proto,
            content_type=content_type,
            encoding=encoding,
            allow_pickle=allow_pickle,
            json_loads=json_loads,
        )
    return obj


def load_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: str = None,
    encoding: str = "utf8",
    proto: Protocol = None,
    allow_pickle: bool = False,
    json_loads: Callable[[str], Any] = json.loads,
) -> Any:
    if isinstance(path, str):
        path = pathlib.Path(path)
    # Check for YAML
    if path.suffix.lower() in (".yml", ".yaml") or (
        content_type and content_type.endswith(("yml", "yaml"))
    ):
        obj = yaml_loads(stream=path.read_bytes())
    else:
        obj = default_load_file(
            path,
            proto=proto,
            content_type=content_type,
            encoding=encoding,
            allow_pickle=allow_pickle,
            json_loads=json_loads,
        )
    return obj
