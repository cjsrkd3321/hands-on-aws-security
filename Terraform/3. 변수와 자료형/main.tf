# terraform.tfvars
# TF_VAR_name

### string ###
variable "string" {
  description = "이것은 문자열 변수입니다."
  type        = string
  default     = "rex"
}

# output "string" {
#   value = var.string
# }

### number ###
variable "number" {
  type    = number
  default = 1
}

# output "number" {
#   value = var.number
# }

### bool ###
variable "bool" {
  type    = bool
  default = true
}

# output "bool" {
#   value = var.bool
# }

### list ###
variable "list" {
  type    = list(number)
  default = [1, 2, 3, 4, 4]
}

# output "list" {
#   value = var.list
#   # value = var.list[0]
# }

### tuple ### -> 거의 쓸 일 없음
variable "tuple" {
  type    = tuple([number, string])
  default = [1, "str"]
}

# output "tuple" {
#   value = var.tuple
#   # value = var.tuple[1]
# }

### set ###
variable "set" {
  type    = set(string)
  default = ["asdf", "str", "str"]
}

# output "set" {
#   value = var.set
#   # value = var.set[1] # 불가능
# }

## list or set -> set or list ###
# output "tolist" {
#   value = tolist(var.set)[0]
# }

# output "toset" {
#   value = toset(var.list)
# }

### map ###
variable "map" {
  type = map(number)
  default = {
    rex     = 1
    vincent = 2
    june    = 3
  }
}

# output "map" {
#   value = var.map
#   # value = var.map["rex"]
#   # value = var.map.rex
# }

### object ###
variable "object" {
  type = object({
    cidr     = string
    dns      = bool
    hostname = bool
  })
  default = {
    cidr     = "10.0.0.0/16",
    dns      = true
    hostname = true
  }
}

# output "object" {
#   value = var.object
#   # value = var.object["cidr"]
#   # value = var.object.cidr
# }

# resource "aws_vpc" "this" {
#   cidr_block           = var.object.cidr
#   enable_dns_hostnames = var.object.hostname
#   enable_dns_support   = var.object.dns

#   tags = {
#     Name = "${var.string}-vpc"
#   }
# }
