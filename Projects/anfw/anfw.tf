resource "aws_networkfirewall_firewall" "this" {
  name                = "${var.prefix_name}-firewall"
  vpc_id              = aws_vpc.this.id
  firewall_policy_arn = aws_networkfirewall_firewall_policy.this.arn

  subnet_mapping {
    subnet_id = aws_subnet.fw.id
  }
}

resource "aws_networkfirewall_firewall_policy" "this" {
  name = "${var.prefix_name}-policy"

  firewall_policy {
    stateless_default_actions          = ["aws:forward_to_sfe"]
    stateless_fragment_default_actions = ["aws:drop"]
    stateful_engine_options {
      rule_order = "STRICT_ORDER"
    }
    stateful_rule_group_reference {
      priority     = 1
      resource_arn = aws_networkfirewall_rule_group.this.arn
    }
  }
}

resource "aws_networkfirewall_rule_group" "this" {
  capacity = 10
  name     = "${var.prefix_name}-domain-filter-rule-group"
  type     = "STATEFUL"
  rule_group {
    stateful_rule_options {
      rule_order = "STRICT_ORDER"
    }
    rules_source {
      rules_source_list {
        generated_rules_type = "DENYLIST"
        target_types         = ["HTTP_HOST", "TLS_SNI"]
        targets              = [".naver.com", ".google.com"]
      }
    }
  }
}

resource "aws_networkfirewall_logging_configuration" "this" {
  firewall_arn = aws_networkfirewall_firewall.this.arn
  logging_configuration {
    log_destination_config {
      log_destination = {
        logGroup = aws_cloudwatch_log_group.this.name
      }
      log_destination_type = "CloudWatchLogs"
      log_type             = "ALERT"
    }
    log_destination_config {
      log_destination = {
        logGroup = aws_cloudwatch_log_group.this.name
      }
      log_destination_type = "CloudWatchLogs"
      log_type             = "TLS"
    }
  }
}

resource "aws_cloudwatch_log_group" "this" {
  name              = "${var.prefix_name}-log-group"
  retention_in_days = 1
}
