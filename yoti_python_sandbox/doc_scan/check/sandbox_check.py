from abc import ABCMeta
from abc import abstractmethod

from .sandbox_check_result import SandboxCheckResult  # noqa: F401
from yoti_python_sdk.utils import YotiSerializable


class SandboxCheck(YotiSerializable):
    def __init__(self, result, handled_check_limit=None):
        """
        :param result: the result
        :type result: SandboxCheckResult
        :param handled_check_limit: optional limit on how many times this check response is used
        :type handled_check_limit: int or None
        """
        self.__result = result
        self.__handled_check_limit = handled_check_limit

    @property
    def result(self):
        """
        :rtype: SandboxCheckResult
        """
        return self.__result

    @property
    def handled_check_limit(self):
        """
        The number of times this configured check response is used before the sandbox
        advances to the next configured response. When None, the backend treats it as
        no limit.

        :rtype: int or None
        """
        return self.__handled_check_limit

    def to_json(self):
        json = {"result": self.result}
        if self.__handled_check_limit is not None:
            json["handled_check_limit"] = self.__handled_check_limit
        return json


class SandboxCheckBuilder(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__recommendation = None
        self.__breakdown = []
        self.__handled_check_limit = None

    def with_recommendation(self, recommendation):
        self.__recommendation = recommendation
        return self

    def with_breakdown(self, breakdown):
        self.__breakdown.append(breakdown)
        return self

    def with_breakdowns(self, breakdowns):
        self.__breakdown = breakdowns
        return self

    def with_handled_check_limit(self, handled_check_limit):
        """
        Sets the number of times this configured check response is used before the sandbox
        advances to the next configured response.

        :param handled_check_limit: the limit
        :type handled_check_limit: int
        :return: the builder
        :rtype: SandboxCheckBuilder
        """
        self.__handled_check_limit = handled_check_limit
        return self

    @property
    def recommendation(self):
        return self.__recommendation

    @property
    def breakdown(self):
        return self.__breakdown

    @property
    def handled_check_limit(self):
        return self.__handled_check_limit

    @abstractmethod
    def build(self):
        raise NotImplementedError
