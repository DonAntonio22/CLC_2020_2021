resource "exoscale_nlb" "autoscaling" {
  zone = var.exoscale_zone
  name = "autoscaling"
}

resource "exoscale_nlb_service" "autoscaling" {
  instance_pool_id = exoscale_instance_pool.autoscaling.id
  name = "HTTP"
  description = "Managed by Terraform!"
  nlb_id = exoscale_nlb.autoscaling.id
  port = 80
  target_port = 8080
  zone = var.exoscale_zone

  healthcheck {
    port = 8080
    mode = "http"
    uri = "/health"
    interval = 5
    timeout = 3
    retries = 1
  }

  depends_on = [
    exoscale_instance_pool.autoscaling
  ]
}
