import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime

import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timezone


def check_jwt_expiration(token):
    try:
        # Decode the JWT without verifying the signature
        payload = jwt.decode(token, options={"verify_signature": False})

        # Extract the 'exp' field from the payload
        exp = payload.get("exp")

        if exp is None:
            return "No expiration claim ('exp') found in token."

        # Convert the expiration timestamp to a datetime object
        exp_timestamp = exp
        exp_date = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)

        # Get the current time in UTC
        current_time = datetime.now(tz=timezone.utc)

        # Check if the token has expired
        if current_time > exp_date:
            return "Token has expired."
        else:
            return f"Token is valid. Expires at: {exp_date}"

    except InvalidTokenError:
        return "Invalid token."


# Example JWT token (replace with your token)
jwt_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjZENEZBMUE5NzgzNkIwQUM2OTJBNUE2MzMyQjBCOTU2IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE3MjU0NDQ1NDMsImV4cCI6MTcyODAzNjU0MywiaXNzIjoiaHR0cHM6Ly9zcHl3LWlkc2FwaS53YWxsZXRnYXRlLmlvIiwiYXVkIjoiTW9iaWxlX0FwaSIsImNsaWVudF9pZCI6IjFCOTM4RUI3LTMyMTEtNDQ1OS05QTQ5LTkzRUMwODQ1QzgzQiIsInN1YiI6IjI0MDgwNTE2NjI3MDI0OTk4OTUiLCJhdXRoX3RpbWUiOjE3MjU0NDQ1NDMsImlkcCI6ImxvY2FsIiwidGVuYW50X2lkIjoiMTg1NTE0NjA5NDIyMzgxMzY0NSIsInRlbmFudF9jb2RlIjoiU1BZVyIsImFjY291bnRfbnVtYmVyIjoiODg5Mzg2MzM5NCIsImp0aSI6IkZCMEEwMTQwMzY1NzMzNjUxM0RCMzQ5QzMyQkEyQTY0IiwiaWF0IjoxNzI1NDQ0NTQzLCJzY29wZSI6WyJhcGlhY2Nlc3NlcyIsIm1vYmlsZV9hcGkiLCJvcGVuaWQiLCJwcm9maWxlIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInB3ZCJdfQ.ekF89dZtZjRYERhxk0gjoAKlhLbd9EgtwiJ3A0mtKWVSIaPjB9DdLjBIfp2Afsj-3W_Z4SRHJV6dYp_Xv9VF5pjNXIYpa-hLNGN9t1JEaBFvZPIy6whfo-60nI4B9En0Ht1eJ4OBPaDG_KOlS0yGvJEoCuW0zPM06oAbdL18t6SmENTvhW0CPGlTC7PgmKijsnzBgROk8Wq2zHOTb68g8OQqDhfGJsux2ZVsoPUbK_ug1-gAn3sWiHbPdZRd8L4theJH-OQZp3lqBFmKOHW3DidL1tYmYeQKGPF_On7DsIt76rOuI9B7rE0hwwbMgkPoMFIeC0YPDEhJGO3yUU0kqQ"

# Check expiration
result = check_jwt_expiration(jwt_token)
print(result)
