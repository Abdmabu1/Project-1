FROM python:3.8
# set a key-value label for the Docker image
# copy files from the host to the container filesystem.
# For example, all the files in the current directory
# to the  `/app` directory in the container
COPY . /Project-1
#  defines the working directory within the container
WORKDIR /Project-1
# run commands within the container.
# For example, invoke a pip command
# to install dependencies defined in the requirements.txt file.
#RUN pip install -r requirements.txt
# provide a command to run on container start.
# For example, start the `app.py` application.
CMD [ "python", "main.py" ]
