from app.extensions import db, bcrypt
from datetime import datetime
from flask_login import UserMixin

# Users-usertable
# Inprocess-productionrecord
# Reception-receptionrecord
# Fulfillment- ñfulfillmentrecord

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(255),nullable=False, )
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    
    production_records = db.relationship('ProductionRecord', back_populates='user', lazy=True)
    reception_records = db.relationship('ReceptionRecord', back_populates='user', lazy=True)
    fulfillment_records = db.relationship('FulfillmentRecord', back_populates='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class ProductionRecord(db.Model):

    __tablename__ = 'production_records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    process_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    product_lot_number = db.Column(db.Text, nullable=False)
    best_before_date = db.Column(db.Date, nullable=False)
    product_sku = db.Column(db.Text, nullable=False)
    filter_integrity_check = db.Column(db.Text, nullable=False)
    sanification_check = db.Column(db.Text, nullable=False)
    general_packaging_control = db.Column(db.Boolean)
    bottle_integrity_control = db.Column(db.Boolean)
    visual_olfatory_control = db.Column(db.Boolean)
    graphics_control = db.Column(db.Boolean)
    lot_number_check = db.Column(db.Text, nullable=False)
    start_pressure_time = db.Column(db.Time, nullable=False)
    start_pressure_value = db.Column(db.Float, nullable=False)
    first_pressure_time = db.Column(db.Time, nullable=False)
    first_pressure_value = db.Column(db.Float, nullable=False)
    second_pressure_time = db.Column(db.Time, nullable=False)
    second_pressure_value = db.Column(db.Float, nullable=False)
    final_pressure_time = db.Column(db.Time, nullable=False)
    final_pressure_value = db.Column(db.Float, nullable=False)
    label_compliance = db.Column(db.Text, nullable=False)
    start_filling_cap_compliance = db.Column(db.Text, nullable=False)
    final_filling_cap_compliance = db.Column(db.Text, nullable=False)
    bottle_breakage = db.Column(db.Text, nullable=False)
    bottle_breakage_qty = db.Column(db.Integer)
    units_produced_qty = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='production_records', lazy=True)

    def __repr__(self):
        return f'<Lot number: {self.product_lot_number}\
        from {self.process_date} added by user id: {self.user_id}'


class ReceptionRecord(db.Model):

    __tablename__ = 'reception_records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reception_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    transport_document_number = db.Column(db.Text, nullable=False)
    transport_document_date = db.Column(db.Date, nullable=False)
    supplier_name = db.Column(db.Text, nullable=False)
    received_products = db.Column(db.Text, nullable=False)
    correspondence_verification = db.Column(db.Text, nullable=False)
    hygienic_transport = db.Column(db.Text, nullable=False)
    is_oliveoil = db.Column(db.Boolean)
    seal_number = db.Column(db.Text)
    pack_integrity = db.Column(db.Text, nullable=False)
    product_characteristics = db.Column(db.Text, nullable=False)
    bestbefore_label = db.Column(db.Text, nullable=False)
    moka_verification = db.Column(db.Text, nullable=False)
    price_quantity_accepted = db.Column(db.Text, nullable=False)
    items_rejected = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='reception_records', lazy=True)

    def __repr__(self):
        return f'<transport document number: {self.transport_document_number}\
        from {self.reception_date} added by user id: {self.user_id}'


class FulfillmentRecord(db.Model):

    __tablename__ = 'fulfillment_records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fulfillment_date = db.Column(db.Date, nullable=False)
    fulfillment_doc_number = db.Column(db.String(120), nullable=False)
    fulfillment_lot = db.Column(db.String(120), nullable=False)
    fulfillment_transporter = db.Column(db.String(120), nullable=False)
    transporter_plate_number = db.Column(db.String(120), nullable=False)
    fullfilled_product_quantity = db.Column(db.Integer)
    higienic_condition_check = db.Column(db.String(50), nullable=False, default="Compliant")
    product_integrity_check = db.Column(db.String(50), nullable=False, default="Compliant")
    operation_result_check = db.Column(db.String(50), nullable=False, default="Compliant")

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='fulfillment_records', lazy=True)
    
    def __repr__(self):
        return f'<transport document number: {self.fulfillment_doc_number}\
        from {self.fulfillment_date} added by user id: {self.user_id}'