variable "prefix" {
  default = "company"
}

variable "common" {
  default = "test"
}

locals {
  prefix_test    = "${var.prefix}-${var.common}"
  prefix_prod    = "${var.prefix}-prod"
  splited_prefix = split("-", local.prefix_test)[0]
}

output "splited_prefix" {
  value = local.splited_prefix
}

output "length" {
  value = length([1, 2, 3])
  # value = length("123123")
}

output "concat" {
  value = concat(["a", ""], ["b", "c"])
}
