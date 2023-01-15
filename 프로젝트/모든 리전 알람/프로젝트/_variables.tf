variable "patterns" {
  type = any
  default = {
    login-alarm       = <<PATTERN
    {
      "source": ["aws.signin"],
      "detail-type": ["AWS Console Sign In via CloudTrail"],
      "detail": {
        "eventSource": ["signin.amazonaws.com"],
        "eventName": ["ConsoleLogin"]
      }
    }
    PATTERN
    create-access-key = <<PATTERN
    {
      "source": ["aws.iam"],
      "detail-type": ["AWS API Call via CloudTrail"],
      "detail": {
        "eventSource": ["iam.amazonaws.com"],
        "eventName": ["CreateAccessKey"]
      }
    }
    PATTERN
  }
}

variable "slack_webhook_url" {
  type      = string
  sensitive = true
}

variable "channel" {
  type = string
}

variable "my_ips" {
  type = list(string)
}