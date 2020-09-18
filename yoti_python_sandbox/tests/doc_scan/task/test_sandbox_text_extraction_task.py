from mock import Mock

from yoti_python_sandbox.doc_scan.document_filter import SandboxDocumentFilter
from yoti_python_sandbox.doc_scan.task import (
    SandboxDocumentTextDataExtractionTaskBuilder,
)


def test_should_allow_single_key_value_document_field():
    task = (
        SandboxDocumentTextDataExtractionTaskBuilder()
        .with_document_field("someKey", "someValue")
        .build()
    )

    assert "someKey" in task.result.document_fields
    assert task.result.document_fields.get("someKey") == "someValue"


def test_should_allow_document_fields_set_with_dictionary():
    task = (
        SandboxDocumentTextDataExtractionTaskBuilder()
        .with_document_fields({"someKey": "someValue"})
        .build()
    )

    assert task.result.document_fields.get("someKey") == "someValue"


def test_should_allow_multiple_document_fields():
    task = (
        SandboxDocumentTextDataExtractionTaskBuilder()
        .with_document_field("someKey", "someValue")
        .with_document_field("someOtherKey", "someOtherValue")
        .build()
    )

    assert task.result.document_fields.get("someKey") == "someValue"
    assert task.result.document_fields.get("someOtherKey") == "someOtherValue"


def test_should_exclude_document_fields_when_not_set():
    task = SandboxDocumentTextDataExtractionTaskBuilder().build()

    assert task.result.document_fields is None
    assert task.result.to_json() == {}


def test_should_accept_document_filter():
    document_filter_mock = Mock(spec=SandboxDocumentFilter)

    task = (
        SandboxDocumentTextDataExtractionTaskBuilder()
        .with_document_filter(document_filter_mock)
        .build()
    )

    assert task.document_filter == document_filter_mock
