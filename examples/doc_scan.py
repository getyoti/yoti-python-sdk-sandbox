from yoti_python_sandbox.doc_scan import (
    ResponseConfigBuilder,
    SandboxDocumentFilterBuilder,
)
from yoti_python_sandbox.doc_scan.check import (
    SandboxDocumentAuthenticityCheckBuilder,
    SandboxBreakdownBuilder,
    SandboxRecommendationBuilder,
    SandboxDocumentFaceMatchCheckBuilder,
    SandboxDocumentTextDataCheckBuilder,
    SandboxZoomLivenessCheckBuilder,
    SandboxDetail,
)
from yoti_python_sandbox.doc_scan.check_reports import SandboxCheckReportsBuilder
from yoti_python_sandbox.doc_scan.client import DocScanSandboxClient
from yoti_python_sandbox.doc_scan.task import (
    SandboxDocumentTextDataExtractionTaskBuilder,
)
from yoti_python_sandbox.doc_scan.task_results import SandboxTaskResultsBuilder


def doc_scan_example_snippet():
    document_filter = (
        SandboxDocumentFilterBuilder()
        .with_country_code("GBR")
        .with_document_type("PASSPORT")
        .build()
    )

    response_config = (
        ResponseConfigBuilder()
        .with_check_reports(
            (
                SandboxCheckReportsBuilder()
                .with_async_report_delay(10)
                .with_document_authenticity_check(
                    (
                        SandboxDocumentAuthenticityCheckBuilder()
                        .with_breakdown(
                            (
                                SandboxBreakdownBuilder()
                                .with_sub_check("security_features")
                                .with_result("NOT_AVAILABLE")
                                .with_detail(
                                    SandboxDetail("some_detail", "some_detail_value")
                                )
                                .build()
                            )
                        )
                        .with_recommendation(
                            (
                                SandboxRecommendationBuilder()
                                .with_value("NOT_AVAILABLE")
                                .with_reason("PICTURE_TOO_DARK")
                                .with_recovery_suggestion("BETTER_LIGHTING")
                                .build()
                            )
                        )
                        .with_document_filter(document_filter)
                        .build()
                    )
                )
                .with_document_face_match_check(
                    (
                        SandboxDocumentFaceMatchCheckBuilder()
                        .with_breakdown(
                            (
                                SandboxBreakdownBuilder()
                                .with_sub_check("security_features")
                                .with_result("PASS")
                                .build()
                            )
                        )
                        .with_recommendation(
                            (
                                SandboxRecommendationBuilder()
                                .with_value("APPROVE")
                                .build()
                            )
                        )
                        .with_document_filter(document_filter)
                        .build()
                    )
                )
                .with_document_text_data_check(
                    (
                        SandboxDocumentTextDataCheckBuilder()
                        .with_breakdown(
                            (
                                SandboxBreakdownBuilder()
                                .with_sub_check("document_in_date")
                                .with_result("PASS")
                                .build()
                            )
                        )
                        .with_recommendation(
                            (
                                SandboxRecommendationBuilder()
                                .with_value("APPROVE")
                                .build()
                            )
                        )
                        .with_document_filter(document_filter)
                        .with_document_field("full_name", "John Doe")
                        .with_document_field("nationality", "GBR")
                        .with_document_field("date_of_birth", "1986-06-01")
                        .with_document_field("document_number", "123456789")
                        .build()
                    )
                )
                .with_liveness_check(
                    (
                        SandboxZoomLivenessCheckBuilder()
                        .with_breakdown(
                            (
                                SandboxBreakdownBuilder()
                                .with_sub_check("security_features")
                                .with_result("PASS")
                                .build()
                            )
                        )
                        .with_recommendation(
                            (
                                SandboxRecommendationBuilder()
                                .with_value("APPROVE")
                                .build()
                            )
                        )
                        .build()
                    )
                )
                .build()
            )
        )
        .with_task_results(
            (
                SandboxTaskResultsBuilder()
                .with_text_extraction_task(
                    (
                        SandboxDocumentTextDataExtractionTaskBuilder()
                        .with_document_field("full_name", "John Doe")
                        .with_document_field("nationality", "GBR")
                        .with_document_field("date_of_birth", "1986-06-01")
                        .with_document_field("document_number", "123456789")
                        .with_document_filter(document_filter)
                        .build()
                    )
                )
                .build()
            )
        )
        .build()
    )

    sandbox_client_sdk_id = "YourSandboxClientSdkIdFromHub"
    pem_file_path = "path/to/your/pem/file.pem"

    doc_scan_sandbox_client = DocScanSandboxClient(sandbox_client_sdk_id, pem_file_path)

    doc_scan_sandbox_client.configure_session_response("yourSessionId", response_config)
