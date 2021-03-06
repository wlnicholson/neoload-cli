# coding: utf-8

"""
    NeoLoad API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SLAPerTestDefinition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'kpi': 'SLAKPIDefinition',
        'status': 'SLAStatusDefinition',
        'value': 'float',
        'warning_threshold': 'ThresholdDefinition',
        'failed_threshold': 'ThresholdDefinition',
        'element': 'SLAElementDefinition'
    }

    attribute_map = {
        'kpi': 'kpi',
        'status': 'status',
        'value': 'value',
        'warning_threshold': 'warningThreshold',
        'failed_threshold': 'failedThreshold',
        'element': 'element'
    }

    def __init__(self, kpi=None, status=None, value=None, warning_threshold=None, failed_threshold=None, element=None, local_vars_configuration=None):  # noqa: E501
        """SLAPerTestDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kpi = None
        self._status = None
        self._value = None
        self._warning_threshold = None
        self._failed_threshold = None
        self._element = None
        self.discriminator = None

        if kpi is not None:
            self.kpi = kpi
        if status is not None:
            self.status = status
        if value is not None:
            self.value = value
        if warning_threshold is not None:
            self.warning_threshold = warning_threshold
        if failed_threshold is not None:
            self.failed_threshold = failed_threshold
        if element is not None:
            self.element = element

    @property
    def kpi(self):
        """Gets the kpi of this SLAPerTestDefinition.  # noqa: E501


        :return: The kpi of this SLAPerTestDefinition.  # noqa: E501
        :rtype: SLAKPIDefinition
        """
        return self._kpi

    @kpi.setter
    def kpi(self, kpi):
        """Sets the kpi of this SLAPerTestDefinition.


        :param kpi: The kpi of this SLAPerTestDefinition.  # noqa: E501
        :type: SLAKPIDefinition
        """

        self._kpi = kpi

    @property
    def status(self):
        """Gets the status of this SLAPerTestDefinition.  # noqa: E501


        :return: The status of this SLAPerTestDefinition.  # noqa: E501
        :rtype: SLAStatusDefinition
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SLAPerTestDefinition.


        :param status: The status of this SLAPerTestDefinition.  # noqa: E501
        :type: SLAStatusDefinition
        """

        self._status = status

    @property
    def value(self):
        """Gets the value of this SLAPerTestDefinition.  # noqa: E501

        SLA value.  # noqa: E501

        :return: The value of this SLAPerTestDefinition.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SLAPerTestDefinition.

        SLA value.  # noqa: E501

        :param value: The value of this SLAPerTestDefinition.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def warning_threshold(self):
        """Gets the warning_threshold of this SLAPerTestDefinition.  # noqa: E501


        :return: The warning_threshold of this SLAPerTestDefinition.  # noqa: E501
        :rtype: ThresholdDefinition
        """
        return self._warning_threshold

    @warning_threshold.setter
    def warning_threshold(self, warning_threshold):
        """Sets the warning_threshold of this SLAPerTestDefinition.


        :param warning_threshold: The warning_threshold of this SLAPerTestDefinition.  # noqa: E501
        :type: ThresholdDefinition
        """

        self._warning_threshold = warning_threshold

    @property
    def failed_threshold(self):
        """Gets the failed_threshold of this SLAPerTestDefinition.  # noqa: E501


        :return: The failed_threshold of this SLAPerTestDefinition.  # noqa: E501
        :rtype: ThresholdDefinition
        """
        return self._failed_threshold

    @failed_threshold.setter
    def failed_threshold(self, failed_threshold):
        """Sets the failed_threshold of this SLAPerTestDefinition.


        :param failed_threshold: The failed_threshold of this SLAPerTestDefinition.  # noqa: E501
        :type: ThresholdDefinition
        """

        self._failed_threshold = failed_threshold

    @property
    def element(self):
        """Gets the element of this SLAPerTestDefinition.  # noqa: E501


        :return: The element of this SLAPerTestDefinition.  # noqa: E501
        :rtype: SLAElementDefinition
        """
        return self._element

    @element.setter
    def element(self, element):
        """Sets the element of this SLAPerTestDefinition.


        :param element: The element of this SLAPerTestDefinition.  # noqa: E501
        :type: SLAElementDefinition
        """

        self._element = element

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SLAPerTestDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SLAPerTestDefinition):
            return True

        return self.to_dict() != other.to_dict()
