# _*_ coding: utf-8 _*_
from decimal import Decimal

from yaml import dump, load
from yaml import YAMLError
from yaml.representer import Representer as BaseRepresenter
from yaml.representer import SafeRepresenter

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper  # type: ignore


__all__ = ["yaml_loads", "yaml_dumps"]

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


class Representer(SafeRepresenter):
    """ """

    def represent_decimal(self, data):
        """ """
        data = float(data)
        return self.represent_float(data)


BaseRepresenter.add_representer(Decimal, Representer.represent_decimal)


def yaml_loads(stream):
    """ """
    try:
        return load(stream, Loader=Loader)
    except YAMLError as exc:
        # ensure Pydantic compatible error handling
        raise ValueError(f"YAMLError: {exc}")


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
    """ """
    try:
        res = dump(
            data,
            stream=stream,
            Dumper=Dumper,
            indent=indent,
            width=width,
            line_break=line_break,
            sort_keys=sort_keys,
            encoding=encoding,
        )
    except YAMLError as exc:
        # ensure Pydantic compatible error handling
        raise ValueError(f"YAMLError: {exc}")

    if stream is None and return_bytes is False:
        res = res.decode()

    return res
