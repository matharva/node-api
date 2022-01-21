const { XRayClient, BatchGetTracesCommand } = require("@aws-sdk/client-xray");
require("dotenv").config();

// a client can be shared by different commands.
const client = new XRayClient({
  region: process.env.AWS_DEFAULT_REGION,
  credentials: {
    // AccessKeyId: process.env.AWS_ACCESS_KEY_ID,
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  },
});

const params = {
  /** input parameters */
  TraceIds: ["1-61e7b72b-525daf7ea57453175fb048cc"],
};
const command = new BatchGetTracesCommand(params);

async function getBatch() {
  try {
    const data = await client.send(command);
    console.log("Data from the API is: ", data.Traces[0].Segments);
    // process data.
  } catch (error) {
    console.log("Error from the API is: ", error);
    // error handling.
  }
}
getBatch();
