
########################################################################
# Terraform 1.8 부터 가능
########################################################################

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {}

# result: 
# {
#   "partition": "aws",
#   "service": "iam",
#   "region": "",
#   "account_id": "444455556666",
#   "resource": "role/example",
# }
output "role" {
  value = provider::aws::arn_parse("arn:aws:iam::444455556666:role/example")
}

# result: 
# {
#   "partition": "aws",
#   "service": "elasticloadbalancing",
#   "region": "us-east-2",
#   "account_id": "123456789012",
#   "resource": "loadbalancer/app/my-load-balancer/1234567890123456",
# }
output "elb" {
  value = provider::aws::arn_parse("arn:aws:elasticloadbalancing:us-east-2:123456789012:loadbalancer/app/my-load-balancer/1234567890123456")
}

