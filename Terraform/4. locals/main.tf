variable "prefix" {
  default = "company"
}

variable "common" {
  default = "test"
}

### 불가능 ###
# variable "prefix_test" {
#   default = "${var.prefix}-${var.common}"
# }

locals {
  prefix_test = "${var.prefix}-${var.common}"
  prefix_prod = "${var.prefix}-prod"
}

# resource "aws_iam_user" "prod" {
#   name = "${var.prefix}-user"
# }

# resource "aws_iam_user" "test1" {
#   name = "${var.prefix}-${var.common}-user"
# }

# resource "aws_iam_user" "test2" {
#   name = "${var.prefix}-${var.common}-user"
# }

# resource "aws_iam_user" "test3" {
#   name = "${local.prefix_test}-user"
# }

