# _*_ coding: utf-8 _*_
import typing
from collections import OrderedDict, deque
from copy import copy
from pathlib import Path

from lxml import etree  # type: ignore
from lxml.etree import QName  # type: ignore

if typing.TYPE_CHECKING:
    from fhir.resources.fhirabstractmodel import FHIRAbstractModel
__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

StrBytes = typing.Union[str, bytes]
StrNone = typing.Union[str, None]
StrBytesNone = typing.Union[str, bytes, None]
DictStr = typing.Dict[str, str]
DictStrBytes = typing.Dict[str, StrBytes]
DictStrNoneKey = typing.Dict[typing.Union[str, None], str]
DictStrBytesNoneKey = typing.Dict[StrNone, StrBytes]
TupleStrKeyVal = typing.Tuple[str, StrBytes]
ROOT_NS = "http://hl7.org/fhir"
XHTML_NS = "http://www.w3.org/1999/xhtml"
EMPTY_VALUE = None


def xml_represent(type_, val):
    """XML  Representation"""
    if val is None:
        return val
    if type_ is bool:
        return val is True and "true" or "false"
    else:
        return type_.to_string(val)


def is_primitive_type(type_):
    """ """
    if getattr(type_, "is_primitive", lambda: False)() is False:
        if type_ is bool:
            return True
        return False
    return True


def get_fhir_type_name(type_):
    """ """
    try:
        return type_.fhir_type_name()
    except AttributeError:
        if type_ is bool:
            return "boolean"
        type_str = str(type_)
        if (
            type_str.startswith("typing.Union[")
            and "fhirtypes.FHIRPrimitiveExtensionType" in type_str
        ):
            return "FHIRPrimitiveExtension"
        raise


class SimpleNodeStorage:

    __slots__ = ("__storage__", "node")
    if typing.TYPE_CHECKING:
        node: "Node"
        __storage__: deque

    def __init__(self, node):
        """ """
        assert isinstance(node, Node)
        object.__setattr__(self, "node", node)
        object.__setattr__(self, "__storage__", deque())

    def __iter__(self):
        """ """
        return iter(self.__storage__)

    def __getitem__(self, index):
        """ """
        return self.__storage__[index]

    def __len__(self):
        """ """
        return len(self.__storage__)

    def append(self, item):
        """ """
        self.__storage__.append(item)

    def extend(self, items):
        """ """
        self.__storage__.extend(items)

    def as_list(self):
        """ """
        return list(self.__storage__)


class NodeContainer(SimpleNodeStorage):
    """ """

    def __init__(self, node):
        """ """
        super(NodeContainer, self).__init__(node)

    def append(self, item):
        """ """
        assert isinstance(item, (Node, etree._Element))
        SimpleNodeStorage.append(self, item)

    def extend(self, items):
        """ """
        if not all([isinstance(i, (Node, etree._Element)) for i in items]):
            raise ValueError("value must be instance of ``Node``")
        SimpleNodeStorage.extend(self, items)


class AttributeContainer(SimpleNodeStorage):
    """ """

    def __init__(self, node: "Node"):
        """ """
        super(AttributeContainer, self).__init__(node)

    def append(self, item: "Attribute"):
        """ """
        assert isinstance(item, Attribute)
        if (
            len(self.node._allowed_attrs) > 0
            and item.name not in self.node._allowed_attrs
        ):
            raise ValueError(f"'{item.name}' is not allowed attribute.")
        SimpleNodeStorage.append(self, item)

    def extend(self, items: typing.List["Attribute"]):
        """ """
        if not all([isinstance(i, Attribute) for i in items]):
            raise ValueError("value must be instance of ``fhirxml.Attribute``")
        for item in items:
            if (
                len(self.node._allowed_attrs) > 0
                and item.name not in self.node._allowed_attrs
            ):
                raise ValueError(f"'{item.name}' is not allowed attribute.")

        SimpleNodeStorage.extend(self, items)


