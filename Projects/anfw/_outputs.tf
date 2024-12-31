output "vpc_id" {
  value = aws_vpc.this.id
}

output "app_subnet_id" {
  value = aws_subnet.private.id
}
