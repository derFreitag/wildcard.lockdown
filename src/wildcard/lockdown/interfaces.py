"""Interfaces."""
from zope import schema
from wildcard.lockdown import _
from zope.interface import Interface


class ILayer(Interface):
    """Add-on browser layer."""


class ISettings(Interface):
    """Add-on settings."""

    enabled = schema.Bool(
        title=_('Enabled'),
        description=_('If enabled, it will by default make the entire site '
                      'read-only unless it is in debug mode or one of the '
                      'activated conditions are met. Basically, this could '
                      'mean that you will prevent yourself from disabling '
                      'this feature unless you uninstall the package.'),
        default=False)

    activated = schema.Set(
        title=_('Activated Commit Conditions'),
        description=_('Select the conditions under which something can be '
                      'committed to the database. Only one rules needs to '
                      'be valid to allow commits to occur.'),
        value_type=schema.Choice(vocabulary='wildcard.lockdown.conditions'),
        default=set(),
        missing_value=set(),
        required=False)

    status_message = schema.Text(
        title=_('Status message'),
        description=_('An status message to be displayed to authenticated '
                      'users users when the lockdown is enabled. Leave empty to '
                      'display nothing.'),
        required=False,
        default='')
