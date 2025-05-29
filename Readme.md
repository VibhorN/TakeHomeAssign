# URL Shortener
This is a simple URL shortener service built using FastAPI, PostgreSQL, Docker, and GitHub Actions for CI/CD, deployed on Google Cloud Run. It provides RESTful API endpoints for creating, redirecting, and tracking shortened URLs.

# Running the project locally:

## Clone the repo:
git clone https://github.com/VibhorN/TakeHomeAssign.git

## Create an env variable for the DATABASE_URL:
DATABASE_URL=postgresql://postgres:<password>@db:5432/url_db

## Run the project:
docker-compose up -- build

## Access the API at http://localhost.8000.

# Example API Commands:

## Create a short URL: 
curl -X POST http://localhost:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'

## Redirect to Original URL: 
curl -i http://localhost:8000/abc123

## Get Analytics for Short URL: 
curl http://localhost:8000/analytics/abc123

# CI/CD

This project uses GitHub Actions for CI/CD automation. The pipeline runs on every push to the main branch. It Executes unit tests, builds the Docker image, pushes the image to Google Artifact Registry, deploys the image to Google Cloud Run using gcloud run deploy.

The CI/CD pipeline connects the deployed Cloud Run service to a Cloud SQL (PostgreSQL) instance using the Unix socket method (/cloudsql/instance-connection-name). The DATABASE_URL environment variable in the deployment specifies the Cloud SQL connection.

# How Deployment Works

The service is deployed to Google Cloud Run using the following steps:

The GitHub Actions workflow builds the Docker image and pushes it to Google Artifact Registry.

The workflow runs gcloud run deploy with the following flags:
--image: The Docker image URL from Artifact Registry.
--region: The deployment region (e.g., us-west1).
--allow-unauthenticated: Allows public access.
--set-env-vars: Injects environment variables, including the DATABASE_URL pointing to the Cloud SQL instance via Unix socket (host=/cloudsql/...).

This connects the Cloud Run service to the Cloud SQL database for production usage.

# Time Breakdown:

API development with FastAPI: 4 hours

Dockerization: 1-2 hours

CI/CD pipeline setup with GitHub Actions (including Cloud SQL integration): 8 hours

Deployment to Google Cloud Run: 5 hours

Testing and edge case handling: 2 hours

Documentation: 1 hour

Total estimated time: approximately 20 hrs

# Trade-Offs:

With the short turn-around, some issues persist. For example in the yml file, the deployment doesn't fully work because of a T90 error that seems to be an issue with the formatting of the file, but I can't seem to fix. In addition, I wasn't able to do some of the optional features for the project. Overall, I do think I was able to get the basic functionality down. In addition, more robust tests could be written to enhance the project.

