from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_warning():
    response = client.post(
        "/notifications",
        json={
            "Type": "Warning",
            "Name": "Backup Failure",
            "Description": "The backup failed due to a database problem.",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Warning received, saved and forwarded to telegram"}


def test_notifications():
    response = client.post(
        "/notifications",
        json={
            "Type": "Info",
            "Name": "Quota Exceeded",
            "Description": "Compute Quota exceeded.",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Notification received and saved"}


def test_warning_lowercase():
    response = client.post(
        "/notifications",
        json={
            "Type": "warning",
            "Name": "Backup Failure",
            "Description": "The backup failed due to a database problem.",
        },
    )

    assert response.status_code == 422


def test_more_params():
    response = client.post(
        "/notifications",
        json={
            "Type": "Info",
            "Name": "Backup Failure",
            "Description": "The backup failed due to a database problem.",
            "Timestamp": "2023-01-01",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Notification received and saved"}

def test_missing_type():
    response = client.post(
        "/notifications",
        json={
            "Name": "Backup Failure",
            "Description": "The backup failed due to a database problem.",
        },
    )

    assert response.status_code == 422


def test_order():
    response = client.post(
        "/notifications",
        json={
            "Name": "Backup Failure2",
            "Type": "Warning",
            "Description": "The backup failed due to a database problem.",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Warning received, saved and forwarded to telegram"}
