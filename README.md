# Lab 08: Dockerized AI App Architecture - Image Descriptions

### Create frontend vm
Creating the frontend VM on Google Cloud Platform (GCP).

![create-frontend-vm-1.png](images/create-frontend-vm-1.png)
![create-frontend-vm-2.png](images/create-frontend-vm-2.png)
![create-frontend-vm-3.png](images/create-frontend-vm-3.png)

### Create backend vm
Creating the backend VM on GCP.

![create-backend-vm-1.png](images/create-backend-vm-1.png)
![create-backend-vm-2.png](images/create-backend-vm-2.png)
![create-backend-vm-3.png](images/create-backend-vm-3.png)

### VM creation done
![vm-creation-done.png](images/vm-creation-done.png)
Both VMs successfully created.

### Accessing vm via ssh
![accessing-vm-via-ssh.png](images/accessing-vm-via-ssh.png)
Accessing the VM using SSH from the browser.

### Creating frontend vm files
![creating-frontend-vm-files.png](images/creating-frontend-vm-files.png)
Creating required files for the frontend container.

### Frontend dockerfile
![frontend-dockerfile.png](images/frontend-dockerfile.png)
Dockerfile used for the frontend FastAPI app.

### Frontend main
![frontend-main.png](images/frontend-main.png)
Frontend FastAPI app's main.py file.

### Frontend requirements
![frontend-requirements.png](images/frontend-requirements.png)
Requirements file for the frontend FastAPI app.

### Frontend docker installation
![frontend-docker-installation-1.png](images/frontend-docker-installation-1.png)
Installing Docker on the frontend VM.

### Frontend docker installation
![frontend-docker-installation-2.png](images/frontend-docker-installation-2.png)
Installing Docker on the frontend VM.

### Backend main
Backend FastAPI app's main.py file.

![backend-main-1.png](images/backend-main-1.png)
![backend-main-2.png](images/backend-main-2.png)

### Backend files dockerfile requirements
![backend-files-dockerfile-requirements.png](images/backend-files-dockerfile-requirements.png)
Dockerfile and requirements for backend container.

### Backend docker installation
Installing Docker on the backend VM.

![backend-docker-installation-1.png](images/backend-docker-installation-1.png)
![backend-docker-installation-2.png](images/backend-docker-installation-2.png)

### Building frontend image
![building-frontend-image.png](images/building-frontend-image.png)
Building the Docker image for the frontend app.

### Building backend image and network
![building-backend-image-and-network.png](images/building-backend-image-and-network.png)
Creating Docker network and building backend image.

### Firewall page
![firewall-page.png](images/firewall-page.png)
Firewall rules page on GCP.

### Allow fastapi frontend
Creating firewall rule to allow public access to frontend.

![allow-fastapi-frontend-1.png](images/allow-fastapi-frontend-1.png)
![allow-fastapi-frontend-2.png](images/allow-fastapi-frontend-2.png)

### Allow frontend to backend
Creating firewall rule to allow frontend VM to access backend.

![allow-frontend-to-backend-1.png](images/allow-frontend-to-backend-1.png)
![allow-frontend-to-backend-2.png](images/allow-frontend-to-backend-2.png)

### Firewall rule creation done
![firewall-rule-creation-done.png](images/firewall-rule-creation-done.png)
All firewall rules successfully configured.

### Running elasticsearch
![running-elasticsearch.png](images/running-elasticsearch.png)
Running the Elasticsearch container.

### Running backend
![running-backend.png](images/running-backend.png)
Running the backend container.

### Running frontend
![running-frontend.png](images/running-frontend.png)
Running the frontend container.

### Netstat backend
![netstat-backend.png](images/netstat-backend.png)
Verifying open ports in backend VM using netstat.

### Netstat frontend
![netstat-frontend.png](images/netstat-frontend.png)
Verifying open ports in frontend VM using netstat.

### Frontend page access (global)
![frontend-page-global-access.png](images/frontend-page-global-access.png)
Accessing the frontend page from the browser.

### Example GET query
![example-get-query.png](images/example-get-query.png)
Performing a GET query from frontend.

### Example when query doesn't exist
![example-not-exist.png](images/example-not-exist.png)
Querying something that doesn't exist.

### Inserting new document
![inserting-nonexistent.png](images/inserting-nonexistent.png)
Inserting a new document using frontend.

### Query new document
![querying-now-existing.png](images/querying-now-existing.png)
Searching the document just inserted.

### Removing frontend
![removing-frontend.png](images/removing-frontend.png)
Removing the frontend container.

### Removing backend and elasticsearch
![removing-backend-and-elasticsearch.png](images/removing-backend-and-elasticsearch.png)
Removing backend and Elasticsearch containers.

### Running frontend
![rerunning-frontend.png](images/rerunning-frontend.png)
Running the frontend container.

### Running backend
![rerunning-backend-and-elasticsearch.png](images/rerunning-backend-and-elasticsearch.png)
Running the backend container.

### Documents are persistent
![persistent-proof.png](images/persistent-proof.png)
Verifying data persistence after container removal.

### Running images frontend
![running-images-frontend.png](images/running-images-frontend.png)
Docker image for frontend after build.

### Running images backend
![running-images-backend.png](images/running-images-backend.png)
Docker image for backend after build.

### Running inspect frontend
![running-inspect-frontend-1.png](images/running-inspect-frontend-1.png)
Docker inspect output for frontend container.

### Running inspect frontend
![running-inspect-frontend-2.png](images/running-inspect-frontend-2.png)
Docker inspect output for frontend container.

### Running inspect frontend
![running-inspect-frontend-3.png](images/running-inspect-frontend-3.png)
Docker inspect output for frontend container.

### Running inspect frontend
![running-inspect-frontend-4.png](images/running-inspect-frontend-4.png)
Docker inspect output for frontend container.

### Running inspect elasticsearch
Docker inspect output for Elasticsearch container.

![running-inspect-es-1.png](images/running-inspect-es-1.png)
![running-inspect-es-2.png](images/running-inspect-es-2.png)
![running-inspect-es-3.png](images/running-inspect-es-3.png)
![running-inspect-es-4.png](images/running-inspect-es-4.png)
![running-inspect-es-5.png](images/running-inspect-es-5.png)

### Running inspect backend
Docker inspect output for backend container.

![running-inspect-backend-1.png](images/running-inspect-backend-1.png)
![running-inspect-backend-2.png](images/running-inspect-backend-2.png)
![running-inspect-backend-3.png](images/running-inspect-backend-3.png)
![running-inspect-backend-4.png](images/running-inspect-backend-4.png)
![running-inspect-backend-5.png](images/running-inspect-backend-5.png)

### Running inspect network
![running-inspect-network.png](images/running-inspect-network.png)
Inspecting the custom Docker network used.

### Hub frontend
![hub-frontend.png](images/hub-frontend.png)  
Docker Hub page with pushed frontend image.

### Hub backend
![hub-backend.png](images/hub-backend.png)
Docker Hub page with pushed backend image.

### Hub dashboard
![hub-dashboard.png](images/hub-dashboard.png)
Docker Hub dashboard with the images.

### Hub tags
![hub-tags.png](images/hub-tags.png)
Docker Hub tags for the images.

### Architecture diagram
Architecture diagram of the application.
![architecture-diagram.png](images/architecture-diagram.png)

### Optimization
For optimization of space and startup speed, we use the alpine base image (~5MB space).  
Also, instead of starting a shell (such as `bash`) when using CMD, we pass the list of arguments directly which decreases the overhead.  
We also pass the `--no-cache-dir` argument to pip to not store unnecessary cache files.
