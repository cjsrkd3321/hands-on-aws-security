variable "lambda_name" {
  type    = string
  default = "lambda_function_name"
}

data "aws_iam_policy_document" "this" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

data "archive_file" "this" {
  type        = "zip"
  source_file = "lambda.py"
  output_path = "lambda_function_payload.zip"
}

resource "aws_iam_role" "this" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.this.json
}

resource "aws_cloudwatch_log_group" "this" {
  name              = "/aws/lambda/${var.lambda_name}"
  retention_in_days = 1
}

resource "aws_lambda_function" "this" {
  filename      = "lambda_function_payload.zip"
  function_name = var.lambda_name
  role          = aws_iam_role.this.arn
  handler       = "lambda.lambda_handler"

  source_code_hash = data.archive_file.this.output_base64sha256
  architectures    = ["arm64"]

  runtime = "python3.11"
}

output "lambda" {
  value = aws_lambda_function.this
}

output "cloudwatch" {
  value = aws_cloudwatch_log_group.this
}
