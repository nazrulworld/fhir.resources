# _*_ coding: utf-8 _*_
import typing
from collections import OrderedDict, deque
from copy import copy

from lxml import etree
from lxml.etree import QName

from .fhirtypes import Boolean, Xhtml

if typing.TYPE_CHECKING:
    from .fhirabstractmodel import FHIRAbstractModel

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


def xml_represent(type_, val):
    """XML  Representation"""
    if val is None:
        return val
    if type_ is bool:
        return Boolean.to_string(val)
    else:
        return type_.to_string(val)


class SimpleNodeStorage:

    __slots__ = ("__storage__", "node")

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
        assert isinstance(item, Node)
        SimpleNodeStorage.append(self, item)

    def extend(self, items):
        """ """
        if not all([isinstance(i, Node) for i in items]):
            raise ValueError("value must be instance of ``Node``")
        SimpleNodeStorage.extend(self, items)


class AttributeContainer(SimpleNodeStorage):
    """ """

    def __init__(self, node):
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

    def __eq__(self, other: "AttributeValue"):
        """ """
        return (self.raw == other.raw) and (self.quote == other.quote)


class Attribute:
    """ """

    def __init__(
        self,
        name: typing.Union[str, QName],
        value: typing.Union[StrBytes, AttributeValue],
    ):
        """ """
        self.name: typing.Union[str, QName] = name
        if typing.TYPE_CHECKING:
            self.value: typing.Union[str, AttributeValue]
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
        val = None
        if isinstance(self.value, AttributeValue):
            val = self.value.to_xml()
        elif self.value is not None:
            val = self.value

        return self.name, val

    def __repr__(self):
        """ """
        return f"<{self.__class__.__name__} {self.__str__()}>"

    def __eq__(self, other: "Attribute"):
        """ """
        return (self.name == other.name) and (self.value == other.value)


class Namespace:
    """ """

    def __init__(self, name: StrNone, location: StrNone):
        """ """
        self.name: StrNone = name
        if isinstance(location, bytes):
            location = location.decode()
        self.location: str = location

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

    def __eq__(self, other: "Namespace"):
        """ """
        return (self.name == other.name) and (self.location == other.location)


class Node:
    """ """

    _allowed_attrs = set()

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
            exists_ns: typing.List[Namespace] = []

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
    def add_fhir_element(parent, field, value, exclude_none, ext=None, ext_field=None):
        """Patient.__fields__['id'].name
        Patient.__fields__['id'].type_
        Patient.__fields__['id'].alias
        Patient.__fields__[*__ext]
        cls.element_properties()
        Patient.__fields__['id'].field_info.extra.get("element_property")
        <name>
          <use value="official"/>
          <given value="Östlund">
             <extension url="http://hl7.org/fhir/StructureDefinition/iso21090-EN-qualifier" >
                <valueCode value="MID"/>
             </extension>
          </given>
        </name>
        """
        child = Node.create(field.alias)
        if getattr(field.type_, "is_primitive", lambda: True)():
            if isinstance(value, list):
                children = list()
                for val in value:
                    child = Node.create(field.alias)
                    child.value = xml_represent(field.type_, val)
                    children.append(child)
                parent.children.extend(children)
            else:
                child.value = xml_represent(field.type_, value)
                if ext is not None:
                    ext_field
                    pass
                parent.children.append(child)
            return
        # we see it's instance of 'FHIRAbstractModel'
        if getattr(field.type_, "__resource_type__", None) is None:
            raise NotImplementedError

        if isinstance(value, list):
            children = list()
            for value_ in value:
                child = Node.create(field.alias)
                for field_ in value_.__class__.element_properties():
                    val = value_.__dict__.get(field_.name)
                    if val is None and exclude_none is True:
                        continue
                    Node.add_fhir_element(child, field_, val, exclude_none=exclude_none)
                children.append(child)
            parent.children.extend(children)

        else:
            for field_ in value.__class__.element_properties():
                val = value.__dict__.get(field_.name)
                if val is None and exclude_none is True:
                    continue
                Node.add_fhir_element(child, field_, val, exclude_none=exclude_none)
            parent.children.append(child)

    @classmethod
    def from_fhir_obj(cls, model: "FHIRAbstractModel", exclude_none=True):
        """"""
        resource_node = cls(model.resource_type, namespaces=[Namespace(None, ROOT_NS)])

        for field in model.__class__.element_properties():
            value = model.__dict__.get(field.name, None)
            value_ext, value_ext_field = None, None
            if getattr(field.type_, "is_primitive", lambda: True)():
                ext_key = f"{field.name}__ext"
                value_ext = model.__dict__.get(ext_key, None)
                if value_ext:
                    value_ext_field = model.__class__.__fields__[ext_key]

            if value_ext is None and value is None and exclude_none is True:
                continue

            Node.add_fhir_element(
                resource_node,
                field,
                value,
                exclude_none=exclude_none,
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

    def to_string(self, pretty_print=False, xml_declaration=True):
        """ """
        el = self.to_xml()
        params = {"encoding": "utf-8", "method": "xml", "pretty_print": pretty_print}
        if xml_declaration:
            params["xml_declaration"] = '<?xml version="1.0" encoding="UTF-8"?>'

        return etree.tostring(el, **params)

    def __str__(self):
        """ """
        return self.to_string(pretty_print=False)
