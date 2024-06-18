from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, EduOps!"


@app.route('/tutorials/terraform')
def terraform_tutorial():
    content = {
        "title": "Terraform Tutorial",
        "steps": [
            "Install Terraform",
            "Write a Terraform configuration",
            "Initialize Terraform",
            "Apply the configuration"
        ]
    }
    return jsonify(content)


@app.route('/tutorials/ansible')
def ansible_tutorial():
    content = {
        "title": "Ansible Tutorial",
        "steps": [
            "Install Ansible",
            "Write an Ansible playbook",
            "Run the playbook"
        ]
    }
    return jsonify(content)


@app.route('/tutorials/github_actions')
def github_actions_tutorial():
    content = {
        "title": "GitHub Actions Tutorial",
        "steps": [
            "Create a .github/workflows/ci.yml file",
            "Add steps for checking out the code",
            "Set up the Python environment",
            "Install dependencies",
            "Run linting and tests"
        ]
    }
    return jsonify(content)


@app.route('/tutorials/gitlab_ci')
def gitlab_ci_tutorial():
    content = {
        "title": "GitLab CI Tutorial",
        "steps": [
            "Create a .gitlab-ci.yml file",
            "Define stages for build and test",
            "Add steps for installing dependencies",
            "Run linting and tests"
        ]
    }
    return jsonify(content)


@app.route('/tutorials/azure_pipelines')
def azure_pipelines_tutorial():
    content = {
        "title": "Azure Pipelines Tutorial",
        "steps": [
            "Create an azure-pipelines.yml file",
            "Define steps for building and testing",
            "Set up the Python environment",
            "Install dependencies",
            "Run tests"
        ]
    }
    return jsonify(content)


@app.route('/tutorials/argo_cd')
def argo_cd_tutorial():
    content = {
        "title": "Argo CD Tutorial",
        "steps": [
            "Install Argo CD",
            "Create an application.yaml file",
            "Apply the configuration to Argo CD",
            "Monitor the deployment"
        ]
    }
    return jsonify(content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