class NamespaceContainer(SimpleNodeStorage):
    """ """

    def __init__(self, node: "Node"):
        """ """
        super(NamespaceContainer, self).__init__(node)

    def append(self, item: "Namespace"):
        """ """
        assert isinstance(item, Namespace)
        SimpleNodeStorage.append(self, item)

    def extend(self, items: typing.List["Namespace"]):
        """ """
        if not all([isinstance(i, Namespace) for i in items]):
            raise ValueError("value must be instance of fhirxml.Namespace")
        SimpleNodeStorage.extend(self, items)


class AttributeValue:
    """ """

    def __init__(self, raw: StrBytes, quote: bool = False):
        """ """
        if isinstance(raw, bytes):
            raw = raw.decode()
        self.raw: str = raw
        self.quote = quote

    def to_xml(self) -> str:
        """ """
        val = self.raw
        if self.quote:
            val = "'{0}'".format(val)
        return val

    def __str__(self):
        return self.to_xml()

    @typing.no_type_check
    def __eq__(self, other: "AttributeValue"):
        """ """
        return (self.raw == other.raw) and (self.quote == other.quote)


class Attribute:
    """ """

    def __init__(
        self,
        name: typing.Union[str, QName],
        value: typing.Union[StrBytes, AttributeValue, None],
    ):
        """ """
        self.name: typing.Union[str, QName] = name
        if typing.TYPE_CHECKING:
            self.value: typing.Union[StrBytes, AttributeValue, None]
        if isinstance(value, (AttributeValue, str)):
            self.value = value
        else:
            if isinstance(value, bytes):
                value = value.decode()
            self.value = value

    def __str__(self):
        """ """
        return '{0}="{1}"'.format(*self.to_xml())

    def to_xml(self) -> typing.Tuple[str, StrNone]:
        """ """
        val: typing.Optional[str] = None

        if isinstance(self.value, AttributeValue):
            val = self.value.to_xml()
        elif self.value is not None:
            val = typing.cast(str, self.value)

        return self.name, val

    def __repr__(self):
        """ """
        return f"<{self.__class__.__name__} {self.__str__()}>"

    @typing.no_type_check
    def __eq__(self, other: "Attribute"):
        """ """
        return (self.name == other.name) and (self.value == other.value)


class Namespace:
    """ """

    def __init__(self, name: StrNone, location: StrBytes):
        """ """
        self.name: StrNone = name
        if isinstance(location, bytes):
            location = location.decode()
        self.location = location

    def __str__(self):
        """ """
        name = ""
        if self.name:
            name = f":{self.name}"
        return 'xmlns{0}="{1}"'.format(name, self.location)

    def to_xml(self):
        """ """
        return self.name, self.location

    def __repr__(self):
        """ """
        return "<{0} {1}>".format(self.__class__.__name__, self.__str__())

    @typing.no_type_check
    def __eq__(self, other: "Namespace"):
        """ """
        return (self.name == other.name) and (self.location == other.location)


