# builds
Fast API service for getting tasks for build.

endpoints:

1) get/

  healthcheck, return {"message": "Hello World"}
  
2) post/get_tasks

input:
{
     "build": "build_name"
}

output:
["task1", "task2", ... , "taskN"]

returns task list for the build "build_name"

returns 404 error if build or task not found

Docker command to run:
docker run --rm -d -p 80:80 annagorbunova/builds
