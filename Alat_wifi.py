import os
import subprocess
from subprocess import check_output

def periksa_host_windows():
    if os.name != "nt":
        return '[!] Silakan Jalankan Aplikasi Di Mesin Windows'
    return '[+] Semua bagus....'

def cmd_daftar_ssid_tersedia():
    return check_output("netsh wlan show networks", shell=True).decode('utf-8')

def cmd_daftar_profil():
    return check_output("netsh wlan show profiles", shell=True).decode('utf-8')

def cmd_daftar_ap_terblokir():
    return check_output("netsh wlan show filters", shell=True).decode('utf-8')

def cmd_tampilkan_antarmuka_saat_ini():
    return check_output("netsh wlan show interfaces", shell=True).decode('utf-8')

def cmd_buat_laporan_lengkap():
    return check_output("netsh wlan show all", shell=True).decode('utf-8')

def cmd_tampilkan_password_cleartext(nama_ap):
    if nama_ap:
        return check_output(f"netsh wlan show profiles name=\"{nama_ap}\" key=clear", shell=True).decode('utf-8')
    return "[!] Masukkan nama titik akses nirkabel yang benar."

def cmd_buka_profil():
    return check_output("notepad profiles.txt", shell=True)

def cmd_dump_profil_terenkripsi():
    return check_output("netsh wlan export profile folder=.", shell=True).decode('utf-8')

# ============================================================================================ 
# Alat_wifi.py
# import os
# import subprocess
# from subprocess import check_output

# def check_host_windows(#):
#     if os.name != "nt":
#         return '[!] Silahkan Jalankan Aplikasi Di Mesin Windows'
#     return '[+] semua bagus....'

# def cmd_list_available_ssids():
#     return check_output("netsh wlan show networks", shell=True).decode('utf-8'#)

# def cmd_list_profiles():
#     return check_output("netsh wlan show profiles", shell=True).decode('utf-8'#)

# def cmd_list_blocked_aps():
#     return check_output("netsh wlan show filters", shell=True).decode('utf-8'#)

# def cmd_show_current_interface():
#     return check_output("netsh wlan show interfaces", shell=True).decode('utf-8'#)

# def cmd_gen_full_report():
#     return check_output("netsh wlan show all", shell=True).decode('utf-8'#)

# def cmd_show_cleartext(ap_selector#):
#     if ap_selector:
#         return check_output(f"netsh wlan show profiles name=\"{ap_selector}\" key=clear", shell=True).decode('utf-8')
#     return "[!] Masukkan nama titik akses nirkabel yang benar."

# def cmd_open_profiles(#):
#     return check_output("notepad profiles.txt", shell=True)

# def cmd_dump_encrypted_profiles():
#     return check_output("netsh wlan export profile folder=.", shell=True).decode('utf-8'#)
# ===========================================================================================================================#