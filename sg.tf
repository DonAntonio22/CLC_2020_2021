resource "exoscale_security_group" "autoscaling" {
  name = "autoscaling"
  description = "Managed by Terraform!"
}

resource "exoscale_security_group_rule" "http" {
  security_group_id = exoscale_security_group.autoscaling.id
  type = "INGRESS"
  cidr = "0.0.0.0/0"
  start_port = "8080"
  end_port = "8080"
  protocol = "TCP"
  description = "Managed by Terraform!"
}

resource "exoscale_security_group_rule" "prometheus" {
  security_group_id = exoscale_security_group.autoscaling.id
  type = "INGRESS"
  cidr = var.admin_ip
  start_port = "9090"
  end_port = "9090"
  protocol = "TCP"
  description = "Managed by Terraform!"
  count = var.admin_ip==""?0:1
}

resource "exoscale_security_group_rule" "internal" {
  security_group_id = exoscale_security_group.autoscaling.id
  user_security_group_id = exoscale_security_group.autoscaling.id
  type = "INGRESS"
  start_port = "1"
  end_port = "65535"
  protocol = "TCP"
  description = "Managed by Terraform!"
}

resource "exoscale_security_group_rule" "ssh" {
  security_group_id = exoscale_security_group.autoscaling.id
  type = "INGRESS"
  cidr = var.admin_ip
  start_port = "22"
  end_port = "22"
  protocol = "TCP"
  description = "Managed by Terraform!"
  count = var.admin_ip==""?0:1
}

resource "exoscale_security_group_rule" "grafana" {
  security_group_id = exoscale_security_group.autoscaling.id
  type = "INGRESS"
  cidr = var.admin_ip
  start_port = "3000"
  end_port = "3000"
  protocol = "TCP"
  description = "Managed by Terraform!"
  count = var.admin_ip==""?0:1
}


resource "exoscale_security_group_rule" "autoscaler" {
  security_group_id = exoscale_security_group.autoscaling.id
  type = "INGRESS"
  cidr = var.admin_ip
  start_port = "6000"
  end_port = "6000"
  protocol = "TCP"
  description = "Managed by Terraform!"
  count = var.admin_ip==""?0:1
}
