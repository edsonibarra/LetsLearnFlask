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