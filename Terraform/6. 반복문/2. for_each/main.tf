variable "users" {
  type = object({
    rex2    = string
    vincent = string
    june    = string
  })
  default = {
    rex2    = "/good/"
    vincent = "/bad/"
    june    = "/hmm/"
  }
}

resource "aws_iam_user" "this" {
  for_each = var.users
  name     = each.key
  path     = each.value
}

# variable "users" {
#   type    = list(string)
#   default = ["rex12", "vincent", "june"]
# }

# resource "aws_iam_user" "this" {
#   for_each = toset(var.users)
#   name     = each.key
#   path     = startswith(each.value, "/") ? each.value : "/"
# }
