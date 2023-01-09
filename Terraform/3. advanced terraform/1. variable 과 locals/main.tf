variable "secret" {
  type    = string
  default = "test"
}

# variable "test2" {
#   default = var.secret
# }

locals {
  test = var.secret
}

output "test" {
  value = var.secret
}

output "test2" {
  value = local.test
}