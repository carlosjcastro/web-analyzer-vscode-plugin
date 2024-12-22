const axios = require("axios");

const apiClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 5000,
});

module.exports = apiClient;
