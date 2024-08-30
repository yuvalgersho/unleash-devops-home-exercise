# Result documentation 
## Dockerize
I created a multi-stage Dockerfile that creates an image for the app with the necessary configurations

## CI
The ci is running on GitHub actions.
It has 2 main jobs, before-merge and after-merge:
* Before-merge: this pipeline dockerizes the app and pushes the image to the docker hub with a unique tag (the number of the pipeline), the aim is to let developers test their changes with the new-created image. this pipeline runs when there is a open merge request to the ‘master’ branch.
* After-merge: this pipeline dockerizes the app and pushes the image to the docker hub with the ‘latest’ tag. The aim is to use this image automatically when deploy the app to the aws k8s cluster.

## CD
The cd is also running on GitHub actions.
Its main purpose is to automatically deploy the bucket and the app (production level) whenever there is a new commit to the ‘master’ branch.

## IAAC
This code is used inside the pipeline (CD part) and does the following:
* created the s3 bucket
* Initialize the bucket with files
* Deploys the app (and other configurations) on eks cluster
I chose to provide 2 methods of iaac, first is to use Helm & GitHub actions to auto deploy the app on the eks cluster and second is to the cdk (IAAC) tool to create and configure the s3 bucket.
Both ways run in the CD pipeline and provide a full cd level deployment. 

## Additional suggestions
These are things I recommend doing but I haven’t done because of time limitations:
* Optimize the Dockerfile and reduce size of the docker image.
* Create and configure the eks cluster with the IAAC.
* Create advanced policies and roles to secure the deployment of the app. (For example - create a role to limit the permissions of the GitHub actions jobs).
* Add full documentation for the components (CI, CD, etc)