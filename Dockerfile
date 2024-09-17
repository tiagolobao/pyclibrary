FROM python:3.11.9-slim

WORKDIR /app

# tools
RUN pip install flake8 pytest pylint wheel pytest-cov debugpy

EXPOSE 5678

# library dependencies
RUN pip install pyparsing==2.3.1
