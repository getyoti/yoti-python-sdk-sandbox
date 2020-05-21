from yoti_python_sdk.utils import YotiSerializable

from .task_results import TaskResults


class ResponseConfig(YotiSerializable):
    def __init__(self, task_results: dict, check_report):
        self.__task_results = task_results
        self.__check_report = check_report

    def to_json(self):
        payload = {}
        if self.__task_results is not None:
            payload["task_results"] = self.__task_results

        if self.__check_report is not None:
            payload["check_reports"] = self.__check_report

        return payload


class ResponseConfigBuilder(object):
    def __init__(self):
        self.__task_results = None
        self.__check_report = None

    def with_task_results(self, results):
        """
        :param results: the task result container
        :type results: TaskResults
        """
        self.__task_results = results
        return self

    def with_check_report(self, report):
        self.__check_report = report
        return self

    def build(self):
        return ResponseConfig(self.__task_results, self.__check_report)
