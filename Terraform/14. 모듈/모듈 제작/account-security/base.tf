module "baseline" {
  source = "../security-baseline"
}

output "ebs_encrypted" {
  value = module.baseline.ebs_encrypted
}
