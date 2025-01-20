# Use the official Apache Superset image as the base
# FROM apache/superset:latest
FROM apache/superset:latest

# Install dependencies for Athena
USER root
RUN apt-get update && apt-get install -y sudo vim \
    && pip install psycopg2-binary

# Add the superset_config.py file from the current directory
# this helps us to overide default parameters and configurations
COPY superset_config.py /app/pythonpath/superset_config.py

# Copy my start up
COPY superset-init.sh /app/superset-init.sh

# Ensure the script is executable
RUN chmod +x /app/superset-init.sh

# Copy our logo
COPY tc-logo.png /app/superset/static/assets/images/tc-logo.png

#RUN chown superset /app/superset/static/assets/images/tc-logo.png

# Switch back to the superset user
USER superset

# Expose the port that superset runs on
EXPOSE 8088

# Initialize superset - creating default admin user
ENTRYPOINT [ "/app/superset-init.sh" ]

