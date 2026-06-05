from urllib.parse import quote


def test_unregister_removes_registered_student(client):
    encoded_activity = quote("Tennis Club", safe="")
    email = "isabella@mergington.edu"

    response = client.delete(
        f"/activities/{encoded_activity}/unregister",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Tennis Club"}

    activities_response = client.get("/activities")
    participants = activities_response.json()["Tennis Club"]["participants"]
    assert email not in participants


def test_unregister_returns_404_for_unknown_activity(client):
    encoded_activity = quote("Unknown Club", safe="")

    response = client.delete(
        f"/activities/{encoded_activity}/unregister",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_returns_400_for_student_not_registered(client):
    encoded_activity = quote("Chess Club", safe="")

    response = client.delete(
        f"/activities/{encoded_activity}/unregister",
        params={"email": "nobody@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Student is not signed up for this activity"
    }
