provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_iam_role" "this" {
  #   name = "test_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          #   Service = "ec2.amazonaws.com"
          AWS = aws_iam_user.this.arn
        }
      },
    ]
  })
  inline_policy {
    name = "my_inline_policy"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Action   = ["ec2:Describe*"]
          Effect   = "Allow"
          Resource = "*"
        },
      ]
    })
  }
  managed_policy_arns = [aws_iam_policy.policy.arn, "arn:aws:iam::aws:policy/ReadOnlyAccess"]
}

resource "aws_iam_policy" "policy" {
  name        = "test_policy"
  path        = "/"
  description = "My test policy"
  policy      = data.aws_iam_policy_document.this.json
}

data "aws_iam_policy_document" "this" {
  statement {
    sid    = "1"
    effect = "Allow"
    # principals {
    #   type        = "Service"
    #   identifiers = ["ec2.amazonaws.com"]
    # }
    actions = [
      "sts:AssumeRole",
    ]
    resources = [
      "arn:aws:s3:::*",
    ]
  }
}

resource "aws_iam_user" "this" {
  name = "rextest"
  path = "/"
}