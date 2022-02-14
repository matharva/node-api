data = {'ResponseMetadata': {'RequestId': '820a2999-c501-4669-837e-71219dda676a', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 26 Jan 2022 10:46:06 GMT', 'content-type': 'application/json', 'content-length': '1736', 'connection': 'keep-alive', 'x-amzn-requestid': '820a2999-c501-4669-837e-71219dda676a'}, 'RetryAttempts': 0}, 'Traces': [{'Id': '1-61e7b72b-525daf7ea57453175fb048cc', 'Duration': 0.083, 'LimitExceeded': False, 'Segments': [{'Id': '79cbee60b78a3bdc', 'Document': '{"id":"79cbee60b78a3bdc","name":"localhost:8000","start_time":1.642575659402E9,"trace_id":"1-61e7b72b-525daf7ea57453175fb048cc","end_time":1.642575659485E9,"http":{"request":{"url":"http://localhost:8000/data/6","method":"GET","user_agent":"PostmanRuntime/7.29.0","client_ip":"::1"},"response":{"status":200}},"aws":{"xray":{"package":"aws-xray-sdk","sdk_version":"3.3.4","sdk":"X-Ray for Node.js"}},"service":{"name":"jobs","version":"1.0.0","runtime":"node","runtime_version":"v14.17.1"},"origin":"AWS::EC2::Instance","subsegments":[{"id":"488e10e2b4602845","name":"DynamoDB","start_time":1.642575659409E9,"end_time":1.642575659484E9,"http":{"response":{"status":200}},"aws":{"retries":0,"region":"ap-south-1","operation":"GetItem","request_id":"4366KIVDS4KUKOQ8HJ8AFDM5BBVV4KQNSO5AEMVJF66Q9ASUAAJG","table_name":"testing","resource_names":["testing"]},"namespace":"aws"}]}'}, {
    'Id': '26abc28612527bfe', 'Document': '{"id":"26abc28612527bfe","name":"DynamoDB","start_time":1.642575659409E9,"trace_id":"1-61e7b72b-525daf7ea57453175fb048cc","end_time":1.642575659484E9,"parent_id":"488e10e2b4602845","inferred":true,"http":{"response":{"status":200}},"aws":{"retries":0,"region":"ap-south-1","operation":"GetItem","request_id":"4366KIVDS4KUKOQ8HJ8AFDM5BBVV4KQNSO5AEMVJF66Q9ASUAAJG","table_name":"testing","resource_names":["testing"]},"origin":"AWS::DynamoDB::Table"}'}]}], 'UnprocessedTraceIds': []}

data = {'aws': {'xray': {'package': 'aws-xray-sdk',
                         'sdk': 'X-Ray for Node.js',
                         'sdk_version': '3.3.4'}},
        'end_time': 1642575659.485,
        'http': {'request': {'client_ip': '::1',
                             'method': 'GET',
                             'url': 'http://localhost:8000/data/6',
                             'user_agent': 'PostmanRuntime/7.29.0'},
                 'response': {'status': 200}},
        'id': '79cbee60b78a3bdc',
        'name': 'localhost:8000',
        'origin': 'AWS::EC2::Instance',
        'service': {'name': 'jobs',
                    'runtime': 'node',
                    'runtime_version': 'v14.17.1',
                    'version': '1.0.0'},
        'start_time': 1642575659.402,
        'subsegments': [{'aws': {'operation': 'GetItem',
                                 'region': 'ap-south-1',
                                 'request_id': '4366KIVDS4KUKOQ8HJ8AFDM5BBVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                 'resource_names': ['testing'],
                                 'retries': 0,
                                 'table_name': 'testing'},
                         'end_time': 1642575659.484,
                         'http': {'response': {'status': 200}},
                         'id': '488e10e2b4602845',
                         'name': 'DynamoDB',
                         'namespace': 'aws',
                         'start_time': 1642575659.409}],
        'trace_id': '1-61e7b72b-525daf7ea57453175fb048cc'}