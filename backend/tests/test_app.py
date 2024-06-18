import pytest
from backend.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    rv = client.get('/')
    assert rv.data == b'Hello, EduOps!'


def test_terraform_tutorial(client):
    rv = client.get('/tutorials/terraform')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'title' in json_data
    assert json_data['title'] == "Terraform Tutorial"


def test_ansible_tutorial(client):
    rv = client.get('/tutorials/ansible')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'title' in json_data
    assert json_data['title'] == "Ansible Tutorial"


def test_github_actions_tutorial(client):
    rv = client.get('/tutorials/github_actions')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'title' in json_data
    assert json_data['title'] == "GitHub Actions Tutorial"


def test_gitlab_ci_tutorial(client):
    rv = client.get('/tutorials/gitlab_ci')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'title' in json_data
    assert json_data['title'] == "GitLab CI Tutorial"


def test_azure_pipelines_tutorial(client):
    rv = client.get('/tutorials/azure_pipelines')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'title' in json_data
    assert json_data['title'] == "Azure Pipelines Tutorial"


def test_argo_cd_tutorial(client):
    rv = client.get('/tutorials/argo_cd')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'title' in json_data
    assert json_data['title'] == "Argo CD Tutorial"
