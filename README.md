# Otel-log-generator
Local otel collector test setup.

## Instructions
1. Run the otel collector 
```sh
docker run --rm -p 5000:4317 -p 5001:4318 \
  -v $(pwd)/otel-config.yaml:/etc/config.yaml \
  otel/opentelemetry-collector-contrib --config /etc/config.yaml
```

2. Run the python log generator
```sh
python generator.py
```
