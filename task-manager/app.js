const express = require("express");
const PORT = process.env.PORT || 8000;
const app = express();
const tasks = require("./routes/tasks");
require("dotenv").config();
const notFound = require("./middleware/not-found");
const errorHandlerMiddleware = require("./middleware/error-handler");

// Connect db
const connectDB = require("./db/connect");
const {
  getData,
  getDataById,
  addOrUpdateData,
  deleteData,
} = require("./dynamo");

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.json({
    data: `server is running!!!!`,
  });
});

app.get("/data", async (req, res) => {
  try {
    const data = await getData();
    res.json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ err: "Something went wrong" });
  }
});

app.get("/data/:id", async (req, res) => {
  const id = req.params.id;
  try {
    const data = await getDataById(id);
    res.json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ err: "Something went wrong" });
  }
});

app.post("/data", async (req, res) => {
  const data = req.body;
  console.log("body: ", data);
  try {
    const newData = await addOrUpdateData(data);
    res.json(newData);
  } catch (err) {
    console.error(err);
    res.status(500).json({ err: "Something went wrong" });
  }
});

app.put("/data/:id", async (req, res) => {
  const data = req.body;
  const { id } = req.params;
  data.id = id;
  try {
    const newData = await addOrUpdateData(data);
    res.json(newData);
  } catch (err) {
    console.error(err);
    res.status(500).json({ err: "Something went wrong" });
  }
});

app.delete("/data/:id", async (req, res) => {
  const { id } = req.params;
  try {
    res.json(await deleteData(id));
  } catch (err) {
    console.error(err);
    res.status(500).json({ err: "Something went wrong" });
  }
});

app.use(notFound);
app.use(errorHandlerMiddleware);

const start = async () => {
  try {
    // await connectDB(process.env.MONGO_URI);
    app.listen(PORT, () => {
      console.log(`Server listening at port ${PORT}...`);
    });
  } catch (error) {
    console.log(error);
  }
};

start();
