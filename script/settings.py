# These are settings for the FHIR class generator.
# All paths are relative to the `fhir-parser` directory. You may want to use
# os.path.join() if the generator should work on Windows, too.
try:
    from Default.settings import *
except ImportError:
    pass

# Base URL for where to load specification data from
base_url = 'http://hl7.org/fhir'
current_version = 'R4'
previous_versions = ['STU3']
specification_url = '/'.join([base_url, current_version])

# In which directory to find the templates. See below for settings that start with `tpl_`: these are the template names.
tpl_base = '../script/templates'

# classes/resources
write_resources = True
tpl_resource_source = 'template-resource.jinja2'
tpl_resource_target = '../fhir/resources'    # target directory to write the generated class files to
tpl_codesystems_source = None                   # the template to use as source when writing enums for CodeSystems; can be `None`

# factory methods
write_factory = True
tpl_factory_target = '../fhir/resources/fhirelementfactory.py'    # where to write the generated factory to
tpl_factory_source = 'template-elementfactory.jinja2'

# unit tests
write_unittests = True
tpl_unittest_source = 'template-unittest.jinja2'
tpl_unittest_target = '../fhir/resources/tests'    # target directory to write the generated unit test files to
tpl_unittest_target_ptrn = 'test_{}.py'
unittest_copyfiles = [
    '../script/templates/conftest.py',
    '../script/templates/fixtures.py'
]

# all these files should be copied to dirname(`tpl_resource_target_ptrn`): tuples of (path/to/file, module, array-of-class-names)
manual_profiles = [
    ('../script/templates/fhirabstractbase.py', 'fhirabstractbase', [
        'boolean',
        'string', 'base64Binary', 'code', 'id',
        'decimal', 'integer', 'unsignedInt', 'positiveInt',
        'uri', 'oid', 'uuid', 'canonical', 'url', 'markdown',
        'FHIRAbstractBase',
    ]),
    ('../script/templates/fhirabstractresource.py', 'fhirabstractresource', ['FHIRAbstractResource']),
    ('../script/templates/fhirreference.py', 'fhirreference', ['FHIRReference']),
    ('../script/templates/fhirdate.py', 'fhirdate', ['date', 'dateTime', 'instant', 'time']),
    ('../script/templates/fhirsearch.py', 'fhirsearch', ['FHIRSearch']),
]

# Testing
# tpl_resource_target = '/tmp/resources'
# tpl_unittest_target = '/tmp/resources/tests'
# tpl_factory_target = '/tmp/resources/fhirelementfactory.py'
