resource "aws_sns_topic" "order_alerts" {
  name = "order-alerts"

  tags = {
    Environment = "production"
  }
}
