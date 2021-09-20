from mock import Mock

from yoti_python_sandbox.doc_scan.check import SandboxThirdPartyCheckBuilder
from yoti_python_sandbox.doc_scan.check.report.recommendation import (
    SandboxRecommendation,
)
from yoti_python_sandbox.doc_scan.check.report.breakdown import SandboxBreakdown


def test_third_party_check_should_set_correct_manual_check_and_type():
    check = SandboxThirdPartyCheckBuilder().with_manual_check("NEVER")

    assert check.manual_check == "NEVER"
    assert check.type == "THIRD_PARTY_IDENTITY"


def test_third_party_check_build_result_object():
    recommendation_mock = Mock(spec=SandboxRecommendation)
    breakdown_mock = Mock(spec=SandboxBreakdown)

    check = (
        SandboxThirdPartyCheckBuilder()
        .with_recommendation(recommendation_mock)
        .with_breakdown(breakdown_mock)
        .build()
    )

    assert check.result.report.recommendation is not None
    assert check.result.report.recommendation == recommendation_mock
    assert len(check.result.report.breakdown) == 1
    assert check.result.report.breakdown[0] == breakdown_mock
