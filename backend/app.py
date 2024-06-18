from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, EduOps!"


@app.route('/tutorials/terraform')
def terraform_tutorial():
    content = {
        "title": "Terraform Tutorial",
        "description": "Learn how to provision infrastructure using Terraform.",
        "steps": [
            {"step": 1, "instruction": "Install Terraform from \
             https://www.terraform.io/downloads.html"},
            {"step": 2, "instruction": "Write a Terraform configuration \
             in main.tf file."},
            {"step": 3, "instruction": "Initialize Terraform using `terraform init`."},
            {"step": 4, "instruction": "Apply the configuration using \
             `terraform apply`."}
        ]
    }
    return jsonify(content)


@app.route('/tutorials/ansible')
def ansible_tutorial():
    content = {
        "title": "Ansible Tutorial",
        "description": "Learn how to automate infrastructure \
            provisioning using Ansible.",
        "steps": [
            {"step": 1, "instruction": "Install Ansible using \
             `pip install ansible`."},
            {"step": 2, "instruction": "Write an Ansible playbook \
             in playbook.yml file."},
            {"step": 3, "instruction": "Run the playbook using \
             `ansible-playbook playbook.yml`."}
        ]
    }
    return jsonify(content)


@app.route('/tutorials/github_actions')
def github_actions_tutorial():
    content = {
        "title": "GitHub Actions Tutorial",
        "description": "Learn how to set up a CI/CD pipeline using GitHub Actions.",
        "steps": [
            {"step": 1, "instruction": "Create a .github/workflows/ci.yml file."},
            {"step": 2, "instruction": "Add steps for checking out the code, \
             setting up Python, installing dependencies, linting, and testing."},
            {"step": 3, "instruction": "Push your code to GitHub \
             and verify the workflow runs."}
        ]
    }
    return jsonify(content)


@app.route('/tutorials/gitlab_ci')
def gitlab_ci_tutorial():
    content = {
        "title": "GitLab CI Tutorial",
        "description": "Learn how to set up a CI/CD pipeline using GitLab CI.",
        "steps": [
            {"step": 1, "instruction": "Create a .gitlab-ci.yml file."},
            {"step": 2, "instruction": "Define stages for build and test."},
            {"step": 3, "instruction": "Add steps for installing dependencies, \
             linting, and testing."},
            {"step": 4, "instruction": "Push your code to GitLab and verify the \
             pipeline runs."}
        ]
    }
    return jsonify(content)


@app.route('/tutorials/azure_pipelines')
def azure_pipelines_tutorial():
    content = {
        "title": "Azure Pipelines Tutorial",
        "description": "Learn how to set up a CI/CD pipeline using Azure Pipelines.",
        "steps": [
            {"step": 1, "instruction": "Create an azure-pipelines.yml file."},
            {"step": 2, "instruction": "Define steps for building and testing."},
            {"step": 3, "instruction": "Set up the Python environment,\
              install dependencies, and run tests."},
            {"step": 4, "instruction": "Push your code to Azure Repos \
             and verify the pipeline runs."}
        ]
    }
    return jsonify(content)


@app.route('/tutorials/argo_cd')
def argo_cd_tutorial():
    content = {
        "title": "Argo CD Tutorial",
        "description": "Learn how to implement GitOps using Argo CD.",
        "steps": [
            {"step": 1, "instruction": "Install Argo CD following the instructions at \
             https://argo-cd.readthedocs.io/en/stable/getting_started/."},
            {"step": 2, "instruction": "Create an application.yaml \
             file with your desired application configuration."},
            {"step": 3, "instruction": "Apply the configuration to Argo CD \
             using `kubectl apply -f application.yaml`."},
            {"step": 4, "instruction": "Monitor the deployment through the Argo CD UI."}
        ]
    }
    return jsonify(content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
