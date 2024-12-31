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
}

resource "aws_vpc" "this" {
  cidr_block = "10.0.0.0/16"
  tags       = local.tags
}

locals {
  # 보안(ABAC, Attribute Based Access Control), 재무(FinOps), 내부통제, 운영 등의 목적으로 활용 가능
  tags = {
    Name = "rex11"
  }
}
