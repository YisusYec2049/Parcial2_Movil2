from config.db import db, ma, app

# The data model for the 'tblreport' table is defined.
class Report(db.Model):
    __tablename__ = "Report"

    idReport = db.Column(db.Integer, primary_key=True)
    date_issue = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(45), nullable=False)

    def __init__(self, date_issue, description):
        self.date_issue = date_issue
        self.description = description

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Definición del esquema de serialización
class ReportSchema(ma.Schema):
    class Meta:
        fields = ("idReport", "date_issue", "description")