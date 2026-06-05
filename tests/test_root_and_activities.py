def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_seeded_data(client):
    response = client.get("/activities")

    assert response.status_code == 200

    data = response.json()
    assert "Chess Club" in data
    assert data["Chess Club"]["max_participants"] == 12
    assert data["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]
