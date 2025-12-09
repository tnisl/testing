
#image
FROM python:3.13-slim


#create working folder named app (same as mkdir /app && cd app)
WORKDIR /app 

#copy requires, optimize layer caching
COPY requirements.txt .


RUN apt-get update && \
    apt-get install -y build-essential python3-dev && \
    \
    pip install --no-cache-dir -r requirements.txt && \
    \
    apt-get purge -y build-essential python3-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*



# install  requires in container, the '--no-cache-dir' reduces image volume
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]








