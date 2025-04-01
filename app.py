from flask import Flask,send_file,jsonify
from fetch_data import fetch_weather_data
from process_data import process_weather_data
from convert_data import convert_to_csv,convert_to_excel,convert_to_xml
from config import CSV_FILE,XML_FILE,EXCEL_FILE

app=Flask(__name__)

@app.route('/get_weather_data',methods=['GET'])
def get_weather_data():
    # fetch raw data from open weather api
    raw_data=fetch_weather_data()
    # process data to clean version
    processed_Data=process_weather_data(raw_data)
    if 'error' in processed_Data:
        return jsonify(processed_Data),400
    
    # save the data in csv,xlsx,xml file
    csv_file=convert_to_csv(processed_Data)
    xml_file=convert_to_xml(processed_Data)
    excel_file=convert_to_excel(processed_Data)

    return jsonify({
        'message':'weather data fetch successfully and processed successfully',
        'csv_file':csv_file,
        'xml_file':xml_file,
        'excel_file':excel_file
    })

@app.route('/download_csv',methods=['GET'])
def download_csv():
    return send_file(CSV_FILE,as_attachment=True)


@app.route('/download_xml',methods=['GET'])
def download_xml():
    return send_file(XML_FILE,as_attachment=True)

@app.route('/download_excel',methods=['GET'])
def download_excel():
    return send_file(EXCEL_FILE,as_attachment=True)

if __name__=="__main__":
    app.run(debug=True)