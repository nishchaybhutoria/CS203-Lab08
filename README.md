# **Lab 08: Containerizing Applications Using Docker**

## **Team Members (Team 17)**
- **Nishchay Bhutoria (23110222)**
- **Srivaths P (23110321)**

## Final Docker Images
- [nishchaybhutoria/fastapi:1](https://hub.docker.com/r/nishchaybhutoria/fastapi/tags?page=1&name=1)
- [nishchaybhutoria/fastapi:2](https://hub.docker.com/r/nishchaybhutoria/fastapi/tags?page=1&name=2)
- [nishchaybhutoria/elasticsearch:latest](https://hub.docker.com/r/nishchaybhutoria/elasticsearch/tags?page=1&name=latest)


### Create Frontend VM
Creating the frontend VM on Google Cloud Platform (GCP).

![create-frontend-vm-1.png](images/create-frontend-vm-1.png)
![create-frontend-vm-2.png](images/create-frontend-vm-2.png)
![create-frontend-vm-3.png](images/create-frontend-vm-3.png)

### Create Backend VM
Creating the backend VM on GCP.

![create-backend-vm-1.png](images/create-backend-vm-1.png)
![create-backend-vm-2.png](images/create-backend-vm-2.png)
![create-backend-vm-3.png](images/create-backend-vm-3.png)

### VM Creation Done
![vm-creation-done.png](images/vm-creation-done.png)
Both VMs successfully created.

### Accessing VM via SSH
![accessing-vm-via-ssh.png](images/accessing-vm-via-ssh.png)
Accessing the VM using SSH from the browser.

### Creating Frontend VM Files
![creating-frontend-vm-files.png](images/creating-frontend-vm-files.png)
Creating required files for the frontend container.

### Frontend Dockerfile
![frontend-dockerfile.png](images/frontend-dockerfile.png)
Dockerfile used for the frontend FastAPI app.

### Frontend Main
![frontend-main.png](images/frontend-main.png)
Frontend FastAPI app's main.py file.

### Frontend Requirements
![frontend-requirements.png](images/frontend-requirements.png)
Requirements file for the frontend FastAPI app.

### Frontend Docker Installation
![frontend-docker-installation-1.png](images/frontend-docker-installation-1.png)
![frontend-docker-installation-2.png](images/frontend-docker-installation-2.png)

### Backend Main
Backend FastAPI app's main.py file.

![backend-main-1.png](images/backend-main-1.png)
![backend-main-2.png](images/backend-main-2.png)

### Backend Files Dockerfile Requirements
![backend-files-dockerfile-requirements.png](images/backend-files-dockerfile-requirements.png)
Dockerfile and requirements for backend container.

### Backend Docker Installation
Installing Docker on the backend VM.

![backend-docker-installation-1.png](images/backend-docker-installation-1.png)
![backend-docker-installation-2.png](images/backend-docker-installation-2.png)

### Building Frontend Image
![building-frontend-image.png](images/building-frontend-image.png)
Building the Docker image for the frontend app.

### Building Backend Image and Creating Network
![building-backend-image-and-network.png](images/building-backend-image-and-network.png)
Creating Docker network and building backend image.

### Firewall Page
![firewall-page.png](images/firewall-page.png)
Firewall rules page on GCP.

### Allow Public Access to FastAPI Frontend
Creating firewall rule to allow public access to the frontend.

![allow-fastapi-frontend-1.png](images/allow-fastapi-frontend-1.png)
![allow-fastapi-frontend-2.png](images/allow-fastapi-frontend-2.png)

### Allow Frontend to Access Backend
Creating firewall rule to allow the frontend VM to access the backend.

![allow-frontend-to-backend-1.png](images/allow-frontend-to-backend-1.png)
![allow-frontend-to-backend-2.png](images/allow-frontend-to-backend-2.png)

### Firewall Rule Creation done
![firewall-rule-creation-done.png](images/firewall-rule-creation-done.png)
All firewall rules successfully configured.

### Running Elasticsearch
![running-elasticsearch.png](images/running-elasticsearch.png)
Running the Elasticsearch container.

### Running Backend
![running-backend.png](images/running-backend.png)
Running the backend container.

### Running Frontend
![running-frontend.png](images/running-frontend.png)
Running the frontend container.

### Netstat Backend
![netstat-backend.png](images/netstat-backend.png)
Verifying open ports in backend VM using netstat.

### Netstat Frontend
![netstat-frontend.png](images/netstat-frontend.png)
Verifying open ports in frontend VM using netstat.

### Frontend Page Access (Global)
![frontend-page-global-access.png](images/frontend-page-global-access.png)
Accessing the frontend page from the browser.

### Example Get Query
![example-get-query.png](images/example-get-query.png)
Performing a GET query from frontend.

### Example When Query Doesn't Exist
![example-not-exist.png](images/example-not-exist.png)
Querying something that doesn't exist.

### Inserting New Document
![inserting-nonexistent.png](images/inserting-nonexistent.png)
Inserting a new document using frontend.

### Query New Document
![querying-now-existing.png](images/querying-now-existing.png)
Searching the document that was just inserted.

### Removing Frontend
![removing-frontend.png](images/removing-frontend.png)
Removing the frontend container.

### Removing Backend and Elasticsearch
![removing-backend-and-elasticsearch.png](images/removing-backend-and-elasticsearch.png)
Removing backend and elasticsearch containers.

### Running Frontend
![rerunning-frontend.png](images/rerunning-frontend.png)
Running the frontend container.

### Running Backend
![rerunning-backend-and-elasticsearch.png](images/rerunning-backend-and-elasticsearch.png)
Running the backend and elasticsearch containers.

### Persistency
![persistent-proof.png](images/persistent-proof.png)
Verifying data persistence after container removal.

### Running Images Frontend
![running-images-frontend.png](images/running-images-frontend.png)
Docker image for frontend after build.

### Running Images Backend
![running-images-backend.png](images/running-images-backend.png)
Docker image for backend after build.

### Running Inspect Frontend
Docker inspect output for frontend container.

![running-inspect-frontend-1.png](images/running-inspect-frontend-1.png)
![running-inspect-frontend-2.png](images/running-inspect-frontend-2.png)
![running-inspect-frontend-3.png](images/running-inspect-frontend-3.png)
![running-inspect-frontend-4.png](images/running-inspect-frontend-4.png)

### Running Inspect Elasticsearch
Docker inspect output for elasticsearch container.

![running-inspect-es-1.png](images/running-inspect-es-1.png)
![running-inspect-es-2.png](images/running-inspect-es-2.png)
![running-inspect-es-3.png](images/running-inspect-es-3.png)
![running-inspect-es-4.png](images/running-inspect-es-4.png)
![running-inspect-es-5.png](images/running-inspect-es-5.png)

### Running Inspect Backend
Docker inspect output for backend container.

![running-inspect-backend-1.png](images/running-inspect-backend-1.png)
![running-inspect-backend-2.png](images/running-inspect-backend-2.png)
![running-inspect-backend-3.png](images/running-inspect-backend-3.png)
![running-inspect-backend-4.png](images/running-inspect-backend-4.png)
![running-inspect-backend-5.png](images/running-inspect-backend-5.png)

### Running Inspect Network
![running-inspect-network.png](images/running-inspect-network.png)
Inspecting the custom Docker network used.

### Hub Frontend
![hub-frontend.png](images/hub-frontend.png)  
Docker Hub page with pushed frontend image.

### Hub Backend
![hub-backend.png](images/hub-backend.png)
Docker Hub page with pushed backend image.

### Hub Dashboard
![hub-dashboard.png](images/hub-dashboard.png)
Docker Hub dashboard with the images.

### Hub Tags
![hub-tags.png](images/hub-tags.png)
Docker Hub tags for the images.

### Architecture Diagram
Architecture diagram of the application.
![architecture-diagram.png](images/architecture-diagram.png)

### Optimization
For optimization of space and startup speed, we use the alpine base image (~5MB space).  
Also, instead of starting a shell (such as `bash`) when using CMD, we pass the list of arguments directly which decreases the overhead.  
We also pass the `--no-cache-dir` argument to pip to not store unnecessary cache files.
