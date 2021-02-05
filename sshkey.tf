resource "exoscale_ssh_keypair" "access" {
  name = "autoscaler-access"
  public_key = var.sshkey
  count = var.sshkey == ""?0:1
}
locals {
  ssh_key_name = var.sshkey == ""?"":element(exoscale_ssh_keypair.access.*.name, 0)
}