from urllib.parse import quote


def test_signup_adds_new_student_to_activity(client):
    encoded_activity = quote("Chess Club", safe="")
    email = "new.student@mergington.edu"

    response = client.post(
        f"/activities/{encoded_activity}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email in participants


def test_signup_returns_404_for_unknown_activity(client):
    encoded_activity = quote("Unknown Club", safe="")

    response = client.post(
        f"/activities/{encoded_activity}/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_returns_400_for_duplicate_student(client):
    encoded_activity = quote("Chess Club", safe="")

    response = client.post(
        f"/activities/{encoded_activity}/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Student already signed up for this activity"
    }
