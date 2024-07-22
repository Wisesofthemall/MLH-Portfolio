# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        
        # More tests
        assert "<section class=\"profile text-white\">" in html
        assert "Robin Batingan Portfolio" in html
        assert "<div id=\"profile-picture\" class=\"profile-picture\">" in html


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # More tests
        # Test POST /api/timeline_post
        response = self.client.post("/api/timeline_post", data={
            'name': 'Ahmed Khaleel',
            'email': 'ahmedkhaleel2004@gmail.com',
            'content': 'Hello world, I\'m Ahmed!'
        })

        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == 'Ahmed Khaleel'
        assert json["email"] == 'ahmedkhaleel2004@gmail.com'
        assert json["content"] == 'Hello world, I\'m Ahmed!'

        # Verify that the post was added to the database
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == 'Ahmed Khaleel'
        assert json["timeline_posts"][0]["email"] == 'ahmedkhaleel2004@gmail.com'
        assert json["timeline_posts"][0]["content"] == 'Hello world, I\'m Ahmed!'

        # Test the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h1>Timeline</h1>" in html
        assert "<h2>Submit a Timeline Post</h2>" in html
        assert "<form action=\"/timeline_post\" method=\"post\">" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
