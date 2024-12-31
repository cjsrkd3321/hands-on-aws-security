resource "aws_ebs_encryption_by_default" "this" {
  enabled = var.ebs_encrypted
}

resource "aws_ebs_snapshot_block_public_access" "this" {
  state = var.ebs_snapshot_block_public_access
}

resource "aws_iam_account_password_policy" "this" {
  minimum_password_length        = var.min_pass_len
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = true
  allow_users_to_change_password = true
}
