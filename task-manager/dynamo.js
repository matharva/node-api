var XRay = require("aws-xray-sdk");
var AWS = XRay.captureAWS(require("aws-sdk"));

require("dotenv").config();

AWS.config.update({
  region: process.env.AWS_DEFAULT_REGION,
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  //   endpoint: "http://localhost:8000",
});

const dynamoClient = new AWS.DynamoDB.DocumentClient();
const TABLE_NAME = "testing";

const getData = async () => {
  const params = {
    TableName: TABLE_NAME,
  };
  try {
    console.log("In try ");
    const data = await dynamoClient.scan(params).promise();
    console.log("Return data: ", data);
    return data;
  } catch (e) {
    console.log("In catch ");
    console.log("the error is: ", e);
  }
};
// getData();

const DATA = {
  testingId: "1",
  name: "test1",
};

const addOrUpdateData = async (character) => {
  const params = {
    TableName: TABLE_NAME,
    Item: character,
  };
  return await dynamoClient.put(params).promise();
};
// addOrUpdateData(DATA);

const getDataById = async (id) => {
  const params = {
    TableName: TABLE_NAME,
    Key: {
      testingId: id,
    },
  };
  return await dynamoClient.get(params).promise();
};

const deleteData = async (id) => {
  const params = {
    TableName: TABLE_NAME,
    Key: {
      testingId: id,
    },
  };
  return await dynamoClient.delete(params).promise();
};

module.exports = {
  dynamoClient,
  getData,
  getDataById,
  addOrUpdateData,
  deleteData,
};
