from flask import Blueprint, render_template, flash, \
                redirect, url_for, request,Response
from flask_login import current_user,login_required
from app.models import FulfillmentRecord
from app.extensions import db
from datetime import datetime
import csv
from io import StringIO

fulfillment_bp = Blueprint('fulfillment_bp', __name__)


@fulfillment_bp.route("/fulfillment", methods=("GET", "POST"))
@login_required
def fulfillment():
    fulfillments = FulfillmentRecord.query.all()
    if request.method == "POST":
        fulfillment_date = request.form.get('fulfillment_date')
        fulfillment_doc_number = request.form.get('fulfillment_doc_number')
        fulfillment_lot = request.form.get('fulfillment_lot')
        fulfillment_transporter = request.form.get('fulfillment_transporter')
        transporter_plate_number = request.form.get('transporter_plate_number')
        fullfilled_product_quantity = request.form.get('fullfilled_product_quantity')
        higienic_condition_check = request.form.get('higienic_condition_check')
        product_integrity_check = request.form.get('product_integrity_check')
        operation_result_check = request.form.get('operation_result_check')
        print('fulfillment_date',fulfillment_date)
        print('fulfillment_date',type(fulfillment_date))
        print('fulfillment_doc_number',fulfillment_doc_number)
        print('fulfillment_lot',fulfillment_lot)
        print('fulfillment_transporter',fulfillment_transporter)
        print('transporter_plate_number',transporter_plate_number)
        print('fullfilled_product_quantity',fullfilled_product_quantity)
        print('higienic_condition_check',higienic_condition_check)
        print('product_integrity_check',product_integrity_check)
        print('operation_result_check',operation_result_check)
        fulfillment_date_obj = datetime.strptime(fulfillment_date, "%Y-%m-%d")
        new_record = FulfillmentRecord(
            fulfillment_date=fulfillment_date_obj,
            fulfillment_doc_number=fulfillment_doc_number,
            fulfillment_lot=fulfillment_lot,
            fulfillment_transporter=fulfillment_transporter,
            transporter_plate_number=transporter_plate_number,
            fullfilled_product_quantity=fullfilled_product_quantity,
            higienic_condition_check=higienic_condition_check,
            product_integrity_check=product_integrity_check,
            operation_result_check=operation_result_check,
            user_id=current_user.id
        )
        db.session.add(new_record)
        db.session.commit()
        flash("Successfully added fulfillment record", "success")
        return redirect(url_for('fulfillment_bp.fulfillment'))
    return render_template("fulfillment.html", fulfillments=fulfillments)



@fulfillment_bp.route('/export_fulfillment_csv')
@login_required
def export_fulfillment_csv():
    fulfillment_records = FulfillmentRecord.query.all()
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Fulfillment Date", "Fulfillment Doc Number", "Fulfillment Lot", 
                     "Fulfillment Transporter", "Transporter Plate Number", 
                     "Fullfilled Product Quantity", "Higienic Condition Check", 
                     "Product Integrity Check", "Operation Result Check","Operator"])

    for record in fulfillment_records:
        writer.writerow([record.fulfillment_date, record.fulfillment_doc_number, 
                         record.fulfillment_lot, record.fulfillment_transporter, 
                         record.transporter_plate_number, record.fullfilled_product_quantity, 
                         record.higienic_condition_check, record.product_integrity_check, 
                         record.operation_result_check,record.user.username])

    output.seek(0)

    response = Response(output.getvalue(), content_type='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=fulfillment_records.csv"

    return response