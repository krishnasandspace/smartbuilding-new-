import boto3
import psycopg2
import json

def lambda_handler(event, context):
    try:
        # Connect to Redshift
        conn = psycopg2.connect(
            dbname='<your-redshift-db>',
            user='<your-username>',
            password='<your-password>',
            host='<your-redshift-cluster-endpoint>',
            port=5439
        )
        cur = conn.cursor()
        
        # Query Data
        cur.execute("SELECT device_id, timestamp, temperature, humidity FROM energy_data LIMIT 10;")
        rows = cur.fetchall()
        
        # Format Data
        response = [{"device_id": row[0], "timestamp": row[1], "temperature": row[2], "humidity": row[3]} for row in rows]
        conn.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
