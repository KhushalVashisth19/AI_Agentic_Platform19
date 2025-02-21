from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_execute_workflow():
    workflow_id = "wf_456"  # Example workflow to test
    response = client.post(f"/execute/{workflow_id}")  # Send POST request

    assert response.status_code == 200  # Ensure successful execution
    assert response.json() == {
        "status": "Workflow executed",
        "workflow_id": workflow_id
    }  # Validate response structure

def test_execute_invalid_workflow():
    workflow_id = "invalid_wf"  # A workflow that does not exist
    response = client.post(f"/execute/{workflow_id}")  # Send POST request

    assert response.status_code == 404  # Ensure it returns "Not Found"
    assert response.json() == {"detail": "Workflow not found"}  # Validate error response
