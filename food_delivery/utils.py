from celery import shared_task  # Celery decorator to register background tasks
from django.core.mail import send_mail  # Function to send emails
from django.template.loader import render_to_string  # Render HTML email templates
from django.utils.html import strip_tags  # Convert HTML to plain text
from .models import Order  # Import the Order model

@shared_task
def send_order_confirmation_email(order_id):
    order = Order.objects.get(pk=order_id)  # Retrieve the order by ID
    subject = f"Order Confirmation - #{order.id}"  # Email subject line

    html_message = render_to_string('food_delivery/emails/order_confirmation.html', {
        'order': order  # Pass order to email template
    })
    plain_message = strip_tags(html_message)  # Generate plain text fallback
    from_email = "noreply@deligo.com"  # Sender email address
    to = [order.customer.email]  # Recipient email address

    send_mail(
        subject,
        plain_message,
        from_email,
        to,
        html_message=html_message,
        fail_silently=False  # Raise an error if email fails to send
    )

    return f"Email sent to {to}"  # Return a simple confirmation message
