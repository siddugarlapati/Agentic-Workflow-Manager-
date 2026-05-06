from langchain.tools import BaseTool
import stripe
from app.core.config import settings


class StripeCreateCustomerTool(BaseTool):
    name = "stripe_create_customer"
    description = "Create a new customer in Stripe"
    
    def _run(self, email: str, name: str, description: str = "") -> str:
        """Create Stripe customer"""
        if not settings.STRIPE_API_KEY:
            return "Stripe API key not configured"
        
        try:
            stripe.api_key = settings.STRIPE_API_KEY
            
            customer = stripe.Customer.create(
                email=email,
                name=name,
                description=description
            )
            
            return f"Customer created: {customer.id}"
        except Exception as e:
            return f"Error creating customer: {str(e)}"
    
    async def _arun(self, *args, **kwargs):
        return self._run(*args, **kwargs)


class StripeCreateSubscriptionTool(BaseTool):
    name = "stripe_create_subscription"
    description = "Create a subscription for a customer in Stripe"
    
    def _run(self, customer_id: str, price_id: str) -> str:
        """Create Stripe subscription"""
        if not settings.STRIPE_API_KEY:
            return "Stripe API key not configured"
        
        try:
            stripe.api_key = settings.STRIPE_API_KEY
            
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{"price": price_id}]
            )
            
            return f"Subscription created: {subscription.id}"
        except Exception as e:
            return f"Error creating subscription: {str(e)}"
    
    async def _arun(self, *args, **kwargs):
        return self._run(*args, **kwargs)
