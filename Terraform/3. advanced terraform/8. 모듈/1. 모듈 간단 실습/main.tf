module "user" {
  source = "./user"
  # name   = "rex"
}

output "user_arn" {
  value = module.user.arn
}