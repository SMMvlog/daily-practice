import pytest
import json
from utils.encrypt_hash_payload import encryptPayloadRsa, decryptRequest

@pytest.fixture(scope="session")
def app():
    # "provide a Flask app instance configured for testing"
    flask = create_app()
    flask_app.config["TESTING"] = True
    flask_app.config["WTF_CSRF_ENABLED"] = False
    with flask_app.app_context():
        yield flask_app #Ensure app context exists

@pytest.fixture(scope="session")
def client(app):
    # "provide a test client for making API requests."
    return app.test_client()

@pytest.fixture
def token_header(app):
    # "Generate an authentication token for tests"
    with app.app_context():
        token = create_token(TEST_MOBILE_NUMBER,source=TEST_SOURCE)
        return {"Token":token}


@pytest.mark.order(19)
@pytest.mark.parametrize("test_payload, expect_success, expected_status",[
    ({},False,400),
    ({"account_id":"","kyc_flow":"","current_stage":""},False,400),
    ({"account_id":"231242","kyc_flow":"VKYC","current_stage":"VKYC"},True,200),
])
def test_face_match(client,test_payload,expect_success,expected_status,token_header):
    # "Test face match api"
    payload = {"data":encryptPayloadRsa(test_payload)}
    response = client.post("/epl/faceMatch",data=payload,headers=token_header)

    if response.status_code ==200:
        response_body = json.loads(decryptRequest(response.text,"EPL"))
        assert response_body.get("Success") is expect_success, f"Unexpected response:{response_body}"
    else:
        assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"


#Payload
@pytest.fixture
def digital_sign_payload(application_form_number):
    return {"application_form_number":application_form_number}



# delink api

@pytes.fixture(scope="session",autouse=True)
def cleaner_after_testes(app):
    "Cleanup function that runs **after all tests**."
    yield # Ensure all tests run first

    with app.app_context():
        application = EplcutomerDetails.query.filter_by(mobile=TEST_MOBILE_NUMBER,source=TEST_SOURCE).first()
        if application:
            delink_api_call(application,TEST_MOBILE_NUMBER,application.source,"CANCELLED","Test case application delinked")
