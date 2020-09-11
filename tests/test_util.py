from hookee.climanager import CliManager
from hookee.pluginmanager import PluginManager

from hookee import util
from tests.testcase import HookeeTestCase

__author__ = "Alex Laird"
__copyright__ = "Copyright 2020, Alex Laird"
__version__ = "1.0.1"


class TestUtil(HookeeTestCase):
    def setUp(self):
        super(TestUtil, self).setUp()

        self.cli_manager = CliManager(self.ctx)
        self.plugin_manager = PluginManager(self.cli_manager)
        self.plugin = self.plugin_manager.get_plugin("request_url_info")

    def test_get_functions(self):
        # WHEN
        funcs = util.get_functions(self.plugin.module)

        # THEN
        self.assertEqual(funcs, ["run", "setup"])

    def get_args(self):
        # WHEN
        args = util.get_args(self.plugin.module.run)

        # THEN
        self.assertEqual(args, ["request"])
