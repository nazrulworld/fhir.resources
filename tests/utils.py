from fhir.resources import fhirxml
from http import client
import sys
import subprocess

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def has_internet_connection():
    """ """
    try:
        res = subprocess.check_call(["ping", "-c", "1", "8.8.8.8"])
        return res == 0
    except subprocess.CalledProcessError:
        return False


def post_xml_resource(
    conn: client.HTTPConnection, resource_node: fhirxml.Node
) -> client.HTTPResponse:
    """ """
    try:
        conn.request(
            "POST",
            f"http://hapi.fhir.org/baseR4/{resource_node.name}?_format=xml&_pretty=true",
            body=resource_node.to_string(False),
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
