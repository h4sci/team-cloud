Here I want to make a docker file for running a Python script.

Windows Users:
- install Docker Desktop: https://docs.docker.com/desktop/windows/install/
- create a folder, I call it "test"
- create the files "Dockerfile", "requirements.txt", "test.py" (check repository code for details in each script)
- open Windows PowerShell for running docker commands (here is the list of Docker commands: https://docs.docker.com/engine/reference/commandline/docker/)
- cd to the path where the 'test' folder is 
- docker build -t 'name for your docker image' Path_to_test_folder (This will build the image)
- docker images (give you list of all current images with IMAGE ID)
- docker run IMAGEID (will run the built image) 
- docker image rm -f IMAGEID (will remove the image -f force deleting if it is running)
- 

AWS Fargate is a serverless compute engine and hosting option for container-based workloads.
What Fargate allows you to do is host your containers on top of a fully managed compute platform.
That means no provisioning infrastructure, no setting up your clusters scaling, and no server management over time. 
You can define image, vCPU, memory, networking ports in task definition.
