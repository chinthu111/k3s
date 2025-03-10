#!/bin/bash

kubectl apply -f fluent-bit-test-job.yaml
kubectl wait --for=condition=complete job/fluent-bit-test-log -n zenoh-monitoring --timeout=60s

kubectl apply -f loki-query-test.yaml
kubectl wait --for=condition=complete job/loki-query-test -n zenoh-monitoring --timeout=60s

LOKI_TEST_RESULT=$(kubectl logs job/loki-query-test -n zenoh-monitoring)

if [[ "$LOKI_TEST_RESULT" == *"Loki test passed"* ]]; then
  echo "Fluent Bit to Loki test passed"
  exit 0
else
  echo "Fluent Bit to Loki test failed"
  exit 1
fi