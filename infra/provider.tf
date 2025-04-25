terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"   # Latest stable AWS provider version
    }
  }
}

provider "aws" {
  region = "us-east-1"    # Or your preferred region
}
