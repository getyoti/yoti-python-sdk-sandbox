import json

from yoti_python_sandbox import SandboxAgeVerificationBuilder
from yoti_python_sandbox import SandboxClientBuilder
from yoti_python_sandbox import YotiTokenRequestBuilder


def profile_example_snippet():
    sandbox_client_sdk_id = "CLIENT_SDK_ID"
    pem_file_path = "/path/to/your-pem-file.pem"

    client = (
        SandboxClientBuilder()
        .for_application(sandbox_client_sdk_id)
        .with_pem_file(pem_file_path)
        .build()
    )

    age_verification = (
        SandboxAgeVerificationBuilder()
        .with_date_of_birth("1989-01-02")
        .with_age_over(18)
        .build()
    )

    some_base64_encoded_selfie = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk"
        "+A8AAQUBAScY42YAAAAASUVORK5CYII= "
    )

    token_request = (
        YotiTokenRequestBuilder()
        .with_remember_me_id("some_remember_me_id")
        .with_given_names("Some Given Names")
        .with_family_name("Some Family Name")
        .with_full_name("Some Full Name")
        .with_date_of_birth("1989-01-02")
        .with_age_verification(age_verification)
        .with_gender("Some Gender")
        .with_phone_number("Some Phone Number")
        .with_nationality("Some Nationality")
        .with_postal_address("Some Postal Address")
        .with_structured_postal_address(
            json.dumps({"building_number": 1, "address_line1": "Some Address"})
        )
        .with_base64_selfie(some_base64_encoded_selfie)
        .with_email_address("Some Email Address")
        .with_document_details("PASSPORT USA 1234abc")
        .build()
    )

    token_response = client.setup_sharing_profile(token_request)

    # Use the share_token to get Activity Details like normal
    share_token = token_response.token

    assert isinstance(share_token, str)
