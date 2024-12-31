# https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle

resource "aws_vpc" "this" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "dynamic-block-vpc"
  }

  # lifecycle {
  #   prevent_destroy = true
  # }
}

resource "aws_iam_user" "this" {
  name = "rex123"
  tags = {
    Team = "cloud"
  }

  # lifecycle {
  #   ignore_changes = [tags]
  # }
}
