resource "aws_subnet" "this" {
  vpc_id     = local.vpc_id
  cidr_block = "10.0.1.0/24"
}

output "subnet_id" {
  value = aws_subnet.this.id
}
