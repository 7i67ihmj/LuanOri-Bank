from flask import Flask, request, jsonify
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

CREDIT_TEXT = "LuanOri"
CREDIT_URL = "https://github.com/luanori"

BANK_LOGOS = {
    "970436": "https://luanoribank.vercel.app/app_v2/img/VCB.png",
    "970415": "https://luanoribank.vercel.app/app_v2/img/CTG.png",
    "970407": "https://luanoribank.vercel.app/app_v2/img/TCB.png",
    "970418": "https://luanoribank.vercel.app/app_v2/img/BIDV.png",
    "970405": "https://luanoribank.vercel.app/app_v2/img/VARB.png",
    "970419": "https://luanoribank.vercel.app/app_v2/img/NVB.png",
    "970403": "https://luanoribank.vercel.app/app_v2/img/STB.png",
    "970416": "https://luanoribank.vercel.app/app_v2/img/ACB.png",
    "970422": "https://luanoribank.vercel.app/app_v2/img/MB.png",
    "970423": "https://luanoribank.vercel.app/app_v2/img/TPB.png",
    "970424": "https://luanoribank.vercel.app/app_v2/img/SVB.png",
    "970441": "https://luanoribank.vercel.app/app_v2/img/VIB.png",
    "970432": "https://luanoribank.vercel.app/app_v2/img/VPB.png",
    "970443": "https://luanoribank.vercel.app/app_v2/img/SHB.png",
    "970431": "https://luanoribank.vercel.app/app_v2/img/EIB.png",
    "970438": "https://luanoribank.vercel.app/app_v2/img/BVB.png",
    "970454": "https://luanoribank.vercel.app/app_v2/img/VCCB.png",
    "970429": "https://luanoribank.vercel.app/app_v2/img/SCB.png",
    "970421": "https://luanoribank.vercel.app/app_v2/img/VRB.png",
    "970425": "https://luanoribank.vercel.app/app_v2/img/ABB.png",
    "970412": "https://luanoribank.vercel.app/app_v2/img/PVCB.png",
    "970414": "https://luanoribank.vercel.app/app_v2/img/MBV.png",
    "970428": "https://luanoribank.vercel.app/app_v2/img/NAB.png",
    "970437": "https://luanoribank.vercel.app/app_v2/img/HDB.png",
    "970420": "https://luanoribank.vercel.app/app_v2/img/HDB.png",
    "970433": "https://luanoribank.vercel.app/app_v2/img/VB.png",
    "970460": "https://luanoribank.vercel.app/app_v2/img/CFC.png",
    "970439": "https://luanoribank.vercel.app/app_v2/img/PBVN.png",
    "970442": "https://luanoribank.vercel.app/app_v2/img/HLB.png",
    "970430": "https://luanoribank.vercel.app/app_v2/img/PGB.png",
    "970446": "https://luanoribank.vercel.app/app_v2/img/COB.png",
    "422589": "https://luanoribank.vercel.app/app_v2/img/CIMB.png",
    "970434": "https://luanoribank.vercel.app/app_v2/img/IVB.png",
    "970406": "https://luanoribank.vercel.app/app_v2/img/VIKKI.png",
    "970408": "https://luanoribank.vercel.app/app_v2/img/GPB.png",
    "970409": "https://luanoribank.vercel.app/app_v2/img/NASB.png",
    "970427": "https://luanoribank.vercel.app/app_v2/img/VAB.png",
    "970400": "https://luanoribank.vercel.app/app_v2/img/SGB.png",
    "970426": "https://luanoribank.vercel.app/app_v2/img/MSB.png",
    "970449": "https://luanoribank.vercel.app/app_v2/img/LPB.png",
    "970452": "https://luanoribank.vercel.app/app_v2/img/KLB.png",
    "970455": "https://luanoribank.vercel.app/app_v2/img/IBK.png",
    "970456": "https://luanoribank.vercel.app/app_v2/img/IBK.png",
    "970457": "https://luanoribank.vercel.app/app_v2/img/WOORI.png",
    "970440": "https://luanoribank.vercel.app/app_v2/img/SEAB.png",
    "970458": "https://luanoribank.vercel.app/app_v2/img/UOB.png",
    "970448": "https://luanoribank.vercel.app/app_v2/img/OCB.png",
    "9777777": "https://luanoribank.vercel.app/app_v2/img/MIRAE.png",
    "970466": "https://luanoribank.vercel.app/app_v2/img/KEBHANA.png",
    "970467": "https://luanoribank.vercel.app/app_v2/img/KEBHANA.png",
    "970410": "https://luanoribank.vercel.app/app_v2/img/STANDARD.png",
    "546034": "https://luanoribank.vercel.app/app_v2/img/CAKE.png",
    "546035": "https://luanoribank.vercel.app/app_v2/img/UBANK.png",
    "801011": "https://luanoribank.vercel.app/app_v2/img/NONGHYUP.png",
    "970462": "https://luanoribank.vercel.app/app_v2/img/KOOKMIN.png",
    "970463": "https://luanoribank.vercel.app/app_v2/img/KOOKMIN.png",
    "796500": "https://luanoribank.vercel.app/app_v2/img/DBS.png",
    "970444": "https://luanoribank.vercel.app/app_v2/img/CBB.png",
    "668888": "https://luanoribank.vercel.app/app_v2/img/KBANK.png",
    "458761": "https://luanoribank.vercel.app/app_v2/img/HSBC.png",
    "533948": "https://luanoribank.vercel.app/app_v2/img/CITI.png",
    "971011": "https://luanoribank.vercel.app/app_v2/img/VNPTMONEY.png",
    "971005": "https://luanoribank.vercel.app/app_v2/img/VIETTELMONEY.png",
    "999888": "https://luanoribank.vercel.app/app_v2/img/VBSP.png",
    "971133": "https://luanoribank.vercel.app/app_v2/img/PVCOMBANK.png",
    "963668": "https://luanoribank.vercel.app/app_v2/img/BNPPARIBAS.png",
    "963666": "https://luanoribank.vercel.app/app_v2/img/BNPPARIBAS.png",
    "168999": "https://luanoribank.vercel.app/app_v2/img/CATHAY.png",
    "555666": "https://luanoribank.vercel.app/app_v2/img/BIDC.png",
    "963368": "https://luanoribank.vercel.app/app_v2/img/SHINHAN.png",
    "963688": "https://luanoribank.vercel.app/app_v2/img/BANKOFCHINA.png",
    "963311": "https://luanoribank.vercel.app/app_v2/img/VIKKI.png",
    "963399": "https://luanoribank.vercel.app/app_v2/img/UMEE.png",
    "963369": "https://luanoribank.vercel.app/app_v2/img/LIOBANK.png",
    "971032": "https://luanoribank.vercel.app/app_v2/img/MOBIFONE.png"
}

