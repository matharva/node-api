const mongoose = require("mongoose");

const DB_USER = "Atharva";
const PASSWORD = encodeURIComponent("atharvamongodb");
const DB_URL = `mongodb+srv://Atharva:atharvamongodb@cluster0.ba5cc.mongodb.net/TaskManager?retryWrites=true&w=majority`;
// const connectionString =
//   "mongodb+srv://Atharva:@cluster0.ba5cc.mongodb.net/TaskManager?retryWrites=true&w=majority";

const connectDB = (url) => {
  return mongoose
    .connect(url)
    .then(() => console.log("Connected to the db... "))
    .catch((err) => console.log(err));
};

module.exports = connectDB;
