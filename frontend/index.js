const express = require("express");
const app = express();

app.use(express.json());

// Sample endpoint to fetch energy data
app.get("/energy-data", (req, res) => {
  const mockData = [
    { device_id: "sensor1", temperature: 28.5, timestamp: "2024-11-22T10:30:00Z" },
    { device_id: "sensor2", temperature: 35.2, timestamp: "2024-11-22T11:00:00Z" },
  ];
  res.json(mockData);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
