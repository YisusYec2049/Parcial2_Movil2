from config.db import db, ma, app

class Report(db.Model):
    __tablename__ = "tblreport"

    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(50))
    content = db.Column(db.String(2000))
    creation_date = db.Column(db.Datatime)

    def __init__(self, type, content, creation_date):
        self.type = type
        self.content = content
        self.creation_date = creation_date

with app.app_context():
    db.create_all()

class ReportSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'content', 'creation_date')