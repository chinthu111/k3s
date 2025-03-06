import logging
import os

from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metrics_exporter import OTLPMetricsExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk.logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk.logs.export import BatchLogRecordProcessor

def configure_otel():
    otlp_endpoint = os.getenv("OTLP_ENDPOINT", "otel-collector.zenoh-monitoring:4317")
    resource = Resource(attributes={"service.name": "log-generator-app"})

    # Trace
    trace_provider = TracerProvider(resource=resource)
    trace_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=otlp_endpoint)))
    trace_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(trace_provider)

    # Metrics
    metric_reader = PeriodicExportingMetricReader(OTLPMetricsExporter(endpoint=otlp_endpoint))
    metrics_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
    metrics_provider.add_metric_reader(ConsoleMetricExporter())
    metrics.set_meter_provider(metrics_provider)
    meter = metrics.get_meter(__name__)
    counter = meter.create_counter("log_generator_requests")

    # Logs
    log_provider = LoggerProvider(resource=resource)
    log_provider.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporter(endpoint=otlp_endpoint)))
    logging.setLoggerClass(logging.getLoggerClass())
    handler = LoggingHandler(level=logging.INFO, logger_provider=log_provider)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return counter, logger