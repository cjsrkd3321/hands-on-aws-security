# variable "is_good" {
#   default = false
# }

# output "is_good" {
#   value = var.is_good ? "YES" : "NO"
# }

variable "need_group" {
  default = true
}

resource "aws_iam_group" "this" {
  count = var.need_group ? 1 : 0

  name = "this_is_my_group"
  path = "/"
}

output "our_group" {
  value = aws_iam_group.this[0].arn
}
