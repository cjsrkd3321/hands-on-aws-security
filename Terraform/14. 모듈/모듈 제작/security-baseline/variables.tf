variable "ebs_encrypted" {
  type    = bool
  default = true
}

variable "ebs_snapshot_block_public_access" {
  type    = string
  default = "block-all-sharing"
}

variable "min_pass_len" {
  type    = number
  default = 10
}
