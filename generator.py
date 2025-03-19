import random
import time
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk.resources import Resource
from  opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
import logging

# Define the resource attributes
resource = Resource.create({
    "app": "raksha-server",
    "component": "webApp",
    "container": "raksha-server",
    "detected_level": "info",
    "namespace": "dps-eng-raksha-server",
    "node_name": "ip-10-191-135-234.ec2.internal",
    "pod": "raksha-server-5495d6778f-hzlsn",
    "service": "raksha-server",
    "service_name": "raksha-server",
    "stream": "stderr",
    "tng_environment": "production",
    "tng_region": "us-east-1",
    "method": "POST",
    "uri": "/graphql",
    "clientID": "iOS"
})

# Set up OpenTelemetry logger provider
logger_provider = LoggerProvider(resource=resource)
# log_exporter = OTLPLogExporter(endpoint="http://localhost:4318/v1/logs")  # otel
log_exporter = OTLPLogExporter(endpoint="http://localhost:5001/v1/logs")  # otel
logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))

# Set up Python logging with OpenTelemetry handler
logging.basicConfig(level=logging.INFO)
otel_handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
logging.getLogger().addHandler(otel_handler)
logger = logging.getLogger(__name__)

# Random messages
messages = [
    "try2: Raksha testing logs",
    "try2: Raksha testing otlp config",
    "try2: Raksha random message 1",
    "try2: Raksha random message 2"
]

def generate_logs():
    while True:
        message = random.choice(messages)
        logger.info(message, extra={"user": "raksha", "ip": "192.168.1.1"})
        time.sleep(random.randint(5, 10))  # Random delay between logs

if __name__ == "__main__":
    generate_logs()

# message = random.choice(messages)
# logger.info(message, extra={"user": "raksha", "ip": "192.168.1.1"})