def fetch_from_original_api(bin_code, stk):
    try:
        url = f"https://mb.acb1s.workers.dev/?bank={bin_code}&stk={stk}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Referer': 'https://mb.acb1s.workers.dev/',
        }
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/', defaults={'path': ''}, methods=['GET', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'OPTIONS'])
def catch_all(path):
    if request.method == 'OPTIONS':
        response = jsonify({})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = '*'
        return response
    
    bank = request.args.get('bank')
    stk = request.args.get('stk')
    
    if not bank or not stk:
        return jsonify({
            "code": 400,
            "success": False,
            "msg": "Missing required parameters: bank and stk",
            "credits": CREDIT_TEXT,
            "credits_url": CREDIT_URL
        })
    
    result = fetch_from_original_api(bank, stk)
    
    if result and result.get("success"):
        data = result.get("data", {})
        if data:
            data["bankLogoUrl"] = BANK_LOGOS.get(bank, "")
            data["Bin_card"] = bank
        result["data"] = data
        result["credits"] = CREDIT_TEXT
        result["credits_url"] = CREDIT_URL
    else:
        result = {
            "code": 404,
            "success": False,
            "msg": "Account not found",
            "credits": CREDIT_TEXT,
            "credits_url": CREDIT_URL
        }
    
    response = jsonify(result)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == "__main__":
    app.run(port=8080)