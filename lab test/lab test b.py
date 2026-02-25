def convert_inr_to_usd(inr_amount):
    conversion_rate = 90  # 1 USD = 90 INR
    usd_amount = inr_amount / conversion_rate
    return usd_amount

# Example usage
inr_value = 4500
usd_value = convert_inr_to_usd(inr_value)
print(f"{inr_value} INR is approximately {usd_value:.2f} USD.") 