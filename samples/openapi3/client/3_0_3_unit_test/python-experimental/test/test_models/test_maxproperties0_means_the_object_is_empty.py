# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.model.maxproperties0_means_the_object_is_empty import Maxproperties0MeansTheObjectIsEmpty
from unit_test_api import configuration


class TestMaxproperties0MeansTheObjectIsEmpty(unittest.TestCase):
    """Maxproperties0MeansTheObjectIsEmpty unit test stubs"""
    _configuration = configuration.Configuration()

    def test_no_properties_is_valid_passes(self):
        # no properties is valid
        Maxproperties0MeansTheObjectIsEmpty._from_openapi_data(
            {
            },
            _configuration=self._configuration
        )

    def test_one_property_is_invalid_fails(self):
        # one property is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            Maxproperties0MeansTheObjectIsEmpty._from_openapi_data(
                {
                    "foo":
                        1,
                },
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()