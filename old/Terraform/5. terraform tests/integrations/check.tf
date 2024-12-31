variable "status_code" {
  type    = number
  default = 200
}

variable "lambda_url" {
  type = string
}

data "http" "lambda" {
  url = var.lambda_url
}
