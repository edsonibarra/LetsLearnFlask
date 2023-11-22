# To build the image:
#   - docker build -t <imageName> .
# To run the container
#   - docker run --name <containerName> -d -p 5000:5000 <imageName>

# Using lightweight alpine image
FROM python:3.8-alpine

# Defining working directory
WORKDIR /usr/src/app

# Adding source code
COPY . .

# Installing packages
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run"]