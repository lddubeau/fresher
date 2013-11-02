import unittest

import os
import sys

import six

from fresher.noseplugin import FresherNosePlugin
from optparse import OptionParser

class TestFresherTestCaseName(unittest.TestCase):

    def __init__(self, method_name='runTest'):
        unittest.TestCase.__init__(self, method_name)
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

    def _make_plugin(self):
        plugin = FresherNosePlugin()
        parser = OptionParser()

        plugin.options(parser, {})

        sys.argv = ['nosetests', '--with-fresher']
        (options, args) = parser.parse_args()

        plugin.configure(options, None)
        return plugin

    def test_should_use_feature_name_as_class_name_when_subclassing_FresherTestCase(self):
        plugin = self._make_plugin()
        test_generator = plugin.loadTestsFromFile(self.cur_dir + '/resources/valid_no_tags_no_use_only.feature')
        test_instance = six.next(test_generator)

        self.assertEquals(test_instance.__class__.__name__, 'Independence of the counter.')

    def test_should_use_scenario_name_as_method_name_when_subclassing_FresherTestCase(self):
        plugin = self._make_plugin()
        test_generator = plugin.loadTestsFromFile(self.cur_dir + '/resources/valid_no_tags_no_use_only.feature')
        test_instance = six.next(test_generator)

        self.assertNotEqual(getattr(test_instance, 'Print counter', None), None)
