# app.py
from flask import Flask, render_template, request, jsonify
import Alat_wifi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    action = request.json['action']
    if action == "periksa_host_windows":
        result = Alat_wifi.periksa_host_windows()
    elif action == "list_ssids":
        result = Alat_wifi.cmd_daftar_ssid_tersedia()
    elif action == "list_profiles":
        result = Alat_wifi.cmd_daftar_profil()
    elif action == "list_blocked_aps":
        result = Alat_wifi.cmd_daftar_ap_terblokir()
    elif action == "show_interface":
        result = Alat_wifi.cmd_tampilkan_antarmuka_saat_ini()
    elif action == "full_report":
        result = Alat_wifi.cmd_buat_laporan_lengkap()
    elif action == "show_cleartext":
        ap_name = request.json.get('ap_name')
        result = Alat_wifi.cmd_tampilkan_password_cleartext(ap_name)
    elif action == "dump_profiles":
        result = Alat_wifi.cmd_dump_profil_terenkripsi()
    else:
        result = '[!] Pilihan Tidak Valid'
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)

# ======================================================================
# from flask import Flask, render_template, request, jsonify
# import Alat_wifi

# app = Flask(__name__#)

# @app.route('/'#)
# def index():
#     return render_template('index.html')

# @app.route('/execute', methods=['POST'])
# def execute():
#     action = request.json['action']
#     if action == "check_host_windows":
#         result = Alat_wifi.check_host_windows()
#     elif action == "list_ssids":
#         result = Alat_wifi.cmd_list_available_ssids()
#     elif action == "list_profiles":
#         result = Alat_wifi.cmd_list_profiles()
#    elif action == "list_blocked_aps":
#         result = Alat_wifi.cmd_list_blocked_aps()
#     elif action == "show_interface":
#         result = Alat_wifi.cmd_show_current_interface()
#     elif action == "full_report":
#         result = Alat_wifi.cmd_gen_full_report()
#     elif action == "show_cleartext":
#         ap_name = request.json.get('ap_name')
#         result = Alat_wifi.cmd_show_cleartext(ap_name)
#     elif action == "dump_profiles":
#         result = Alat_wifi.cmd_dump_encrypted_profiles()
#     else:
#         result = '[!] Pilihan Tidak Valid'
#     return jsonify(result=result)

# if __name__ == "__main__":
#     app.run(debug=True#)
