FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt


# Run the test script when the container starts
CMD ["python", "./api_tasks_tests.py"]

#
#
# FROM python:3.12
#
#
# WORKDIR /usr/src/tests
#
# COPY . .
#
# RUN pip install --no-cache-dir -r requirements.txt
#
# RUN pip install chromedriver-py
#
# RUN apt-get update && apt-get install -y \
#     wget \
#     unzip \
#     && rm -rf /var/lib/apt/lists/*
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
#     && apt-get update && apt-get install -y \
#     google-chrome-stable \
#     && rm -rf /var/lib/apt/lists/*
#
# RUN CHROMEDRIVER_VERSION=curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE && \
#     wget -N http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip -P ~/ \
#     && unzip ~/chromedriver_linux64.zip -d ~/ \
#     && rm ~/chromedriver_linux64.zip \
#     && mv -f ~/chromedriver /usr/local/bin/chromedriver \
#     && chmod 0755 /usr/local/bin/chromedriver
# CMD ["python", "api_test_runner.py"]
# CMD ["python", "add_food_to_meal_test_runner.py"]
##use an offical python
#FROM python:3.12-slim
#
##set the working folder in the continer
#WORKDIR PycharmProjects/To_Doist_project
#
#COPY . .
#
#RUN pip install --no-cache-dir -r requirements.txt
#
##copy the app file to the contienr
#
##run command
#CMD ["python", "api_tasks_tests.py"]
#FROM python:3.12
#
#
#WORKDIR /usr/src/tests
#
#COPY . .
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#RUN pip install chromedriver-py
#
#RUN apt-get update && apt-get install -y \
#    wget \
#    unzip \
#    && rm -rf /var/lib/apt/lists/*
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
#    && apt-get update && apt-get install -y \
#    google-chrome-stable \
#    && rm -rf /var/lib/apt/lists/*
#
#RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
#    wget -N http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip -P ~/ \
#    && unzip ~/chromedriver_linux64.zip -d ~/ \
#    && rm ~/chromedriver_linux64.zip \
#    && mv -f ~/chromedriver /usr/local/bin/chromedriver \
#    && chmod 0755 /usr/local/bin/chromedriver
#FROM python:3.12
#
#
#WORKDIR /PycharmProjects/To_Doist_project
#
#COPY . .
#
#RUN pip install --no-cache-dir -r requirements.txt
#
##run command
#CMD ["python", "api_tasks_tests.py"]

#RUN apt-get update && apt-get install -y \
#    wget \
#    unzip \
#    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
#    && apt install ./google-chrome-stable_current_amd64.deb -y \
#    && rm -rf /var/lib/apt/lists/* \
#    && rm google-chrome-stable_current_amd64.deb
#
## Download matching ChromeDriver
#RUN chromeVersion=$(google-chrome --product-version) && \
#    chromeMajorVersion=${chromeVersion%%.*} && \
#    latestDriverReleaseURL="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$chromeMajorVersion" && \
#    wget -O latestDriverVersion "$latestDriverReleaseURL" && \
#    latestFullDriverVersion=$(cat latestDriverVersion) && \
#    finalURL="http://chromedriver.storage.googleapis.com/$latestFullDriverVersion/chromedriver_linux64.zip" && \
#    wget -O chromedriver_linux64.zip "$finalURL" && \
#    unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
#    rm chromedriver_linux64.zip && \
#    chmod +x /usr/local/bin/chromedriver