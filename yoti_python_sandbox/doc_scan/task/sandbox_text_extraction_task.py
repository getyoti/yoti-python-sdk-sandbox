from yoti_python_sdk.utils import YotiSerializable
from yoti_python_sandbox.doc_scan.document_filter import (  # noqa: F401
    SandboxDocumentFilter,
)


class SandboxDocumentTextDataExtractionTaskResult(YotiSerializable):
    def __init__(self, document_fields=None):
        self.__document_fields = document_fields

    @property
    def document_fields(self):
        return self.__document_fields

    def to_json(self):
        json = {}

        if self.document_fields is not None:
            json["document_fields"] = self.document_fields

        return json


class SandboxDocumentTextDataExtractionTask(YotiSerializable):
    def __init__(self, result, document_filter):
        self.__result = result
        self.__document_filter = document_filter

    @property
    def result(self):
        """
        :rtype: SandboxDocumentTextDataExtractionTaskResult
        """
        return self.__result

    @property
    def document_filter(self):
        """
        :rtype: SandboxDocumentFilter
        """
        return self.__document_filter

    def to_json(self):
        obj = {
            "result": self.__result,
        }
        if self.__document_filter is not None:
            obj["document_filter"] = self.__document_filter
        return obj


class SandboxDocumentTextDataExtractionTaskBuilder(object):
    def __init__(self):
        self.__document_fields = None
        self.__document_filter = None

    def with_document_field(self, key, value):
        """
        :type key: str
        :type value: str or dict
        :rtype: SandboxDocumentTextDataExtractionTaskBuilder
        """
        self.__document_fields = self.__document_fields or {}
        self.__document_fields[key] = value
        return self

    def with_document_fields(self, document_fields):
        """
        :type document_fields: dict
        :rtype: SandboxDocumentTextDataExtractionTaskBuilder
        """
        self.__document_fields = document_fields
        return self

    def with_document_filter(self, document_filter):
        """
        :type document_filter: SandboxDocumentFilter
        :rtype: SandboxDocumentTextDataExtractionTaskBuilder
        """
        self.__document_filter = document_filter
        return self

    def build(self):
        result = SandboxDocumentTextDataExtractionTaskResult(self.__document_fields)
        return SandboxDocumentTextDataExtractionTask(result, self.__document_filter)
