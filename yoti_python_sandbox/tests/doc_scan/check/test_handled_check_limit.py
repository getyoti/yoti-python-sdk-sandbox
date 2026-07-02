"""
Tests for handled_check_limit on all IDV sandbox check-report types.
"""
import pytest

from yoti_python_sandbox.doc_scan.check import (
    SandboxDocumentAuthenticityCheckBuilder,
    SandboxDocumentFaceMatchCheckBuilder,
    SandboxDocumentTextDataCheckBuilder,
    SandboxIdDocumentComparisonCheckBuilder,
    SandboxSupplementaryDocumentTextDataCheckBuilder,
    SandboxZoomLivenessCheckBuilder,
)


HANDLED_CHECK_LIMIT = 3

ALL_BUILDER_CLASSES = [
    SandboxDocumentAuthenticityCheckBuilder,
    SandboxDocumentFaceMatchCheckBuilder,
    SandboxDocumentTextDataCheckBuilder,
    SandboxIdDocumentComparisonCheckBuilder,
    SandboxSupplementaryDocumentTextDataCheckBuilder,
    SandboxZoomLivenessCheckBuilder,
]


@pytest.mark.parametrize("builder_class", ALL_BUILDER_CLASSES)
def test_handled_check_limit_is_included_in_json_when_set(builder_class):
    check = builder_class().with_handled_check_limit(HANDLED_CHECK_LIMIT).build()

    json = check.to_json()

    assert json.get("handled_check_limit") == HANDLED_CHECK_LIMIT


@pytest.mark.parametrize("builder_class", ALL_BUILDER_CLASSES)
def test_handled_check_limit_is_omitted_from_json_when_not_set(builder_class):
    check = builder_class().build()

    json = check.to_json()

    assert "handled_check_limit" not in json


@pytest.mark.parametrize("builder_class", ALL_BUILDER_CLASSES)
def test_handled_check_limit_property_returns_set_value(builder_class):
    check = builder_class().with_handled_check_limit(HANDLED_CHECK_LIMIT).build()

    assert check.handled_check_limit == HANDLED_CHECK_LIMIT


@pytest.mark.parametrize("builder_class", ALL_BUILDER_CLASSES)
def test_handled_check_limit_property_returns_none_when_not_set(builder_class):
    check = builder_class().build()

    assert check.handled_check_limit is None


def test_document_authenticity_check_handled_check_limit_end_to_end():
    check = (
        SandboxDocumentAuthenticityCheckBuilder()
        .with_handled_check_limit(5)
        .build()
    )

    json = check.to_json()

    assert json.get("handled_check_limit") == 5
    assert check.handled_check_limit == 5


def test_zoom_liveness_check_handled_check_limit_end_to_end():
    check = (
        SandboxZoomLivenessCheckBuilder()
        .with_handled_check_limit(2)
        .build()
    )

    json = check.to_json()

    assert json.get("handled_check_limit") == 2
    assert check.handled_check_limit == 2
    assert check.liveness_type == "ZOOM"


def test_id_document_comparison_check_handled_check_limit_end_to_end():
    check = (
        SandboxIdDocumentComparisonCheckBuilder()
        .with_handled_check_limit(1)
        .build()
    )

    json = check.to_json()

    assert json.get("handled_check_limit") == 1


def test_document_face_match_check_handled_check_limit_end_to_end():
    check = (
        SandboxDocumentFaceMatchCheckBuilder()
        .with_handled_check_limit(10)
        .build()
    )

    json = check.to_json()

    assert json.get("handled_check_limit") == 10


def test_document_text_data_check_handled_check_limit_end_to_end():
    check = (
        SandboxDocumentTextDataCheckBuilder()
        .with_handled_check_limit(7)
        .build()
    )

    json = check.to_json()

    assert json.get("handled_check_limit") == 7


def test_supplementary_document_text_data_check_handled_check_limit_end_to_end():
    check = (
        SandboxSupplementaryDocumentTextDataCheckBuilder()
        .with_handled_check_limit(4)
        .build()
    )

    json = check.to_json()

    assert json.get("handled_check_limit") == 4


def test_existing_builder_calls_remain_backward_compatible():
    """Ensure existing callers that do not set handled_check_limit still work."""
    check = (
        SandboxDocumentAuthenticityCheckBuilder()
        .build()
    )

    assert check.handled_check_limit is None
    json = check.to_json()
    assert "handled_check_limit" not in json
