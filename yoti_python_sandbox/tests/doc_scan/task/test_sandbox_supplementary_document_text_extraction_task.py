from mock import Mock

from yoti_python_sandbox.doc_scan.document_filter import SandboxDocumentFilter
from yoti_python_sandbox.doc_scan.task import (
    SandboxSupplementaryDocumentTextDataExtractionTaskBuilder,
)
from yoti_python_sandbox.doc_scan.task.sandbox_text_extraction_recommendation import (
    SandboxTextDataExtractionRecommendation,
)


def test_should_allow_single_key_value_document_field():
    task = (
        SandboxSupplementaryDocumentTextDataExtractionTaskBuilder()
        .with_document_field("someKey", "someValue")
        .build()
    )

    assert "someKey" in task.result.document_fields
    assert task.result.document_fields.get("someKey") == "someValue"


def test_should_allow_document_fields_set_with_dictionary():
    task = (
        SandboxSupplementaryDocumentTextDataExtractionTaskBuilder()
        .with_document_fields({"someKey": "someValue"})
        .build()
    )

    assert task.result.document_fields.get("someKey") == "someValue"


def test_should_allow_multiple_document_fields():
    task = (
        SandboxSupplementaryDocumentTextDataExtractionTaskBuilder()
        .with_document_field("someKey", "someValue")
        .with_document_field("someOtherKey", "someOtherValue")
        .build()
    )

    assert task.result.document_fields.get("someKey") == "someValue"
    assert task.result.document_fields.get("someOtherKey") == "someOtherValue"


def test_json_should_include_document_fields_when_set():
    task = (
        SandboxSupplementaryDocumentTextDataExtractionTaskBuilder()
        .with_document_field("someKey", "someValue")
        .build()
    )

    json = task.to_json()

    assert (
        json.get("result").to_json().get("document_fields").get("someKey")
        == "someValue"
    )


def test_json_should_exclude_document_fields_when_not_set():
    task = SandboxSupplementaryDocumentTextDataExtractionTaskBuilder().build()

    json = task.to_json()

    assert json.get("result").to_json().get("document_fields") is None


def test_should_accept_document_filter():
    document_filter_mock = Mock(spec=SandboxDocumentFilter)

    task = (
        SandboxSupplementaryDocumentTextDataExtractionTaskBuilder()
        .with_document_filter(document_filter_mock)
        .build()
    )

    assert task.document_filter == document_filter_mock


def test_json_includes_document_filter():
    document_filter_mock = Mock(spec=SandboxDocumentFilter)

    task = (
        SandboxSupplementaryDocumentTextDataExtractionTaskBuilder()
        .with_document_filter(document_filter_mock)
        .build()
    )

    json = task.to_json()

    assert json.get("document_filter") == document_filter_mock


def test_json_should_not_include_recommendation_when_not_set():
    task = SandboxSupplementaryDocumentTextDataExtractionTaskBuilder().build()

    json = task.to_json()
    json_result = json.get("result").to_json()

    assert json_result.get("recommendation") is None


def test_json_should_include_recommendation_when_set():
    recommendation_mock = Mock(spec=SandboxTextDataExtractionRecommendation)

    task = (
        SandboxSupplementaryDocumentTextDataExtractionTaskBuilder()
        .with_recommendation(recommendation_mock)
        .build()
    )

    json = task.to_json()
    json_result = json.get("result").to_json()

    assert json_result.get("recommendation") == recommendation_mock


def test_json_should_not_include_detected_country_when_not_set():
    task = SandboxSupplementaryDocumentTextDataExtractionTaskBuilder().build()

    json = task.to_json()
    json_result = json.get("result").to_json()

    assert json_result.get("detected_country") is None


def test_json_should_include_detected_country_when_set():
    some_country = "some-country"

    task = (
        SandboxSupplementaryDocumentTextDataExtractionTaskBuilder()
        .with_detected_country(some_country)
        .build()
    )

    json = task.to_json()
    json_result = json.get("result").to_json()

    assert json_result.get("detected_country") == some_country
