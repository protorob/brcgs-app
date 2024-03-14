from flask import Blueprint, render_template, flash, \
                redirect, url_for, request,Response
from flask_login import current_user, login_required
from app.models import ReceptionRecord
from app.extensions import db
from datetime import datetime
import csv
from io import StringIO

reception_bp = Blueprint('reception_bp', __name__)



@reception_bp.route("/reception", methods=("GET", "POST"))
@login_required
def reception():    
    receptions = ReceptionRecord.query.all()
    if request.method == "POST":
        reception_date = request.form.get('reception_date')
        transport_document_number = request.form.get('transport_document_number')
        transport_document_date = request.form.get('transport_document_date')
        supplier_name = request.form.get('supplier_name')
        received_products = request.form.get('received_products')
        correspondence_verification = request.form.get('correspondence_verification')
        hygienic_transport = request.form.get('hygienic_transport')
        is_oliveoil = request.form.get('is_oliveoil') == 'is_oliveoil'
        seal_number = request.form.get('seal_number')
        pack_integrity = request.form.get('pack_integrity')
        product_characteristics = request.form.get('product_characteristics')
        bestbefore_label = request.form.get('bestbefore_label')
        moka_verification = request.form.get('moka_verification')
        price_quantity_accepted = request.form.get('price_quantity_accepted')
        items_rejected = request.form.get('items_rejected')
        
        print('reception_date',reception_date)
        print('transport_document_number',transport_document_number)
        print('transport_document_date',transport_document_date)
        print('supplier_name',supplier_name)
        print('received_products',received_products)
        print('correspondence_verification',correspondence_verification)
        print('hygienic_transport',hygienic_transport)
        print('is_oliveoil',is_oliveoil)
        print('seal_number',seal_number)
        print('pack_integrity',pack_integrity)
        print('product_characteristics',product_characteristics)
        print('bestbefore_label',bestbefore_label)
        print('moka_verification',moka_verification)
        print('price_quantity_accepted',price_quantity_accepted)
        print('items_rejected',items_rejected)
        
        reception_date_obj = datetime.strptime(reception_date, "%Y-%m-%d")
        transport_document_date_obj = datetime.strptime(transport_document_date, "%Y-%m-%d")
        new_record = ReceptionRecord(
            reception_date=reception_date_obj,
            transport_document_number=transport_document_number,
            transport_document_date=transport_document_date_obj,
            supplier_name=supplier_name,
            received_products=received_products,
            correspondence_verification=correspondence_verification,
            hygienic_transport=hygienic_transport,
            is_oliveoil=is_oliveoil,
            seal_number=seal_number,
            pack_integrity=pack_integrity,
            product_characteristics=product_characteristics,
            bestbefore_label=bestbefore_label,
            moka_verification=moka_verification,
            price_quantity_accepted=price_quantity_accepted,
            items_rejected=items_rejected,
            user_id=current_user.id
        )
        db.session.add(new_record)
        db.session.commit()
        flash("Successfully added reception record", "success")
        return redirect(url_for('reception_bp.reception'))
    return render_template("reception.html", receptions=receptions)



@reception_bp.route('/export_reception_csv')
@login_required
def export_reception_csv():
    reception_records = ReceptionRecord.query.all()
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Reception Date", "Transport Document Number", "Transport Document Date", 
                     "Supplier Name", "Received Products", "Correspondence Verification", 
                     "Hygienic Transport", "Is Olive Oil", "Seal Number", "Pack Integrity", 
                     "Product Characteristics", "Best Before Label", "Moka Verification", 
                     "Price Quantity Accepted", "Items Rejected","Received by"])

    for record in reception_records:
        writer.writerow([record.reception_date, record.transport_document_number, 
                         record.transport_document_date, record.supplier_name, 
                         record.received_products, record.correspondence_verification, 
                         record.hygienic_transport, record.is_oliveoil, 
                         record.seal_number, record.pack_integrity, 
                         record.product_characteristics, record.bestbefore_label, 
                         record.moka_verification, record.price_quantity_accepted, 
                         record.items_rejected,record.user.username])

    output.seek(0)

    response = Response(output.getvalue(), content_type='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=reception_records.csv"

    return response