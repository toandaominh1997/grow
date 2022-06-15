# install redis 
# helm upgrade my-redis bitnami/redis --values services/redis/values-redis.yaml

# install ingress
# helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install nginx-ingress ingress-nginx/ingress-nginx --set controller.publishService.enabled=true

# install kafka

# kubectl run my-kafka-client --restart='Never' --image docker.io/bitnami/kafka:3.2.0-debian-11-r3 --namespace default --command -- sleep infinity
# kubectl exec --tty -i my-kafka-client --namespace default -- bash
# install grow chart
kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
helm install grow-chart ./grow-chart