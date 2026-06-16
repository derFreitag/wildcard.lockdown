from plone.app.registry.browser import controlpanel
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from wildcard.lockdown import _
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from wildcard.lockdown import getConditionNames
from wildcard.lockdown.interfaces import ISettings


@implementer(IVocabularyFactory)
class ConditionsVocabulary:
    """Creates a vocabulary with all the routes available on the
    site.
    """

    def __call__(self, context):
        items = []
        for name in getConditionNames():
            items.append(SimpleVocabulary.createTerm(name,
                                                     name,
                                                     name))
        return SimpleVocabulary(items)
ConditionsVocabularyFactory = ConditionsVocabulary()


class LockdownSettingsEditForm(controlpanel.RegistryEditForm):
    schema = ISettings
    label = _('Lockdown Settings')
    description = _('Here you can modify the settings for '
                    'locking down writes to database.')

    def updateFields(self):
        super().updateFields()
        self.fields['activated'].widgetFactory = CheckBoxFieldWidget


class LockdownConfiglet(controlpanel.ControlPanelFormWrapper):
    form = LockdownSettingsEditForm
