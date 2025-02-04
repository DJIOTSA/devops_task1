const axios = require("axios");

/**
 * Fetches a fun fact about a number from the Numbers API.
 * @param {number} num - The number to fetch a fun fact for.
 * @returns {string} - A fun fact about the number or a fallback message.
 */
const fetchFunFact = async (num) => {
  try {
    const response = await axios.get(`https://numbersapi.com/${num}/math?json`);
    return response.data.text;
  } catch (error) {
    return "No fun fact available.";
  }
};

module.exports = { fetchFunFact };
