# Use the official Python runtime image
FROM python:3.13  

# Install tzdata (needed for timezone support)
RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*

# Set timezone via environment variable (overridable at runtime)
ENV TZ=Europe/Warsaw
 
# Create the app directory
RUN mkdir /app
 
# Set the working directory inside the container
WORKDIR /app
 
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project  and install dependencies
COPY requirements.txt  /app/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the Django project to the container
COPY . /app/

WORKDIR /app/leszek_projekt

# Expose the Django port
EXPOSE 8000
# copy entrypoint.sh
# COPY app//entrypoint.sh .
# RUN sed -i 's/\r$//g' ./entrypoint.sh
# RUN chmod +x ./entrypoint.sh
#  run entrypoint.sh
# ENTRYPOINT ["/app/leszek_projekt/entrypoint.sh"]

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
