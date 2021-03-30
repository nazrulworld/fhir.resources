import logging
import subprocess
import sys
from http import client
from typing import Union

from fhir.resources.fhirabstractmodel import FHIRAbstractModel
from fhir.resources.utils import xml

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

LOG = logging.getLogger("tests.utils")


def has_internet_connection():
    """ """
    try:
        res = subprocess.check_call(["ping", "-c", "1", "8.8.8.8"])
        return res == 0
    except subprocess.CalledProcessError:
        return False


def post_xml_resource(  # type: ignore
    conn: client.HTTPConnection, resource: Union[xml.Node, FHIRAbstractModel]
) -> client.HTTPResponse:
    """ """
    if isinstance(resource, FHIRAbstractModel):
        resource_str = resource.xml(return_bytes=True, pretty_print=False)
        resource_type = resource.resource_type
    else:
        resource_type = resource.name
        resource_str = resource.to_string(pretty_print=False)
    try:
        url = f"http://hapi.fhir.org/baseR4/{resource_type}?_format=xml&_pretty=true"
        LOG.info(f"POST request to `{url}`")
        conn.request(
            "POST",
            url,
            body=resource_str,
            headers={
                "Accept-Charset": "utf-8",
                "Accept": "application/fhir+xml;q=1.0, application/xml+fhir;q=0.9",
                "Content-Type": "application/fhir+xml; charset=UTF-8",
            },
        )
        response = conn.getresponse()
        return response
    except client.HTTPException as exc:
        sys.stderr.write(f"{exc}\n")
