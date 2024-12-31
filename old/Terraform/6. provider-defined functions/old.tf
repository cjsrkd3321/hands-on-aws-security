module "parsed_arn" {
  source = "./modules/arn_parse"

  arn = "arn:aws:elasticloadbalancing:us-east-2:123456789012:loadbalancer/app/my-load-balancer/1234567890123456"
}

output "parsed_arn" {
  value = module.parsed_arn.value
}
