variable "users" {
  default = ["rex", "vincent", "june"]
}

# 기본 형태 (함수 + count)
resource "aws_iam_user" "count" {
  count = length(var.users)

  name = var.users[count.index]
  path = "/"
}

# # 변수 형태 변경 불가능 (for_each 변경 + for 표현식)
# resource "aws_iam_user" "for" {
#   for_each = toset([for user in var.users : user])

#   name = each.key
#   path = "/"
# }

# # 변수 형태 변경 불가능 (for_each 변경 + for 표현식)
# # + vincent 제외하고 싶음
# resource "aws_iam_user" "for_exclude" {
#   for_each = toset([for user in var.users : user if user != "vincent"])

#   name = each.key
#   path = "/"
# }

variable "users_with_path" {
  default = {
    rex     = "/admin/"
    vincent = "/admin/"
    june    = "/user/"
  }
}

# # 기본 형태
# resource "aws_iam_user" "for_kv" {
#   for_each = var.users_with_path

#   name = each.key
#   path = each.value
# }

# # june 제외하고 싶음
# resource "aws_iam_user" "for_kv_exclude" {
#   for_each = { for k, v in var.users_with_path : k => v if k != "june" }

#   name = each.key
#   path = each.value
# }
