resource "aws_iam_user" "this" {
    name = var.name
    path = "/rex/"
}