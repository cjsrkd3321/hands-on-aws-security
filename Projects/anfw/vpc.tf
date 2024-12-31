data "aws_availability_zones" "first" {
  state = "available"
}

variable "vpc_cidr" {
  default = "10.64.0.0/16"
}

locals {
  az = data.aws_availability_zones.first.names[0]
}

resource "aws_vpc" "this" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${var.prefix_name}-vpc"
  }
}

##### PUBLIC #####
resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.this.id
  cidr_block        = "10.64.0.0/24"
  availability_zone = local.az

  tags = {
    Name = "${var.prefix_name}-public"
  }
}

resource "aws_internet_gateway" "this" {}

resource "aws_internet_gateway_attachment" "this" {
  internet_gateway_id = aws_internet_gateway.this.id
  vpc_id              = aws_vpc.this.id
}

resource "aws_eip" "this" {
  domain = "vpc"
}

resource "aws_nat_gateway" "this" {
  allocation_id = aws_eip.this.id
  subnet_id     = aws_subnet.public.id

  depends_on = [aws_internet_gateway.this]
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.this.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.this.id
  }

  route {
    cidr_block      = aws_subnet.private.cidr_block
    vpc_endpoint_id = tolist(aws_networkfirewall_firewall.this.firewall_status[0].sync_states)[0].attachment[0].endpoint_id
  }

  tags = {
    Name = "${var.prefix_name}-public"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

##### private #####
resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.this.id
  cidr_block        = "10.64.128.0/20"
  availability_zone = local.az

  tags = {
    Name = "${var.prefix_name}-private"
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.this.id

  route {
    cidr_block      = "0.0.0.0/0"
    vpc_endpoint_id = tolist(aws_networkfirewall_firewall.this.firewall_status[0].sync_states)[0].attachment[0].endpoint_id
  }

  tags = {
    Name = "${var.prefix_name}-private"
  }
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

##### FW #####
resource "aws_subnet" "fw" {
  vpc_id            = aws_vpc.this.id
  cidr_block        = "10.64.255.0/28"
  availability_zone = local.az

  tags = {
    Name = "${var.prefix_name}-fw"
  }
}

resource "aws_route_table" "fw" {
  vpc_id = aws_vpc.this.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.this.id
  }

  tags = {
    Name = "${var.prefix_name}-fw"
  }
}

resource "aws_route_table_association" "fw" {
  subnet_id      = aws_subnet.fw.id
  route_table_id = aws_route_table.fw.id
}
