FROM python:3.9

WORKDIR /app
ADD . /app

# Set up Python interactive prompt to use fancy readline.
ENV PYTHONSTARTUP=/root/.pythonrc
RUN echo "import rlcompleter, readline\nreadline.parse_and_bind('tab: complete')" > $PYTHONSTARTUP

# Make the script executable and source it.
RUN chmod +x /app/commands.sh
CMD ["/bin/bash", "-c", "source /app/commands.sh; /bin/bash"]
