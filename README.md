# Mtcars Flask API

This is a simple example of an actual model deployed locally through a Flask API. The environment is created through a `docker-compose` command, that again references the corresponding Dockerfile and requirements.txt file. 

This API uses the mtcars dataset to create a predictive linear model to predict `mpg` from some other remaining variables using Python in a Docker container.

First as usual you will need to sync your repo to pull the new files. To run this API, change your directory to the docker folder and run:

`docker-compose up`

If it has created the localhost server correctly you will not get your prompt back. You will need to open a new terminal (be in the same directory) and run the following curl command to get a response

`curl http://localhost:5000/`

Finally, let's test out some predictions. If you open the `prediction.py` script you can see that the inputs into the model are "cyl", "disp", "hp", "drat", "wt", and "qsec". We will pass these through a json formatted input through a curl POST request to the API. This is done as

`curl -H "Content-Type: application/json" -X POST -d '{"cyl": "6", "disp": "168.3", "hp": "123", "drat": "3.17", "wt": "2.734", "qsec": "18.73"}' "http://localhost:5000/predict_mpg"`

You can change some of the values to see the prediction change.  Both of the curl commands can be found in the file `curl_test.sh`. To stop your server running the API, type `ctrl-C`. As usual, check to see if you have any docker containers running using `docker container ls` and stop them through `docker container kill <container-name>`
