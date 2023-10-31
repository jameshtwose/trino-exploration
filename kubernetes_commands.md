# General
- `minikube start` # Start minikube
- `minikube dashboard` # Open dashboard (optional)

# Kafka
- `helm repo add bitnami https://charts.bitnami.com/bitnami` # Add Bitnami repo
- `helm install my-release bitnami/kafka` # Install Kafka
- `kubectl get pods --namespace default -l "app.kubernetes.io/name=kafka,app.kubernetes.io/instance=my-release"` # List Kafka pods
- `kubectl exec --tty -i my-release-kafka-0 --namespace default -- bash` # Connect to Kafka pod

# Trino
- https://trino.io/docs/current/installation/kubernetes.html
- `kubectl get pods` # List all pods
- `kubectl cluster-info` # Get cluster info
- `helm repo add trino https://trinodb.github.io/charts` # Add Trino repo
- `helm install example-trino-cluster trino/trino`  # Install Trino cluster
  - `helm install -f example_trino_kubernetes.yaml example-trino-cluster trino/trino` # Install Trino cluster with custom config
- `kubectl get all` # List all resources
- `POD_NAME=$(kubectl get pods -l "app=trino,release=example-trino-cluster,component=coordinator" -o name)` # set POD_NAME variable
- `kubectl port-forward $POD_NAME 8080:8080` # Forward port to localhost
- download if necessary: `curl -L https://repo1.maven.org/maven2/io/trino/trino-cli/431/trino-cli-431-executable.jar -o trino-cli`
  - `chmod +x trino-cli` # Make executable
- `trino-cli --server localhost:8080` # Connect to Trino (make sure to download the CLI first)