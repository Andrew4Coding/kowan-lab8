import json
import urllib3
import math

LUAS_LINGKARAN_URL = "https://t7ow9idud3.execute-api.us-east-1.amazonaws.com/circle-surface/calculate"
LUAS_PERSEGI_URL = "https://t7ow9idud3.execute-api.us-east-1.amazonaws.com/square-surface/calculate"

http = urllib3.PoolManager()

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        jari_jari = float(body.get('jari_jari', 0))
        tinggi = float(body.get('tinggi', 0))
        
        if jari_jari <= 0 or tinggi <= 0:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
                },
                'body': json.dumps({'error': 'Jari-jari dan tinggi harus lebih besar dari 0'})
            }

        payload = {'side': tinggi}
        encoded_payload = json.dumps(payload).encode('utf-8')

        response = http.request(
            'POST',
            LUAS_PERSEGI_URL,
            body=encoded_payload,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status != 200:
            return {
                'statusCode': 500,
                'headers': {
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': f'Error calling square function, status: {response.status}',
                    'details': response.data.decode('utf-8')
                })
            }
        
        response_data = json.loads(response.data.decode('utf-8'))
        
        luas_persegi = response_data.get('surface_area', 0)
        
        payload = {'radius': jari_jari}
        encoded_payload = json.dumps(payload).encode('utf-8')
        
        response = http.request(
            'POST',
            LUAS_LINGKARAN_URL,
            body=encoded_payload,
            headers={'Content-Type': 'application/json'}
        )

        if response.status != 200:
            return {
                'statusCode': 500,
                'headers': {
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': f'Error calling square function, status: {response.status}',
                    'details': response.data.decode('utf-8')
                })
            }

        response_data = json.loads(response.data.decode('utf-8'))
        
        luas_lingkaran = response_data.get('surface_area', 0)

        luas_alas_tabung = 2 * luas_lingkaran

        luas_selimut_tabung = luas_lingkaran * 0 +  2 * math.pi * jari_jari * luas_persegi / tinggi
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
            },
            'body': json.dumps({
                'jari_jari': jari_jari,
                'tinggi': tinggi,
                'luas_selimut': luas_selimut_tabung,
                'satuan': 'satuan persegi'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }