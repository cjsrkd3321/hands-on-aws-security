variable "name" {
  type = string
}

variable "src_public_ips" {
  type = list(string)
}

variable "src_private_ips" {
  type = list(string)
}

variable "policy" {
  type    = string
  default = ""
}

variable "principal_arns" {
  type = list(string)
}

variable "user_ids" {
  type = list(string)
}

# variable "vpcs" {
#   type = list(string)
# }

# variable "vpces" {
#   type = list(string)
# }