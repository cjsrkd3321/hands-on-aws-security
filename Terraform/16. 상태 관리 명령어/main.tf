# terraform import aws_iam_user.this state-mgmt
# resource "aws_iam_user" "this" {
#   name = "state-mgmt"
# }

# terraform state mv aws_iam_user.this aws_iam_user.state_mgmt
# terraform state rm aws_iam_user.state_mgmt
# terraform state rm 'aws_iam_user.this["rex2"]'
resource "aws_iam_user" "state_mgmt" {
  name = "state-mgmt"
}
