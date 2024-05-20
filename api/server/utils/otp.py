import pyotp

# Create a secret key (keep it secret!)
secret_key = pyotp.random_base32()


class OTPGenerator:

    def __init__(self, interval=60) -> None:
        self.interval = interval
        self.totp = pyotp.TOTP(secret_key, digits=6, interval=self.interval)

    def generate_code(self) -> str:
        return self.totp.now()

    def verify_code(self, code) -> bool:
        return self.totp.verify(code)
