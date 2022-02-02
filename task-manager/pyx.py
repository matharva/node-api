import boto3
import os
from dotenv import load_dotenv
import json
import pprint
from datetime import datetime
load_dotenv()

client = boto3.client('xray',
                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                      region_name=os.getenv('AWS_DEFAULT_REGION')
                      )


def batch_traces():
    response = client.batch_get_traces(
        TraceIds=[
            '1-61e7b72b-525daf7ea57453175fb048cc',
        ],
        # NextToken='string'
    )
    pprint.pprint(json.loads(response["Traces"][0]["Segments"][0]["Document"]))
    # print(type(response))


def trace_summaries():
    response = client.get_trace_summaries(
        StartTime=datetime(2022, 1, 19, hour=1, minute=43),
        EndTime=datetime(2022, 1, 19, hour=7, minute=43),
    )
    traces = response["TraceSummaries"]
    print(json.dumps(traces))


def trace_graph():
    response = client.get_trace_graph(
        TraceIds=[
            '1-61e7b72b-525daf7ea57453175fb048cc',
        ],
        # NextToken='string'
    )
    # pprint.pprint(json.loads(response["Traces"][0]["Segments"][0]["Document"]))
    print(json.dumps(response))


trace_graph()
