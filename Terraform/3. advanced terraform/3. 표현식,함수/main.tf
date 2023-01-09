# variable "is_true" {
#   default = true
# }

# output "test" {
#   value = var.is_true ? 1 : 0
# }

# variable "settings" {
#   default = {
#     a = {
#       namespace = "123"
#       name      = "1"
#       value     = "124151"
#     }
#     b = {
#       namespace = "asdf"
#       name      = "asdf"
#       value     = "asdf"
#     }
#   }
# }

# resource "aws_elastic_beanstalk_environment" "tfenvtest" {
#   name                = "tf-test-name"
#   application         = "123"
#   solution_stack_name = "64bit Amazon Linux 2018.03 v2.11.4 running Go 1.12.6"

#   dynamic "setting" {
#     for_each = var.settings
#     content {
#       namespace = setting.value["namespace"]
#       name      = setting.value["name"]
#       value     = setting.value["value"]
#     }
#   }
# }


# variable "test" {
#   default = {
#     rex     = "good"
#     vincent = "bad"
#     june    = "hmm"
#   }
# }

# output "test2" {
#   #   value = { for k, v in var.test : k => v }
#   value = [for k, _ in var.test : k]
# }

# variable "rex" {
#   default = "rex"
# }

# output "test3" {
#   value = startswith(var.rex, "rex")
# }

output "test4" {
  value = file("main.tf")
}