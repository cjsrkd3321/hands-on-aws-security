provider "aws" {
  region = "ap-northeast-2"
  default_tags {
    tags = {
      Name = "rex"
      Team = "Cloud"
    }
  }
}

resource "aws_iam_user" "this" {
  name = "rex"
  #   tags = local.tags
}

# locals {
#   tags = {
#     Name = "rex"
#     Team = "Cloud"
#   }
# }