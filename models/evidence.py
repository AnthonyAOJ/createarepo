from models import db


class Evidence(db.Model):
    """
    Stores one retained evidence source for a completed verification.

    Linked to its parent Submission so a saved verification's full
    evidence set can be reconstructed later (see Verification Detail Page).

    relevance is nullable until relevance scoring (issue #13) is
    implemented; it is not populated by this feature.
    """

    id = db.Column(db.Integer, primary_key=True)

    submission_id = db.Column(
        db.Integer,
        db.ForeignKey("submission.id"),
        nullable=False
    )

    title = db.Column(
        db.Text,
        nullable=False
    )

    url = db.Column(
        db.Text,
        nullable=False
    )

    publisher = db.Column(
        db.Text,
        nullable=True
    )

    excerpt = db.Column(
        db.Text,
        nullable=True
    )

    relevance = db.Column(
        db.Float,
        nullable=True
    )

    submission = db.relationship(
        "Submission",
        backref=db.backref("evidence_items", lazy=True)
    )

    def __repr__(self):
        return f"<Evidence {self.id} for Submission {self.submission_id}>"
