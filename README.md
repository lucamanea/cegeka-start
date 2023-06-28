As various CVs might differ, the application was designed to produce dynamically
the possible endpoints by extracting them from the CV binary file.
 
 The app requires Python 3.x and Flask 2.x to work.
 
 In order to run the Flask application and test the REST API JSON requests, one
 must issue the following command:
 `flask run`
 
 To check the CLI commands the following command should be used:
 `flask present-cv <cv_field>`
 where `<cv_field>` is one valid field. 
 
 As sent, the valid CV fields are: `personal`, `experience` and `education`.
 They can be altered by modifying and running the store_data.py script, which
 is not part of the project but was left for convenience.
 
To run with docker, run the following commands from this directory:
`docker image build -t docker_cegeka .`
followed by:
`docker run -p 5000:5000 -d docker_cegeka`
