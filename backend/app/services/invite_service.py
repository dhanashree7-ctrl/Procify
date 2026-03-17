import os
import resend
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

class InviteService:
    """
    Email magic links via Resend.
    """
    def send_invite(self, email: str, magic_link: str):
        params = {
            "from": "Procify <noreply@procify.io>",
            "to": [email],
            "subject": "Your Exam Invite",
            "html": f"<p>Access your exam here: <a href='{magic_link}'>{magic_link}</a></p>",
        }
        # resend.Emails.send(params)
        return {"status": "sent"}

invite_service = InviteService()
