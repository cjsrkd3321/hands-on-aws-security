resource "aws_vpc" "this" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "dynamic-block-vpc"
  }
}

resource "aws_security_group" "allow_http_https" {
  name   = "allow_http_https"
  vpc_id = aws_vpc.this.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # dynamic "ingress" {
  #   for_each = var.ingress_rules
  #   content {
  #     from_port   = ingress.value["from_port"]
  #     to_port     = ingress.value["to_port"]
  #     protocol    = ingress.value["protocol"]
  #     cidr_blocks = ingress.value["cidr_blocks"]
  #   }
  # }
}

variable "ingress_rules" {
  default = {
    http = {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
    https = {
      from_port   = 443
      to_port     = 443
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
