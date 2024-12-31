variables {
  lambda_name = "test_rex_lambda_function"
}

run "test_lambda_architecture" {
  command = plan

  assert {
    condition     = aws_lambda_function.this.architectures[0] == "arm64"
    error_message = "Lambda's architecture must set arm64."
  }
}

run "test_lambda_runtime" {
  command = plan

  assert {
    condition     = contains(["python3.11", "python3.10", "python3.9"], aws_lambda_function.this.runtime)
    error_message = "Lambda's runtime must be one of python3.11/3.10/3.9."
  }
}

run "test_lambda_vpc" {
  command = plan

  assert {
    condition     = length(aws_lambda_function.this.vpc_config) != 0
    error_message = "Lambda's vpc must set."
  }
}

run "test_lambda_log_group_retention_days" {
  command = plan

  assert {
    condition     = aws_cloudwatch_log_group.this.retention_in_days < 365
    error_message = "Lambda's log group retention days must be bigger than 365 days."
  }
}

// run "test_lambda_arn" {
//   command = plan

//   assert {
//     condition     = endswith(aws_lambda_function.this.arn, var.lambda_name)
//     error_message = "GOOD."
//   }
// }