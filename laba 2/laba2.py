from abc import ABC, abstractmethod

# Абстрактний клас для повідомлення (Open/Closed Principle)
class Message(ABC):
    @abstractmethod
    def send(self):
        pass

# Повідомлення електронною поштою (Single Responsibility)
class EmailMessage(Message):
    def __init__(self, recipient, subject):
        self.recipient = recipient
        self.subject = subject

    def send(self):
        return f"Sending email to {self.recipient} with subject '{self.subject}'"

# SMS-повідомлення
class SMSMessage(Message):
    def __init__(self, phone_number, text):
        self.phone_number = phone_number
        self.text = text

    def send(self):
        return f"Sending SMS to {self.phone_number}: '{self.text}'"

# Клас, відповідальний тільки за виведення результату надсилання (Single Responsibility)
class DeliveryLogger:
    def log_delivery(self, message: Message):
        print(message.send())

# Головна функція
def start_delivery():
    email = EmailMessage("user@example.com", "Welcome to US!")
    sms = SMSMessage("+38000234535", "Your code is 9876")

    logger = DeliveryLogger()
    logger.log_delivery(email)
    logger.log_delivery(sms)

if __name__ == "__main__":
    start_delivery()
