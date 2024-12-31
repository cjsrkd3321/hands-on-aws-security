# ### count 간단 실습 ###
resource "aws_iam_user" "this" {
  count = 3
  name  = "rex-${count.index}"
}

output "users" {
  value = aws_iam_user.this
  # value = aws_iam_user.this[0].arn
  # value = aws_iam_user.this[*].arn # splat expression
}

### count의 문제점 ###
# variable "users" {
#   type    = list(string)
#   default = ["rex", "june"]
# }

# resource "aws_iam_user" "this" {
#   count = length(var.users)
#   name  = "${var.users[count.index]}-${count.index}"
# }
