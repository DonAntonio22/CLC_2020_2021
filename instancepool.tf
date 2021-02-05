resource "exoscale_instance_pool" "autoscaling" {
  name = "autoscaling"
  service_offering = "micro"
  description = "Managed by Terraform!"
  size = 2
  disk_size = 10
  template_id = data.exoscale_compute_template.ubuntu.id
  zone = var.exoscale_zone
  key_pair = local.ssh_key_name

  security_group_ids = [exoscale_security_group.autoscaling.id]

  user_data = file("userdata.sh")

  lifecycle {
    ignore_changes = [
      size
    ]
  }
}