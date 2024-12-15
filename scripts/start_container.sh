 #!/bin/bash
set -e


docker pull maharanaprathap793/simple-python-flask-app:latest

docker run -d -p 5000:5000 maharanaprathap793/simple-python-flask-app:latest
