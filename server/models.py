from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Define custom naming convention for migrations
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)  # Message content
    username = db.Column(db.String, nullable=False)  # User who sent the message
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Default to current time
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Auto-update timestamp

    # SerializerMixin automatically serializes model instances to JSON-like dictionaries.
    serialize_rules = ('-created_at', '-updated_at')  # Example: exclude timestamps if needed
