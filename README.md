# EduOps

EduOps is an interactive DevOps simulation environment designed to help users practice and enhance their DevOps skills. This project includes setting up Infrastructure as Code (IaC), managing CI/CD pipelines, deploying applications, monitoring and alerting, troubleshooting, and receiving real-time feedback with progress tracking.

## Features

- **Infrastructure as Code (IaC) Setup:** Provision and manage infrastructure using tools like Terraform and Ansible.
- **CI/CD Pipelines:** Automate build, test, and deployment processes using GitHub Actions, GitLab CI, Azure DevOps, and Argo CD.
- **Application Deployment:** Deploy applications using Docker and Kubernetes.
- **Monitoring and Alerting:** Set up monitoring and alerting systems using Prometheus and Grafana.
- **Troubleshooting:** Practice troubleshooting common issues in a DevOps environment.
- **Real-Time Feedback:** Receive immediate feedback on actions performed within the environment.
- **Progress Tracking:** Track learning progress and performance analytics.

## Getting Started

Follow these instructions to set up the project locally and start contributing.

### Prerequisites

- [Python 3.x](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

### Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/yourusername/EduOps.git
    cd EduOps
    ```

2. **Set Up the Backend:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r backend/requirements.txt
    ```

3. **Set Up Docker and Docker Compose:**

    ```sh
    docker-compose up --build
    ```

4. **Run the Application:**

    - Backend: Access the Flask application at `http://localhost:5000`
    - Frontend: Access the frontend at `http://localhost`

## Usage

- **Access the Frontend:**
  Open a browser and navigate to `http://localhost`.

- **Access the Backend API:**
  Use a tool like Postman or curl to interact with the API endpoints at `http://localhost:5000`.

## Contributing

We welcome contributions from the community. Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Docker](https://www.docker.com/)
- [GitHub Actions](https://github.com/features/actions)
