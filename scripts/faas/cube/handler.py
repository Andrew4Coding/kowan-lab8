import json
import urllib3

LUAS_PERSEGI_URL = "https://t7ow9idud3.execute-api.us-east-1.amazonaws.com/square-surface/calculate"

http = urllib3.PoolManager()

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        rusuk = float(body.get('rusuk', 0))
        
        if rusuk <= 0:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
                },
                'body': json.dumps({'error': 'Rusuk harus lebih besar dari 0'})
            }
        
        payload = {'side': rusuk}
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
        
        luas_sisi = response_data.get('surface_area', 0)
        
        luas_permukaan = 6 * luas_sisi
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
            },
            'body': json.dumps({
                'rusuk': rusuk,
                'luas_sisi': luas_sisi,
                'luas_permukaan': luas_permukaan,
                'satuan': 'satuan persegi'
            })
        }
    except json.JSONDecodeError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Invalid JSON response from square function',
                'details': str(e)
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