# We are going to use the official Python Docker image.
FROM python:3.9

# Set the working directory in the container to /app.
WORKDIR /app

# Add the current directory contents into the container at /app.
ADD . /app

# Set up Python interactive prompt to use fancy readline.
ENV PYTHONSTARTUP=/root/.pythonrc
RUN echo "import rlcompleter, readline\nreadline.parse_and_bind('tab: complete')" > $PYTHONSTARTUP

# Make the script executable and source it.
RUN chmod +x /app/commands.sh

# Run the bash command when the container launches and source commands.sh.
CMD ["/bin/bash", "-c", "source /app/commands.sh; /bin/bash"]
