def test_index(client):
    """Test the index route"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"My Personal Portfolio" in rv.data

def test_about(client):
    """Test the about route"""
    rv = client.get('/about')
    assert rv.status_code == 200
    assert b"About" in rv.data

def test_work(client):
    """Test the work route"""
    rv = client.get('/work')
    assert rv.status_code == 200
    assert b"Work Experience" in rv.data

def test_hobby(client):
    """Test the hobby route"""
    rv = client.get('/hobby')
    assert rv.status_code == 200
    assert b"Hobbies" in rv.data

def test_education(client):
    """Test the education route"""
    rv = client.get('/education')
    assert rv.status_code == 200
    assert b"Education" in rv.data

def test_place(client):
    """Test the place route"""
    rv = client.get('/place')
    assert rv.status_code == 200
    assert b"Places" in rv.data



