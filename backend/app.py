from flask import Flask, jsonify
from pytheus.metrics import Histogram
from pytheus.exposition import generate_metrics

app = Flask(__name__)


histogram = Histogram('page_visits_latency_seconds', 'used for testing')


@app.route('/metrics')
def metrics():
    return generate_metrics()


@app.route('/')
def hello():
    with histogram.time():
        return "Hello, EduOps!"


@app.route('/tutorials/terraform')
def terraform_tutorial():
    content = {
        "title": "Terraform Tutorial",
        "description": "Learn how to provision infrastructure using Terraform.",
        "steps": [
            {"step": 1, "instruction": "Install Terraform from https://www.terraform.io/downloads.html"},
            {"step": 2, "instruction": "Write a Terraform configuration in main.tf file."},
            {"step": 3, "instruction": "Initialize Terraform using `terraform init`."},
            {"step": 4, "instruction": "Apply the configuration using `terraform apply`."},
            {"step": 5, "instruction": "Example code:\n```hcl\nprovider \"aws\" {\n  region = \"us-west-2\"\n}\n\nresource \"aws_instance\" \"example\" {\n  ami           = \"ami-0c55b159cbfafe1f0\"\n  instance_type = \"t2.micro\"\n\n  tags = {\n    Name = \"ExampleInstance\"\n  }\n}\n```"}
        ]
    }
    return jsonify(content)

@app.route('/tutorials/ansible')
def ansible_tutorial():
    content = {
        "title": "Ansible Tutorial",
        "description": "Learn how to automate infrastructure provisioning using Ansible.",
        "steps": [
            {"step": 1, "instruction": "Install Ansible using `pip install ansible`."},
            {"step": 2, "instruction": "Write an Ansible playbook in playbook.yml file."},
            {"step": 3, "instruction": "Run the playbook using `ansible-playbook playbook.yml`."},
            {"step": 4, "instruction": "Example code:\n```yaml\n- hosts: localhost\n  tasks:\n    - name: Ensure Apache is installed\n      apt:\n        name: apache2\n        state: present\n```"}
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
            {"step": 2, "instruction": "Add steps for checking out the code, setting up Python, installing dependencies, linting, and testing."},
            {"step": 3, "instruction": "Push your code to GitHub and verify the workflow runs."},
            {"step": 4, "instruction": "Example code:\n```yaml\nname: CI\n\non: [push, pull_request]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n\n    steps:\n    - uses: actions/checkout@v4\n\n    - name: Set up Python\n      uses: actions/setup-python@v5\n      with:\n        python-version: '3.x'\n\n    - name: Install dependencies\n      run: |\n        python -m pip install --upgrade pip\n        pip install -r backend/requirements.txt\n\n    - name: List installed packages\n      run: |\n        pip list\n\n    - name: Lint with flake8\n      run: |\n        flake8 backend\n\n    - name: Run tests\n      run: |\n        cd backend\n        python3 -m pytest tests/\n```"}
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
            {"step": 3, "instruction": "Add steps for installing dependencies, linting, and testing."},
            {"step": 4, "instruction": "Push your code to GitLab and verify the pipeline runs."},
            {"step": 5, "instruction": "Example code:\n```yaml\nstages:\n  - build\n  - test\n\nbuild-job:\n  stage: build\n  script:\n    - echo \"Building the application...\"\n    - python -m pip install --upgrade pip\n    - pip install -r backend/requirements.txt\n\ntest-job:\n  stage: test\n  script:\n    - echo \"Running tests...\"\n    - cd backend\n    - python3 -m pytest tests/\n```"}
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
            {"step": 3, "instruction": "Set up the Python environment, install dependencies, and run tests."},
            {"step": 4, "instruction": "Push your code to Azure Repos and verify the pipeline runs."},
            {"step": 5, "instruction": "Example code:\n```yaml\ntrigger:\n  - main\n\npool:\n  vmImage: 'ubuntu-latest'\n\nsteps:\n  - script: echo Building the application...\n    displayName: 'Build Step'\n    - script: |\n      python -m pip install --upgrade pip\n      pip install -r backend/requirements.txt\n\n  - script: echo Running tests...\n    displayName: 'Test Step'\n    - script: |\n      cd backend\n      python3 -m pytest tests/\n```"}
        ]
    }
    return jsonify(content)

@app.route('/tutorials/argo_cd')
def argo_cd_tutorial():
    content = {
        "title": "Argo CD Tutorial",
        "description": "Learn how to implement GitOps using Argo CD.",
        "steps": [
            {"step": 1, "instruction": "Install Argo CD following the instructions at https://argo-cd.readthedocs.io/en/stable/getting_started/."},
            {"step": 2, "instruction": "Create an application.yaml file with your desired application configuration."},
            {"step": 3, "instruction": "Apply the configuration to Argo CD using `kubectl apply -f application.yaml`."},
            {"step": 4, "instruction": "Monitor the deployment through the Argo CD UI."},
            {"step": 5, "instruction": "Example code:\n```yaml\napiVersion: argoproj.io/v1alpha1\nkind: Application\nmetadata:\n  name: eduops-application\n  namespace: argocd\nspec:\n  project: default\n\n  source:\n    repoURL: 'https://github.com/yourusername/EduOps.git'\n    targetRevision: HEAD\n    path: examples/kubernetes\n\n  destination:\n    server: 'https://kubernetes.default.svc'\n    namespace: default\n\n  syncPolicy:\n    automated:\n      prune: true\n      selfHeal: true\n    syncOptions:\n      - CreateNamespace=true\n```"}
        ]
    }
    return jsonify(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
