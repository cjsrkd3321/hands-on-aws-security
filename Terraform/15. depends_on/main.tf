# 사용예시: https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on#usage
data "aws_availability_zones" "first" {
  state = "available"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

locals {
  az = data.aws_availability_zones.first.names[0]
}

resource "aws_vpc" "this" {
  cidr_block = var.vpc_cidr
}

##### PUBLIC #####
resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.this.id
  cidr_block        = "10.0.220.0/24"
  availability_zone = local.az
}

resource "aws_internet_gateway" "this" {}

resource "aws_internet_gateway_attachment" "this" {
  internet_gateway_id = aws_internet_gateway.this.id
  vpc_id              = aws_vpc.this.id
}

resource "aws_nat_gateway" "this" {
  subnet_id = aws_subnet.public.id

  depends_on = [aws_internet_gateway.this]
}
