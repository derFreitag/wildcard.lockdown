from plone.registry.interfaces import IRegistry
from wildcard.lockdown.interfaces import ISettings
from zope.component import getUtility


def uninstall_various(context):
    """Uninstall the add-on."""
    registry = getUtility(IRegistry)
    records = registry.records
    to_delete = [ISettings.__identifier__ + "." + name for name in ISettings]
    to_delete = [r for r in to_delete if r in records]
    for record in to_delete:
        del records[record]
