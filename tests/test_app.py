import json
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
        assert "<title>My Personal Portfolio</title>" in html
        # TODO: Add more tests relating to the home page
        self.assertIn('Lovinson Dieujuste', html)

    def test_timeline(self):
        response = self.client.get("/api/timeline")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert 'posts' in json
        # assert len(json["posts"]) == 0 # uncomment when the malformed_timeline_post test is fixed
        # TODO: Add more tests relating to the timeline page
        response2 = self.client.get("/feed")
        assert response2.status_code == 200
        html = response2.get_data(as_text=True)
        self.assertIn('Timeline Feed', html)


    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

    def test_create_timeline_post(self):
        # Create a new timeline post
        response = self.client.post("/api/timeline", data={"name": "John Doe", "email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 200
        json = response.get_json()
        assert "id" in json

        # Get the timeline again
        response = self.client.get("/api/timeline")
        assert response.status_code == 200
        json = response.get_json()
        assert "posts" in json
        assert len(json["posts"]) == 1
        assert json["posts"][0]["name"] == "John Doe"
        assert json["posts"][0]["email"] == "john@example.com"
        assert json["posts"][0]["content"] == "Hello world, I'm John!"
    

    def test_delete_timeline_post(self):
        # Create a new timeline post
        response = self.client.post("/api/timeline", data={"name": "John Doe", "email": "john@example.com", "content": "Hello world, I'm John!"})
        self.assertEqual(response.status_code, 200)
        post = json.loads(response.data.decode('utf-8'))
        post_id = post['id']

        # Delete the post
        response = self.client.delete(f"/api/timeline?id={post_id}")
        self.assertEqual(response.status_code, 200)
        deleted_post = json.loads(response.data.decode('utf-8'))
        self.assertEqual(deleted_post['id'], post_id)

        # Verify the post was deleted
        response = self.client.get("/api/timeline")
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertNotIn(post_id, [post["id"] for post in json_data["posts"]])

if __name__ == '__main__':
    unittest.main()
