class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserRepository:
    def save_user(self, user):
        print(f"Saving user {user.username} to database")


class EmailService:
    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.email}")


class UserReport:
    def generate_report(self, user):
        print(f"User report for {user.username}")

