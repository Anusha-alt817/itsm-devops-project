
variable "aws_region" {
  description = "AWS region where ITSM infrastructure will be created"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR range for the ITSM VPC"
  type        = string
  default     = "10.20.0.0/16"
}

variable "public_subnet_cidrs" {
  description = "CIDR ranges for public subnets"
  type        = list(string)
  default     = ["10.20.1.0/24", "10.20.2.0/24"]
}

variable "private_subnet_cidrs" {
  description = "CIDR ranges for private subnets"
  type        = list(string)
  default     = ["10.20.11.0/24", "10.20.12.0/24"]
}