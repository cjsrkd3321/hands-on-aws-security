provider "aws" {
  region = "ap-northeast-2"
}

variable "role_name" {
  type    = string
  default = "rex"

  validation {
    condition     = length(var.role_name) < 32
    error_message = "\"role_name\" must be less than 32 characters"
  }
}

resource "aws_iam_role" "this" {
  name = "${var.role_name}_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

output "test" {
  value = aws_iam_role.this
}
