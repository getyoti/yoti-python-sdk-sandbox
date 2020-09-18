from mock import Mock

from yoti_python_sandbox.doc_scan.check import SandboxDocumentTextDataCheckBuilder
from yoti_python_sandbox.doc_scan.check.report.breakdown import SandboxBreakdown
from yoti_python_sandbox.doc_scan.check.report.recommendation import (
    SandboxRecommendation,
)
from yoti_python_sandbox.doc_scan.document_filter import SandboxDocumentFilter


def test_should_build_sandbox_document_authenticity_check():
    recommendation_mock = Mock(spec=SandboxRecommendation)
    breakdown_mock = Mock(spec=SandboxBreakdown)

    check = (
        SandboxDocumentTextDataCheckBuilder()
        .with_recommendation(recommendation_mock)
        .with_breakdown(breakdown_mock)
        .build()
    )

    assert check.result.report.recommendation is not None
    assert check.result.report.recommendation == recommendation_mock
    assert len(check.result.report.breakdown) == 1
    assert check.result.report.breakdown[0] == breakdown_mock


def test_should_accept_document_filter():
    recommendation_mock = Mock(spec=SandboxRecommendation)
    breakdown_mock = Mock(spec=SandboxBreakdown)
    document_filter_mock = Mock(spec=SandboxDocumentFilter)

    check = (
        SandboxDocumentTextDataCheckBuilder()
        .with_recommendation(recommendation_mock)
        .with_breakdown(breakdown_mock)
        .with_document_filter(document_filter_mock)
        .build()
    )

    assert check.document_filter == document_filter_mock


def test_should_accept_with_breakdowns():
    recommendation_mock = Mock(spec=SandboxRecommendation)
    breakdowns_mock = [Mock(spec=SandboxBreakdown), Mock(spec=SandboxBreakdown)]

    check = (
        SandboxDocumentTextDataCheckBuilder()
        .with_recommendation(recommendation_mock)
        .with_breakdowns(breakdowns_mock)
        .build()
    )

    assert check.result.report.breakdown == breakdowns_mock


def test_should_allow_document_fields_set_with_dictionary():
    check = (
        SandboxDocumentTextDataCheckBuilder()
        .with_document_fields({"someKey": "someValue"})
        .build()
    )

    assert check.result.document_fields.get("someKey") == "someValue"


def test_should_exclude_document_fields_when_not_set():
    check = SandboxDocumentTextDataCheckBuilder().build()

    assert check.result.document_fields is None
