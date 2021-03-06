from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.app.testing import applyProfile
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing.layers import IntegrationTesting
from zope.configuration import xmlconfig
from plone.testing import z2
from plone import api


IS_PLONE_5 = api.env.plone_version().startswith('5')


class Lockdown(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        if IS_PLONE_5:
            import plone.app.contenttypes
            self.loadZCML(package=plone.app.contenttypes)
        # load ZCML
        import wildcard.lockdown
        xmlconfig.file('configure.zcml', wildcard.lockdown,
            context=configurationContext)
        z2.installProduct(app, 'wildcard.lockdown')

    def setUpPloneSite(self, portal):
        if IS_PLONE_5:
            applyProfile(portal, 'plone.app.contenttypes:default')

        # install into the Plone site
        applyProfile(portal, 'wildcard.lockdown:default')
        setRoles(portal, TEST_USER_ID, ('Member', 'Manager'))


Lockdown_FIXTURE = Lockdown()
Lockdown_INTEGRATION_TESTING = IntegrationTesting(
    bases=(Lockdown_FIXTURE,), name="Lockdown:Integration")
Lockdown_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(Lockdown_FIXTURE,), name="Lockdown:Functional")


def browserLogin(portal, browser, username=None, password=None):
    handleErrors = browser.handleErrors
    try:
        browser.handleErrors = False
        browser.open(portal.absolute_url() + '/login_form')
        if username is None:
            username = TEST_USER_NAME
        if password is None:
            password = TEST_USER_PASSWORD
        browser.getControl(name='__ac_name').value = username
        browser.getControl(name='__ac_password').value = password
        browser.getControl(name='submit').click()
    finally:
        browser.handleErrors = handleErrors


def createObject(context, _type, id, delete_first=False,
                 check_for_first=False, **kwargs):
    if delete_first and id in context.objectIds():
        context.manage_delObjects([id])
    if not check_for_first or id not in context.objectIds():
        return context[context.invokeFactory(_type, id, **kwargs)]

    return context[id]
