import pytest
from loan import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get("/")

    assert resp.status_code == 200

def test_predict(client):
    test_data = {
    "ApplicantIncome":10,
    "Credit_History":1.0,
    "Gender":"Male",
    "LoanAmount":120000,
    "Married":"No"
    }
    resp = client.post("/predict", json = test_data)
    assert resp.status_code == 200

    assert resp.json == {"loan_approval_status": "Rejected"}
    