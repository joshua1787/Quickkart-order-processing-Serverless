resource "aws_sqs_queue" "order_queue" {
  name                      = "order-queue.fifo"
  fifo_queue                = true
  content_based_deduplication = true

  tags = {
    Environment = "production"
  }
}
