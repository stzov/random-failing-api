I wrote this random failing API for testing linkerd retries, but it can possibly be used for other purposes.

# Build
> docker build -t random-failing-api:latest .

# Run
> docker run -d --name random-failing-api --rm -p 5678:5678  random-failing-api

# Try it out
> curl -v localhost:5678/get