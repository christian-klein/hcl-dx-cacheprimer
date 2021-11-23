# For more information, please refer to https://aka.ms/vscode-docker-python
# docker build --no-cache --progress plain .
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV APP_HOME /app 

WORKDIR ${APP_HOME}
COPY . ${APP_HOME}

#install python dependencies
RUN pip install -r /app/requirements.txt 

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "-u", "app.py"]