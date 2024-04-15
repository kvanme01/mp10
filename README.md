# Deploying Hugging Face Transformers model on AWS Lambda with Docker containers

## Steps for implementation:

Ensure you have Python 3.11 installed.

### Install Required Libraries

1. Create a virtual environment: `python -m venv venv`
2. Activate it:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
3. Install libraries with pip: `pip install transformers torch`


### Download Model and Tokenizer

1. Navigate to the `lambda-service` folder.
2. Create a Python script, e.g., `download_model.py`.
3. Copy and paste the provided code into the script.
4. Execute the script: `python download_model.py`

### Why Download Directly into Docker?

To overcome Lambda environment constraints.

### Add requirements.txt

Create a file named `requirements.txt` and list the required libraries:
```
torch
transformers
```

### Dockerfile

Use a Dockerfile to define the Docker image setup:

```Dockerfile
# Dockerfile
FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

COPY ./ ${LAMBDA_TASK_ROOT}/

CMD [ "handler.handler" ]
```

### Build the Docker Image

Build the Docker image using the following command:

```bash
docker build -t sentiment-analyzer:latest .
```

### Run the Docker Image

Run the Docker image using the following command:

```bash
docker run -p 9000:8080 sentiment-analyzer:latest
```

### Invoke Lambda Function Locally

Test the function with curl:

```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"text": "I love AI"}'
```
