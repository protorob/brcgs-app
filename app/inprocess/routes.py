from flask import Blueprint, render_template, flash, \
                redirect, url_for, request,Response
from flask_login import current_user, login_required
from app.models import ProductionRecord
import csv
from io import StringIO
from datetime import datetime
from app.extensions import db

inprocess_bp = Blueprint('inprocess_bp', __name__)


def string_to_time(time_str):
    return datetime.strptime(time_str, '%H:%M').time()


@inprocess_bp.route("/inprocess", methods=("GET", "POST"))
@login_required
def inprocess():
    records = ProductionRecord.query.all()
    if request.method == "POST":
        process_date = request.form.get('process_date')
        product_lot_number = request.form.get('product_lot_number')
        best_before_date = request.form.get('best_before_date')
        product_sku = request.form.get('product_sku')
        filter_integrity_check = request.form.get('filter_integrity_check')
        sanification_check = request.form.get('sanification_check')
        general_packaging_control = request.form.get('general_packaging_control') == 'Checked'
        bottle_integrity_control = request.form.get('bottle_integrity_control') == 'Checked'
        visual_olfatory_control = request.form.get('visual_olfatory_control') == 'Checked'
        graphics_control = request.form.get('graphics_control') == 'Checked'
        lot_number_check = request.form.get('lot_number_check')
        start_pressure_time = request.form.get('start_pressure_time')
        start_pressure_value = request.form.get('start_pressure_value')
        first_pressure_time = request.form.get('first_pressure_time')
        first_pressure_value = request.form.get('first_pressure_value')
        second_pressure_time = request.form.get('second_pressure_time')
        second_pressure_value = request.form.get('second_pressure_value')
        final_pressure_time = request.form.get('final_pressure_time')
        final_pressure_value = request.form.get('final_pressure_value')
        label_compliance = request.form.get('label_compliance')
        start_filling_cap_compliance = request.form.get('start_filling_cap_compliance')
        final_filling_cap_compliance = request.form.get('final_filling_cap_compliance')
        bottle_breakage = request.form.get('bottle_breakage')
        bottle_breakage_qty = request.form.get('bottle_breakage_qty')
        units_produced_qty = request.form.get('units_produced_qty')
        
        print('process_date',process_date)
        print('product_lot_number',product_lot_number)
        print('best_before_date',best_before_date)
        print('product_sku',product_sku)
        print('filter_integrity_check',filter_integrity_check)
        print('sanification_check',sanification_check)
        print('general_packaging_control',general_packaging_control)
        print('bottle_integrity_control',bottle_integrity_control)
        print('visual_olfatory_control',visual_olfatory_control)
        print('graphics_control',graphics_control)
        print('lot_number_check',lot_number_check)
        print('start_pressure_time',start_pressure_time)
        print('start_pressure_value',start_pressure_value)
        print('first_pressure_time',first_pressure_time)
        print('first_pressure_value',first_pressure_value)
        print('second_pressure_time',second_pressure_time)
        print('second_pressure_value',second_pressure_value)
        print('final_pressure_time',final_pressure_time)
        print('final_pressure_value',final_pressure_value)
        print('label_compliance',label_compliance)
        print('start_filling_cap_compliance',start_filling_cap_compliance)
        print('final_filling_cap_compliance',final_filling_cap_compliance)
        print('bottle_breakage',bottle_breakage)
        print('bottle_breakage_qty',bottle_breakage_qty)
        print('units_produced_qty',units_produced_qty)
        
        process_date_obj = datetime.strptime(process_date, "%Y-%m-%d")
        best_before_date_obj = datetime.strptime(best_before_date, "%Y-%m-%d")
        new_record = ProductionRecord(
            process_date=process_date_obj,
            product_lot_number=product_lot_number,
            best_before_date=best_before_date_obj,
            product_sku=product_sku,
            filter_integrity_check=filter_integrity_check,
            sanification_check=sanification_check,
            general_packaging_control=general_packaging_control,
            bottle_integrity_control=bottle_integrity_control,
            visual_olfatory_control=visual_olfatory_control,
            graphics_control=graphics_control,
            lot_number_check=lot_number_check,
            start_pressure_time=string_to_time(start_pressure_time),
            start_pressure_value=start_pressure_value,
            
            first_pressure_time=string_to_time(first_pressure_time),
            first_pressure_value=first_pressure_value,
            
            second_pressure_time=string_to_time(second_pressure_time),
            second_pressure_value=second_pressure_value,
            
            final_pressure_time=string_to_time(final_pressure_time),
            final_pressure_value=final_pressure_value,
            
            label_compliance=label_compliance,
            start_filling_cap_compliance=start_filling_cap_compliance,
            final_filling_cap_compliance=final_filling_cap_compliance,
            bottle_breakage=bottle_breakage,
            bottle_breakage_qty=bottle_breakage_qty,
            units_produced_qty=units_produced_qty,
            
            user_id=current_user.id
        )
        db.session.add(new_record)
        db.session.commit()
        flash("Successfully added inprocess record", "success")
        return redirect(url_for('inprocess_bp.inprocess'))
    return render_template("inprocess.html", records=records)



@inprocess_bp.route('/export_production_csv')
@login_required
def export_production_csv():
    production_records = ProductionRecord.query.all()
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Process Date", "Product Lot Number", "Best Before Date", 
                     "Product SKU", "Filter Integrity Check", "Sanification Check", 
                     "General Packaging Control", "Bottle Integrity Control", 
                     "Visual Olfactory Control", "Graphics Control", "Lot Number Check", 
                     "Start Pressure Time", "Start Pressure Value", 
                     "First Pressure Time", "First Pressure Value", 
                     "Second Pressure Time", "Second Pressure Value", 
                     "Final Pressure Time", "Final Pressure Value", 
                     "Label Compliance", "Start Filling Cap Compliance", 
                     "Final Filling Cap Compliance", "Bottle Breakage", 
                     "Bottle Breakage Qty", "Units Produced Qty","Operator"])

    for record in production_records:
        writer.writerow([record.process_date, record.product_lot_number, 
                         record.best_before_date, record.product_sku, 
                         record.filter_integrity_check, record.sanification_check, 
                         record.general_packaging_control, record.bottle_integrity_control, 
                         record.visual_olfatory_control, record.graphics_control, 
                         record.lot_number_check, record.start_pressure_time, 
                         record.start_pressure_value, record.first_pressure_time, 
                         record.first_pressure_value, record.second_pressure_time, 
                         record.second_pressure_value, record.final_pressure_time, 
                         record.final_pressure_value, record.label_compliance, 
                         record.start_filling_cap_compliance, record.final_filling_cap_compliance, 
                         record.bottle_breakage, record.bottle_breakage_qty, 
                         record.units_produced_qty,record.user.username])

    output.seek(0)

    response = Response(output.getvalue(), content_type='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=production_records.csv"

    return response