class Node:
    """ """

    _allowed_attrs: typing.Set[str] = set()

    def __init__(
        self,
        name: typing.Union[str, QName],
        *,
        value: StrBytes = None,
        text: typing.Union[StrBytes, "Node"] = None,
        attributes: typing.List[Attribute] = None,
        namespaces: typing.List[Namespace] = None,
        parent: "Node" = None,
        children: typing.List["Node"] = None,
    ):
        """ """
        self.name = name
        self._value = None
        self._text = None
        self.attributes = AttributeContainer(self)
        self.namespaces = NamespaceContainer(self)
        self.parent = None
        self.children = NodeContainer(self)

        if text:
            self.set_text(text)
        if value:
            self.value = value

        if attributes:
            self.attributes.extend(attributes)
        if namespaces:
            self.namespaces.extend(namespaces)
        if parent:
            assert isinstance(parent, Node)
            self.parent = parent
        if children:
            self.children.extend(children)

    def rename(self, new_name):
        """Rename the current Node name"""
        if self.name == new_name:
            raise ValueError("Current Node name and provided name are identical!")
        self.name = new_name

    def add_namespace(
        self,
        ns: typing.Union[Namespace, StrNone],
        location: StrBytes = None,
    ):
        """ """
        if isinstance(ns, Namespace):
            self.namespaces.append(ns)
            return
        if location is None:
            raise ValueError("'location' value is required.")

        self.namespaces.append(Namespace(ns, location))

    def add_attribute(self, attr: typing.Union[str, Attribute], value: StrBytes = None):
        """ """
        if isinstance(attr, Attribute):
            self.attributes.append(attr)
            return
        self.attributes.append(Attribute(attr, value))

    @property
    def text(self):
        """ """
        return self._text

    @text.setter
    def text(self, val):
        """ """
        self._text = val

    @property
    def value(self):
        """ """
        return self._value

    @value.setter
    def value(self, val):
        """ """
        self._value = val

    def set_text(self, value):
        """ """
        if isinstance(value, Node):
            value = value.to_string(pretty_print=False, xml_declaration=False)
        self._text = value

    def add_text(self, value, prefix="", suffix=""):
        """ """
        if isinstance(value, Node):
            value = value.to_string(pretty_print=False, xml_declaration=False)
        if not isinstance(value, str):
            if isinstance(value, bytes):
                value = value.decode()
            else:
                value = str(value)

        value = prefix + value + suffix
        if not self._text:
            self._text = ""
        self._text += value

    @classmethod
    def create(
        cls,
        name,
        *,
        value: typing.Union[str, bytes] = None,
        text: typing.Union[typing.Union[str, bytes], "Node"] = None,
        attrs: typing.Union[
            DictStrBytes,
            typing.List[typing.Union[Attribute, typing.Tuple[str, StrBytes]]],
        ] = None,
        namespaces: typing.Union[
            DictStrBytesNoneKey,
            typing.List[typing.Union[Namespace, typing.Tuple[StrNone, StrBytes]]],
        ] = None,
    ):
        """ """
        self = cls(name=name, value=value, text=text)

        if attrs:
            if isinstance(attrs, dict):
                attrs = list(attrs.items())
            if isinstance(attrs, list):
                for attr in attrs:
                    if isinstance(attr, tuple):
                        self.add_attribute(*attr)
                    else:
                        self.add_attribute(attr)
            else:
                raise NotImplementedError

        if namespaces:
            if isinstance(namespaces, dict):
                namespaces = list(namespaces.items())

            if isinstance(namespaces, list):
                for ns in namespaces:
                    if isinstance(ns, tuple):
                        self.add_namespace(*ns)
                    else:
                        self.add_namespace(ns)
            else:
                raise NotImplementedError

        return self

    @classmethod
    def from_element(
        cls,
        element: etree._Element,
        parent: "Node" = None,
        exists_ns: typing.List[Namespace] = None,
    ):
        """ """
        name = element.tag.capitalize()
        me = cls(name)
        if element.text:
            me.text = element.text
        # Attributes
        for attr, value in element.attrib:
            if attr == "value":
                me.value = value
            else:
                me.add_attribute(attr, value)

        if exists_ns is None:
            exists_ns = []

        if parent is not None:
            exists_ns += parent.namespaces.as_list()

        # handle namespaces
        for prefix, location in element.nsmap:
            ns = Namespace(prefix, location)
            if ns in exists_ns:
                continue
            me.namespaces.append(ns)
            exists_ns.append(ns)

        for child in element:
            child_name = child.tag.capitalize()
            child_class = globals().get(child_name, Node)
            child_class.from_element(child, parent=me, exists_ns=copy(exists_ns))

        if parent is not None:
            parent.children.append(me)

        return me

    @staticmethod
    def inject_comments(
        node: "Node", comments: typing.Union[str, typing.List[str]]
    ) -> None:
        """working comments"""
        if comments is None:
            return
        if comments:
            if isinstance(comments, str):
                comments = [comments]
            for cm in comments:
                node.children.append(etree.Comment(cm))

    @staticmethod
    def add_fhir_element(parent, field, value, ext=None, ext_field=None):
        """"""
        child = Node.create(field.alias)
        field_type = field.type_
        if is_primitive_type(field_type):
            if isinstance(value, list):
                if ext and not isinstance(ext, list):
                    raise NotImplementedError
                if ext and len(ext) != len(value):
                    raise NotImplementedError

                for idx, val in enumerate(value):
                    ext_ = ext and ext[idx] or None
                    if ext_ is None and val is None:
                        continue
                    Node.add_fhir_element(
                        parent,
                        field,
                        value=val,
                        ext=ext_,
                        ext_field=ext_field,
                    )
            elif value is not None:
                child.value = xml_represent(field.type_, value)
                if ext is not None:
                    Node.inject_comments(
                        parent, ext.__dict__.get("fhir_comments", None)
                    )
                    Node.add_fhir_element(
                        child,
                        field=ext_field,
                        value=ext,
                        ext=None,
                        ext_field=None,
                    )
                parent.children.append(child)
            else:
                child.value = EMPTY_VALUE
                if ext is not None:
                    exts = not isinstance(ext, list) and [ext] or ext
                    for ext_ in exts:
                        if ext_ is None:
                            continue
                        Node.inject_comments(
                            parent, ext_.__dict__.get("fhir_comments", None)
                        )
                        Node.add_fhir_element(
                            child,
                            field=ext_field,
                            value=ext_,
                            ext=None,
                            ext_field=None,
                        )
                parent.children.append(child)
            return

        # Handle Multiple non primitive type values
        if isinstance(value, list):
            for value_ in value:
                Node.add_fhir_element(
                    parent,
                    field,
                    value_,
                    ext=ext,
                    ext_field=ext_field,
                )
            return
        # we see it's instance of 'FHIRAbstractModel'
        if getattr(field_type, "__resource_type__", None) is None:
            type_str = str(field_type)
            if (
                type_str.startswith(("typing.Union[", "typing.Optional["))
                and "fhirtypes.FHIRPrimitiveExtensionType" in type_str
            ):
                for cls in field_type.__args__:
                    if cls.__name__ == "FHIRPrimitiveExtensionType":
                        field_type = cls
            else:
                raise NotImplementedError

        parent_child = None
        if get_fhir_type_name(field_type) == "Resource":
            # special case
            parent_child = child
            child = Node.create(value.resource_type)
            parent_child.children.append(child)

        if get_fhir_type_name(field_type) == "FHIRPrimitiveExtension":
            # this is an special primitive extension
            del child
            # xxx: handle comments (add comment to main element, parent in this case)
            field = value.__class__.__fields__["extension"]
            value = value.__dict__.get(field.name, None)
            if not value:
                return
            Node.add_fhir_element(
                parent,
                field,
                value,
                ext=ext,
                ext_field=ext_field,
            )
            return
        # working comments
        comments = value.__dict__.get("fhir_comments", None)
        Node.inject_comments(parent, comments)

        alias_maps = value.__class__.get_alias_mapping()
        for prop_name in value.__class__.elements_sequence():
            field_ = value.__class__.__fields__[alias_maps[prop_name]]
            val = value.__dict__.get(field_.name)
            if (
                field_type.fhir_type_name() == "Extension"
                and field_.alias in ("url", "id")
                and val
            ):
                child.add_attribute(field_.alias, val)
                continue
            if get_fhir_type_name(field_.type_) == "xhtml" and val:
                # xxx: fhir-xhtml.xsd validation
                xhtml_element = etree.fromstring(val)
                if not (
                    xhtml_element.nsmap[None] == XHTML_NS
                    and str(etree.QName(XHTML_NS, field_.alias))
                ):
                    raise ValueError
                else:
                    child.children.append(xhtml_element)
                    continue

            value_ext, value_ext_field = None, None
            if is_primitive_type(field_.type_):
                ext_key = f"{field_.name}__ext"
                value_ext = value.__dict__.get(ext_key, None)
                if value_ext:
                    value_ext_field = value.__class__.__fields__[ext_key]

            if value_ext is None and val is None:
                continue

            Node.add_fhir_element(
                child,
                field_,
                val,
                ext=value_ext,
                ext_field=value_ext_field,
            )
        if parent_child is None:
            parent.children.append(child)
        else:
            parent.children.append(parent_child)

    @classmethod
    def from_fhir_obj(cls, model: "FHIRAbstractModel"):
        """ """
        resource_node = cls(model.resource_type, namespaces=[Namespace(None, ROOT_NS)])
        alias_maps = model.__class__.get_alias_mapping()
        for prop_name in model.__class__.elements_sequence():
            field = model.__class__.__fields__[alias_maps[prop_name]]
            value = model.__dict__.get(field.name, None)
            value_ext, value_ext_field = None, None
            if is_primitive_type(field.type_):
                ext_key = f"{field.name}__ext"
                value_ext = model.__dict__.get(ext_key, None)
                if value_ext:
                    value_ext_field = model.__class__.__fields__[ext_key]

            if value_ext is None and value is None:
                continue

            Node.add_fhir_element(
                resource_node,
                field,
                value,
                ext=value_ext,
                ext_field=value_ext_field,
            )

        return resource_node

    def to_xml(self, parent=None):
        """ """
        params = {}
        nsmap = self.normalize_namespaces()
        if len(nsmap) > 0:
            params["nsmap"] = nsmap

        attrib = self.normalize_attributes()
        if len(attrib) > 0:
            params["attrib"] = attrib
        if self.value:
            params["value"] = (
                isinstance(self.value, AttributeValue)
                and self.value.to_xml()
                or self.value
            )

        if parent is None:
            me = etree.Element(self.name, **params)

        else:
            me = parent.makeelement(self.name, **params)

        if self.text:
            me.text = (
                isinstance(self.text, AttributeValue)
                and self.text.to_xml()
                or self.text
            )

        if len(self.children) == 0:
            return me

        for child in self.children:

            if isinstance(child, Node):
                child_node = child.to_xml(me)
            elif isinstance(child, etree._Element):
                child_node = child
            elif isinstance(child, (str, bytes)):
                child_node = etree.fromstring(child)
            else:
                raise NotImplementedError

            me.append(child_node)

        return me

    def normalize_attributes(self):
        """ """
        attrib = OrderedDict()
        for attr in self.attributes:
            key, val = attr.to_xml()
            attrib[key] = val
        return attrib

    def normalize_namespaces(self):
        """ """
        nsmap = OrderedDict()
        for ns in self.namespaces:
            key, val = ns.to_xml()
            nsmap[key] = val
        return nsmap

    @classmethod
    def validate(
        cls,
        element: typing.Union["Node", etree._Element, bytes],
        xsd_file: Path = None,
        xmlparser: etree.XMLParser = None,
    ):
        """ """
        if isinstance(element, cls):
            element_str = element.to_string(pretty_print=False)
        elif isinstance(element, etree._Element):
            element_str = etree.tostring(element)
        else:
            element_str = element
        if xmlparser is None and xsd_file is None:
            raise ValueError("Any of `xsd_file` or `parser` is required")

        if xmlparser is None:
            assert xsd_file and xsd_file.exists() and xsd_file.is_file()
            schema = etree.XMLSchema(file=str(xsd_file))
            xmlparser = etree.XMLParser(schema=schema)

        try:
            etree.fromstring(element_str, parser=xmlparser)
        except (etree.XMLSchemaError, etree.XMLSyntaxError) as exc:
            raise ValueError(str(exc))

    def to_string(
        self,
        pretty_print=False,
        xml_declaration=True,
        with_comments=True,
        strip_text=False,
    ):
        """ """
        el = self.to_xml()
        params = {"encoding": "utf-8", "method": "xml", "pretty_print": pretty_print}
        if xml_declaration:
            params["xml_declaration"] = '<?xml version="1.0" encoding="UTF-8"?>'
        params["with_comments"] = (with_comments,)
        params["strip_text"] = strip_text

        return etree.tostring(el, **params)

    def __str__(self):
        """ """
        return self.to_string(pretty_print=False)


def xml_dumps(
    model: "FHIRAbstractModel",
    *,
    pretty_print=False,
    xml_declaration=True,
    with_comments=True,
    strip_text=False,
):
    """ """
    node = Node.from_fhir_obj(model)
    return node.to_string(
        pretty_print=pretty_print,
        xml_declaration=xml_declaration,
        with_comments=with_comments,
        strip_text=strip_text,
    )


__all__ = [
    "xml_dumps",
]
