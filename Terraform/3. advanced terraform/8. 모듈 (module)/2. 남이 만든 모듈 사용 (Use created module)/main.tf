module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "my-lambda1"
  description   = "My awesome lambda function"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  source_path = "func/"

  tags = {
    Name = "my-lambda1"
  }

  architectures                     = ["arm64"]
  cloudwatch_logs_retention_in_days = 1
}