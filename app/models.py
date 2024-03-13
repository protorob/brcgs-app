from . import db
from flask import current_app
from datetime import datetime


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):

        self.email = email
        self.password = password
        self.password = current_app.bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):

        return f'<email {self.email}>'


class ProductionRecord(db.Model):

    __tablename__ = 'production_records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
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

    def __init__(self, user_id, product_lot_number, best_before_date, product_sku,
                filter_integrity_check, sanification_check, general_packaging_control,
                bottle_integrity_control, visual_olfatory_control, graphics_control,
                lot_number_check, start_pressure_time, start_pressure_value, first_pressure_time,
                first_pressure_value, second_pressure_time, second_pressure_value,
                final_pressure_time, final_pressure_value, label_compliance,
                start_filling_cap_compliance, final_filling_cap_compliance, bottle_breakage,
                bottle_breakage_qty, units_produced_qty, process_date=None):
        self.user_id = user_id
        self.process_date = process_date if process_date else datetime.now()
        self.product_lot_number = product_lot_number
        self.best_before_date = best_before_date
        self.product_sku = product_sku
        self.filter_integrity_check = filter_integrity_check
        self.sanification_check = sanification_check
        self.general_packaging_control = general_packaging_control
        self.bottle_integrity_control = bottle_integrity_control
        self.visual_olfatory_control = visual_olfatory_control
        self.graphics_control = graphics_control
        self.lot_number_check = lot_number_check
        self.start_pressure_time = start_pressure_time
        self.start_pressure_value = start_pressure_value
        self.first_pressure_time = first_pressure_time
        self.first_pressure_value = first_pressure_value
        self.second_pressure_time = second_pressure_time
        self.second_pressure_value = second_pressure_value
        self.final_pressure_time = final_pressure_time
        self.final_pressure_value = final_pressure_value
        self.label_compliance = label_compliance
        self.start_filling_cap_compliance = start_filling_cap_compliance
        self.final_filling_cap_compliance = final_filling_cap_compliance
        self.bottle_breakage = bottle_breakage
        self.bottle_breakage_qty = bottle_breakage_qty
        self.units_produced_qty = units_produced_qty

    def __repr__(self):
        return f'<Lot number: {self.product_lot_number}\
        from {self.process_date} added by user id: {self.user_id}'


class ReceptionRecord(db.Model):

    __tablename__ = 'reception_records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
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


    def __init__(self, user_id, transport_document_number, transport_document_date, supplier_name,
                 received_products, correspondence_verification, hygienic_transport, is_oliveoil,
                 seal_number, pack_integrity, product_characteristics, bestbefore_label,
                 moka_verification, price_quantity_accepted, items_rejected, reception_date=None):

        self.user_id = user_id
        self.reception_date = reception_date if reception_date else datetime.utcnow()
        self.transport_document_number = transport_document_number
        self.transport_document_date = transport_document_date
        self.supplier_name = supplier_name
        self.received_products = received_products
        self.correspondence_verification = correspondence_verification
        self.hygienic_transport = hygienic_transport
        self.is_oliveoil = is_oliveoil
        self.seal_number = seal_number
        self.pack_integrity = pack_integrity
        self.product_characteristics = product_characteristics
        self.bestbefore_label = bestbefore_label
        self.moka_verification = moka_verification
        self.price_quantity_accepted = price_quantity_accepted
        self.items_rejected = items_rejected

    def __repr__(self):
        return f'<transport document number: {self.transport_document_number}\
        from {self.reception_date} added by user id: {self.user_id}'


# Define the Fulfillment model
class FulfillmentRecords(db.Model):

    __tablename__ = 'fulfillment_records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fulfillment_date = db.Column(db.Date, nullable=False)
    fulfillment_doc_number = db.Column(db.String(120), nullable=False)
    fulfillment_lot = db.Column(db.String(120), nullable=False)
    fulfillment_transporter = db.Column(db.String(120), nullable=False)
    transporter_plate_number = db.Column(db.String(120), nullable=False)
    fullfilled_product_quantity = db.Column(db.Integer)
    higienic_condition_check = db.Column(db.String(50), nullable=False, default="Compliant")
    product_integrity_check = db.Column(db.String(50), nullable=False, default="Compliant")
    operation_result_check = db.Column(db.String(50), nullable=False, default="Compliant")

    def __init__(self, user_id, fulfillment_doc_number, fulfillment_lot,
        fulfillment_transporter, transporter_plate_number, fullfilled_product_quantity,
        higienic_condition_check, product_integrity_check, operation_result_check, fulfillment_date=None ):
        
        self.user_id = user_id
        self.fulfillment_date = fulfillment_date if fulfillment_date else datetime.utcnow()
        self.fulfillment_doc_number = fulfillment_doc_number
        self.fulfillment_lot = fulfillment_lot
        self.fulfillment_transporter = fulfillment_transporter
        self.transporter_plate_number = transporter_plate_number
        self.fullfilled_product_quantity = fullfilled_product_quantity
        self.higienic_condition_check = higienic_condition_check
        self.product_integrity_check = product_integrity_check
        self.operation_result_check = operation_result_check

    def __repr__(self):
        return f'<transport document number: {self.fulfillment_doc_number}\
        from {self.fulfillment_date} added by user id: {self.user_id}'
