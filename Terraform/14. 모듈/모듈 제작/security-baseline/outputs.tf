output "ebs_encrypted" {
  value = aws_ebs_encryption_by_default.this.enabled
}
