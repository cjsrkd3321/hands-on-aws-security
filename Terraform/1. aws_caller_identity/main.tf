provider "aws" {
  region = "ap-northeast-2"
}

data "aws_caller_identity" "current" {}

output "test" {
  value = data.aws_caller_identity.current
}