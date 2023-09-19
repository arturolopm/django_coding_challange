FROM python:3.10
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

WORKDIR /app

# Copy the rest of the application code
COPY . /app

# Copy the init.sh script
COPY ./init.sh /app/init.sh
# Copy requirements and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


# Set the entrypoint
ENTRYPOINT ["./init.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

