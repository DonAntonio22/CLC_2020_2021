variable "exoscale_key" {
  type = string
  description = "Exoscale API key"
  default = "EXO724f563dc38a1017c5b8c4e5"
}
variable "exoscale_secret" {
  type = string
  description = "Exoscale API secret"
  default = "HFmu0pQ6ZDzQU3a-V84L5vebQdqM_uYvDE_R8Qhk44Q"
}
variable "exoscale_zone" {
  type = string
  description = "Exoscale zone"
  default = "at-vie-1"
}
variable "exoscale_zone_id" {
  type = string
  description = "ID of the exoscale zone"
  default = "4da1b188-dcd6-4ff5-b7fd-bde984055548"
}
variable "admin_ip" {
  type = string
  description = "IP for SSH access"
  default = "0.0.0.0/0"
}
variable "sshkey" {
  type = string
  description = "SSH key in OpenSSH format"
  default = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDB385u/D2/7rtKkJZUvqNGZgDVO9L6tvJF3DHWiPiEpOCIbVxTqIE8suGsR0spTiG8eUVbmmlHC+8l+hkjaEJz36GTrXTm+gK/V3djuLlRD6eY0+Dqh9eajk25dlEckckIYbJb9syht4wvJAIAoRG08Qk8ZjLRJtzqvrF71Ne3iBAJKgrkeSOfgP0V2fCnza/0YTL4gwadWMjy3gB9FX9318tyUW70AtFcDyq/nukCwE9E/EfhOX7DtnJfeOLzcDfTU1wp2poZbmpDhThI8rW9OGG8lr8qo0cSEpWQDn6ot9S03LY3XwGSN2XcM6WiznqOPXrrO1U6a6iuy6QRkLCDjxO19TdNBEOPoPmPdHN98/hht65mPYBbuKVQ7MiqZ2BVPLDkgJ5X/i4+YZCy97wsghTlvSrnGoaNNSc2zM+kqVcw7RHWLivUEgtfMwVt2htjmHN8Cst2donVBxsprIQkeWLbErzZOIDWS/JKAmvZcX94EWUhcgtsRCdbucLNyFE= AntonioLastro@MacBook-Pro.local"
}