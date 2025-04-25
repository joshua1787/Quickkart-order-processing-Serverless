resource "aws_s3_bucket" "order_files" {
  bucket = "quickkart-order-files-${random_id.suffix.hex}"  # Correct random suffix
  force_destroy = true

  tags = {
    Environment = "production"
  }
}

resource "random_id" "suffix" {
  byte_length = 4
}
