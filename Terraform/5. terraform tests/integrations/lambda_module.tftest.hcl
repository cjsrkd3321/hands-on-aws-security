variables {
  lambda_name = "test_rex_lambda_funciton"
}

run "test_lambda_url" {
  module {
    source = "./modules/lambda"
  }
}

run "test_lambda_url_status_code" {
  variables {
    lambda_url  = run.test_lambda_url.lambda_url
    status_code = 200
  }

  assert {
    condition     = data.http.lambda.status_code == var.status_code
    error_message = "Lambda's url was not running normally."
  }
}