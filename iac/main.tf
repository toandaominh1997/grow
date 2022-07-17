provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}



resource "helm_release" "grafana" {
  name       = "grow-grafana"

  repository = "https://grafana.github.io/helm-charts"
  chart      = "grafana/grafana"

  set {
    name  = "service.type"
    value = "ClusterIP"
  }
}
