"""Tests for the views of the app."""


def test_index_page(client):
    """Test that the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Task Manager' in response.data
