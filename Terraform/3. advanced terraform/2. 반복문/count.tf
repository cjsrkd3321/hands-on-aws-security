provider "aws" {
  region = "ap-northeast-2"
}

# count 간단 실습
# resource "aws_iam_user" "this" {
#   count = 4
#   name  = "rex-${count.index}"
# }

# output "users" {
#   # value = aws_iam_user.this[0].name
#   # value = aws_iam_user.this[*].name
# }

# count의 문제점
# variable "users" {
#   type    = list(string)
#   default = ["rex", "june"]
# }

# resource "aws_iam_user" "this" {
#   count = length(var.users)
#   name  = var.users[count.index]
# }

# count 와 조건 표현식 응용
# variable "create" {
#   type    = bool
#   default = true
# }

# resource "aws_iam_user" "this" {
#   count = var.create ? 1 : 0
#   name  = "rex"
# }