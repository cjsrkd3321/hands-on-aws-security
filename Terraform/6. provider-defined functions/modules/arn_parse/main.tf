variable "arn" {
  type = string
}

locals {
  splitted_arn = split(":", var.arn)
}

output "value" {
  value = {
    partition  = local.splitted_arn[1],
    service    = local.splitted_arn[2],
    region     = local.splitted_arn[3],
    account_id = local.splitted_arn[4],
    resource   = local.splitted_arn[5],
  }
}
