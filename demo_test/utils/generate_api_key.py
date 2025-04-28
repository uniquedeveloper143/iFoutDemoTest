import secrets

# Generate a random API key
api_key_secret = secrets.token_hex(32)  # 16 bytes = 32 hex characters

# Convert it into bytes
api_key_secret_bytes = bytes(api_key_secret, 'utf-8')

# Print both
print("Generated API Key Secret:", api_key_secret)
print("Bytes:", api_key_secret_bytes)
